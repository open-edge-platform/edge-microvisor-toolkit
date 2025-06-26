Name:           k3s-disable-cni
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Version:        0.0.1
Release:        1%{?dist}
Summary:        Manifest to disable the default CNI in K3s
License:        Apache-2.0
# Source0 is a YAML manifest that disables the default Flannel CNI in K3s.
# This allows other CNI plugins (like Calico) to be used instead of the default one.
Source0:        00-disable-flannel.yaml
Requires:       k3s

%description
This package provides the manifest that disables the default CNI in k3s cluster.

%prep
%setup -c -T

%install
mkdir -p %{buildroot}%{_sysconfdir}/rancher/k3s/config.yaml.d
install -m 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/rancher/k3s/config.yaml.d/

%files
%defattr(-,root,root,-)
%{_sysconfdir}/rancher/k3s/config.yaml.d/00-disable-flannel.yaml

%changelog

* Wed Jun 25 2025 Denisio Togashi <denisio.togashi@intel.com> - 0.0.1-1
- Original version for Edge Microvisor Toolkit. License verified.
