Name:           k3s-calico
Version:        3.30.1
Release:        3%{?dist}
Summary:        Calico manifests and container images for k3s kubernetes cluster.

License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit

URL:            https://github.com/projectcalico/calico
Source0:        https://github.com/projectcalico/calico/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
# Generate tar.zst images by running `docker save <image> | zstd -T0 -16 -f --long=25 > <image>.tar.zst`
Source1:        %{name}-cni-image-v%{version}.tar.zst
Source2:        %{name}-node-image-v%{version}.tar.zst
Source3:        %{name}-controllers-image-v%{version}.tar.zst

BuildArch:      noarch

%description
This package provides Calico manifests and container images for k3s kubernetes cluster.

%prep
%setup -q -n calico-%{version}

%build
# No build steps required

%install
mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/00-calico
mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images

# Copy calico manifest
install -m 644 ./manifests/calico.yaml %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/00-calico/

# Calico manifest uses 3 images
# docker.io/calico/cni:v3.30.1
# docker.io/calico/node:v3.30.1
# docker.io/calico/kube-controllers:v3.30.1

install -m 644 %{SOURCE1} %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/calico-cni.tar.zst
install -m 644 %{SOURCE2} %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/calico-node.tar.zst
install -m 644 %{SOURCE3} %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/calico-kube-controllers.tar.zst


%files
%dir %{_sharedstatedir}/rancher/k3s/server/manifests/00-calico
%dir %{_sharedstatedir}/rancher/k3s/agent/images
%{_sharedstatedir}/rancher/k3s/server/manifests/00-calico/calico.yaml
%{_sharedstatedir}/rancher/k3s/agent/images/calico-cni.tar.zst
%{_sharedstatedir}/rancher/k3s/agent/images/calico-node.tar.zst
%{_sharedstatedir}/rancher/k3s/agent/images/calico-kube-controllers.tar.zst

%changelog
* Wed Jun 25 2025 Eoghan Lawless <eoghan.lawless@intel.com> - 3.30.1-3
- Move images to common install directory

* Tue Jun 24 2025 Eoghan Lawless <eoghan.lawless@intel.com> - 3.30.1-2
- Update Source0 from release to source tarball
- Add sources for zstd-compressed images replacing the uncompressed release images

* Mon Jun 09 2025 Julia Okuniewska <julia.okuniewska@intel.com> - 3.30.1-1
- Initial Edge Microvisor Toolkit import from the source project (license: same as "License" tag).
- License verified.
