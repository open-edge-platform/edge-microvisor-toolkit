Name:           intel-gpu-device-plugin
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Version:        0.32.1
Release:        3%{?dist}
Summary:        Intel GPU device plugin manifests and container images for k3s Kubernetes cluster.
License:        Apache-2.0
URL:            https://github.com/intel/intel-device-plugins-for-kubernetes
Source0:        https://github.com/intel/intel-device-plugins-for-kubernetes/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
# Generate image tar.zst by running `docker save <image> | zstd -T0 -16 -f --long=25 > intel-gpu-device-plugin-image-<version>.tar.zst`
Source1:        %{name}-image-v%{version}.tar.zst
Requires:       k3s

%description
This package provides Intel GPU device plugin manifests and container images for k3s Kubernetes cluster.

%prep
%setup -q -n intel-device-plugins-for-kubernetes-%{version}

%install
mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/00-intel-gpu
mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images

# Install the pre-pulled image tarball and manifest
install -m 0644 %{SOURCE1} %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/intel-gpu-plugin.tar.zst
install -m 0644 ./deployments/gpu_plugin/base/intel-gpu-plugin.yaml %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/00-intel-gpu/

%files
%{_sharedstatedir}/rancher/k3s/server/manifests/00-intel-gpu/intel-gpu-plugin.yaml
%{_sharedstatedir}/rancher/k3s/agent/images/intel-gpu-plugin.tar.zst

%changelog
* Wed Jun 25 2025 Eoghan Lawless <eoghan.lawless@intel.com> - 0.32.1-3
- Move images to common install directory

* Tue Jun 24 2025 Eoghan Lawless <eoghan.lawless@intel.com> - 0.32.1-2
- Update Source1 to use a zstd-compressed image

* Tue Jun 17 2025 Krishnamurthy Jambur <krishna.j.murthy@intel.com> - 0.32.1-1
- Original version for Edge Microvisor Toolkit. License verified.
