Summary:        An agent gathering statistics from Open Edge Platform installations
Name:           reporting-agent
Version:        0.0.4
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/open-edge-platform/edge-node-agents
Source0:        %{url}/archive/refs/tags/%{name}/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        edge-node-metrics.cron

BuildRequires:  golang >= 1.24.1
BuildRequires:  systemd-rpm-macros

Requires(pre):  %{_bindir}/systemd-sysusers

Requires:       cronie
Requires:       dmidecode
Requires:       lsb-release
Requires:       lshw
Requires:       util-linux

%global debug_package   %{nil}
%global _build_id_links none

%description
Reporting agent gathering statistics from Open Edge Platform installations. This agent is triggered by a cron job hourly and at system startup.

%prep
%setup -q

%build
make build

%install
# Create user
mkdir -p %{buildroot}%{_sysusersdir}
cp %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

# Install binary from the build directory
install -Dm755 build/%{name} %{buildroot}%{_bindir}/%{name}

# Install cron job
mkdir -p %{buildroot}%{_sysconfdir}/cron.d
cp %{SOURCE2} %{buildroot}%{_sysconfdir}/cron.d/edge-node-metrics.cron

# Install sudoers file
mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
cp config/sudoers.d/reporting-agent %{buildroot}%{_sysconfdir}/sudoers.d/

# Create metrics and log directories with correct permissions
install -d -m 755 %{buildroot}%{_sysconfdir}/edge-node/metrics
install -d -m 755 %{buildroot}%{_var}/log/edge-node

# Install config file
install -m 644 config/reporting-agent.yaml %{buildroot}%{_sysconfdir}/edge-node/metrics/reporting-agent.yaml

# Copy license
mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
cp copyright %{buildroot}%{_defaultlicensedir}/%{name}

%files
%{_sysusersdir}/%{name}.conf
%{_bindir}/reporting-agent
%config %{_sysconfdir}/sudoers.d/reporting-agent
%config %{_sysconfdir}/cron.d/edge-node-metrics.cron
%dir %attr(0755,reporting-agent,bm-agents) %{_sysconfdir}/edge-node/metrics
%config(noreplace) %{_sysconfdir}/edge-node/metrics/reporting-agent.yaml
%dir %attr(0755,reporting-agent,bm-agents) %{_var}/log/edge-node

%license %{_defaultlicensedir}/%{name}/copyright

%pre
%sysusers_create_package %{name} %{SOURCE1}

%changelog
* Wed Jun 11 2025 Jakub Sikorski <jakub.sikorski@intel.com> - 0.0.4-1
- Original version for Edge Microvisor Toolkit. License verified
