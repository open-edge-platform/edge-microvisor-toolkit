Name:           k3s-multus-cni
Version:        4.2.1
Release:        1%{?dist}
Summary:        Multus manifests and container images for k3s kubernetes cluster.

License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit

URL:            https://github.com/k8snetworkplumbingwg/multus-cni
Source0:        https://github.com/k8snetworkplumbingwg/multus-cni/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
# Generate image tar by running `docker save ghcr.io/k8snetworkplumbingwg/multus-cni:version -o multus-cni.tar`
Source1:        %{name}-image-v%{version}.tar
Patch0:         multus-daemonset.patch
Requires:       k3s

BuildArch:      noarch

%description
This package provides Multus manifests and container image for k3s kubernetes cluster.

%prep
%setup -q -n multus-cni-%{version}
%autopatch -v -p1

%build
# No build steps required

%install
mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/00-multus
mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/00-multus

# Copy multus manifest
install -m 644 ./deployments/multus-daemonset.yml %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/00-multus/

# Multus manifest uses 1 image
# 
# ghcr.io/k8snetworkplumbingwg/multus-cni:v4.2.1
install -m 644 %{SOURCE1} %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/00-multus/multus-cni.tar

%files
%dir %{_sharedstatedir}/rancher/k3s/server/manifests/00-multus
%dir %{_sharedstatedir}/rancher/k3s/agent/images/00-multus
%{_sharedstatedir}/rancher/k3s/server/manifests/00-multus/multus-daemonset.yml
%{_sharedstatedir}/rancher/k3s/agent/images/00-multus/multus-cni.tar

%changelog
* Wed Jun 19 2025 Hyunsun Moon <hyunsun.moon@intel.com> - 4.2.1-1
- Initial Edge Microvisor Toolkit import from the source project (license: same as "License" tag).
- License verified.
