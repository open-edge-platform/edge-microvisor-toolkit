Name:           intel-gpu-device-plugin
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Version:        0.32.1
Release:        1%{?dist}
Summary:        Intel GPU device plugin manifests and container images for k3s Kubernetes cluster.
License:        Apache-2.0
URL:            https://github.com/intel/intel-device-plugins-for-kubernetes
Source0:        https://github.com/intel/intel-device-plugins-for-kubernetes/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
# Source1 is a pre-built container image tarball for the Intel gpu device plugin.
# to avoid building container images as part of the RPM build process, 
# the required image is built locally in advance and included as a tarball.
# With `docker build` and `docker save` 
# and uploaded to the source package repository after is has been tested locally.
Source1:        %{name}-image-v%{version}.tar
Requires:       k3s

%description
This package provides Intel GPU device plugin manifests and container images for k3s Kubernetes cluster.

%prep
%setup -q -n intel-device-plugins-for-kubernetes-%{version}

%install
mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/00-intel-gpu
mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/00-intel-gpu

# Install the pre-pulled image tarball and manifest
install -m 0644 %{SOURCE1} %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/00-intel-gpu/intel-gpu-plugin.tar
install -m 0644 ./deployments/gpu_plugin/base/intel-gpu-plugin.yaml %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/00-intel-gpu/

%files
%{_sharedstatedir}/rancher/k3s/server/manifests/00-intel-gpu/intel-gpu-plugin.yaml
%{_sharedstatedir}/rancher/k3s/agent/images/00-intel-gpu/intel-gpu-plugin.tar

%changelog
* Tue Jun 17 2025 Krishnamurthy Jambur <krishna.j.murthy@intel.com> - 0.32.1-1
- Original version for Edge Microvisor Toolkit. License verified.
