Summary:        Remote Provisioning Client for Intel AMT
Name:           rpc
Version:        2.48.9
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/device-management-toolkit/rpc-go
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-go-%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.gz
BuildRequires:  golang >= 1.24.4
BuildRequires:  golang < 1.25.0
%global modulename      rpc

%description
rpc is required to provision and activate Intel AMT. The rpc module communicates
with the CSME/ME over a host interface over PCIe to configure ME with endpoint
details and a CIRA profile. Once activated Intel AMT will establish a connection
to the mps (Manageability Presence Server) which in turns allows for out-of-band
connectivity between the edge node and ITEP. 

%prep
%setup -q -n rpc-go-%{version}
tar -xzf %{SOURCE1} -C .

%build
export CGO_ENABLED=0
export GOOS=linux
export GOARCH=amd64

go build \
    -mod=vendor \
    -ldflags "-X 'rpc/pkg/utils.ProjectVersion=%{version}'" \
    -trimpath \
    -o %{name} \
    ./cmd/rpc/main.go

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0644 internal/certs/trustedstore/OnDie_CA_RootCA_Certificate.cer %{buildroot}%{_datadir}/OnDie_CA_RootCA_Certificate.cer

mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
cp LICENSE %{buildroot}%{_defaultlicensedir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/OnDie_CA_RootCA_Certificate.cer

%license %{_defaultlicensedir}/%{name}/LICENSE

%changelog
* Wed Dec 3 2025 Polmoorx shiva kumar <polmoorx.shiva.kumar@intel.com> - 2.48.9-1
- Upgraded the RPC version from 2.45.1 to 2.48.9
- fixes CVE-2025-47913, CVE-2025-47914 and CVE-2025-58181

* Fri Oct 3 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 2.45.1-3
- build with golang < 1.25

* Tue Sep 2 2025 Polmoorx shiva kumar <polmoorx.shiva.kumar@intel.com> - 2.45.1-2
- Update go version to use above 1.24.4

* Tue Apr 8 2025 kintali Jayanth <jayanthx.kintali@intel.com> - 2.45.1-1
- Upgrade the RPC component version from 2.43.0 to 2.45.1

* Fri Mar 21 2025 Anuj Mittal <anuj.mittal@intel.com> - 2.43.0-10
- Bump Release to rebuild

* Mon Mar 03 2025 Mats Agerstam <mats.g.agerstam@intel.com> - 2.43.0
- Inital spec file for rpc (remote provisioning client).
- Original version for Edge Microvisor Toolkit. License verified.
