Name:           cni-calico
Version:        3.30.1
Release:        1%{?dist}
Summary:        Calico manifests and container images for k3s kubernetes cluster.

License:        Apache-2.0
URL:            https://github.com/projectcalico/calico
Source0:        https://github.com/projectcalico/calico/releases/download/v%{version}/release-v%{version}.tgz

BuildArch:      noarch
# Requires:     k3s # Add this requirement later

%description
This package provides Calico manifests and container images for k3s kubernetes cluster.

%prep
%setup -q -n release-v%{version}

%build
# No build steps required

%install
mkdir -p %{buildroot}/var/lib/rancher/k3s/server/manifests/00-calico
mkdir -p %{buildroot}/var/lib/rancher/k3s/agent/images/00-calico

# Copy calico manifest
cp -r ./manifests/calico.yaml %{buildroot}/var/lib/rancher/k3s/server/manifests/00-calico

# Calico manifest uses 3 images
# docker.io/calico/cni:v3.30.1
# docker.io/calico/node:v3.30.1
# docker.io/calico/kube-controllers:v3.30.1

cp ./images/calico-cni.tar %{buildroot}/var/lib/rancher/k3s/agent/images/00-calico
cp ./images/calico-node.tar %{buildroot}/var/lib/rancher/k3s/agent/images/00-calico
cp ./images/calico-kube-controllers.tar %{buildroot}/var/lib/rancher/k3s/agent/images/00-calico


%files
/var/lib/rancher/k3s/server/manifests/00-calico/calico.yaml
/var/lib/rancher/k3s/agent/images/00-calico/calico-cni.tar
/var/lib/rancher/k3s/agent/images/00-calico/calico-node.tar
/var/lib/rancher/k3s/agent/images/00-calico/calico-kube-controllers.tar

%changelog
* Mon Jun 09 2025 Julia Okuniewska <julia.okuniewska@intel.com> - 1.0.0
- Initial package