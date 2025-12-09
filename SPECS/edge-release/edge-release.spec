%define emt_ver 3
%define dist_version 26.06
%define build_number_no_dist_no_time %(echo %{distro_release_version} | cut -d. -f 3)

Summary:        Edge Microvisor Toolkit release files
Name:           edge-release
Version:        %{dist_version}
Release:        1%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Base
URL:            https://github.com/open-edge-platform/edge-microvisor-toolkit

#%define distro_full_version %{dist_version}.%(echo "%{release}" | sed 's/[^0-9].*//' | xargs printf "%02d")~preview
%define distro_full_version %{dist_version}

Source1:        90-default.preset
Source2:        90-default-user.preset
Source3:        99-default-disable.preset
Source4:        15-default.conf

Provides:       system-release
Provides:       system-release(%{version})
Provides:       azurelinux-release = %{version}-%{release}
Obsoletes:      azurelinux-release < 3.0

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
BUILD_NUMBER=%{distro_full_version}-%{build_number_no_dist_no_time}
EOF
ln -sv ..%{_libdir}/edge-release %{buildroot}%{_sysconfdir}/edge-release

cat <<-"EOF" > %{buildroot}%{_libdir}/lsb-release
DISTRIB_ID="Edge Microvisor Toolkit"
DISTRIB_RELEASE="%{distro_full_version}"
DISTRIB_CODENAME=emt
DISTRIB_DESCRIPTION="%{distribution} %{version}"
EOF
ln -sv ..%{_libdir}/lsb-release %{buildroot}%{_sysconfdir}/lsb-release

cat <<-"EOF" > %{buildroot}%{_libdir}/os-release
NAME="%{distribution}"
VERSION="%{distro_full_version}"
ID="Edge Microvisor Toolkit"
VERSION_ID="3.0"
PRETTY_NAME="%{distribution} %{distro_full_version}"
ANSI_COLOR="1;34"
HOME_URL="%{url}"
BUG_REPORT_URL="%{url}"
SUPPORT_URL="%{url}"
EOF
ln -sv ..%{_libdir}/os-release %{buildroot}%{_sysconfdir}/os-release

cat <<-"EOF" > %{buildroot}%{_libdir}/issue
Welcome to %{distribution} %{distro_full_version} (%{_arch}) - (\l)
EOF
ln -sv ..%{_libdir}/issue %{buildroot}%{_sysconfdir}/issue

cat <<-"EOF" > %{buildroot}%{_libdir}/issue.net
Welcome to %{distribution} %{distro_full_version} (%{_arch})
EOF
ln -sv ..%{_libdir}/issue.net %{buildroot}%{_sysconfdir}/issue.net

install -d -m 755 %{buildroot}%{_sysconfdir}/issue.d

cat <<-"EOF" > %{buildroot}%{_rpmmacrodir}/macros.dist
# dist macros.

%%__bootstrap         ~bootstrap
%%emt                 %{emt_ver}
%%emt%{emt_ver}  1
%%dist                .emt%{emt_ver}%%{?with_bootstrap:%%{__bootstrap}}
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
* Mon Mar 30 2026 Lee Chee Yang <chee.yang.lee@intel.com> - 26.06-1
- bump version for 26.06  release.

* Thu Jan 29 2026 Lee Chee Yang <chee.yang.lee@intel.com> - 26.06~preview-1
- bump version for 26.06 preview release.

* Mon Nov 24 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 25.06-1
- bump version for release, change versioning number for 3.0 series to 25.06.

* Tue Jun 24 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 3.0-4
- bump version for release.

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
