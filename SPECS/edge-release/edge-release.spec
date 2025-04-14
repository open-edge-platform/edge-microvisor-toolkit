
%define dist_version 3
%define distro_release_version_no_time %(echo %{distro_release_version} | cut -d. -f 1-3)

Summary:        Edge Microvisor Toolkit release files
Name:           edge-release
Version:        %{dist_version}.0
Release:        3%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Base
URL:            https://github.com/open-edge-platform/edge-microvisor-toolkit

Source1:        90-default.preset
Source2:        90-default-user.preset
Source3:        99-default-disable.preset
Source4:        15-default.conf

Provides:       system-release
Provides:       system-release(%{version})
Provides:       azurelinux-release = %{version}-%{release}
Obsoletes:      azurelinux-release < %{version}-%{release}

BuildArch:      noarch

BuildRequires:  systemd-bootstrap-rpm-macros

%description
Edge Microvisor Toolkit release files such as dnf configs and other %{_sysconfdir}/ release related files
and systemd preset files that determine which services are enabled by default.

%install
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_rpmmacrodir}

cat <<-"EOF" > %{buildroot}%{_libdir}/edge-release
%{distribution} %{version}
BUILD_NUMBER=%{distro_release_version_no_time}
EOF
ln -sv ..%{_libdir}/edge-release %{buildroot}%{_sysconfdir}/edge-release

cat <<-"EOF" > %{buildroot}%{_libdir}/lsb-release
DISTRIB_ID="Edge Microvisor Toolkit"
DISTRIB_RELEASE="%{distro_release_version_no_time}"
DISTRIB_CODENAME=emt
DISTRIB_DESCRIPTION="%{distribution} %{version}"
EOF
ln -sv ..%{_libdir}/lsb-release %{buildroot}%{_sysconfdir}/lsb-release

cat <<-"EOF" > %{buildroot}%{_libdir}/os-release
NAME="%{distribution}"
VERSION="%{distro_release_version_no_time}"
ID="Edge Microvisor Toolkit"
VERSION_ID="%{version}"
PRETTY_NAME="%{distribution} %{version}"
ANSI_COLOR="1;34"
HOME_URL="%{url}"
BUG_REPORT_URL="%{url}"
SUPPORT_URL="%{url}"
EOF
ln -sv ..%{_libdir}/os-release %{buildroot}%{_sysconfdir}/os-release

cat <<-"EOF" > %{buildroot}%{_libdir}/issue
Welcome to %{distribution} %{version} (%{_arch}) - (\l)
EOF
ln -sv ..%{_libdir}/issue %{buildroot}%{_sysconfdir}/issue

cat <<-"EOF" > %{buildroot}%{_libdir}/issue.net
Welcome to %{distribution} %{version} (%{_arch})
EOF
ln -sv ..%{_libdir}/issue.net %{buildroot}%{_sysconfdir}/issue.net

install -d -m 755 %{buildroot}%{_sysconfdir}/issue.d

cat <<-"EOF" > %{buildroot}%{_rpmmacrodir}/macros.dist
# dist macros.

%%__bootstrap         ~bootstrap
%%emt                 %{dist_version}
%%emt%{dist_version}  1
%%dist                .emt%{dist_version}%%{?with_bootstrap:%%{__bootstrap}}
%%dist_vendor         %{vendor}
%%dist_name           %{distribution}
%%dist_home_url       %{url}
%%dist_bug_report_url %{url}
%%dist_debuginfod_url %{url}
EOF

# Default presets for system and user
install -Dm0644 %{SOURCE1} -t %{buildroot}%{_presetdir}/
install -Dm0644 %{SOURCE2} -t %{buildroot}%{_userpresetdir}/

# Default disable presets
install -Dm0644 %{SOURCE3} -t %{buildroot}%{_presetdir}/
install -Dm0644 %{SOURCE3} -t %{buildroot}%{_userpresetdir}/

# Default sysctl settings
install -Dm0644 %{SOURCE4} -t %{buildroot}%{_sysctldir}/

%files
%defattr(-,root,root,-)
%{_libdir}/edge-release
%{_libdir}/lsb-release
%{_libdir}/os-release
%{_libdir}/issue
%{_libdir}/issue.net
%{_sysconfdir}/edge-release
%{_sysconfdir}/lsb-release
%{_sysconfdir}/os-release
%config(noreplace) %{_sysconfdir}/issue
%config(noreplace) %{_sysconfdir}/issue.net
%dir %{_sysconfdir}/issue.d
%{_rpmmacrodir}/macros.dist
%{_presetdir}/*.preset
%{_userpresetdir}/*.preset
%{_sysctldir}/*.conf

%changelog
* Fri Apr 11 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 3.0-3
- bump version for release.

* Tue Mar 11 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 3.0-2
- update URL

* Thu Dec 26 2024 Lee Chee Yang <chee.yang.lee@intel.com> - 3.0-1
- Bump distribution version to 3.0

* Wed Dec 18 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 1.0-26
- Update URL to Edge Microvisor Toolkit repository.

* Mon Dec 16 2024 Lee Chee Yang <chee.yang.lee@intel.com> - 1.0-25
- Add Obsoletes for azurelinux-release
- specify version for Provides

* Fri Dec 13 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 1.0-24
- Original version for Edge Microvisor Toolkit. License verified.
- Based on azurelinux-release
