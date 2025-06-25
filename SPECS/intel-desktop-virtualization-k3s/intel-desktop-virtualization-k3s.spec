Name:           intel-desktop-virtualization-k3s
Version:        0.1
Release:        1%{?dist}
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/open-edge-platform/edge-desktop-virtualization
Summary:        Provides Kubevirt (enabled with GTK libarary support and Intel SR-IOV patched QEMU in Virt-Launcher) and IDV Device Plugin for enabling support of local GTK display using pre-built container tar files
License:        Apache-2.0
Source0:        https://github.com/open-edge-platform/edge-desktop-virtualization/releases/download/pre-release-v0.1/intel-idv-kubevirt-v0.1.tar.gz
Source1:        https://github.com/open-edge-platform/edge-desktop-virtualization/releases/download/pre-release-v0.1/intel-idv-device-plugin-v0.1.tar.gz
BuildArch:      x86_64
Requires:       k3s

%description
Provides Kubevirt (enabled with GTK libarary support and Intel SR-IOV patched QEMU in Virt-Launcher) and IDV Device Plugin for enabling support of local GTK display using pre-built container tar files

%prep
tar -xzf %{SOURCE0} -C .
tar -xzf %{SOURCE1} -C .

%build

%install
mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/
cp *.tar.zst %{buildroot}%{_sharedstatedir}/rancher/k3s/agent/images/

mkdir -p %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/
cp *.yaml %{buildroot}%{_sharedstatedir}/rancher/k3s/server/manifests/

%files
%{_sharedstatedir}/rancher/k3s/agent/images/virt-api.tar.zst
%{_sharedstatedir}/rancher/k3s/agent/images/virt-controller.tar.zst
%{_sharedstatedir}/rancher/k3s/agent/images/virt-handler.tar.zst
%{_sharedstatedir}/rancher/k3s/agent/images/virt-launcher.tar.zst
%{_sharedstatedir}/rancher/k3s/agent/images/virt-operator.tar.zst
%{_sharedstatedir}/rancher/k3s/agent/images/busybox.tar.zst
%{_sharedstatedir}/rancher/k3s/agent/images/device-plugin.tar.zst
%{_sharedstatedir}/rancher/k3s/agent/images/sidecar-shim.tar.zst
%{_sharedstatedir}/rancher/k3s/server/manifests/device-plugin.yaml
%{_sharedstatedir}/rancher/k3s/server/manifests/kubevirt-cr.yaml
%{_sharedstatedir}/rancher/k3s/server/manifests/kubevirt-operator.yaml
%{_sharedstatedir}/rancher/k3s/server/manifests/kubevirt-cr-gfx-sriov.yaml


%post

%changelog
* Thu Jun 5 2025 D M, Karthik <karthik.d.m@intel.com> - 0.1-1
- Original version for Edge Microvisor Toolkit. License verified.
- Pre-release version of Kubevirt v1.5.0 with Display Virtualization and GTK library support identified as v1.5.0_DV
- Pre-release version of Device Plugin v1 to support Display Virtualization on local display

