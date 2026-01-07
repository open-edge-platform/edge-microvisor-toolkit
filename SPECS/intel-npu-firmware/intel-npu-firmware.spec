%global debug_package %{nil}
%global __os_install_post %{nil}
%global _firmwarepath    /lib/firmware/updates/intel/vpu/
%define _binaries_in_noarch_packages_terminate_build   0

Summary:        Intel NPU Firmware
Name:           intel-npu-firmware
Version:        1.28.0
Release:        1%{?dist}
License:        MIT AND Redistributable, no modification permitted
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://github.com/intel/linux-npu-driver/
Source0:        %{url}/archive/refs/tags/v%{version}/linux-npu-driver-%{version}.tar.gz
BuildArch:      noarch

%description
This package includes Intel NPU(VPU) firmware files required for some devices to operate.

%prep
%setup -q -n linux-npu-driver-%{version} 

%install
mkdir -p %{buildroot}%{_firmwarepath}
cp -a firmware/bin/COPYRIGHT firmware/bin/mtl_vpu_v0.0.bin firmware/bin/vpu_37xx_v0.0.bin firmware/bin/vpu_50xx_v1.bin %{buildroot}%{_firmwarepath}

%files
%defattr(-,root,root)
%{_firmwarepath}/COPYRIGHT
%{_firmwarepath}/mtl_vpu_v0.0.bin
%{_firmwarepath}/vpu_37xx_v0.0.bin
%{_firmwarepath}/vpu_50xx_v1.bin

%changelog
* Mon Jan 5 2026 Lishan Liu <lishan.liu@intel.com> - 1.28.0-1
- Update version to v1.28.0

* Thu Feb 13 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 1.10.1-3
- Add source url.

* Thu Dec 26 2024 Lee Chee Yang <chee.yang.lee@intel.com> - 1.10.1-2
- rename to intel-npu-firmware.

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 1.10.1-1
- Original version for Edge Microvisor Toolkit. License verified.
