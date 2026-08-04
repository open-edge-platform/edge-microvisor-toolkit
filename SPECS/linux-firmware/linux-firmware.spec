Summary:        Linux Firmware
Name:           linux-firmware
Version:        20260622
Release:        2%{?dist}
License:        GPL+ AND GPLv2+ AND MIT AND Redistributable, no modification permitted
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://www.kernel.org/
Source0:        https://www.kernel.org/pub/linux/kernel/firmware/%{name}-%{version}.tar.xz
Source1:        https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/xe/nvl_guc_70.bin
Source2:        https://github.com/intel/ipu7-camera-bins/raw/refs/heads/main/lib/firmware/intel/ipu/ipu8_fw.bin

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
Requires:       dracut
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

%package       qat
Summary:        Firmware for Intel QAT controller

%description   qat
Firmware for Intel QAT controller.

%prep
%setup -q

%build

%install
# Use upstream copy-firmware.sh to install all firmware files and symlinks from WHENCE
mkdir -p %{buildroot}%{_firmwarepath}
./copy-firmware.sh %{buildroot}%{_firmwarepath}

# Remove firmware we don't package to keep the RPM size down
# Keep only: bnx2x brcm qed rsi ath10k i915 xe intel
find %{buildroot}%{_firmwarepath} -maxdepth 1 \
    ! -name firmware \
    ! -name bnx2x ! -name brcm ! -name qed ! -name rsi ! -name rsi_91x.fw \
    ! -name ath10k ! -name i915 ! -name xe ! -name intel \
    -exec rm -rf {} +

# Re-create root-level compat symlinks for firmware the kernel loads by legacy name.
# copy-firmware.sh creates these from WHENCE, but the cleanup above removes them.
# Only create symlinks for firmware prefixes listed in our %files sections.
for pattern in iwlwifi-8000C iwlwifi-so-a0-gf-a0 iwlwifi-ma-b0-gf-a0 \
               iwlwifi-sc-a0-wh-b0 iwlwifi-ty-a0-gf-a0 iwlwifi-9000 \
               iwlwifi-9260 iwlwifi-bz-b0-gf-a0 iwlwifi-gl-c0-fm-c0; do
    for f in %{buildroot}%{_firmwarepath}/intel/iwlwifi/${pattern}*; do
        [ -f "$f" ] || continue
        base=$(basename "$f")
        ln -s "intel/iwlwifi/$base" "%{buildroot}%{_firmwarepath}/$base"
    done
done

# QAT root-level compat symlinks (kernel modules request e.g. "qat_4xxx.bin")
for f in %{buildroot}%{_firmwarepath}/intel/qat/qat_*.bin; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    ln -s "intel/qat/$base" "%{buildroot}%{_firmwarepath}/$base"
done

mkdir -p %{buildroot}%{_firmwarepath}/xe
install -m 0644 %{SOURCE1} %{buildroot}%{_firmwarepath}/xe/nvl_guc_70.bin

mkdir -p %{buildroot}%{_firmwarepath}/intel/ipu
install -m 0644 %{SOURCE2} %{buildroot}%{_firmwarepath}/intel/ipu/ipu8_fw.bin

%post qat
dracut --force

%files
%defattr(-,root,root)
%license LICENSES/GPL-2.0
%license WHENCE LICENSES/LICENCE.iwlwifi_firmware
%{_firmwarepath}/rsi
%{_firmwarepath}/rsi_91x.fw
%{_firmwarepath}/intel/iwlwifi/iwlwifi-8000C-*.ucode
%{_firmwarepath}/iwlwifi-8000C-*

%files broadcom
%defattr(-,root,root)
%license WHENCE LICENSES/LICENCE.broadcom_bcm43xx LICENSES/LICENCE.cypress
%{_firmwarepath}/bnx2x
%{_firmwarepath}/brcm

%files qlogic
%defattr(-,root,root)
%license WHENCE LICENSES/LICENCE.qla1280
%{_firmwarepath}/qed

%files qualcomm
%defattr(-,root,root)
%license WHENCE LICENSES/LICENSE.QualcommAtheros_ath10k
%{_firmwarepath}/ath10k

%files intel
%defattr(-,root,root)
%license WHENCE LICENSES/LICENSE.i915
%license LICENSES/LICENSE.ipu3_firmware LICENSES/LICENCE.ibt_firmware LICENSES/LICENCE.fw_sst_0f28
%license LICENSES/LICENCE.IntcSST2 LICENSES/LICENCE.adsp_sst LICENSES/LICENSE.ice
%{_firmwarepath}/i915
%{_firmwarepath}/xe
%{_firmwarepath}/intel

%files i915
%defattr(-,root,root)
%license WHENCE LICENSES/LICENSE.i915
%{_firmwarepath}/i915/mtl_guc_70.bin
%{_firmwarepath}/i915/adlp_guc_70.bin
%{_firmwarepath}/i915/dg1_guc_70.bin
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
%{_firmwarepath}/i915/xe2lpd_dmc.bin
%{_firmwarepath}/i915/xe3p_lpd_dmc.bin
%{_firmwarepath}/i915/xe3lpd_dmc.bin
%{_firmwarepath}/i915/xe3lpd_3002_dmc.bin
%{_firmwarepath}/xe/bmg_guc_70.bin
%{_firmwarepath}/xe/bmg_huc.bin
%{_firmwarepath}/xe/ptl_guc_70.bin
%{_firmwarepath}/xe/ptl_huc.bin
%{_firmwarepath}/xe/ptl_gsc_1.bin
%{_firmwarepath}/xe/nvl_guc_70.bin

%files iwlwifi
%defattr(-,root,root)
%license WHENCE LICENSES/LICENCE.iwlwifi_firmware
%{_firmwarepath}/intel/iwlwifi/iwlwifi-so-a0-gf-a0-89.ucode
%{_firmwarepath}/intel/iwlwifi/iwlwifi-so-a0-gf-a0.pnvm
%{_firmwarepath}/intel/iwlwifi/iwlwifi-ma-b0-gf-a0-83.ucode
%{_firmwarepath}/intel/iwlwifi/iwlwifi-ma-b0-gf-a0-86.ucode
%{_firmwarepath}/intel/iwlwifi/iwlwifi-ma-b0-gf-a0-89.ucode
%{_firmwarepath}/intel/iwlwifi/iwlwifi-ma-b0-gf-a0.pnvm
%{_firmwarepath}/intel/iwlwifi/iwlwifi-sc-a0-wh-b0-101.ucode
%{_firmwarepath}/intel/iwlwifi/iwlwifi-sc-a0-wh-b0-c101.ucode
%{_firmwarepath}/intel/iwlwifi/iwlwifi-sc-a0-wh-b0-c102.ucode
%{_firmwarepath}/intel/iwlwifi/iwlwifi-ty-a0-gf-a0-89.ucode
%{_firmwarepath}/intel/iwlwifi/iwlwifi-ty-a0-gf-a0.pnvm
%{_firmwarepath}/intel/iwlwifi/iwlwifi-9000-*.ucode
%{_firmwarepath}/intel/iwlwifi/iwlwifi-9260-*.ucode
%{_firmwarepath}/intel/iwlwifi/iwlwifi-bz-b0-gf-a0-100.ucode
%{_firmwarepath}/intel/iwlwifi/iwlwifi-gl-c0-fm-c0-100.ucode
# Root-level compat symlinks for kernel firmware loader
%{_firmwarepath}/iwlwifi-so-a0-gf-a0-*
%{_firmwarepath}/iwlwifi-so-a0-gf-a0.pnvm
%{_firmwarepath}/iwlwifi-ma-b0-gf-a0-*
%{_firmwarepath}/iwlwifi-ma-b0-gf-a0.pnvm
%{_firmwarepath}/iwlwifi-sc-a0-wh-b0-*
%{_firmwarepath}/iwlwifi-ty-a0-gf-a0-*
%{_firmwarepath}/iwlwifi-ty-a0-gf-a0.pnvm
%{_firmwarepath}/iwlwifi-9000-*
%{_firmwarepath}/iwlwifi-9260-*
%{_firmwarepath}/iwlwifi-bz-b0-gf-a0-*
%{_firmwarepath}/iwlwifi-bz-b0-gf-a0.pnvm
%{_firmwarepath}/iwlwifi-gl-c0-fm-c0-*
%{_firmwarepath}/iwlwifi-gl-c0-fm-c0.pnvm

%files ice
%defattr(-,root,root)
%license WHENCE LICENSES/LICENSE.ice
%{_firmwarepath}/intel/ice

%files qat
%defattr(-,root,root)
%license WHENCE LICENSES/LICENCE.qat_firmware
%{_firmwarepath}/intel/qat/qat_402xx.bin
%{_firmwarepath}/intel/qat/qat_402xx_mmp.bin
%{_firmwarepath}/intel/qat/qat_420xx.bin
%{_firmwarepath}/intel/qat/qat_420xx_mmp.bin
%{_firmwarepath}/intel/qat/qat_4xxx.bin
%{_firmwarepath}/intel/qat/qat_4xxx_mmp.bin
%{_firmwarepath}/intel/qat/qat_895xcc.bin
%{_firmwarepath}/intel/qat/qat_895xcc_mmp.bin
%{_firmwarepath}/intel/qat/qat_c3xxx.bin
%{_firmwarepath}/intel/qat/qat_c3xxx_mmp.bin
%{_firmwarepath}/intel/qat/qat_c62x.bin
%{_firmwarepath}/intel/qat/qat_c62x_mmp.bin
# Root-level compat symlinks for kernel firmware loader
%{_firmwarepath}/qat_*.bin

%changelog
* Mon Aug 3 2026 Andy <andy.peng@intel.com> - 20260622-2
- Add ipu8_fw.bin firmware.

* Mon Jun 27 2026 Andy <andy.peng@intel.com> - 20260622-1
- Upgrade firmware to 20260622.

* Wed Apr 15 2026 Andy <andy.peng@intel.com> - 20260309-3
- Use upstream copy-firmware.sh to install firmware with proper symlinks.
- Fixes missing ibt-19-* Bluetooth firmware symlinks.
- Add root-level iwlwifi-* and qat_* compat symlinks so kernel can find firmware.

* Fri Apr 3 2026 Andy <andy.peng@intel.com> - 20260309-2
- Include more i915 xe file from firmware.

* Fri Mar 27 2026 Andy <andy.peng@intel.com> - 20260309-1
- Upgrade firmware to 20260309.

* Thu Feb 5 2026 Andy <andy.peng@intel.com> - 20260110-2
- modify target value of symlink to point ice package.

* Tue Jan 13 2026 Andy <andy.peng@intel.com> - 20260110-1
- Upgrade firmware to 20260110.

* Tue Nov 11 2025 Shalini Singhal <shalinix.singhal@intel.com> - 20251021-1
- Upgrade firmware to 20251021.

* Tue Oct 14 2025 Junxiao Chang <junxiao.chang@intel.com> - 20250509-3
- Added QAT firmware.

* Wed Sep 17 2025 Swee Yee Fonn <swee.yee.fonn@intel.com> - 20250509-2
- Added iwlwifi package for Intel Wi-Fi AX210, Jefferson Peak, Thunder Peak.

* Wed Jun 18 2025 Junxiao Chang <junxiao.chang@intel.com> - 20250509-1
- Upgrade i915 GuC firmware version to 70.44.1.

+* Tue June 10 2025 shalinix singhal <shalinix.singhal@intel.com> - 20250311-4
+- Added iwlwifi ucode file in firmware

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
