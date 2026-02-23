# Macros needed by SELinux
%global selinuxtype targeted
%global debug_package %{nil}

Summary:        An agent to manage systems via in-band connection
Name:           in-band-manageability
Version:        1.1.1
Release:        1%{?dist}
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
License:        Apache-2.0
URL:            https://github.com/open-edge-platform/edge-node-agents
Source0:        %{url}/archive/refs/tags/%{name}/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        intel_manageability.conf
Source2:        inbm-configuration-replace-FQDN.sh
Source3:        inbm.te
Source4:        inbm.fc
BuildRequires:  golang < 1.26
BuildRequires:  golang >= 1.25.5
BuildRequires:  systemd-rpm-macros
BuildRequires:  selinux-policy-devel
BuildRequires:  make
BuildRequires:  git
Requires:       systemd
Requires:       (%{name}-selinux if selinux-policy-targeted)
Obsoletes:      inbm

%description
The Intel In-Band Manageability Framework is software which enables an
administrator to perform critical Device Management operations over-the-air
remotely from the cloud.

%package        selinux
Summary:        SELinux security policy for inbm
Requires(post): %{name} = %{version}-%{release}
BuildArch:      noarch
%{?selinux_requires}

%description    selinux
SELinux security policy for inbm.

%prep
%setup -q -n %{name}-%{version}

%build
# Build SELinux policy
mkdir selinux
cp -p %{SOURCE3} selinux/
cp -p %{SOURCE4} selinux/
make -f %{_datadir}/selinux/devel/Makefile inbm.pp
# Build Go-based in-band-manageability binaries
# Note: We're already in the in-band-manageability-1.0.0 directory

# Configure Go toolchain to avoid proxy DNS issues during the RPM build
export GOEXPERIMENT=nosystemcrypto
export GOARCH=amd64
export GOOS=linux
export GOSUMDB=off

# Common build configuration
BUILD_DIR=$(pwd)/build/artifacts
mkdir -p "${BUILD_DIR}"

if [ ! -d vendor ]; then
    echo "ERROR: Go vendor directory missing. Regenerate the source tarball with 'go mod vendor'." >&2
    exit 1
fi

BUILD_VERSION=%{version}
BUILD_COMMIT=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

COMMON_LDFLAGS="-s -w -extldflags=-static \
    -X github.com/open-edge-platform/edge-node-agents/in-band-manageability/internal/inbd/telemetry.Version=${BUILD_VERSION} \
    -X github.com/open-edge-platform/edge-node-agents/in-band-manageability/internal/inbd/telemetry.GitCommit=${BUILD_COMMIT} \
    -X github.com/open-edge-platform/edge-node-agents/in-band-manageability/internal/inbd/telemetry.BuildDate=${BUILD_DATE}"

# Build the inbc CLI binary
go build -buildmode=pie -trimpath -mod=vendor \
    -gcflags "all=-spectre=all -l" -asmflags "all=-spectre=all" \
    -ldflags "${COMMON_LDFLAGS} -X main.Version=${BUILD_VERSION}" \
    -o "${BUILD_DIR}/inbc" cmd/inbc/main.go

# Build the inbd daemon binary
go build -buildmode=pie -trimpath -mod=vendor \
    -gcflags "all=-spectre=all -l" -asmflags "all=-spectre=all" \
    -ldflags "${COMMON_LDFLAGS}" \
    -o "${BUILD_DIR}/inbd" cmd/inbd/main.go

%install
find . -type d -name "test*" -exec rm -rf {} +
find . -name "*_test.go" -exec rm -f {} +

# Set up bindir
install -d %{buildroot}%{_bindir}

# Install Go-based in-band-manageability binaries
install -m 755 build/artifacts/inbc %{buildroot}%{_bindir}/inbc
install -m 755 build/artifacts/inbd %{buildroot}%{_bindir}/inbd

# Install systemd service file
install -D -m 0644 debian/inbd.service %{buildroot}%{_unitdir}/inbd.service

# Modify inbd service file to add it into bm-agents group
sed -i '/^Group=inbd$/a SupplementaryGroups=bm-agents' %{buildroot}%{_unitdir}/inbd.service

# Install configuration files
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/intel_manageability.conf
install -D -m 0644 configs/firmware_tool_info.conf %{buildroot}%{_sysconfdir}/firmware_tool_info.conf

# Copy inbm-configuration-replace-FQDN.sh 
FQDN_REPLACE_SCRIPT_PATH_TARGET=%{_bindir}/inbm-configuration-replace-FQDN.sh
FQDN_REPLACE_SCRIPT_PATH_BUILD=%{buildroot}$FQDN_REPLACE_SCRIPT_PATH_TARGET
install -D -m 0755 %{SOURCE2} "$FQDN_REPLACE_SCRIPT_PATH_BUILD"
# Modify inbd service file to add ExecStartPre to customize config file at runtime for FQDN
sed -i "/^ExecStart/i ExecStartPre=$FQDN_REPLACE_SCRIPT_PATH_TARGET" %{buildroot}%{_unitdir}/inbd.service
# and also inject LP agent variables
sed -i '/^ExecStart/i EnvironmentFile=/etc/edge-node/node/agent_variables' %{buildroot}%{_unitdir}/inbd.service

# Install schema files
install -d %{buildroot}%{_datadir}
install -m 644 configs/inbd_schema.json %{buildroot}%{_datadir}/inbd_schema.json
install -m 644 configs/firmware_tool_config_schema.json %{buildroot}%{_datadir}/firmware_tool_config_schema.json

# make new files/directories so they can be persisted
mkdir -p %{buildroot}%{_var}/intel-manageability
mkdir -p %{buildroot}%{_var}/cache/manageability/repository-tool/sota
mkdir -p %{buildroot}%{_var}/log
touch %{buildroot}%{_var}/log/inbm-update-status.log
echo '"UpdateLog": []' > %{buildroot}%{_var}/log/inbm-update-log.log
touch %{buildroot}%{_sysconfdir}/intel_manageability.conf_bak

# Install SELinux policy
mkdir -p %{buildroot}%{_datadir}/selinux/packages
install -m 644 inbm.pp %{buildroot}%{_datadir}/selinux/packages/inbm.pp

# drop already installed documentation, we will use an RPM macro to install it
rm -rf %{buildroot}%{_docdir}

%files    selinux
%{_datadir}/selinux/packages/inbm.pp

%post     selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/inbm.pp
# Apply the file contexts
/sbin/restorecon -Rv /usr/bin/inbc
/sbin/restorecon -Rv /usr/bin/inbd
/sbin/restorecon -Rv /etc/intel_manageability.conf

%postun   selinux
%selinux_modules_uninstall -s %{selinuxtype} inbm


%files

%config(noreplace) %{_sysconfdir}/intel_manageability.conf
%config(noreplace) %{_sysconfdir}/firmware_tool_info.conf
%{_sysconfdir}/intel_manageability.conf_bak
%{_bindir}/inbc
%{_bindir}/inbd
%{_bindir}/inbm-configuration-replace-FQDN.sh
%{_unitdir}/inbd.service
%{_datadir}/inbd_schema.json
%{_datadir}/firmware_tool_config_schema.json
%license LICENSE
%{_var}/cache/manageability/*
%{_var}/intel-manageability
%{_var}/log/*

%pre
    # Create inbc group if it doesn't exist
    getent group inbc >/dev/null || groupadd -r inbc
    
    # Create inbc user if it doesn't exist
    if ! id "inbc" &>/dev/null; then
        if getent group inbc > /dev/null; then
            useradd --system --no-create-home --shell /usr/sbin/nologin -g inbc inbc
        else
            useradd --system --no-create-home --shell /usr/sbin/nologin inbc
        fi
    fi

    # Create inbd group if it doesn't exist
    getent group inbd >/dev/null || groupadd -r inbd


%post
# Set proper permissions on configuration files
if [ -f /etc/intel_manageability.conf ]; then
    chown root:inbd /etc/intel_manageability.conf
    chmod 640 /etc/intel_manageability.conf
fi

if [ -f /etc/firmware_tool_info.conf ]; then
    chown root:inbd /etc/firmware_tool_info.conf
    chmod 644 /etc/firmware_tool_info.conf
fi

# Reload systemd manager configuration and enable/start the service
%systemd_post inbd.service

%preun
# Before uninstallation, stop the service
%systemd_preun inbd.service

%postun
# If this is an uninstall (not an upgrade), disable the service
%systemd_postun inbd.service

%changelog
* Fri Feb 20 2026 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.1.1-1
- Update to golang 1.25.7

* Fri Feb 06 2026 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.1.0-1
- Update to golang 1.25.5

* Tue Dec 02 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.0.6-1
- Update to latest version

* Tue Nov 25 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 1.0.2-2
- amend build required golang version

* Wed Nov 5 2025 Kishan Mochi <kishan.mochi@intel.com> - 1.0.2-1
- update in-band to 1.0.2

* Wed Oct 08 2025 Kishan Mochi <kishan.mochi@intel.com> - 1.0.0-1
- Initial Go-based in-band-manageability package
- Complete rewrite from Python to Go

* Tue Sep 2 2025 Polmoorx shiva kumar <polmoorx.shiva.kumar@intel.com> - 4.2.8.6-2
- Update go version to use above 1.24.4

* Thu Apr 03 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8.6-1
- Update INBM to v4.2.8.6

* Tue Mar 25 2025 Christopher Nolan <christopher.nolan@intel.com> - 4.2.8.5-3
- Update configuration and agent binary paths to use edge-node/

* Fri Mar 21 2025 Anuj Mittal <anuj.mittal@intel.com> - 4.2.8.5-2
- Bump Release to rebuild

* Mon Mar 17 2025 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.8.5-1
- Update INBM to v4.2.8.5

* Fri Mar 14 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8.4-4
- Update files for rebranding.

* Mon Mar 3 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 4.2.8.4-3
- Update SELinux policy.

* Mon Feb 24 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8.4-2
- Fix SELinux policy to access os-update-tool lock.

* Fri Feb 14 2025 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.8.4-1
- Rename Emt references

* Tue Jan 21 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8.2-7
- Add SELinux policy for access os-update-tool lock.

* Fri Jan 17 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 4.2.8.2-6
- Add SELinux policy for root access.

* Tue Jan 07 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 4.2.8.2-5
- Fix license installation.

* Mon Jan 06 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 4.2.8.2-4
- Update Source URL.

* Mon Dec 30 2024 Jia Yong Tan <jia.yong.tan@intel.com> - 4.2.8.2-3
- Add SELinux policy to allow root to read inbm_conf_rw_t

* Fri Dec 20 2024 Jia Yong Tan <jia.yong.tan@intel.com> - 4.2.8.2-2
- Fix SELinux policy

* Wed Dec 18 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8.2-1
- Update inbm to v4.2.8.2

* Tue Dec 17 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8-4
- Add missing SELinux policy for INBM

* Wed Dec 4 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8-3
- Add SELinux policy for INBM

* Wed Dec 4 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.8-2
- Remove tpm2-abrmd dependency from both INBM and INBM's mqtt service

* Mon Dec 2 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.8-1
- Update INBM to v4.2.8

* Mon Nov 25 2024 Andy <andy.peng@intel.com> - 4.2.7-2
- Update go build flag to reduce binary size
- -N to enable compiler optimization 

* Tue Nov 19 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.7-1
- Update INBM version
- Customize INBM config file for Edge Microvisor Toolkit

* Mon Nov 18 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.6.2-2
- Update INBM config and logging config files

* Fri Oct 25 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.6.2-1
- Update inbm to v4.2.6.2

* Fri Oct 18 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.6.1-2
- Add psutil as dependency

* Fri Oct 18 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.6.1-1
- Update inbm to v4.2.6.1
- Add inbm-dispatcher to bm-agents group

* Thu Oct 17 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.6-2
- Fix iteration warning during groupadd

* Tue Oct 1 2024 Gavin Lewis <gavin.b.lewis@inteloc.m> - 4.2.6-1
- Pull in latest INBM
- Update dependency list
- Create some files meant to be runtime-persistent at install time

* Wed Sep 4 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.5-1
- Original version for Edge Microvisor Toolkit. License verified.
