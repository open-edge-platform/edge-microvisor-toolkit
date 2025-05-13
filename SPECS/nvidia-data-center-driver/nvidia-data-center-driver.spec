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
Release:        1%{?dist}
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
./NVIDIA-Linux-x86_64-%{version}.run -x

%build
export KERNEL_UNAME=%{kernel_ver}
unset LDFLAGS
cd NVIDIA-Linux-x86_64-%{version}/kernel
make %{?_smp_mflags} modules

%install
cd NVIDIA-Linux-x86_64-%{version}/kernel
make INSTALL_MOD_PATH=%{buildroot} modules_install

%files
%defattr(-,root,root)
%license NVIDIA-Linux-x86_64-%{version}/LICENSE
/lib/modules/

%post
/sbin/depmod -a

%changelog
* Fri May 9 2025 Junxiao Chang <junxiao.chang@intel.com> 570.133.20-1
- Original version for Edge Microvisor Toolkit. License verified.
