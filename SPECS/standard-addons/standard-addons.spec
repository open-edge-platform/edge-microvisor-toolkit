%define calico_version 3.30.1
%define network_policy_version 1.1.4
Name:           standard-addons
Summary:        Standard Addons install Calico CNI and Network Policies
Version:        1.0.0
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Base

# Calico URL         https://github.com/projectcalico/calico
# Network Policy URL https://github.com/open-edge-platform/cluster-extensions/tree/main/helm/network-policies
URL:            https://github.com/projectcalico/calico

# That's not the right path for us. Can't build docker images from source due to error 
# "fatal: not a git repository (or any of the parent directories): .git"
# It expects to be run in git cloned repo.
# To be changed to release tarball https://github.com/projectcalico/calico/releases/tag/v3.30.1.
Source0:        https://github.com/projectcalico/calico/archive/refs/tags/v%%{calico_version}.tar.gz#/calico-%{calico_version}.tar.gz
BuildArch:      noarch

%description
Standard Add-ons installs Calico CNI (version %{calico_version})
and network policies (version %{network_policy_version})

%prep
# This downloads calico full repo context
%setup -q -n calico-%{calico_version}

%build
# Nothing to build for a shell script

%install

%files

%changelog
* Mon Jun 09 2025 Julia Okuniewska <julia.okuniewska@intel.com> - 1.0.0
- Initial package