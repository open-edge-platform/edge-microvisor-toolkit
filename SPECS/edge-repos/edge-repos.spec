Summary:        Edge Microvisor Toolkit repo files, gpg keys
Name:           edge-repos
Version:        3.0
Release:        4%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Base
URL:            https://github.com/open-edge-platform/edge-microvisor-toolkit
Source0:        INTEL-RPM-GPG-KEY
Source2:        edge-base.repo

Requires:       %{name}-shared = %{version}-%{release}

BuildArch:      noarch

%description
Edge Microvisor Toolkit repo files and gpg keys

%package shared
Summary:        Directories and files needed by all %{name} configurations.
Group:          System Environment/Base

Requires(post): gpgme

Requires(preun): gpgme

%description shared
%{summary}

%install
export REPO_DIRECTORY="%{buildroot}%{_sysconfdir}/yum.repos.d"
install -d -m 755 $REPO_DIRECTORY
install -m 644 %{SOURCE2} $REPO_DIRECTORY

export RPM_GPG_DIRECTORY="%{buildroot}%{_sysconfdir}/pki/rpm-gpg"

install -d -m 755 $RPM_GPG_DIRECTORY
install -m 644 %{SOURCE0} $RPM_GPG_DIRECTORY

%posttrans shared
gpg --import %{_sysconfdir}/pki/rpm-gpg/INTEL-RPM-GPG-KEY

%preun shared
# Remove the INTEL-RPM-GPG-KEY
gpg --batch --yes --delete-keys 84910237BDFAAD16C4F9D44411FF864ABDCE8692

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/edge-base.repo

%files shared
%dir %{_sysconfdir}/yum.repos.d
%{_sysconfdir}/pki/rpm-gpg/INTEL-RPM-GPG-KEY

%changelog
* Mon Apr 21 2025 Mun Chun Yep <mun.chun.yep@intel.com> - 3.0-4
- Update Intel rpm gpg key.

* Wed Mar 12 2025 Mun Chun Yep <mun.chun.yep@intel.com> - 3.0-3
- Update Intel gpg key.
- update URL.

* Wed Feb 26 2025 Mun Chun Yep <mun.chun.yep@intel.com> - 3.0-2
- Replace Intel gpg key and enable gpgcheck.

* Thu Dec 19 2024 Chee Yang Lee <chee.yang.lee@intel.com> - 3.0-1
- bump version.

* Wed Dec 18 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 1.0-2
- Update URL to Edge Microvisor Toolkit repository.

* Mon Jul 29 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 2.0-1
- Original version for Edge Microvisor Toolkit.
