// Copyright Microsoft Corporation.
// Licensed under the MIT License.

package configuration

import (
	"os"
	"path/filepath"
	"testing"

	"github.com/microsoft/azurelinux/toolkit/tools/internal/file"
	"github.com/stretchr/testify/assert"
)

// TestMain found in configuration_test.go.

var (
	validPackageRepos = []PackageRepo{
		{
			Name:         "edge-official-base",
			BaseUrl:      "https://files-rs.edgeorchestration.intel.com/files-edge-orch/microvisor/rpm/3.0/",
			Install:      false,
			GPGCheck:     true,
			RepoGPGCheck: true,
			GPGKeys:      "file:///etc/pki/rpm-gpg/INTEL-RPM-GPG-KEY",
		},
		{
			Name:         "edge-official-preview",
			BaseUrl:      "https://files-rs.edgeorchestration.intel.com/files-edge-orch/microvisor/rpm/3.0/",
			Install:      true,
			GPGCheck:     true,
			RepoGPGCheck: true,
			GPGKeys:      "file:///etc/pki/rpm-gpg/INTEL-RPM-GPG-KEY",
		},
	}

	validRepoContent = []string{
		"[edge-official-base]",
		"name=edge-official-base",
		"baseurl=https://files-rs.edgeorchestration.intel.com/files-edge-orch/microvisor/rpm/3.0/",
		"gpgkey=file:///etc/pki/rpm-gpg/INTEL-RPM-GPG-KEY",
		"gpgcheck=1",
		"repo_gpgcheck=1",
		"enabled=1",
		"skip_if_unavailable=True",
		"sslverify=1",
	}

	validRepoJson          = `{"name":"edge-official-base","baseurl":"https://files-rs.edgeorchestration.intel.com/files-edge-orch/microvisor/rpm/3.0/","install":false}`
	validRepoNoGPGJson     = `{"name":"edge-official-base","baseurl":"https://files-rs.edgeorchestration.intel.com/files-edge-orch/microvisor/rpm/3.0/","install":false,"gpgcheck":false}`
	validRepoNoRepoGPGJson = `{"name":"edge-official-base","baseurl":"https://files-rs.edgeorchestration.intel.com/files-edge-orch/microvisor/rpm/3.0/","install":false,"RepoGPGCheck":false}`
	validRepoCustomKey     = `{"name":"edge-official-base","baseurl":"https://files-rs.edgeorchestration.intel.com/files-edge-orch/microvisor/rpm/3.0/","install":true,"gpgkeys":"file:///etc/pki/rpm-gpg/my-custom-key"}`
)

func TestShouldPassParsingValidPackageRepos_PackageRepo(t *testing.T) {
	for _, p := range validPackageRepos {
		var checkedPackageRepo PackageRepo
		assert.NoError(t, p.IsValid())
		err := remarshalJSON(p, &checkedPackageRepo)
		assert.NoError(t, err)
		assert.Equal(t, p, checkedPackageRepo)
	}
}

// TestShouldFailParsingInvalidName
// validates that an empty PackageRepo.Name fails IsValid
func TestShouldFailParsingInvalidName_PackageRepo(t *testing.T) {
	var checkedPackageRepo PackageRepo
	testPackageRepo := validPackageRepos[0]
	testPackageRepo.Name = ""

	err := testPackageRepo.nameIsValid()
	assert.Error(t, err)
	assert.Equal(t, "invalid value for package repo [Name] (), name cannot be empty", err.Error())

	err = remarshalJSON(testPackageRepo, &checkedPackageRepo)
	assert.Error(t, err)
	assert.Equal(t, "failed to parse [PackageRepo]: invalid value for package repo [Name] (), name cannot be empty", err.Error())
}

// TestShouldFailParsingInvalidBaseUrl
// validates that an empty PackageRepo.BaseUrl fails IsValid
func TestShouldFailParsingInvalidBaseUrlEmptyString_PackageRepo(t *testing.T) {
	var checkedPackageRepo PackageRepo
	testPackageRepo := validPackageRepos[0]
	testPackageRepo.BaseUrl = ""

	err := testPackageRepo.repoUrlIsValid()
	assert.Error(t, err)
	assert.Equal(t, "invalid value for package repo [BaseUrl] (), URL cannot be empty", err.Error())

	err = remarshalJSON(testPackageRepo, &checkedPackageRepo)
	assert.Error(t, err)
	assert.Equal(t, "failed to parse [PackageRepo]: invalid value for package repo [BaseUrl] (), URL cannot be empty", err.Error())
}

// TestShouldFailParsingInvalidBaseUrl
// validates that a bogus URL fails IsValid
func TestShouldFailParsingInvalidBaseUrlBogusUrl_PackageRepo(t *testing.T) {
	var checkedPackageRepo PackageRepo
	testPackageRepo := validPackageRepos[0]
	testPackageRepo.BaseUrl = "asjhdjkshd"

	err := testPackageRepo.repoUrlIsValid()
	assert.Error(t, err)
	assert.Equal(t, "failed to parse input URL (asjhdjkshd):\nparse \"asjhdjkshd\": invalid URI for request", err.Error())

	err = remarshalJSON(testPackageRepo, &checkedPackageRepo)
	assert.Error(t, err)
	assert.Equal(t, "failed to parse [PackageRepo]: failed to parse input URL (asjhdjkshd):\nparse \"asjhdjkshd\": invalid URI for request", err.Error())
}

// TestShouldSucceedCreatingPackageRepoFile
// validates that package repo file can be created
func TestShouldSucceedCreatingPackageRepoFile_PackageRepo(t *testing.T) {
	curDir, err := os.Getwd()
	assert.NoError(t, err)
	testRepoFile := filepath.Join(curDir, "edge-official-base.repo")
	testPackageRepo := validPackageRepos[0]

	err = createCustomPackageRepo(nil, testPackageRepo, curDir)
	assert.NoError(t, err)
	t.Cleanup(func() {
		os.Remove(testRepoFile)
	})

	testRepoContents, err := file.ReadLines(testRepoFile)
	assert.NoError(t, err)
	assert.Equal(t, validRepoContent, testRepoContents)
}

func TestShouldSucceedLoadingJSON_PackageRepo(t *testing.T) {
	var checkedPackageRepo PackageRepo
	err := marshalJSONString(validRepoJson, &checkedPackageRepo)

	assert.NoError(t, err)
	assert.Equal(t, validPackageRepos[0], checkedPackageRepo)

}

func TestShouldDisableGPG_PackageRepo(t *testing.T) {
	var checkedPackageRepo PackageRepo
	err := marshalJSONString(validRepoNoGPGJson, &checkedPackageRepo)

	noGPGRepo := validPackageRepos[0]
	noGPGRepo.GPGCheck = false

	assert.NoError(t, err)
	assert.Equal(t, noGPGRepo, checkedPackageRepo)
}

func TestShouldDisableRepoGPG_PackageRepo(t *testing.T) {
	var checkedPackageRepo PackageRepo
	err := marshalJSONString(validRepoNoRepoGPGJson, &checkedPackageRepo)

	noGPGRepo := validPackageRepos[0]
	noGPGRepo.RepoGPGCheck = false

	assert.NoError(t, err)
	assert.Equal(t, noGPGRepo, checkedPackageRepo)
}

func TestShouldSetCustomKeys_PackageRepo(t *testing.T) {
	var checkedPackageRepo PackageRepo
	validRepoContentCustomKey := append([]string{}, validRepoContent...)
	validRepoContentCustomKey[4] = "gpgkey=file:///etc/pki/rpm-gpg/my-custom-key"

	err := marshalJSONString(validRepoCustomKey, &checkedPackageRepo)

	// Use custom keys, and set install to true since we don't support custom keys for non-installed repos
	repoCustomKeys := validPackageRepos[0]
	repoCustomKeys.Install = true
	repoCustomKeys.GPGKeys = "file:///etc/pki/rpm-gpg/my-custom-key"

	assert.NoError(t, err)
	assert.Equal(t, repoCustomKeys, checkedPackageRepo)
}

func TestShouldFailNonInstalledCustomKeys_PackageRepo(t *testing.T) {
	var checkedPackageRepo PackageRepo
	testPackageRepo := validPackageRepos[0]
	testPackageRepo.Install = false
	testPackageRepo.GPGKeys = "file:///etc/pki/rpm-gpg/my-custom-key"

	err := testPackageRepo.IsValid()
	assert.Error(t, err)
	assert.Equal(t, "invalid value for package repo 'edge-official-base' [GPGKeys] (file:///etc/pki/rpm-gpg/my-custom-key), custom GPG keys are only supported for repos that are installed into the final image by setting 'Install=true'", err.Error())

	err = remarshalJSON(testPackageRepo, &checkedPackageRepo)
	assert.Error(t, err)
	assert.Equal(t, "failed to parse [PackageRepo]: invalid value for package repo 'edge-official-base' [GPGKeys] (file:///etc/pki/rpm-gpg/my-custom-key), custom GPG keys are only supported for repos that are installed into the final image by setting 'Install=true'", err.Error())
}

func TestShouldSucceedlInstalledCustomKeys_PackageRepo(t *testing.T) {
	var checkedPackageRepo PackageRepo
	testPackageRepo := validPackageRepos[0]
	testPackageRepo.Install = true
	testPackageRepo.GPGKeys = "file:///etc/pki/rpm-gpg/my-custom-key"

	err := testPackageRepo.IsValid()
	assert.NoError(t, err)

	err = remarshalJSON(testPackageRepo, &checkedPackageRepo)
	assert.NoError(t, err)
}

func TestShouldSucceedSettingDefaults_PackageRepo(t *testing.T) {
	var checkedPackageRepo PackageRepo
	err := marshalJSONString(`{"name": "test", "BaseUrl":"https://www.contoso.com"}`, &checkedPackageRepo)

	assert.NoError(t, err)
	assert.True(t, checkedPackageRepo.GPGCheck)
	assert.True(t, checkedPackageRepo.RepoGPGCheck)
	assert.Equal(t, "file:///etc/pki/rpm-gpg/INTEL-RPM-GPG-KEY", checkedPackageRepo.GPGKeys)
}
