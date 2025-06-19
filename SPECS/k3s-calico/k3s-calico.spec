Name:           k3s-calico
Version:        3.30.1
Release:        1%{?dist}
Summary:        Calico manifests and container images for k3s kubernetes cluster.

License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit

URL:            https://github.com/projectcalico/calico
Source0:        https://github.com/projectcalico/calico/releases/download/v%{version}/release-v%{version}.tgz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
This package provides Calico manifests and container images for k3s kubernetes cluster.

%prep
%setup -q -n release-v%{version}

%build
# No build steps required

%install
mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/00-calico
mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/00-calico

# Copy calico manifest
install -m 644 ./manifests/calico.yaml %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/00-calico/

# Calico manifest uses 3 images
# docker.io/calico/cni:v3.30.1
# docker.io/calico/node:v3.30.1
# docker.io/calico/kube-controllers:v3.30.1

install -m 644 ./images/calico-cni.tar %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/00-calico/
install -m 644 ./images/calico-node.tar %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/00-calico/
install -m 644 ./images/calico-kube-controllers.tar %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/00-calico/


%files
%dir %{_sharedstatedir}/rancher/k3s/server/manifests/00-calico
%dir %{_sharedstatedir}/rancher/k3s/agent/images/00-calico
%{_sharedstatedir}/rancher/k3s/server/manifests/00-calico/calico.yaml
%{_sharedstatedir}/rancher/k3s/agent/images/00-calico/calico-cni.tar
%{_sharedstatedir}/rancher/k3s/agent/images/00-calico/calico-node.tar
%{_sharedstatedir}/rancher/k3s/agent/images/00-calico/calico-kube-controllers.tar

%changelog
* Mon Jun 09 2025 Julia Okuniewska <julia.okuniewska@intel.com> - 3.30.1-1
- Initial Edge Microvisor Toolkit import from the source project (license: same as "License" tag).
- License verified.
