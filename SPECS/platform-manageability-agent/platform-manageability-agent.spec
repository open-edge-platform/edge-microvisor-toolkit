Summary:        Platform managebility agent for out of band opration. 
Name:           platform-manageability-agent
Version:        0.4.7
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/open-edge-platform/edge-node-agents
Source0:        %{url}/archive/refs/tags/%{name}/v%{version}.tar.gz#/pm-agent-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}.service
Source3:        env_wrapper.sh
Source4:        %{name}.sudoers
BuildRequires:  golang < 1.26
BuildRequires:  golang >= 1.25.5
BuildRequires:  systemd-rpm-macros
Requires:       rpc

%global debug_package   %{nil}
%global _build_id_links none
%global modulename      pm_agent

%description
platform-manageability-agent detects what manageability features are available after the OS is deployed
and performs device management operations requested by users.

%prep
%autosetup -n pm-agent-%{version}

%build
export GOEXPERIMENT=nosystemcrypto
make pmabuild GO_MOD=vendor


%install
make pmainstall DESTDIR=%{buildroot} PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_sysusersdir}
cp %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

mkdir -p %{buildroot}%{_unitdir}
cp %{SOURCE2} %{buildroot}%{_unitdir}

install -d -m 755 %{buildroot}%{_sysconfdir}/edge-node/node/confs
install -m 644 configs/platform-manageability-agent.yaml %{buildroot}%{_sysconfdir}/edge-node/node/confs/platform-manageability-agent.yaml
install -m 744 %{SOURCE3} %{buildroot}%{_sysconfdir}/edge-node/node/confs/pm-agent

mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
cp %{SOURCE4} %{buildroot}%{_sysconfdir}/sudoers.d/platform-manageability-agent

mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
cp copyright %{buildroot}%{_defaultlicensedir}/%{name}


%files
%{_bindir}/pm-agent
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf

%config %attr(-, -, bm-agents) %{_sysconfdir}/edge-node/node/confs
%config %attr(-, pm-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/platform-manageability-agent.yaml
%config %attr(-, pm-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/pm-agent
%config %{_sysconfdir}/sudoers.d/platform-manageability-agent

%license %{_defaultlicensedir}/%{name}/copyright

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%{systemd_post %{name}.service}

%preun
%{systemd_preun %{name}.service}

%postun
%{systemd_postun_with_restart %{name}.service}

%changelog
* Mon Mar 11 2026 Ipsita Nayak <ipsita.nayak@intel.com> - 0.4.7-1
- Updated PMA Version.
- Added activation progress flag.

* Mon Mar 02 2026 Jagrat Acharya <jagrat.acharya@intel.com> - 0.4.4-1
- Updated PMA Version.
- Introduced ACM mode for Vpro.

* Fri Feb 20 2026 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 0.4.3-1
- Update to golang 1.25.7

* Fri Feb 06 2026 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 0.4.1-1
- Update to golang 1.25.5

* Thu Nov 20 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 0.3.1-1
- Update to golang 1.24.9
- Fix CVE-2025-47913

* Mon Nov 10 2025 Jagrat Acharya <jagrat.acharya@intel.com> - 0.2.2-1
- Updated PMA Version.
- PMA User Lock issue fixed.

* Mon Oct 31 2025 Ipsita Nayak <ipsita.nayak@intel.com> - 0.2.1-1
- Updated PMA Version.
- PMA Error Handling.

* Mon Oct 13 2025 Ipsita Nayak <ipsita.nayak@intel.com> - 0.2.0-1
- Updated PMA Version.
- Support AMT feature capabilities.

* Fri Oct 3 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 0.1.8-2
- build with golang < 1.25

* Tue Aug 12 2025 Jagrat Acharya <jagrat.acharya@intel.com> - 0.1.8-1
- Updated PMA Version.
- Fix for PROFILE enviroment variable for secure profile name.
- Fix for Ready status for host.

* Fri Aug 8 2025 Jagrat Acharya <jagrat.acharya@intel.com> - 0.1.7-1
- Updated PMA Version.
- Updated sudoers file for AMT Password
- Fix status reporting when vPRO disabled


* Wed Jul 30 2025 Jagrat Acharya <jagrat.acharya@intel.com> - 0.1.3-1
- Binary name updated in spec file.
- Original version for Edge Microvisor Toolkit. License verified.


