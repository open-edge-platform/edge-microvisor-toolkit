%global infraonboarding_gitpath github.com/open-edge-platform/infra-onboarding

Summary:        Device Discovery Agent for Edge Node
Name:           device-discovery
Version:        1.17.2
Release:        1%{?dist}
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
License:        Apache-2.0
URL:            https://github.com/open-edge-platform/infra-onboarding/tree/main/hook-os/device_discovery
Source0:        https://%{infraonboarding_gitpath}/archive/refs/tags/tinker-actions/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        device-discovery.service
Source2:        device-discovery-1.17.2-vendor.tar.gz

%{?systemd_requires}

BuildRequires:  golang >= 1.23
BuildRequires:  systemd-rpm-macros
Requires: curl


%description
The Device Discovery Agent for Edge Node in order to retrieve the specific configuration to start for the current/correct machine.


%prep
%setup -q -n infra-onboarding-emt-uos
cd hook-os/device_discovery
tar -xzf %{SOURCE2} -C .

%build
cd hook-os/device_discovery
CGO_ENABLED=0 go build -buildmode=pie -mod=vendor -trimpath -ldflags '-extldflags "-static"' -gcflags=all="-l -B" -o device-discovery

%install
install -d -m 0755 %{buildroot}%{_bindir}/device-discovery 
install -m 0755 ./hook-os/device_discovery/device-discovery %{buildroot}%{_bindir}/device-discovery/device-discovery
install -m 0755 ./hook-os/device_discovery/client-auth.sh %{buildroot}%{_bindir}/device-discovery/client-auth.sh

# systemd units
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/device-discovery.service

%post
%systemd_post device-discovery.service

%files
%{_bindir}/device-discovery/*
%{_unitdir}/device-discovery.service

%changelog
* Tue May 20 2025 Andy <andy.peng@intel.com> - 1.17.2-1
- Original version for Edge Microvisor Toolkit. License verified.