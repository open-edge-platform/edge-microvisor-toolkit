Name:           intel-desktop-virtualization-k3s
Version:        v1.0
Release:        1%{?dist}
Summary:        Installs Kubevirt (v1.5.0 enabled with GTK libarary support and Intel SR-IOV patched QEMU in Virt-Launcher) and Device Plugin(v1) for enabling support of local GTK display using pre-built container tar files

License:        APACHE 2.0
Source0:        https://github.com/open-edge-platform/edge-desktop-virtualization/releases/download/pre-release-v0.1/kubevirt.tar.gz
Source1:        https://github.com/open-edge-platform/edge-desktop-virtualization/releases/download/pre-release-v0.1/dv-device-plugin.tar.gz
BuildArch:      x86_64

%description
This RPM Installs Kubevirt (v1.5.0 enabled with GTK libarary support and Intel SR-IOV patched QEMU in Virt-Launcher) and Device Plugin(v1) for enabling support of local GTK display using pre-built container tar files

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/%{name}
cp -a %{SOURCE0} %{buildroot}/usr/share/%{name}/
cp -a %{SOURCE1} %{buildroot}/usr/share/%{name}/

%files
/usr/share/%{name}/kubevirt.tar.gz
/usr/share/%{name}/dv-device-plugin.tar.gz

%post
#tar -xzvf /usr/share/%{name}/kubevirt.tar.gz
#tar -xzvf /usr/share/%{name}/dv-device-plugin.tar.gz


%changelog
* Thu Jun 5 2025 D M, Karthik <karthik.d.m@intel.com> - v1.0
- Initial version of Kubevirt v1.5.0 with Display Virtualization and GTK library support
- Initial version of Device Plugin v1 to support Display Virtualization on local display
