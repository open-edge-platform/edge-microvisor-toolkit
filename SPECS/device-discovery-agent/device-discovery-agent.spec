Summary:        Device Discovery Agent for Edge Node
Name:           device-discovery-agent
Epoch:          1
Version:        1.0.1
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/open-edge-platform/edge-node-agents
Source0:        %{url}/archive/refs/tags/%{name}/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}.service
Source3:        %{name}-%{version}-vendor.tar.gz
BuildRequires:  golang < 1.26
BuildRequires:  golang >= 1.25.5
BuildRequires:  systemd-rpm-macros
Requires(pre):  %{_bindir}/systemd-sysusers
Requires:       dmidecode

%global debug_package   %{nil}
%global _build_id_links none

%description
device-discovery-agent discovers and onboards edge devices.
The Device Discovery Agent automatically discovers device hardware information,
registers devices with the onboarding manager, and facilitates both interactive
and non-interactive onboarding workflows for edge nodes.

%prep
%setup -q -n edge-node-agents-device-discovery-agent-v%{version}
tar -xzf %{SOURCE3} -C device-discovery-agent

%build
export GOEXPERIMENT=nosystemcrypto
make -C device-discovery-agent ddabuild GO_MOD=vendor

%install
make -C device-discovery-agent install DESTDIR=%{buildroot} PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_sysusersdir}
cp %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

mkdir -p %{buildroot}%{_unitdir}
cp %{SOURCE2} %{buildroot}%{_unitdir}

mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
cp device-discovery-agent/configs/sudoers.d/device-discovery-agent %{buildroot}%{_sysconfdir}/sudoers.d

install -d -m 755 %{buildroot}%{_sysconfdir}/edge-node/node/confs

install -d -m 700 %{buildroot}%{_sysconfdir}/intel_edge_node
install -d -m 700 %{buildroot}%{_sysconfdir}/intel_edge_node/client-credentials

install -d -m 755 %{buildroot}%{_localstatedir}/log/client-auth

mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
cp device-discovery-agent/debian/copyright %{buildroot}%{_defaultlicensedir}/%{name}

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf

%config %{_sysconfdir}/sudoers.d/device-discovery-agent

%dir %{_sysconfdir}/edge-node
%dir %{_sysconfdir}/edge-node/node
%dir %attr(0755, device-discovery-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs

%dir %attr(0700, device-discovery-agent, bm-agents) %{_sysconfdir}/intel_edge_node
%dir %attr(0700, device-discovery-agent, bm-agents) %{_sysconfdir}/intel_edge_node/client-credentials

%dir %attr(0755, device-discovery-agent, bm-agents) %{_localstatedir}/log/client-auth

%license %{_defaultlicensedir}/%{name}/copyright

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog
* Wed Apr 08 2026 Piyush Panigrahi <piyush.panigrahi@intel.com> - 1:1.0.1-1
- Original version for Edge Microvisor Toolkit. License verified.
