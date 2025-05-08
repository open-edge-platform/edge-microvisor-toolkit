Summary:        Installs/uninstalls orchestration software on an edge node using command obtained from Cluster Orchestrator.
Name:           cluster-agent
Version:        1.6.2
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit 
URL:            https://github.com/open-edge-platform/edge-node-agents
Source0:        %{url}/archive/refs/tags/%{name}/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        env_wrapper.sh
Source3:        %{name}.conf
Source4:        rke2-path.conf
Source5:        cluster-agent.sudoers
Source6:        cluster_agent.te
Source7:        cluster_agent.fc
BuildRequires:  golang >= 1.24.1
BuildRequires:  systemd-rpm-macros
Requires(pre):  %{_bindir}/systemd-sysusers
Requires:       curl
Requires:       (%{name}-selinux if selinux-policy-targeted)

%global debug_package   %{nil}
%global _build_id_links none
%global selinuxtype     targeted
%global modulename      cluster_agent

%description
Cluster Agent is part of Edge Node Zero Touch Provisioning.
Its main responsibility is to register in Cluster Orchestrator service and bootstrap Kubernetes Engine on to the node on which it is executing.

%package        selinux
Summary:        %{name} SELinux policy
Requires:       %{name} = %{version}-%{release}
Requires:       fluent-bit-selinux
Requires:       hardware-discovery-agent-selinux
Requires:       inbm-selinux
Requires:       node-agent-selinux
Requires:       otelcol-contrib-selinux
Requires:       platform-telemetry-agent-selinux
Requires:       platform-update-agent-selinux
Requires:       telegraf-selinux
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildArch:      noarch
%{?selinux_requires}

%description    selinux
SELinux policy for %{name}.

%prep
%setup -q

%build
make cabuild GO_MOD=vendor

mkdir selinux
cp -p %{SOURCE6} selinux/
cp -p %{SOURCE7} selinux/
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp

%install
make cainstall DESTDIR=%{buildroot} PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_sysusersdir}
cp %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf

mkdir -p %{buildroot}%{_unitdir}
cp %{SOURCE1} %{buildroot}%{_unitdir}

install -d -m 755 %{buildroot}%{_sysconfdir}/edge-node/node/confs
install -m 644 configs/cluster-agent.yaml %{buildroot}%{_sysconfdir}/edge-node/node/confs/%{name}.yaml
install -m 744 %{SOURCE2} %{buildroot}%{_sysconfdir}/edge-node/node/confs/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
cp %{SOURCE5} %{buildroot}%{_sysconfdir}/sudoers.d/cluster-agent

mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/rancher-system-agent.service.d
cp configs/rancher-system-agent.service.d/caddy.conf %{buildroot}%{_sysconfdir}/systemd/system/rancher-system-agent.service.d
cp %{SOURCE4} %{buildroot}%{_sysconfdir}/systemd/system/rancher-system-agent.service.d

mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
cp copyright %{buildroot}%{_defaultlicensedir}/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/rancher
mkdir -p %{buildroot}%{_sysconfdir}/cni
mkdir -p %{buildroot}%{_sysconfdir}/kubernetes
mkdir -p %{buildroot}%{_var}/lib/rancher

mkdir -p %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{modulename}.pp %{buildroot}%{_datadir}/selinux/packages/%{modulename}.pp

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysconfdir}/rancher
%{_var}/lib/rancher
%{_sysconfdir}/kubernetes
%{_sysconfdir}/cni

%{_sysusersdir}/%{name}.conf
%config %attr(-, -, bm-agents) %{_sysconfdir}/edge-node/node/confs
%config %attr(-, cluster-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/%{name}.yaml
%config %attr(-, cluster-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/%{name}
%config %{_sysconfdir}/systemd/system/rancher-system-agent.service.d
%config %{_sysconfdir}/sudoers.d/cluster-agent
%license %{_defaultlicensedir}/%{name}/copyright

%pre
%sysusers_create_package %{name} %{SOURCE3}

%post
%systemd_post %{name}.service

%preun
# Before uninstallation, stop the service
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files selinux
%{_datadir}/selinux/packages/%{modulename}.pp

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{modulename}.pp

%postun selinux
%selinux_modules_uninstall -s %{selinuxtype} %{modulename}

%changelog
* Mon May 05 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.6.2-1
- Fix readiness reporting to NA during cluster install

* Thu Apr 03 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.6.1-1
- Update common to 1.6.8

* Wed Apr 02 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.6.0-1
- Upgrade agent version

* Thu Mar 27 2025 Hemanthkumar Sm <hemanthkumar.sm@intel.com> - 1.5.11-2
- Add user entries for tc-agent and tc-ima in cluster-agent configuration

* Tue Mar 25 2025 Nolan Christopher <christopher.nolan@intel.com> - 1.5.11-1
- Update configuration and agent binary paths to use edge-node/

* Mon Mar 24 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.5.10-1
- Update CO API version to 0.3.10
- Cluster Agent status client

* Fri Mar 21 2025 Anuj Mittal <anuj.mittal@intel.com> - 1.4.2-12
- Bump Release to rebuild

* Tue Mar 18 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.2-11
- Add systemd service hardening settings

* Mon Mar 10 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.2-10
- Fix typo in URL

* Fri Feb 28 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.2-9
- Update URL for agents

* Wed Feb 26 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.2-8
- Set nologin shell for cluster agent

* Wed Jan 22 2025 Anuj Mittal <anuj.mittal@intel.com> - 1.4.2-7
- Revert systemd service hardening changes

* Tue Jan 21 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.2-6
- Optimize the agent systemd service

* Fri Jan 17 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.2-5
- Add SELinux policy for root access.

* Wed Jan 15 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.2-4
- Fix SELinux policy

* Tue Jan 14 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.2-3
- Update SELinux policy to connect to otelcol_contrib
- Add otelcol-contrib-selinux as dependency

* Fri Jan 10 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.2-2
- Update ownership of agent configuration files

* Thu Jan 09 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.2-1
- Fix CVE-2024-45338. Upgrade golang.org/x/net to v0.33.0

* Mon Jan 06 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 1.4.0-6
- Update Source URL.

* Mon Dec 30 2024 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.0-5
- Add SELinux policy to allow root to read cluster_agent_conf_t

* Tue Dec 24 2024 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.0-4
- Update permission to allow write access for confs directory and cluster-agent.yaml

* Mon Dec 23 2024 Christopher Nolan <christopher.nolan@intel.com> 1.4.0-3
- Fix file permissions for cluster agent configuration

* Fri Dec 20 2024 Tan Jia Yong <jia.yong.tan@intel.com> - 1.4.0-2
- Fix SELinux policy

* Mon Dec 16 2024 Niket Kumar <niket.kumar@intel.com> 1.4.0-1
- Patch RKE2 uninstall script when running on Edge Microvisor Toolkit (rm /etc/cni -> rm /etc/cni/*)
- Remove logical volumes from Edge Node after cluster deletion

* Mon Dec 16 2024 Tan, Jia Yong <jia.yong.tan@intel.com> - 1.3.7-4
- Fix incorrect SELinux permission in cluster_agent.te

* Fri Dec 13 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.3.7-3
- Fix SELinux policy

* Mon Dec 02 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.3.7-2
- Add SELinux subpackage

* Tue Nov 26 2024 Andy <andy.peng@intel.com> - 1.3.7-1
- Bump version to 1.3.7

* Fri Nov 08 2024 Krzysztof Kornalewski <krzysztof.kornalewski@intel.com> - 1.3.6-3
- Include policies for SELinux

* Fri Nov 08 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.3.6-2
- Change login shell to /usr/bin/sh for cluster-agent
- Add Edge Microvisor Toolkit specific sudoers config

* Tue Nov 05 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.3.6-1
- Update grpc dependency to 1.60.1

* Tue Oct 15 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.3.3-12
- Remove dependency on cloud-init

* Tue Oct 08 2024 Niket Kumar <niket.kumar@intel.com> - 1.3.3-11
- Added rancher path in cluster agent service env 

* Fri Oct 04 2024 Anuj Mittal <anuj.mittal@intel.com> - 1.3.3-10
- Add dependency on cloud-init before the service is started

* Thu Oct 03 2024 Niket Kumar <niket.kumar@intel.com> - 1.3.3-9
- Added rke2 server path to rancher service 

* Sat Sep 14 2024 Anuj Mittal <anuj.mittal@intel.com> - 1.3.3-8
- Make sure new directories are packaged

* Fri Sep 13 2024 Anuj Mittal <anuj.mittal@intel.com> - 1.3.3-7
- Include directories needed for kubernetes

* Mon Sep 09 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.3.3-6
- Create /etc/rancher and /var/lib/rancher directories for rancher setup

* Fri Sep 06 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.3.3-5
- Fix agent configuration file update on agent start

* Mon Sep 02 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.3.3-4
- Update agent service file and environment wrapper script

* Fri Aug 30 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.3.3-3
- Store config in /etc/edge-node/node/confs
- Add sysusers

* Thu Aug 29 2024 Krzysztof Kornalewski <krzysztof.kornalewski@intel.com> - 1.3.3-2
- Files permissions adjusted

* Mon Aug 26 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.3.3-1
- Retrieve Edge Node's UUID instead of build machine's

* Mon Aug 19 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.3.2-1
- Move binary from /opt to /usr/bin

* Mon Aug 05 2024 Krzysztof Kornalewski <krzysztof.kornalewski@intel.com> - 1.3.1-1
- Original version for Edge Microvisor Toolkit. License verified.
