Name:          k3s
Summary:       K3s - Lightweight Kubernetes
Version:       1.32.4
Release:       2%{?dist}
License:       ASL 2.0
Vendor:        Intel Corporation
Distribution:  Edge Microvisor Toolkit
Group:         System Environment/Base
URL:           https://k3s.io/
Source0:       https://github.com/k3s-io/k3s/archive/refs/tags/v%{version}+k3s1.tar.gz#/%{name}-v%{version}.tar.gz
Source1:       https://github.com/k3s-io/k3s/releases/download/v%{version}+k3s1/k3s-airgap-images-amd64.tar.zst#/%{name}-airgap-images-v%{version}.tar.zst
Source2:       %{name}-vendor-v%{version}.tar.gz
Source3:       https://github.com/k3s-io/k3s-root/releases/download/v0.14.1/k3s-root-amd64.tar
Source4:       https://github.com/opencontainers/runc/archive/refs/tags/v1.2.5.tar.gz#/runc-v1.2.5.tar.gz
Source5:       https://github.com/k3s-io/containerd/archive/refs/tags/v2.0.4-k3s2.tar.gz#/containerd-v2.0.4-k3s2.tar.gz
Source6:       https://k3s.io/k3s-charts/assets/traefik-crd/traefik-crd-34.2.1+up34.2.0.tgz
Source7:       https://k3s.io/k3s-charts/assets/traefik/traefik-34.2.1+up34.2.0.tgz
Source8:       https://github.com/rancher/plugins/archive/refs/tags/v1.6.0-k3s1.tar.gz#/rancher-plugins-v1.6.0-k3s1.tar.gz
Source9:       https://github.com/flannel-io/cni-plugin/archive/refs/tags/v1.6.0-flannel1.tar.gz#/flannel-v1.6.0-flannel1.tar.gz
Patch0:        k3s-version.patch
Patch1:        k3s-build.patch
Patch2:        k3s-package-cli.patch
Patch3:        flannel.patch
BuildRequires: yq
BuildRequires: golang-1.23.7
BuildRequires: libseccomp-devel

%description
K3s - Lightweight Kubernetes %{version}

%prep
%setup -n %{name}-%{version}-k3s1
mkdir -p build/src/github.com/opencontainers/runc build/src/github.com/containerd/containerd  build/static/charts build/src/github.com/containernetworking/plugins bin dist
tar -xf %{SOURCE2} --no-same-owner
tar -xf %{SOURCE3} --no-same-owner
tar -xf %{SOURCE4} --no-same-owner --strip-components 1 -C build/src/github.com/opencontainers/runc
tar -xf %{SOURCE5} --no-same-owner --strip-components 1 -C build/src/github.com/containerd/containerd
mv %{SOURCE6} build/static/charts/
mv %{SOURCE7} build/static/charts/
tar -xf %{SOURCE8} --no-same-owner --strip-components 1 -C build/src/github.com/containernetworking/plugins
rm -rf build/src/github.com/containernetworking/plugins/plugins/meta/flannel/*
tar -xf %{SOURCE9} --no-same-owner --strip-components 1 -C build/src/github.com/containernetworking/plugins/plugins/meta/flannel
%autopatch -v -p0

%build
./scripts/build
./scripts/package-cli

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 dist/artifacts/k3s %{buildroot}%{_bindir}

mkdir %{buildroot}/opt
install -m 0755 install.sh %{buildroot}/opt/install.sh

mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images
install -m 0644 %{SOURCE1} %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/k3s-airgap-images-amd64.tar.zst

%files
%{_bindir}/k3s
/opt/install.sh
%{_sharedstatedir}/rancher/k3s/agent/images/k3s-airgap-images-amd64.tar.zst

%changelog
* Wed Jun 25 2025 Eoghan Lawless <eoghan.lawless@intel.com> - 1.32.4-2
- Move images to common install directory
- Use _sharedstatedir macro for /var/lib paths

* Tue Jun 17 2025 Eoghan Lawless <eoghan.lawless@intel.com> - 1.32.4-1
- Initial Edge Microvisor Toolkit import from the source project (license: same as "License" tag).
- License verified.
