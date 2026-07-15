%global debug_package %{nil}
%global __os_install_post %{nil}
%global _firmwarepath    /lib/firmware/updates/intel/vpu/
%define _binaries_in_noarch_packages_terminate_build   0

Summary:        Intel NPU Firmware
Name:           intel-npu-firmware
Version:        1.34.0
Release:        1%{?dist}
License:        MIT AND Redistributable, no modification permitted
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://github.com/intel/linux-npu-driver/
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/intel-npu-driver-v%{version}-firmware.tar.gz
BuildArch:      noarch

%description
This package includes Intel NPU(VPU) firmware files required for some devices to operate.

%prep
%setup -q -n firmware 

%install
mkdir -p %{buildroot}%{_firmwarepath}
cp -a firmware/bin/* %{buildroot}%{_firmwarepath}

%files
%defattr(-,root,root)
%{_firmwarepath}/vpu_37xx_v1.bin
%{_firmwarepath}/vpu_40xx_v1.bin
%{_firmwarepath}/vpu_50xx_v1.bin
%{_firmwarepath}/vpu_60xx_v1.bin

%changelog
* Thu Jul 16 2026 Andy <andy.peng@intel.com> - 1.34.0-1
- Update version to v1.34.0

* Thu Jul 2 2026 Andy <andy.peng@intel.com> - 1.33.0-1
- Update version to v1.33.0

* Mon Apr 14 2026 Andy <andy.peng@intel.com> - 1.32.0-1
- Update version to v1.32.0

* Fri Apr 10 2026 Lishan Liu <lishan.liu@intel.com> - 1.30.0-1
- Update version to v1.30.0

* Mon Jan 5 2026 Lishan Liu <lishan.liu@intel.com> - 1.28.0-1
- Update version to v1.28.0

* Thu Feb 13 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 1.10.1-3
- Add source url.

* Thu Dec 26 2024 Lee Chee Yang <chee.yang.lee@intel.com> - 1.10.1-2
- rename to intel-npu-firmware.

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 1.10.1-1
- Original version for Edge Microvisor Toolkit. License verified.
