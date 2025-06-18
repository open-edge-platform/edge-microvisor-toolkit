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

%build

%install
mkdir -p %{buildroot}/usr/share/%{name}
cp -a %{SOURCE0} %{buildroot}/usr/share/%{name}/
cp -a %{SOURCE1} %{buildroot}/usr/share/%{name}/

%files
/usr/share/%{name}/intel-idv-kubevirt-v0.1.tar.gz
/usr/share/%{name}/intel-idv-device-plugin-v0.1.tar.gz

%post

%changelog
* Thu Jun 5 2025 D M, Karthik <karthik.d.m@intel.com> - v0.1
- Pre-release version of Kubevirt v1.5.0 with Display Virtualization and GTK library support identified as v1.5.0_DV
- Pre-release version of Device Plugin v1 to support Display Virtualization on local display
