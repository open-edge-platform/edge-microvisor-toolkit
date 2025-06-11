Summary:        An agent gathering statistics from Open Edge Platform installations
Name:           reporting-agent
Version:        0.0.3
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/open-edge-platform/edge-node-agents
Source0:        %{url}/archive/refs/tags/%{name}/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        edge-node-metrics.cron
Source3:        reporting-agent.yaml

BuildRequires:  golang >= 1.24.1

Requires(pre):  %{_bindir}/systemd-sysusers

Requires:       cronie
Requires:       dmidecode
Requires:       lsb-release
Requires:       lshw

%description
Reporting agent gathering statistics from Open Edge Platform installations. This agent is triggered by a cron job hourly and at system startup.

%prep
%setup -q

%build
make build

%install
# Install binary from the build directory
install -Dm755 build/%{name} %{buildroot}%{_bindir}/%{name}

# Create user
install -Dm644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

# Install cron job
install -Dm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/cron.d/edge-node-metrics.cron

# Install sudoers file
mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
cp config/sudoers.d/reporting-agent %{buildroot}%{_sysconfdir}/sudoers.d/

# Create metrics and log directories with correct permissions
install -d -m 755 -o reporting-agent -g bm-agents %{buildroot}%{_sysconfdir}/edge-node/metrics
install -d -m 755 -o reporting-agent -g bm-agents %{buildroot}%{_var}/log/edge-node

# Install config file
install -Dm644 %{SOURCE3} %{buildroot}%{_sysconfdir}/edge-node/metrics/reporting-agent.yaml

%files
%{_sysusersdir}/%{name}.conf
%{_bindir}/reporting-agent
%config %{_sysconfdir}/sudoers.d/reporting-agent
%config %{_sysconfdir}/cron.d/edge-node-metrics.cron
%dir %attr(0755,reporting-agent,bm-agents) %{_sysconfdir}/edge-node/metrics
%config(noreplace) %{_sysconfdir}/edge-node/metrics/reporting-agent.yaml
%dir %attr(0755,reporting-agent,bm-agents) %{_var}/log/edge-node

%pre
%sysusers_create_package %{name} %{SOURCE1}

%license %{_defaultlicensedir}/%{name}/copyright

%changelog
* Wed Jun 11 2025 Jakub Sikorski <jakub.sikorski@intel.com> - 0.0.3-1
- Original version for Edge Microvisor Toolkit
