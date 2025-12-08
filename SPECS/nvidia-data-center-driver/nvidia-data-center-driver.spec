%global debug_package %{nil}

# Currently this spec could be built nvidia driver for one kernel-devel
# package - It is ok because there is only one kernel in uki image. If there is
# requirement that there are two or more kernels in system, related kernel
# versions need to be pre-defined in this spec so nvidia driver could be built
# with these kernels.
%global kernel_ver `ls /lib/modules/`

Summary:        nvidia gpu driver kernel module for data center devices
Name:           nvidia-data-center-driver
Version:        580.105.08
Release:        3%{?dist}
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

%files
%defattr(-,root,root)
%license NVIDIA-Linux-x86_64-%{version}/LICENSE
/lib/modules/

%post
/sbin/depmod -a

%changelog
* Mon Dec 1 2025 Lishan Liu <lishan.liu@intel.com> - 580.105.08-2
- Bump release to rebuild

* Mon Nov 10 2025 Junxiao Chang <junxiao.chang@intel.com> - 580.105.08-1
- Updrade Nvidia data center driver to 580.105.08

* Tue Nov 18 2025 Lishan Liu <lishan.liu@intel.com> - 570.133.20-11
- Bump release to rebuild

* Fri Nov 14 2025 Lishan Liu <lishan.liu@intel.com> - 570.133.20-10
- Bump release to rebuild

* Tue Nov 4 2025 Lishan Liu <lishan.liu@intel.com> - 570.133.20-9
- Bump release to rebuild

* Thu Oct 23 2025 Lishan Liu <lishan.liu@intel.com> - 570.133.20-8
- Revert to working kernel config

* Fri Oct 10 2025 Zhang Baoli <baoli.zhang@intel.com> - 570.133.20-7
- Fix ISO mouse detection and cmdline params in non-rt kernel

* Tue Sep 30 2025 Zhang Baoli <baoli.zhang@intel.com> - 570.133.20-6
- Bump release to rebuild

* Tue Sep 09 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 570.133.20-5
- Bump release to rebuild

* Thu Jul 24 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 570.133.20-4
- Bump release to rebuild

* Thu Jul 10 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 570.133.20-3
- Bump release to rebuild

* Fri Jul 04 2025 Anuj Mittal <anuj.mittal@intel.com> - 570.133.20-2
- Bump release to rebuild

* Mon May 26 2025 Junxiao Chang <junxiao.chang@intel.com> 570.133.20-1
- Original version for Edge Microvisor Toolkit. License verified.
