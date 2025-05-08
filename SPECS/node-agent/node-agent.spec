Summary:        Edge node registration and trust management
Name:           node-agent
Version:        1.6.3
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/open-edge-platform/edge-node-agents
Source0:        %{url}/archive/refs/tags/%{name}/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        env_wrapper.sh
Source3:        %{name}.conf
Source4:        node_agent.te
Source5:        node_agent.fc
BuildRequires:  golang >= 1.24.1
BuildRequires:  systemd-rpm-macros
Requires(pre):  %{_bindir}/systemd-sysusers
Requires:       caddy
Requires:       incron
Requires:       openssl
Requires:       (%{name}-selinux if selinux-policy-targeted)

%global debug_package   %{nil}
%global _build_id_links none
%global selinuxtype     targeted
%global modulename      node_agent

%description
Node Agent registers and authenticates the Edge Node with
the Edge Infrastructure Manager service. It also creates and renews
tokens for other agents running on the Edge Node. It reports status
of Edge Node to the Edge Infrastructure Manager as it onboards.

%package        selinux
Summary:        %{name} SELinux policy
Requires:       %{name} = %{version}-%{release}
Requires:       fluent-bit-selinux
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
make nabuild GO_MOD=vendor

mkdir selinux
cp -p %{SOURCE4} selinux/
cp -p %{SOURCE5} selinux/
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp

%install
make nainstall DESTDIR=%{buildroot} PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_sysusersdir}
cp %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf

mkdir -p %{buildroot}%{_unitdir}
cp %{SOURCE1} %{buildroot}%{_unitdir}

install -d -m 755 %{buildroot}%{_sysconfdir}/edge-node/node/confs
cp configs/node-agent.yaml %{buildroot}%{_sysconfdir}/edge-node/node/confs/%{name}.yaml
cp %{SOURCE2} %{buildroot}%{_sysconfdir}/edge-node/node/confs/%{name}
cp configs/san.conf %{buildroot}%{_sysconfdir}/edge-node/node/confs

mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
cp configs/sudoers.d/node-agent %{buildroot}%{_sysconfdir}/sudoers.d

mkdir -p %{buildroot}%{_sysconfdir}/caddy
cp configs/containerd.caddy %{buildroot}%{_sysconfdir}/caddy

mkdir -p %{buildroot}%{_sysconfdir}/incron.d
cp configs/incron-caddy.conf %{buildroot}%{_sysconfdir}/incron.d

mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
cp copyright %{buildroot}%{_defaultlicensedir}/%{name}

mkdir -p %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{modulename}.pp %{buildroot}%{_datadir}/selinux/packages/%{modulename}.pp

mkdir -p %{buildroot}%{_rundir}/node-agent
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/caddy
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/caddy/certs
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/caddy/.keys
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/client-credentials
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/tokens
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/tokens/attestation-manager
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/tokens/cluster-agent
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/tokens/connect-agent
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/tokens/hd-agent
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/tokens/node-agent
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/tokens/platform-observability-agent
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/tokens/platform-telemetry-agent
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/tokens/license-agent
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/tokens/platform-update-agent
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/tokens/prometheus
mkdir -p %{buildroot}%{_sysconfdir}/intel_edge_node/tokens/release-service

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf

%license %{_defaultlicensedir}/%{name}/copyright

%config %attr(-, -, bm-agents) %{_sysconfdir}/edge-node/node/confs
%config %attr(-, node-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/%{name}.yaml
%config %attr(-, node-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/%{name}
%config %{_sysconfdir}/sudoers.d/node-agent
%config %{_sysconfdir}/caddy/containerd.caddy
%config %{_sysconfdir}/incron.d/incron-caddy.conf

%dir %attr(0750, node-agent, bm-agents) %{_rundir}/node-agent
%dir %{_sysconfdir}/intel_edge_node
%dir %{_sysconfdir}/intel_edge_node/caddy
%dir %{_sysconfdir}/intel_edge_node/caddy/certs
%dir %{_sysconfdir}/intel_edge_node/caddy/.keys
%dir %{_sysconfdir}/intel_edge_node/client-credentials
%dir %{_sysconfdir}/intel_edge_node/tokens
%dir %{_sysconfdir}/intel_edge_node/tokens/attestation-manager
%dir %{_sysconfdir}/intel_edge_node/tokens/cluster-agent
%dir %{_sysconfdir}/intel_edge_node/tokens/connect-agent
%dir %{_sysconfdir}/intel_edge_node/tokens/hd-agent
%dir %{_sysconfdir}/intel_edge_node/tokens/node-agent
%dir %{_sysconfdir}/intel_edge_node/tokens/platform-observability-agent
%dir %{_sysconfdir}/intel_edge_node/tokens/platform-telemetry-agent
%dir %{_sysconfdir}/intel_edge_node/tokens/license-agent
%dir %{_sysconfdir}/intel_edge_node/tokens/platform-update-agent
%dir %{_sysconfdir}/intel_edge_node/tokens/prometheus
%dir %{_sysconfdir}/intel_edge_node/tokens/release-service

%pre
%sysusers_create_package %{name} %{SOURCE3}

%post
if ! grep -q "EnvironmentFile" "%{_unitdir}/caddy.service"; then
    sed -i '/^\[Service\]$/a EnvironmentFile=\/etc\/environment' %{_unitdir}/caddy.service
    sed -i '/^\[Service\]$/a EnvironmentFile=\/etc\/edge-node\/node\/agent_variables' %{_unitdir}/caddy.service
fi

# Add node-agent to the list of allowed user to incron
if [ ! -e "%{_sysconfdir}/incron.allow" ] || ! grep -q "node-agent" "%{_sysconfdir}/incron.allow"; then
    echo "node-agent" >> %{_sysconfdir}/incron.allow
fi

chmod -R 710 %{_sysconfdir}/intel_edge_node/caddy
chmod 700 %{_sysconfdir}/intel_edge_node/client-credentials
chmod 600 %{_sysconfdir}/intel_edge_node/client-credentials/*
chmod -R 750 %{_sysconfdir}/intel_edge_node/tokens

# Ensure path exists when node-agent starts
chown node-agent:bm-agents %{_rundir}/node-agent
chmod 750 %{_rundir}/node-agent

# Ensure file exists when incron starts
touch %{_sysconfdir}/intel_edge_node/tokens/release-service/access_token
chmod 640 %{_sysconfdir}/intel_edge_node/tokens/release-service/access_token

# create self signed cert for Containerd with SAN
if [ ! -e "%{_sysconfdir}/intel_edge_node/caddy/certs/caddy-containerd-cert.pem" ]; then
    openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout %{_sysconfdir}/intel_edge_node/caddy/.keys/caddy-containerd-key.pem -out %{_sysconfdir}/intel_edge_node/caddy/certs/caddy-containerd-cert.pem -config %{_sysconfdir}/edge-node/node/confs/san.conf -extensions 'v3_req'
    cp %{_sysconfdir}/intel_edge_node/caddy/certs/caddy-containerd-cert.pem %{_sysconfdir}/pki/ca-trust/source/anchors/caddy-containerd-cert.crt
fi

chmod 600 %{_sysconfdir}/intel_edge_node/caddy/.keys/caddy-containerd-key.pem

# Entry for containerd proxy, Not adding to no_proxy as .internal expected
if ! grep -q "127.0.0.1 localhost.internal localhost" "%{_sysconfdir}/hosts"; then
    echo "127.0.0.1 localhost.internal localhost" >> %{_sysconfdir}/hosts
fi

update-ca-trust

# Add single line in main Caddyfile to use the other *.caddy files
echo "import %{_sysconfdir}/caddy/*.caddy" > %{_sysconfdir}/caddy/Caddyfile

# Update file/dir ownership
chown -R node-agent:bm-agents %{_sysconfdir}/intel_edge_node
chown -R caddy:caddy %{_sysconfdir}/intel_edge_node/caddy
usermod -a -G bm-agents caddy

chmod 750 %{_sysconfdir}/caddy
chmod 640 %{_sysconfdir}/caddy/*
chown -R node-agent:bm-agents %{_sysconfdir}/caddy

# Restart incron to ensure it loads the new rule
systemctl restart incrond
# Restart caddy as systemd service file is updated
systemctl daemon-reload
systemctl restart caddy

chmod 644 %{_sysconfdir}/edge-node/node/confs/%{name}.yaml
chmod 744 %{_sysconfdir}/edge-node/node/confs/%{name}
chmod 750 %{_sysconfdir}/caddy

%systemd_post %{name}.service

%preun
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
* Mon May 05 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.6.3-1
- Update release service token handling for anonymous

* Thu Apr 03 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.6.2-1
- Update common to 1.6.8

* Wed Apr 02 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.6.0-1
- Upgrade agent version

* Sat Mar 29 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.5.12-6
- Fix typo in env_wrapper.sh

* Fri Mar 28 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.5.12-5
- Configure systemd unit to create runtime directory

* Fri Mar 28 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.5.12-4
- Create directory for connect agent's access token

* Fri Mar 28 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.5.12-3
- Add dir directive for run/node-agent

* Tue Mar 25 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.5.12-2
- Add agent variable as env in caddy as well

* Tue Mar 25 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.5.12-1
- Update configuration and agent binary paths to use edge-node/

* Tue Mar 25 2025 Andrea Campanella <andrea.campanella@intel.com> - 1.5.11-2
- Move from RSTYPE to RS_TYPE in wrapper for node-agent

* Mon Mar 24 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.5.11-1
- Add token folder for attestation manager service
- Support to monitor network endpoints for status
- Add status service implementation

* Fri Mar 21 2025 Anuj Mittal <anuj.mittal@intel.com> - 1.4.4-14
- Bump Release to rebuild

* Tue Mar 18 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.4-13
- Add systemd service hardening settings

* Mon Mar 10 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.4-12
- Fix typo in URL

* Mon Mar 10 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.4-11
- Update node agent to support no-auth release service

* Mon Mar 10 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.4-10
- Update URL for agents

* Fri Feb 28 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.4-9
- Add token folder for new edge node service

* Wed Jan 22 2025 Anuj Mittal <anuj.mittal@intel.com> - 1.4.4-8
- Revert systemd service hardening changes

* Tue Jan 21 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.4-7
- Optimize the agent systemd service

* Fri Jan 17 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.4-6
- Add SELinux policy for root access.

* Wed Jan 15 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.4-5
- Fix SELinux policy

* Tue Jan 14 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.4-4
- Update SELinux policy to connect to otelcol_contrib and write in var_run_t
- Add dependency for otelcol-contrib-selinux

* Mon Jan 13 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.4-3
- Update ownership of agent configuration files

* Mon Jan 13 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.4-2
- Add SELinux policy to do system module_request

* Thu Jan 09 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.4-1
- Fix CVE-2024-45338. Upgrade golang.org/x/net to v0.33.0
- Fix CVE-2024-51744. Upgrade github.com/golang-jwt/jwt/v4 to v4.5.1

* Mon Jan 06 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 1.4.2-7
- Update Source URL.

* Mon Dec 30 2024 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.2-6
- Add SELinux policy to allow root to read node_agent_conf_t

* Tue Dec 24 2024 Jia Yong Tan <jia.yong.tan@intel.com> - 1.4.2-5
- Update permission to allow write access for confs directory and node-agent.yaml

* Mon Dec 23 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.4.2-4
- Fix file permissions for node agent configuration

* Fri Dec 20 2024 Tan Jia Yong <jia.yong.tan@intel.com> - 1.4.2-3
- Fix SELinux policy

* Tue Dec 17 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.2-2
- Fix SELinux policy

* Mon Dec 16 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.2-1
- Revert tenant ID changes from 1.3.4
- Fix SELinux policy

* Fri Dec 13 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.1-3
- Fix SELinux policy

* Mon Dec 02 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.1-2
- Add SELinux subpackage

* Thu Nov 21 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.4.1-1
- Reduce delay for the first heartbeat
- Add reporting OS boot statistics
- Add node agent to adm group

* Fri Nov 08 2024 Krzysztof Kornalewski <Krzysztof.Kornalewski@intel.com> - 1.3.4-2
- Include policies for SELinux

* Tue Oct 29 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.3.4-1
- Create tenant ID file if it doesn't exist
- License verified

* Tue Oct 15 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.3.2-3
- Remove dependency on cloud-init

* Fri Oct 04 2024 Anuj Mittal <anuj.mittal@intel.com> - 1.3.2-2
- Add dependency on cloud-init before the service is started

* Mon Sep 16 2024 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.3.2-1
- Eliminate pua.caddy config file 

* Thu Sep 12 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.3.1-7
- Add missing file permission settings

* Tue Sep 10 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.3.1-6
- Add missing caddy file install

* Fri Sep 06 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.3.1-5
- Fix agent configuration file updated on agent start

* Mon Sep 02 2024 Christopher Nolan <christopher.nolan@intel.com> - 1.3.1-4
- Update agent service file, environment wrapper script and post install stage

* Fri Aug 30 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.3.1-3
- Store config in /etc/edge-node/node/confs
- Add sysusers

* Thu Aug 29 2024 Krzysztof Kornalewski <krzysztof.kornalewski@intel.com> - 1.3.1-2
- Files permissions adjusted

* Mon Aug 26 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.3.1-1
- Retrieve Edge Node's UUID instead of build machine's

* Mon Aug 19 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.3.0-1
- Move binary from /opt to /usr/bin

* Thu Jul 25 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.2.4-2
- Bump release to rebuild with go 1.21.11

* Thu Jun 27 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.2.4-1
- Original version for Edge Microvisor Toolkit.
