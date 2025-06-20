%global infraonboarding_gitpath github.com/open-edge-platform/infra-onboarding

Summary:        Device Discovery Agent for Edge Node
Name:           device-discovery
Epoch:          1
Version:        0.0.3
Release:        1%{?dist}
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
License:        Apache-2.0
URL:            https://github.com/open-edge-platform/infra-onboarding/tree/main/hook-os/device_discovery
Source0:        https://%{infraonboarding_gitpath}/archive/refs/tags/%{name}/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        device-discovery.service
Source2:        %{name}-%{version}-vendor.tar.gz

%{?systemd_requires}

BuildRequires:  golang >= 1.24.1
BuildRequires:  systemd-rpm-macros
Requires: curl
Requires: dmidecode

%description
The Device Discovery Agent for Edge Node in order to retrieve the specific configuration to start for the current/correct machine.


%prep
%setup -q -n infra-onboarding-%{name}-%{version}
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
* Wed Jun 18 2025 Andy <andy.peng@intel.com> - 1:0.0.3-1
- Update go version to 1.24.1

* Tue Jun 17 2025 Andy <andy.peng@intel.com> - 1:0.0.2-1
- Update version to fix grpc CVE

* Thu Jun 12 2025 Andy <andy.peng@intel.com> - 1:0.0.1-1
- Add Epoch 1 to package, to be able to change the version number to actual version
- Update the source name and service file

* Fri May 30 2025 Anuj Mittal <anuj.mittal@intel.com> - 1.17.2-2
- Update the source directory name

* Tue May 20 2025 Andy <andy.peng@intel.com> - 1.17.2-1
- Original version for Edge Microvisor Toolkit. License verified.
