Name:           k3s-disable-cni
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Version:        0.0.1
Release:        2%{?dist}
Summary:        Manifest to disable the default CNI in K3s
License:        Apache-2.0
# Source0 is a tarball containing the YAML manifest that disables the default Flannel CNI in K3s.
# This allows other CNI plugins (like Calico) to be used instead of the default one.
# The tarball is created from the 00-disable-flannel.yaml file and packaged with a directory
# structure matching the package name and version.
Source0:        %{name}-manifest-v%{version}.tar
Requires:       k3s

%description
This package provides the manifest that disables the default CNI in k3s cluster.

%prep
%setup -q -n k3s-disable-cni-%{version}

%install
mkdir -p %{buildroot}%{_sysconfdir}/rancher/k3s/config.yaml.d

# Install the pre-pulled manifest tarball
install -m 0644 ./00-disable-flannel.yaml %{buildroot}%{_sysconfdir}/rancher/k3s/config.yaml.d/

%files
%defattr(-,root,root,-)
%{_sysconfdir}/rancher/k3s/config.yaml.d/00-disable-flannel.yaml

%changelog

* Wed Jun 25 2025 Denisio Togashi <denisio.togashi@intel.com> - 0.0.1
- Original version for Edge Microvisor Toolkit. License verified.
