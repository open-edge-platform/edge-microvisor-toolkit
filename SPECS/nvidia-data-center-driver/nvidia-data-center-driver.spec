%global debug_package %{nil}

# Currently this spec could be built nvidia driver for one kernel-devel
# package - It is ok because there is only one kernel in uki image. If there is
# requirement that there are two or more kernels in system, related kernel
# versions need to be pre-defined in this spec so nvidia driver could be built
# with these kernels.
%global kernel_ver `ls /lib/modules/`

Summary:        nvidia gpu driver kernel module for data center devices
Name:           nvidia-data-center-driver
Version:        570.133.20
Release:        4%{?dist}
License:        Public Domain
Source0:        https://us.download.nvidia.com/tesla/%{version}/NVIDIA-Linux-x86_64-%{version}.run
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit

BuildRequires:  kernel-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  binutils
BuildRequires:  make

%description
This kernel driver package contains Nvidia data center GPU driver.

%package       libs
Summary:       Nvidia SDK user space libraries
Requires:      libX11
Requires:      libXext

%description   libs
Nvidia SDK user space libraries.

%package       apps
Summary:       Nvidia SDK applications
Requires:      %{name}-libs = %{version}-%{release}

%description   apps
Nvidia SDK user space applications.

%prep
cp -p %{SOURCE0} .
chmod 755 %{SOURCE0}
rm -rf NVIDIA-Linux-x86_64-%{version}
sh ./NVIDIA-Linux-x86_64-%{version}.run -x

%build
export KERNEL_UNAME=%{kernel_ver}
unset LDFLAGS
cd NVIDIA-Linux-x86_64-%{version}/kernel
make %{?_smp_mflags} modules

%install
export KERNEL_UNAME=%{kernel_ver}
cd NVIDIA-Linux-x86_64-%{version}/kernel
make INSTALL_MOD_PATH=%{buildroot} modules_install
cd ..

# install user space libraries
mkdir -p %{buildroot}/%{_libdir}
for i in `ls lib*.%{version}`
do
	cp $i %{buildroot}/%{_libdir}
	cd %{buildroot}/%{_libdir}
	ln -s $i ${i//.%{version}/.1}
	ln -s ${i//.%{version}/.1}  ${i//.%{version}/}
	cd -
done

cp libnvidia-api.so.1 %{buildroot}/%{_libdir}

# install icd config and other config files
mkdir -p %{buildroot}/%{_sysconfdir}/vulkan/icd.d
cp nvidia_icd.json %{buildroot}/%{_sysconfdir}/vulkan/icd.d

mkdir -p %{buildroot}/%{_sysconfdir}/vulkan/implicit_layer.d
cp nvidia_layers.json %{buildroot}/%{_sysconfdir}/vulkan/implicit_layer.d

mkdir -p %{buildroot}/%{_sysconfdir}/OpenCL/vendors
cp nvidia.icd %{buildroot}/%{_sysconfdir}/OpenCL/vendors

# Install user space apps
mkdir -p %{buildroot}/%{_bindir}
cp nvidia-cuda-mps-control %{buildroot}/%{_bindir}
cp nvidia-settings %{buildroot}/%{_bindir}
cp nvidia-cuda-mps-server %{buildroot}/%{_bindir}
cp nvidia-pcc %{buildroot}/%{_bindir}
cp nvidia-debugdump %{buildroot}/%{_bindir}
cp nvidia-smi %{buildroot}/%{_bindir}

%files
%defattr(-,root,root)
%license NVIDIA-Linux-x86_64-%{version}/LICENSE
/lib/modules/

%files libs
%defattr(-,root,root)
%{_libdir}/
%{_sysconfdir}/
%exclude %{_libdir}/libnvidia-egl*
%exclude %{_libdir}/libnvidia-fbc.so*
%exclude %{_libdir}/libGLX_nvidia.so*
%exclude %{_libdir}/libnvidia-pkcs11.so*
%exclude %{_libdir}/libnvidia-gtk3.so*
%exclude %{_libdir}/libnvidia-gtk2.so*
%exclude %{_libdir}/libnvidia-wayland-client.so*
%exclude %{_libdir}/libEGL.so*

%files apps
%defattr(-,root,root)
%{_bindir}/

%post
/sbin/depmod -a

%changelog
* Thu Jul 17 2025 Junxiao Chang <junxiao.chang@intel.com> - 570.133.20-4
- Adding Nvidia user space library package and app package

* Thu Jul 10 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 570.133.20-3
- Bump release to rebuild

* Fri Jul 04 2025 Anuj Mittal <anuj.mittal@intel.com> - 570.133.20-2
- Bump release to rebuild

* Mon May 26 2025 Junxiao Chang <junxiao.chang@intel.com> 570.133.20-1
- Original version for Edge Microvisor Toolkit. License verified.
