Summary:        Linux Firmware
Name:           linux-firmware
Version:        20250311
Release:        3%{?dist}
License:        GPL+ AND GPLv2+ AND MIT AND Redistributable, no modification permitted
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://www.kernel.org/
Source0:        https://www.kernel.org/pub/linux/kernel/firmware/%{name}-%{version}.tar.xz
%global debug_package %{nil}
%global __os_install_post %{nil}
%global _firmwarepath    /lib/firmware
%define _binaries_in_noarch_packages_terminate_build   0
Requires:       %{name}-broadcom = %{version}-%{release}
Requires:       %{name}-i915 = %{version}-%{release}
Requires:       %{name}-intel = %{version}-%{release}
Requires:       %{name}-qlogic = %{version}-%{release}
Requires:       %{name}-qualcomm = %{version}-%{release}
Requires:       %{name}-iwlwifi = %{version}-%{release}
Requires:       %{name}-ice = %{version}-%{release}
BuildArch:      noarch

%description
This package includes firmware files required for some devices to operate.

%package       broadcom
Summary:        Firmware for Broadcom devices

%description   broadcom
Firmware for Broadcom devices.

%package       intel
Summary:        Firmware for Intel devices

%description   intel
Firmware for Intel devices.

%package       qlogic
Summary:        Firmware for QLogic devices

%description   qlogic
Firmware for QLogic devices.

%package       qualcomm
Summary:        Firmware for Qualcomm devices

%description   qualcomm
Firmware for Qualcomm devices.

%package       i915
Summary:        Firmware for Intel I915 devices

%description   i915
Firmware for Intel I915 devices.

%package       iwlwifi
Summary:        Firmware for Intel wireless devices

%description   iwlwifi
Firmware for Intel wireless devices.

%package       ice
Summary:        Firmware for Intel Ethernet controller

%description   ice
Firmware for Intel Ethernet controller.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_firmwarepath}
cp -r bnx2x %{buildroot}%{_firmwarepath}
cp -r qed %{buildroot}%{_firmwarepath}
cp -r brcm %{buildroot}%{_firmwarepath}
cp -r rsi %{buildroot}%{_firmwarepath}
cp rsi_91x.fw %{buildroot}%{_firmwarepath}
cp -r ath10k %{buildroot}%{_firmwarepath}
cp -r i915 %{buildroot}%{_firmwarepath}
cp -r xe %{buildroot}%{_firmwarepath}
cp -r intel %{buildroot}%{_firmwarepath}
cp iwlwifi-8000C-*.ucode %{buildroot}%{_firmwarepath}
cp iwlwifi-so-a0-gf-a0-89.ucode %{buildroot}%{_firmwarepath}
cp iwlwifi-so-a0-gf-a0.pnvm %{buildroot}%{_firmwarepath}

%files
%defattr(-,root,root)
%license GPL*
%license WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/rsi
%{_firmwarepath}/rsi_91x.fw
%{_firmwarepath}/iwlwifi-8000C-*.ucode

%files broadcom
%defattr(-,root,root)
%license WHENCE LICENCE.broadcom_bcm43xx LICENCE.cypress
%{_firmwarepath}/bnx2x
%{_firmwarepath}/brcm

%files qlogic
%defattr(-,root,root)
%license WHENCE LICENCE.qla1280
%{_firmwarepath}/qed

%files qualcomm
%defattr(-,root,root)
%license WHENCE LICENSE.QualcommAtheros_ath10k
%{_firmwarepath}/ath10k

%files intel
%defattr(-,root,root)
%license WHENCE LICENSE.i915
%license LICENSE.ipu3_firmware LICENCE.ibt_firmware LICENCE.fw_sst_0f28
%license LICENCE.IntcSST2 LICENCE.adsp_sst LICENSE.ice
%{_firmwarepath}/i915
%{_firmwarepath}/xe
%{_firmwarepath}/intel

%files i915
%defattr(-,root,root)
%license WHENCE LICENSE.i915
%{_firmwarepath}/i915/mtl_guc_70.bin
%{_firmwarepath}/i915/adlp_guc_70.bin
%{_firmwarepath}/i915/dg2_guc_70.bin
%{_firmwarepath}/i915/tgl_guc_70.bin
%{_firmwarepath}/i915/tgl_huc.bin
%{_firmwarepath}/i915/dg2_huc_gsc.bin
%{_firmwarepath}/i915/mtl_huc_gsc.bin
%{_firmwarepath}/i915/mtl_dmc.bin
%{_firmwarepath}/i915/adlp_dmc.bin
%{_firmwarepath}/i915/adls_dmc_ver2_01.bin
%{_firmwarepath}/i915/dg2_dmc_ver2_08.bin
%{_firmwarepath}/i915/mtl_gsc_1.bin
%{_firmwarepath}/xe/bmg_guc_70.bin
%{_firmwarepath}/xe/bmg_huc.bin

%files iwlwifi
%defattr(-,root,root)
%license WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-so-a0-gf-a0-89.ucode
%{_firmwarepath}/iwlwifi-so-a0-gf-a0.pnvm

%files ice
%defattr(-,root,root)
%license WHENCE LICENSE.ice
%{_firmwarepath}/intel/ice

%changelog
* Fri May 16 2025 Junxiao Chang <junxiao.chang@intel.com> - 20250311-3
- Added B580 GPU firmware.

* Fri Mar 21 2025 Mun Chun Yep <mun.chun.yep@intel.com> - 20250311-2
- Added ice package for Intel Ethernet controller.

* Wed Mar 19 2025 Junxiao Chang <junxiao.chang@intel.com> - 20250311-1
- Upgrade firmware to 20250311

* Mon Mar 10 2025 Mun Chun Yep <mun.chun.yep@intel.com> - 20241110-3
- Added iwlwifi package for Intel Wi-Fi 6E AX211 device.

* Wed Jan 08 2025 Junxiao Chang <junxiao.chang@intel.com> - 20241110-2
- Added MTL GSC firmware

* Fri Dec 20 2024 Junxiao Chang <junxiao.chang@intel.com> - 20241110-1
- Upgrade to 20241110
- Upgrade version for Edge Microvisor Toolkit.
- Added i915 package for ADLp/s, RPL, DG2 and MTL

* Fri Oct 27 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 20230804-1
- Auto-upgrade to 20230804 - Azure Linux 3.0 - package upgrades

* Mon Nov 28 2022 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 20211216-2
- Split linux-firmware to sub packages.

* Tue Feb 01 2022 Chris Co <chrco@microsoft.com> - 20211216-1
- Update to 20211216.

* Fri Feb 19 2021 Chris Co <chrco@microsoft.com> - 20200316-3
- Add bnx2x and qed firmware.
- Add WHENCE and relevant LICENSE files.

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 20200316-2
- Added %%license line automatically

* Thu Mar 19 2020 Henry Beberman <henry.beberman@microsoft.com> 20200316-1
- Update to 20200316. Remove LS1012a binaries. Source0 URL Fixed. License verified.

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 20190205-2
- Initial CBL-Mariner import from Photon (license: Apache2).

* Tue Feb 05 2019 Alexey Makhalov <amakhalov@vmware.com> 20190205-1
- Added ath10k firmware (for ls1012a).
- Use 1:1 folder layout for ppfe firmware.

* Wed Jan 09 2019 Alexey Makhalov <amakhalov@vmware.com> 20190109-1
- Added Compulab Fitlet2 firmware.

* Thu Nov 29 2018 Srinidhi Rao <srinidhir@vmware.com> 20181129-1
- Updated pfe firmware files for NXP LS1012A FRWY board

* Wed Oct 10 2018 Ajay Kaher <akaher@vmware.com> 20181010-1
- Updated brcm firmwares for Rpi B and Rpi B+

* Thu Aug 23 2018 Alexey Makhalov <amakhalov@vmware.com> 20180823-1
- Initial version. RPi3 and Dell Edge Gateway 3001 support.
