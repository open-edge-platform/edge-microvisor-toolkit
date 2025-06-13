Summary:        Fast and Lightweight Log processor and forwarder for Linux, BSD and OSX
Name:           fluent-bit
Version:        3.1.9
Release:        12%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://fluentbit.io
Source0:        https://github.com/fluent/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        fluent_bit.te
Source2:        fluent_bit.fc
Patch0:         CVE-2024-34250.patch
Patch1:         CVE-2024-25431.patch
Patch2:         CVE-2024-27532.patch
Patch3:         CVE-2024-50608.patch
Patch4:         CVE-2024-50609.patch
Patch5:         CVE-2025-29087.patch
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  graphviz
BuildRequires:  libpq-devel
BuildRequires:  libyaml-devel
BuildRequires:  luajit-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
Requires:       (%{name}-selinux if selinux-policy-targeted)

%description

Fluent Bit is a fast Log Processor and Forwarder for Linux, Embedded Linux, MacOS and BSD
family operating systems. It's part of the Fluentd Ecosystem and a CNCF sub-project.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
Development files for %{name}

%global selinuxtype targeted
%global modulename  fluent_bit

%package        selinux
Summary:        %{name} SELinux policy
Requires:       %{name} = %{version}-%{release}
Requires:       otelcol-contrib-selinux
Requires:       inbm-selinux
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildArch:      noarch
%{?selinux_requires}

%description    selinux
SELinux policy for %{name}.

%prep
%autosetup -p1

%build
%cmake\
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DFLB_EXAMPLES=Off \
    -DFLB_SHARED_LIB=Off \
%if %{with_check}
    -DFLB_TESTS_RUNTIME=On \
    -DFLB_TESTS_INTERNAL=On \
%endif
    -DFLB_RELEASE=On \
    -DFLB_DEBUG=Off \
    -DFLB_TLS=On \
    -DFLB_JEMALLOC=off \
    -DFLB_LUAJIT=Off \
    -DFLB_IN_COLLECTD=off \
    -DFLB_IN_CPU=off \
    -DFLB_IN_DISK=off \
    -DFLB_IN_DOCKER=off \
    -DFLB_IN_EXEC_WASI=off \
    -DFLB_IN_FLUENTBIT_METRICS=off \
    -DFLB_IN_ELASTICSEARCH=off \
    -DFLB_IN_FORWARD=off \
    -DFLB_IN_HEAD=off \
    -DFLB_IN_HEALTH=off \
    -DFLB_IN_KMSG=off \
    -DFLB_IN_MEM=off \
    -DFLB_IN_MQTT=off \
    -DFLB_IN_NETIF=off \
    -DFLB_IN_PROC=off \
    -DFLB_IN_RANDOM=off \
    -DFLB_IN_SERIAL=off \
    -DFLB_IN_STDIN=off \
    -DFLB_IN_SYSLOG=off \
    -DFLB_IN_TCP=off \
    -DFLB_IN_THERMAL=off \
    -DFLB_IN_UDP=off \
    -DFLB_IN_WINLOG=off \
    -DFLB_IN_WINEVTLOG=off \
    -DFLB_FILTER_AWS=off \
    -DFLB_FILTER_ECS=off \
    -DFLB_FILTER_EXPECT=off \
    -DFLB_FILTER_KUBERNETES=off \
    -DFLB_FILTER_LUA=off \
    -DFLB_FILTER_MODIFY=off \
    -DFLB_FILTER_NEST=off \
    -DFLB_FILTER_PARSER=off \
    -DFLB_FILTER_REWRITE_TAG=off \
    -DFLB_FILTER_STDOUT=off \
    -DFLB_FILTER_SYSINFO=off \
    -DFLB_FILTER_THROTTLE=off \
    -DFLB_FILTER_TYPE_CONVERTER=off \
    -DFLB_FILTER_WASM=off \
    -DFLB_OUT_AZURE=off \
    -DFLB_OUT_AZURE_KUSTO=off \
    -DFLB_OUT_BIGQUERY=off \
    -DFLB_OUT_COUNTER=off \
    -DFLB_OUT_CLOUDWATCH_LOGS=off \
    -DFLB_OUT_DATADOG=off \
    -DFLB_OUT_ES=off \
    -DFLB_OUT_FILE=off \
    -DFLB_OUT_KINESIS_FIREHOSE=off \
    -DFLB_OUT_KINESIS_STREAMS=off \
    -DFLB_OUT_FLOWCOUNTER=off \
    -DFLB_OUT_GELF=off \
    -DFLB_OUT_HTTP=off \
    -DFLB_OUT_INFLUXDB=off \
    -DFLB_OUT_KAFKA=off \
    -DFLB_OUT_KAFKA_REST=off \
    -DFLB_OUT_LIB=off \
    -DFLB_OUT_NATS=off \
    -DFLB_OUT_NULL=off \
    -DFLB_OUT_PGSQL=off \
    -DFLB_OUT_PLOT=off \
    -DFLB_OUT_SLACK=off \
    -DFLB_OUT_S3=off \
    -DFLB_OUT_SPLUNK=off \
    -DFLB_OUT_STACKDRIVER=off \
    -DFLB_OUT_TCP=off \
    -DFLB_OUT_TD=off \
    -DFLB_PROCESSOR_METROCS_SELECTOR=off \
    -DFLB_PROCESSOR_LABELS=off \

%cmake_build

mkdir selinux
cp -p %{SOURCE1} selinux/
cp -p %{SOURCE2} selinux/
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp

%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{modulename}.pp %{buildroot}%{_datadir}/selinux/packages/%{modulename}.pp

%check
%ctest --exclude-regex "flb-rt-in_podman_metrics|.*\\.sh"

%files
%license LICENSE
%doc README.md
%exclude %{_prefix}/src/debug
%{_unitdir}/fluent-bit.service
%{_bindir}/*
%{_prefix}%{_sysconfdir}/fluent-bit/*

%files devel
%{_includedir}/*

%files selinux
%{_datadir}/selinux/packages/%{modulename}.pp

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{modulename}.pp

%postun selinux
%selinux_modules_uninstall -s %{selinuxtype} %{modulename}

%changelog
* Fri Jun 13 2025 Tham Jing Hui <jing.hui.tham@intel.com> - 3.1.9-12
- Include patch for CVE-2025-29087

* Tue Mar 18 2025 Ranjan Dutta <ranjan.dutta@intel.com> - 3.1.9-11
- Bump version for merge AZL tag: 3.0.20250311-3.0
- Address CVE-2024-50608 and CVE-2024-50609

* Fri Mar 07 2025 Ranjan Dutta <ranjan.dutta@intel.com> - 3.1.9-10
- Bump up the version on merge frm AZL tag 3.0.20250206-3.0
- Backport fixes for CVE-2024-27532

* Mon Jan 27 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 3.1.9-9
- Add SElinux policy to read tmp_t.

* Tue Jan 21 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 3.1.9-8
- Add SElinux policy to access rasdaemon_t.

* Thu Jan 16 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 3.1.9-7
- Add dependency for inbm-selinux

* Wed Jan 15 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 3.1.9-6
- Fix SELinux policy

* Tue Jan 14 2024 Tan Jia Yong <jia.yong.tan@intel.com> - 3.1.9-5
- Update SELinux policy to connect to otelcol_contrib
- Add dependency for otelcol-contrib-selinux

* Fri Dec 20 2024 Tan Jia Yong <jia.yong.tan@intel.com> - 3.1.9-4
- Fix SELinux policy

* Mon Dec 16 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 3.1.9-3
- Require SELinux subpackage if selinux-policy-targeted is present

* Fri Dec 13 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 3.1.9-2
- Add SELinux subpackage

* Tue Nov 23 2024 Paul Meyer <paul.meyer@microsoft.com> - 3.1.9-1
- Update to 3.1.9 to enable Lua filter plugin using system luajit library.
- Remove patches for CVE-2024-25629 and CVE-2024-28182 as they are fixed in 3.1.9.
- [Jon Slobodzian] Reconciled with Fasttrack/3.0 on 11/23, updated Changelog date from 11/5.

* Tue Aug 27 2024 Christopher Nolan <christopher.nolan@intel.com> - 3.0.7-2
- Modify compile command to only include required plugins

* Thu Jul 18 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 3.0.7-1
- Upgrade version for Edge Microvisor Toolkit.
- Updating to version 3.0.7

* Fri Nov 15 2024 Ankita Pareek <ankitapareek@microsoft.com> - 3.0.6-3
- Address CVE-2024-25431

* Tue Oct 15 2024 Chris Gunn <chrisgun@microsoft.com> - 3.0.6-2
- CVE-2024-34250
- CVE-2024-25629
- CVE-2024-28182

* Thu May 16 2024 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 3.0.3-1
- Auto-upgrade to 3.0.3 - https://microsoft.visualstudio.com/OS/_workitems/edit/50531424

* Tue Feb 20 2024 Sumedh Sharma <sumsharma@microsoft.com> - 2.2.2-1
- Upgrade to version 2.2.2

* Tue Oct 31 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 2.1.10-1
- Auto-upgrade to 2.1.10 - upgrade to latest

* Wed Sep 20 2023 Jon Slobodzian <joslobo@microsoft.com> - 2.0.9-2
- Recompile with stack-protection fixed gcc version (CVE-2023-4039)

* Fri Feb 24 2023 Olivia Crain <oliviacrain@microsoft.com> - 2.0.9-1
- Upgrade version to 2.0.9
- Use SPDX license expression in license tag
- Explicitly disable luajit

* Wed Aug 03 2022 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 1.9.6-1
- Upgrade version to 1.9.6
- Add build time dependency libyaml-devel

* Sat Feb 19 2022 Sriram Nambakam <snambakam@microsoft.com> - 1.8.12-2
- Compile with -DFLB_JEMALLOC=on.

* Tue Feb 01 2022 Cameron Baird <cameronbaird@microsoft.com> - 1.8.12-1
- Update to version 1.8.12

* Mon May 24 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 1.5.2-1
- Update to version 1.5.2

* Mon Oct 19 2020 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.4.1-2
- License verified.
- Fixed source URL.
- Added 'Vendor' and 'Distribution' tags.

* Mon Mar 30 2020 Jonathan Chiu <jochi@microsoft.com> - 1.4.1-1
- Original version for CBL-Mariner.
