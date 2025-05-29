Summary:        Platform Observability Agent
Name:           platform-observability-agent
Version:        1.8.0
Release:        3%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/open-edge-platform/edge-node-agents
Source0:        %{url}/archive/refs/tags/%{name}/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        platform-observability-collector.service
Source2:        platform-observability-health-check.service
Source3:        platform-observability-logging.service
Source4:        platform-observability-metrics.service
Source5:        env_wrapper_collector.sh
Source6:        env_wrapper_health_check.sh
Source7:        env_wrapper_logging.sh
Source8:        %{name}.conf
BuildRequires:  systemd-rpm-macros
Requires:       fluent-bit
Requires:       ipmitool
Requires:       jq
Requires:       otelcol-contrib
Requires:       rasdaemon
Requires:       smartmontools
Requires:       telegraf
Requires(pre):  %{_bindir}/systemd-sysusers

%description
Platform Observability Agent is a common log scraper handling logs from all Bare Metal Agents.
The agent also handles installation of Telegraf as telemetry metrics source, as well as installation of OpenTelemetry Collector serving as metrics endpoint.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_sysusersdir}
cp %{SOURCE8} %{buildroot}%{_sysusersdir}/%{name}.conf

mkdir -p %{buildroot}%{_unitdir}
cp %{SOURCE1} %{buildroot}%{_unitdir}/platform-observability-collector.service
cp %{SOURCE2} %{buildroot}%{_unitdir}/platform-observability-health-check.service
cp %{SOURCE3} %{buildroot}%{_unitdir}/platform-observability-logging.service
cp %{SOURCE4} %{buildroot}%{_unitdir}/platform-observability-metrics.service

install -d -m 755 %{buildroot}%{_sysconfdir}/edge-node/node/confs
install -m 740 %{SOURCE5} %{buildroot}%{_sysconfdir}/edge-node/node/confs/platform-observability-collector
install -m 740 %{SOURCE6} %{buildroot}%{_sysconfdir}/edge-node/node/confs/platform-observability-health-check
install -m 740 %{SOURCE7} %{buildroot}%{_sysconfdir}/edge-node/node/confs/platform-observability-logging
install -m 740 %{SOURCE7} %{buildroot}%{_sysconfdir}/edge-node/node/confs/platform-observability-metrics

mkdir -p %{buildroot}%{_sysconfdir}/fluent-bit
cp configs/fluent-bit.conf %{buildroot}%{_sysconfdir}/fluent-bit

mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
cp configs/sudoers.d/platform-observability-agent %{buildroot}%{_sysconfdir}/sudoers.d

mkdir -p %{buildroot}%{_sysconfdir}/health-check
cp configs/microvisor-health-check.conf %{buildroot}%{_sysconfdir}/health-check/health-check.conf

mkdir -p %{buildroot}%{_sysconfdir}/telegraf
mkdir -p %{buildroot}%{_sysconfdir}/telegraf/telegraf.d/
cp configs/poa-telegraf.conf %{buildroot}%{_sysconfdir}/telegraf/telegraf.d/poa-telegraf.conf

mkdir -p %{buildroot}%{_sysconfdir}/otelcol
cp configs/otelcol.yaml %{buildroot}%{_sysconfdir}/otelcol


mkdir -p %{buildroot}/opt/telegraf/bin/
cp scripts/collect_gpu_metrics.sh %{buildroot}/opt/telegraf/bin/
cp scripts/collect_disk_info.sh %{buildroot}/opt/telegraf/bin/
cp scripts/core_metrics.sh %{buildroot}/opt/telegraf/bin/

mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
cp copyright %{buildroot}%{_defaultlicensedir}/%{name}

mkdir -p %{buildroot}%{_var}/log/edge-node/poa
mkdir -p %{buildroot}%{_rundir}/platform-observability-agent/fluent-bit

%files
%{_sysusersdir}/%{name}.conf
%config %{_sysconfdir}/sudoers.d/platform-observability-agent
%config %attr(-, -, bm-agents) %{_sysconfdir}/edge-node/node/confs
%config %attr(-, platform-observability-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/platform-observability-collector
%config %attr(-, platform-observability-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/platform-observability-health-check
%config %attr(-, platform-observability-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/platform-observability-logging
%config %attr(-, platform-observability-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/platform-observability-metrics
%config %attr(-, platform-observability-agent, bm-agents) %{_sysconfdir}/fluent-bit/fluent-bit.conf
%config %attr(-, platform-observability-agent, bm-agents) %{_sysconfdir}/health-check/health-check.conf
%config %attr(-, platform-observability-agent, bm-agents) %{_sysconfdir}/telegraf/telegraf.d/poa-telegraf.conf
%config %attr(-, platform-observability-agent, bm-agents) %{_sysconfdir}/otelcol/otelcol.yaml

%{_unitdir}/platform-observability-logging.service
%config %attr(-, platform-observability-agent, bm-agents) %{_sysconfdir}/fluent-bit
%dir %attr(-, platform-observability-agent, bm-agents) %{_var}/log/edge-node/poa
%dir %attr(-, platform-observability-agent, bm-agents) %{_rundir}/platform-observability-agent/fluent-bit

%{_unitdir}/platform-observability-health-check.service
%attr(-, platform-observability-agent, bm-agents) %config %{_sysconfdir}/health-check

%{_unitdir}/platform-observability-metrics.service
%config %{_sysconfdir}/telegraf/telegraf.d/poa-telegraf.conf
%attr(-, platform-observability-agent, bm-agents) /opt/telegraf/bin/collect_gpu_metrics.sh
%attr(-, platform-observability-agent, bm-agents) /opt/telegraf/bin/core_metrics.sh
%attr(-, platform-observability-agent, bm-agents) /opt/telegraf/bin/collect_disk_info.sh

%{_unitdir}/platform-observability-collector.service
%config %attr(-, platform-observability-agent, bm-agents) %{_sysconfdir}/otelcol

%license %{_defaultlicensedir}/%{name}/copyright

%pre
%sysusers_create_package %{name} %{SOURCE8}

%post
%{systemd_post platform-observability-collector.service}
%{systemd_post platform-observability-health-check.service}
%{systemd_post platform-observability-logging.service}
%{systemd_post platform-observability-metrics.service}

%preun
%{systemd_preun platform-observability-collector.service}
%{systemd_preun platform-observability-health-check.service}
%{systemd_preun platform-observability-logging.service}
%{systemd_preun platform-observability-metrics.service}

%postun
%{systemd_postun_with_restart platform-observability-collector.service}
%{systemd_postun_with_restart platform-observability-health-check.service}
%{systemd_postun_with_restart platform-observability-logging.service}
%{systemd_postun_with_restart platform-observability-metrics.service}

%changelog
* Tue May 06 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.8.0-3
- Update file permissions for agent wrapper scripts

* Fri Apr 11 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.8.0-2
- Update log and metrics service to start after collector service

* Wed Apr 02 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.8.0-1
- Upgrade agent version

* Tue Mar 25 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.7.6-1
- Update configuration and agent binary paths to use edge-node/

* Mon Mar 24 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.7.5-1
- Update dependencies

* Tue Mar 18 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.7.2-4
- Add systemd service hardening settings

* Mon Mar 10 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.7.2-3
- Fix typo in URL

* Mon Mar 10 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.7.2-2
- Update URL for agents

* Mon Mar 03 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.7.2-1
- Update agent version to use new storage path

* Fri Feb 28 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.6.1-3
- Update log storage path for agent

* Tue Feb 11 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.6.1-2
- Fix collector's wrapper script

* Fri Feb 07 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.6.1-1
- Update health check config file name

* Wed Jan 22 2025 Anuj Mittal <anuj.mittal@intel.com> - 1.5.10-3
- Revert systemd service hardening changes

* Tue Jan 21 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.5.10-2
- Optimize the agent systemd service

* Mon Jan 20 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.5.10-1
- Disable internal metrics collection for collector service

* Tue Jan 14 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.5.9-1
- Remove License Agent status reporting
- Don't use yq

* Mon Jan 06 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.5.6-5
- Update ownership of agent configuration files

* Tue Dec 31 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.5.6-4
- Update Source URL.

* Tue Dec 24 2024 Jia Yong Tan <jia.yong.tan@intel.com> - 1.5.6-3
- Update permission to allow write access for confs directory

* Mon Dec 23 2024 Lee Chee Yang <chee.yang.lee@intel.com> - 1.5.6-2
- Fix file permissions for agent configuration

* Fri Nov 08 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.5.6-1
- Fix health check config syntax error
- Use dummy TENANT_ID value if tenant ID file is not present

* Tue Nov 05 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.5.4-1
- Fix TENANT_ID reference in otelcol config
- Add projectId to otel attributes and headers
- Update default collection intervals
- Add new entries for checking SELinux profile status to health check service

* Tue Oct 15 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.5.2-8
- Remove dependency on cloud-init

* Fri Oct 04 2024 Anuj Mittal <anuj.mittal@intel.com> - 1.5.2-7
- Add dependency on cloud-init before the service is started

* Fri Sep 13 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.5.2-6
- Split environment wrapper script between services

* Fri Sep 06 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.5.2-5
- Fix agent configuration file update on agent start

* Mon Sep 02 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.5.2-4
- Update agent service files and environment wrapper script

* Fri Aug 30 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.5.2-3
- Store config in /etc/edge-node/node/confs
- Add sysusers and systemd service macros

* Thu Aug 29 2024 Krzysztof Kornalewski <krzysztof.kornalewski@intel.com> - 1.5.2-2
- Files permissions adjusted

* Mon Aug 26 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.5.2-1
- Retrieve Edge Node's UUID and hostname instead of build machine's

* Tue Aug 20 2024 Krzysztof Kornalewski <krzysztof.kornalewski@intel.com> - 1.5.1-1
- Remove AA from health-check config file
- Correct bin locations in service files

* Tue Aug 06 2024 Krzysztof Kornalewski <krzysztof.kornalewski@intel.com> - 1.5.0-2
- Update service file names.

* Mon Aug 05 2024 Krzysztof Kornalewski <krzysztof.kornalewski@intel.com> - 1.5.0-1
- Update POA tarball version

* Wed Jul 31 2024 Chee Yang <chee.yang.lee@intel.com> - 1.4.3-2
- Fix conflict telegraf.conf

* Thu Jul 25 2024 Krzysztof Kornalewski <krzysztof.kornalewski@intel.com> - 1.4.3-1
- Original version for Edge Microvisor Toolkit. License verified.
