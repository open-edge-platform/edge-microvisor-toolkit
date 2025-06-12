%global cluster_extensions_version 1.1.4
Summary:        network-policy for k3s
Name:           k3s-network-policy
Version:        0.2.0
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/open-edge-platform/cluster-extensions
Source0:        https://github.com/open-edge-platform/cluster-extensions/archive/refs/tags/v%{cluster_extensions_version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       helm

%description
This package provides a comprehensive set of Kubernetes and Calico network policies 
designed to ensure secure and reliable k3s cluster operation within the Edge Microvisor Toolkit environment.

%prep
%setup -q -n cluster-extensions-%{cluster_extensions_version}

%build
helm package helm/network-policies

%install
# copy helm charts and install them under /var/lib/rancher/k3s/server/static/*.tar
mkdir -p  %{buildroot}/var/lib/rancher/k3s/server/static/01-network-policy
install network-policies-%{version}.tgz  %{buildroot}/var/lib/rancher/k3s/server/static/01-network-policy

%files
/var/lib/rancher/k3s/server/static/01-network-policy/network-policies-%{version}.tgz

%changelog
* Tue Jun 10 2025 Julia Okuniewska <julia.okuniewska@intel.com> - 0.2.0
- Original version for Edge Microvisor Toolkit. License verified.
