Summary:        agent for collecting, processing, aggregating, and writing metrics.
Name:           telegraf
Version:        1.31.0
Release:        21%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          Development/Tools
URL:            https://github.com/influxdata/telegraf
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Use the generate_source_tarbbal.sh script to get the vendored sources.
Source1:        %{name}-%{version}-vendor.tar.gz
Source2:        telegraf.te
Source3:        telegraf.fc
Patch0:         CVE-2024-37298.patch
Patch1:         CVE-2024-45337.patch
Patch2:         CVE-2024-45338.patch
Patch3:         CVE-2025-22868.patch
Patch4:         CVE-2025-22869.patch
Patch5:         CVE-2025-22870.patch
Patch6:         CVE-2024-51744.patch
Patch7:         CVE-2025-30204.patch
BuildRequires:  golang
BuildRequires:  systemd-devel
Requires:       logrotate
Requires:       procps-ng
Requires:       shadow-utils
Requires:       systemd
Requires:       (%{name}-selinux if selinux-policy-targeted)
Requires(pre):  %{_sbindir}/useradd
Requires(pre):  %{_sbindir}/groupadd
Requires(postun): %{_sbindir}/userdel
Requires(postun): %{_sbindir}/groupdel


%description
Telegraf is an agent written in Go for collecting, processing, aggregating, and writing metrics.

Design goals are to have a minimal memory footprint with a plugin system so that developers in
the community can easily add support for collecting metrics from well known services (like Hadoop,
Postgres, or Redis) and third party APIs (like Mailchimp, AWS CloudWatch, or Google Analytics).

%global selinuxtype targeted
%global modulename  telegraf

%package        selinux
Summary:        %{name} SELinux policy
Requires:       %{name} = %{version}-%{release}
Requires:       fluent-bit-selinux
Requires:       inbm-selinux
Requires:       otelcol-contrib-selinux
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildArch:      noarch
%{?selinux_requires}

%description    selinux
SELinux policy for %{name}.

%prep
%autosetup -N
# setup vendor before patching
tar -xf %{SOURCE1} --no-same-owner
%autopatch -p1

%build
CGO_ENABLED=0 go build -trimpath -tags \
"custom,inputs.cpu,inputs.disk,inputs.diskio,inputs.ethtool,inputs.ethtool,inputs.exec,inputs.intel_pmu,inputs.intel_pmu,\
inputs.intel_powerstat,inputs.intel_powerstat,inputs.ipmi_sensor,inputs.lvm,inputs.mem,inputs.net,inputs.ras,inputs.ras,\
inputs.redfish,inputs.smart,inputs.system,inputs.temp,outputs.opentelemetry,parsers.json_v2,parsers.json" \
-buildvcs=false -mod=vendor -gcflags="all=-spectre=all -l" -asmflags="all=-spectre=all" -ldflags="all=-extldflags=-static" \
./cmd/telegraf

mkdir selinux
cp -p %{SOURCE2} selinux/
cp -p %{SOURCE3} selinux/
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp

%install
mkdir -pv %{buildroot}%{_sysconfdir}/%{name}/%{name}.d
install -m 755 -D %{name} %{buildroot}%{_bindir}/%{name}
install -m 755 -D scripts/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -m 755 -D etc/logrotate.d/%{name} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{modulename}.pp %{buildroot}%{_datadir}/selinux/packages/%{modulename}.pp

# Provide empty config file.
./%{name} config > telegraf.conf
install -m 644 -D telegraf.conf %{buildroot}%{_sysconfdir}/%{name}/telegraf.conf

%pre
getent group telegraf >/dev/null || groupadd -r telegraf
getent passwd telegraf >/dev/null || useradd -c "Telegraf" -d %{_localstatedir}/lib/%{name} -g %{name} \
        -s /sbin/nologin -M -r %{name}

%post
chown -R telegraf:telegraf %{_sysconfdir}/telegraf
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
if [ $1 -eq 0 ] ; then
    getent passwd telegraf >/dev/null && userdel telegraf
    getent group telegraf >/dev/null && groupdel telegraf
fi
%systemd_postun_with_restart %{name}.service

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}/telegraf.conf
%license LICENSE
%{_bindir}/telegraf
%{_unitdir}/telegraf.service
%{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/%{name}/telegraf.d

%files selinux
%{_datadir}/selinux/packages/%{modulename}.pp

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{modulename}.pp

%postun selinux
%selinux_modules_uninstall -s %{selinuxtype} %{modulename}

%changelog
* Thu Apr 28 2025 Ranjan Dutta <ranjan.dutta@intel.com> - 1.31.0-21
- Bump up the version on merge frm AZL tag 3.0.20250423-3.0
- Patch CVE-2025-30204
- Fix CVE-2025-22870, CVE-2024-51744 with an upstream patch
- Patch CVE-2025-22868, CVE-2025-22869

* Fri Mar 21 2025 Anuj Mittal <anuj.mittal@intel.com> - 1.31.0-20
- Bump Release to rebuild

* Fri Mar 07 2025 Ranjan Dutta <ranjan.dutta@intel.com> - 1.31.0-19
- Bump up the version on merge frm AZL tag 3.0.20250206-3.0
- Patch CVE-2024-45338
- Patch CVE-2024-45337

* Mon Jan 27 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.31.0-18
- Update SELinux policy.

* Wed Jan 15 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.31.0-17
- Fix SELinux policy

* Fri Jan 10 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.31.0-16
- Add dependency on inbm-selinux for selinux subpackage

* Fri Jan 10 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.31.0-15
- Add SElinux policy to access inbm conf file

* Tue Jan 07 2025 Mun Chun Yep <mun.chun.yep@intel.com> - 1.31.0-14
- Remove orig file in CVE-2024-45338.patch

* Wed Dec 25 2024 Anuj Mittal <anuj.mittal@intel.com> - 1.31.0-13
- Backport patch for CVE-2024-45338

* Wed Dec 25 2024 Anuj Mittal <anuj.mittal@intel.com> - 1.31.0-12
- Include patch for CVE-2024-45337

* Mon Dec 23 2024 Tan Jia Yong <jia.yong.tan@intel.com> - 1.31.0-11
- Remove additional types from SELinux policy

* Mon Dec 23 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.31.0-10
- Fix file permissions for telegraf configuration file

* Fri Dec 20 2024 Tan Jia Yong <jia.yong.tan@intel.com> - 1.31.0-9
- Fix SELinux policy

* Tue Dec 17 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.31.0-8
- Fix SELinux policy
- Add dependency on otelcol-contrib-selinux for selinux subpackage

* Mon Dec 16 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.31.0-7
- Require SELinux subpackage if selinux-policy-targeted is present

* Fri Dec 13 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.31.0-6
- Add SELinux subpackage

* Tue Nov 26 2024 Andy <andy.peng@intel.com> - 1.31.0-5
- Update go build flag for size optimization
- `-l` to disable inling
- `-trimpath` to remove absolute path 

* Thu Sep 19 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.31.0-4
- Add missing parser to telegraf build

* Fri Sep 13 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.31.0-3
- Fix telegraf build command

* Thu Jul 11 2024 Sumedh Sharma <sumsharma@microsoft.com> - 1.31.0-2
- Add patch for CVE-2024-37298

* Tue Jun 18 2024 Nicolas Guibourge <nicolasg@microsoft.com> - 1.31.0-1
- Auto-upgrade to 1.31.0 - Address CVEs

* Tue Aug 27 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.29.4-6
- Modify compile command to only include required plugins

* Thu Jun 06 2024 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.29.4-5
- Bump release to rebuild with go 1.21.11

* Thu Mar 28 2024 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.29.4-1
- Auto-upgrade to 1.29.4 - Azure Linux 3.0 Package Upgrades
- Remove additional logging as it has been added upstream

* Mon Oct 16 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.27.3-4
- Bump release to rebuild with go 1.20.10

* Tue Oct 10 2023 Dan Streetman <ddstreet@ieee.org> - 1.27.3-3
- Bump release to rebuild with updated version of Go.

* Mon Aug 28 2023 Cameron Baird <cameronbaird@microsoft.com> - 1.27.3-2
- Bump release to rebuild with go 1.20.7

* Mon Aug 07 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.27.3-1
- Auto-upgrade to 1.27.3 - resolve vulnerability with jaeger v1.38.0

* Fri Jul 14 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.27.2-1
- Auto-upgrade to 1.27.2 to fix CVE-2023-34231, CVE-2023-25809, CVE-2023-28642

* Thu Jul 13 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.26.0-4
- Bump release to rebuild with go 1.19.11

* Thu Jun 15 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.26.0-3
- Bump release to rebuild with go 1.19.10

* Wed Apr 05 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.26.0-2
- Bump release to rebuild with go 1.19.8

* Wed Mar 29 2023 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.26.0-1
- Updating to version 1.26.0 to address CVEs in vendored sources for "containerd".

* Tue Mar 28 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.25.2-3
- Bump release to rebuild with go 1.19.7

* Wed Mar 15 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.25.2-2
- Bump release to rebuild with go 1.19.6

* Fri Feb 24 2023 Olivia Crain <oliviacrain@microsoft.com> - 1.25.2-1
- Upgrade to latest upstream version to fix the following CVEs in vendored packages:
  CVE-2019-3826, CVE-2022-1996, CVE-2022-29190, CVE-2022-29222, CVE-2022-29189, 
  CVE-2022-32149, CVE-2022-23471

* Fri Feb 03 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.23.0-6
- Bump release to rebuild with go 1.19.5

* Wed Jan 18 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.23.0-5
- Bump release to rebuild with go 1.19.4

* Fri Dec 16 2022 Daniel McIlvaney <damcilva@microsoft.com> - 1.23.0-4
- Bump release to rebuild with go 1.18.8 with patch for CVE-2022-41717

* Tue Nov 01 2022 Olivia Crain <oliviacrain@microsoft.com> - 1.23.0-3
- Bump release to rebuild with go 1.18.8

* Mon Aug 22 2022 Olivia Crain <oliviacrain@microsoft.com> - 1.23.0-2
- Bump release to rebuild against Go 1.18.5

* Thu Jun 16 2022 Muhammad Falak <mwani@microsoft.com> 1.23.0-1
- Bump version to 1.23.0

* Tue Jun 14 2022 Muhammad Falak <mwani@microsoft.com> - 1.21.2-2
- Bump release to rebuild with golang 1.18.3

* Tue Jan 18 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 1.21.2-1
- Update to version 1.21.2.
- Modified patch to apply to new version.

* Thu Dec 16 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.14.5-8
- Removing the explicit %%clean stage.

* Tue Jun 08 2021 Henry Beberman <henry.beberman@microsoft.com> 1.14.5-7
- Increment release to force republishing using golang 1.15.13.

* Mon Apr 26 2021 Nicolas Guibourge <nicolasg@microsoft.com> 1.14.5-6
- Increment release to force republishing using golang 1.15.11.

* Thu Dec 10 2020 Andrew Phelps <anphel@microsoft.com> 1.14.5-5
- Increment release to force republishing using golang 1.15.

* Thu Oct 15 2020 Pawel Winogrodzki <pawelwi@microsoft.com> 1.14.5-4
- License verified.
- Added %%license macro.
- Fixed source URL.
- Switched to %%autosetup.

* Fri Aug 21 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.14.5-3
- Add runtime required procps-ng and shadow-utils

* Tue Jul 14 2020 Jonathan Chiu <jochi@microsoft.com> 1.14.5-1
- Update to version 1.14.5

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 1.7.4-2
- Initial CBL-Mariner import from Photon (license: Apache2).

* Fri Sep 07 2018 Michelle Wang <michellew@vmware.com> 1.7.4-1
- Update version to 1.7.4 and its plugin version to 1.4.0.

* Mon Sep 18 2017 Alexey Makhalov <amakhalov@vmware.com> 1.3.4-2
- Remove shadow from requires and use explicit tools for post actions

* Tue Jul 18 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.3.4-1
- first version
