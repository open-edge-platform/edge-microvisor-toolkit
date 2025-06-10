Summary:        network-policy for k3s
Name:           network-policy
Version:        1.1.4
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/open-edge-platform/cluster-extensions
Source0:        https://github.com/open-edge-platform/cluster-extensions/archive/refs/tags/v%{version}.tar.gz#/cluster-extensions-%{version}.tar.gz

BuildArch:      noarch
# Requires:     k3s # Add this requirement later

%description
This package provides a comprehensive set of Kubernetes and Calico network policies 
designed to ensure secure and reliable k3s cluster operation within the Edge Microvisor Toolkit environment.

%prep
%setup -q -n cluster-extensions-%{version}

%build
# No build steps required

# %install
# copy helm charts and install them under /var/lib/rancher/k3s/server/static/*.tar

%changelog
* Mon Jun 10 2025 Julia Okuniewska <julia.okuniewska@intel.com> - 1.0.0
- Original version for Edge Microvisor Toolkit. License verified.