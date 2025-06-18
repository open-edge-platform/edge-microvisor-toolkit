Name:           intel-gpu-device-plugin
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Version:        0.32.1
Release:        1%{?dist}
Summary:        Intel GPU device plugin manifests and container images for k3s Kubernetes cluster.

License:        Apache-2.0
URL:            https://github.com/intel/intel-device-plugins-for-kubernetes
Source0:        https://github.com/intel/intel-device-plugins-for-kubernetes/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
# Requires:     k3s # Add this requirement if needed

%description
This package provides Intel GPU device plugin manifests and container images for k3s Kubernetes cluster.

%prep
%setup -q -n intel-device-plugins-for-kubernetes-%{version}

%build
# No build steps required

%install
mkdir -p %{buildroot}/var/lib/rancher/k3s/server/manifests/00-intel-gpu
mkdir -p %{buildroot}/var/lib/rancher/k3s/agent/images/00-intel-gpu

# Copy the device plugin manifest (assume it's named intel-gpu-plugin.yaml)
cp ./deployments/gpu_plugin/base/intel-gpu-plugin.yaml %{buildroot}/var/lib/rancher/k3s/server/manifests/00-intel-gpu

# Copy the pre-pulled image tarball (must be prepared separately)
cp ./images/intel-gpu-plugin.tar %{buildroot}/var/lib/rancher/k3s/agent/images/00-intel-gpu

%files
/var/lib/rancher/k3s/server/manifests/00-intel-gpu/intel-gpu-plugin.yaml
/var/lib/rancher/k3s/agent/images/00-intel-gpu/intel-gpu-plugin.tar

%changelog
* Tue Jun 17 2025 Krishnamurthy Jambur <krishna.j.murthy@intel.com> - 0.32.1-1
- Original version for Edge Microvisor Toolkit. License verified.