Summary:        Edge node hardware information reporting
Name:           hardware-discovery-agent
Version:        1.7.1
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/open-edge-platform/edge-node-agents
Source0:        %{url}/archive/refs/tags/%{name}/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}.service
Source3:        env_wrapper.sh
Source4:        hd_agent.te
Source5:        hd_agent.fc
BuildRequires:  golang >= 1.24.1
BuildRequires:  systemd-rpm-macros
Requires(pre):  %{_bindir}/systemd-sysusers
Requires:       dmidecode
Requires:       ipmitool
Requires:       lsb-release
Requires:       lshw
Requires:       pciutils
Requires:       udev
Requires:       usbutils
Requires:       (%{name}-selinux if selinux-policy-targeted)

%global debug_package   %{nil}
%global _build_id_links none
%global selinuxtype     targeted
%global modulename      hd_agent

%description
hd-agent reports host hardware information to Edge Infrastructure Manager.
Collected hardware description consist of cpu, memory, disks,
network and usb devices.

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
%setup -q

%build
make hdabuild GO_MOD=vendor

mkdir selinux
cp -p %{SOURCE4} selinux/
cp -p %{SOURCE5} selinux/
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_sysusersdir}
cp %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

mkdir -p %{buildroot}%{_unitdir}
cp %{SOURCE2} %{buildroot}%{_unitdir}

install -d -m 755 %{buildroot}%{_sysconfdir}/edge-node/node/confs
install -m 644 config/hd-agent.yaml %{buildroot}%{_sysconfdir}/edge-node/node/confs/hd-agent.yaml
install -m 744 %{SOURCE3} %{buildroot}%{_sysconfdir}/edge-node/node/confs/hd-agent

mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
cp config/sudoers.d/hd-agent %{buildroot}%{_sysconfdir}/sudoers.d

mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
cp copyright %{buildroot}%{_defaultlicensedir}/%{name}

mkdir -p %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{modulename}.pp %{buildroot}%{_datadir}/selinux/packages/%{modulename}.pp

%files
%{_bindir}/hd-agent
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf

%config %attr(-, -, bm-agents) %{_sysconfdir}/edge-node/node/confs
%config %attr(-, hd-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/hd-agent.yaml
%config %attr(-, hd-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/hd-agent
%config %{_sysconfdir}/sudoers.d/hd-agent

%license %{_defaultlicensedir}/%{name}/copyright

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%{systemd_post %{name}.service}

%preun
%{systemd_preun %{name}.service}

%postun
%{systemd_postun_with_restart %{name}.service}

%files selinux
%{_datadir}/selinux/packages/%{modulename}.pp

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{modulename}.pp

%postun selinux
%selinux_modules_uninstall -s %{selinuxtype} %{modulename}

%changelog
* Wed Jun 04 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.7.1-1
- Add backoff/retry on northbound grpc interfaces

* Tue May 27 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.7.0-1
- Fix GPU detection when vendor information is empty
- HW Discovery Agent version 1.7.0

* Thu Apr 03 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.6.1-1
- Update common to 1.6.8

* Wed Apr 02 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.6.0-1
- Upgrade agent version

* Tue Mar 25 2025 Christopher Nolan<christopher.nolan@intel.com> - 1.5.9-1
- Update configuration and agent binary paths to use edge-node/

* Mon Mar 24 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.5.8-1
- Fix flickering status
- Update module paths
- Fix CPU Topology detection
- Send status to Node Agent
- Conditional import on common.mk

* Fri Mar 21 2025 Anuj Mittal <anuj.mittal@intel.com> - 1.4.7-13
- Bump Release to rebuild

* Tue Mar 18 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.7-12
- Add systemd service hardening settings

* Mon Mar 10 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.7-11
- Fix typo in URL

* Fri Feb 28 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.7-10
- Update URL for agents

* Wed Jan 22 2025 Anuj Mittal <anuj.mittal@intel.com> - 1.4.7-9
- Revert systemd service hardening changes

* Tue Jan 21 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.7-8
- Optimize the agent systemd service

* Fri Jan 17 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.7-7
- Add SELinux policy for root access.

* Wed Jan 15 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.7-6
- Fix SELinux policy

* Tue Jan 14 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.7-5
- Update SELinux policy to connect to otelcol_contrib 
- Update SELinux policy for var_run_t and fixed_disk_device_t
- Add dependency for otelcol-contrib-selinux

* Mon Jan 13 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.7-4
- Update ownership of agent configuration files

* Mon Jan 13 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.7-3
- Add SELinux policy to getattr and read for fixed_disk_device_t

* Fri Jan 10 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.7-2
- Add getattr permission for hd_agent to inbm_conf
- Add dependency on inbm-selinux for selinux subpackage

* Thu Jan 09 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.7-1
- Fix CVE-2024-45338. Upgrade golang.org/x/net to v0.33.0

* Mon Jan 06 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 1.4.4-9
- Update Source URL.

* Mon Dec 30 2024 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.4-8
- Add SELinux policy to allow root to read hd_agent_conf_t

* Tue Dec 24 2024 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.4-7
- Update permission to allow write access for confs directory and hd-agent.yaml

* Mon Dec 23 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.4.4-6
- Fix file permissions for hardware discovery agent configuration

* Fri Dec 20 2024 Tan Jia Yong <jia.yong.tan@intel.com> - 1.4.4-5
- Fix SELinux policy

* Tue Dec 17 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.4-4
- Fix SELinux policy

* Fri Dec 13 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.4-3
- Fix SELinux policy

* Mon Dec 02 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.4-2
- Add SELinux subpackage

* Thu Nov 21 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.4.4-1
- Update Hardware Discovery Agent to version 1.4.4

* Thu Nov 07 2024 Krzysztof Kornalewski <Krzysztof.Kornalewski@intel.com> - 1.4.1-2
- Include policies for SELinux
- Verified license

* Tue Nov 05 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.1-1
- Update grpc dependency to 1.60.1
- Fix CPU detection

* Tue Oct 15 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.4.0-7
- Remove dependency on cloud-init

* Fri Oct 04 2024 Anuj Mittal <anuj.mittal@intel.com> - 1.4.0-6
- Add dependency on cloud-init before the service is started

* Fri Sep 06 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.4.0-5
- Fix agent configuration file update on agent start

* Mon Sep 02 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.4.0-4
- Add agent service file and environment wrapper script

* Fri Aug 30 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.0-3
- Add sysusers

* Thu Aug 29 2024 Krzysztof Kornalewski <krzysztof.kornalewski@intel.com> - 1.4.0-2
- Files permissions adjusted

* Mon Aug 19 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.0-1
- Move binary from /opt to /usr/bin

* Wed Jul 24 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.3.1-1
- Original version for Edge Microvisor Toolkit.
