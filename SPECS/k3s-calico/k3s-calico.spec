Name:           k3s-calico
Version:        3.30.1
Release:        3%{?dist}
Summary:        Calico manifests and container images for k3s kubernetes cluster.

License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit

URL:            https://github.com/projectcalico/calico
Source0:        https://github.com/projectcalico/calico/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz

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


%files
%dir %{_sharedstatedir}/rancher/k3s/server/manifests/00-calico
%dir %{_sharedstatedir}/rancher/k3s/agent/images
%{_sharedstatedir}/rancher/k3s/server/manifests/00-calico/calico.yaml

%changelog
* Wed Jun 25 2025 Eoghan Lawless <eoghan.lawless@intel.com> - 3.30.1-3
- Move images to common install directory

* Tue Jun 24 2025 Eoghan Lawless <eoghan.lawless@intel.com> - 3.30.1-2
- Update Source0 from release to source tarball
- Add sources for zstd-compressed images replacing the uncompressed release images

* Mon Jun 09 2025 Julia Okuniewska <julia.okuniewska@intel.com> - 3.30.1-1
- Initial Edge Microvisor Toolkit import from the source project (license: same as "License" tag).
- License verified.
