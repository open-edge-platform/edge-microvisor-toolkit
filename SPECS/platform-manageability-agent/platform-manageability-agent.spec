Summary:        Platform managebility agent for out of band opration. 
Name:           platform-manageability-agent
Version:        1.0.0
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/open-edge-platform/edge-node-agents
Source0:        %{url}/archive/refs/tags/%{name}/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}.service
Source3:        env_wrapper.sh
Source4:        %{name}.sudoers
BuildRequires:  golang >= 1.24.1
BuildRequires:  systemd-rpm-macros
Requires(pre):  %{_bindir}/systemd-sysusers
Requires:       dmidecode
Requires:       rpc

%global debug_package   %{nil}
%global _build_id_links none
%global modulename      pm_agent

%description
pm-agent ensures that all required manageability features are available as soon as the OS is deployed.
and execute manageability opration on node. 



%prep
%setup -q

%build
make pmabuild GO_MOD=vendor


%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_sysusersdir}
cp %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

mkdir -p %{buildroot}%{_unitdir}
cp %{SOURCE2} %{buildroot}%{_unitdir}

install -d -m 755 %{buildroot}%{_sysconfdir}/edge-node/node/confs
install -m 644 config/platform-manageability-agent.yaml %{buildroot}%{_sysconfdir}/edge-node/node/confs/platform-manageability-agent.yaml
install -m 744 %{SOURCE3} %{buildroot}%{_sysconfdir}/edge-node/node/confs/pm-agent

mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
cp %{SOURCE5} %{buildroot}%{_sysconfdir}/sudoers.d/platform-manageability-agent

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


