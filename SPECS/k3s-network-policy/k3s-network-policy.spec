Summary:        network-policy for k3s
Name:           k3s-network-policy
Version:        0.1.0
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/open-edge-platform/edge-microvisor-toolkit
Source0:        00-kube-system.yaml

BuildArch:      noarch

%description
This package provides a comprehensive set of Kubernetes network policies 
designed to ensure reliable k3s cluster operation within the Edge Microvisor Toolkit environment.

%install
# copy manifests and install them under /var/lib/rancher/k3s/server/manifests/network-policy/*.yaml
mkdir -p  %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/network-policy
install %{_sourcedir}/00-kube-system.yaml  %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/network-policy

%files
%{_sharedstatedir}/rancher/k3s/server/manifests/network-policy/00-kube-system.yaml

%changelog
* Tue Jun 17 2025 Julia Okuniewska <julia.okuniewska@intel.com> - 0.1.0
- Original version for Edge Microvisor Toolkit. License verified.
