Summary:        Full Disk Encryption with DM-verity to ensure confidentiality and integrity
Name:           tpm-cryptsetup
Version:        1.0
Release:        10%{?dist}
License:        GPLv2+
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Base
URL:            https://github.com/open-edge-platform/edge-microvisor-toolkit
Source0:        tpm-cryptsetup.conf
Source1:        01tpm-cryptsetup/module-setup.sh
Source2:        01tpm-cryptsetup/tpm-cryptsetup.sh
Source3:        01tpm-cryptsetup/systemd-cryptsetup@root.service
Source4:        COPYING
Requires:       dracut
Requires:       kpartx

%description
Purpose of this module is to enable FDE and dm-verity on select partitions. Details on the
architecture can be found in the ADR. 

%install
mkdir -p %{buildroot}%{_sysconfdir}/dracut.conf.d
install -D -m 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/dracut.conf.d/

mkdir -p %{buildroot}%{_libdir}/dracut/modules.d/01tpm-cryptsetup/
install -p -m 0755 %{SOURCE1} %{buildroot}%{_libdir}/dracut/modules.d/01tpm-cryptsetup/
install -p -m 0755 %{SOURCE2} %{buildroot}%{_libdir}/dracut/modules.d/01tpm-cryptsetup/
install -p -m 0755 %{SOURCE3} %{buildroot}%{_libdir}/dracut/modules.d/01tpm-cryptsetup/

cp %{SOURCE4} COPYING

%files
%{_sysconfdir}/dracut.conf.d/tpm-cryptsetup.conf
%dir %{_libdir}/dracut/modules.d/01tpm-cryptsetup
%{_libdir}/dracut/modules.d/01tpm-cryptsetup/*

%changelog
* Thu Sep 3 2026 Chee Yang Lee <chee.yang.lee@intel.com> - 1.0-10
- drop use of awk in the script.

* Mon Mar 10 2025 Adithya Baglody <adithya.nagaraj.baglody@intel.com> - 1.0-9
- Support a usecase where only dm-verity is enabled without FDE
- The script first checks if FDE is enabled, if not, it will
  check if DM-verity is enabled. If not then dmsetup will create a
  logical volume for the entire rootfs.

* Tue Mar 11 2025 Chee Yang Lee <chee.yang.lee@intel.com> - 1.0-8
- update URL.

* Fri Feb 21 2025 SupriyaPamulpati <pamulapati.supriya@intel.com> - 1.0-7
- Update rootfs_number extraction to prevent syntax issues at boot time

* Wed Dec 18 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 1.0-6
- Update URL to Edge Microvisor Toolkit repository.

* Thur Nov 28 2024 Adithya Baglody <adithya.nagaraj.baglody@intel.com> - 1.0-5
- Updated to handle boot_uuid from UKI to select the correct rootfs

* Thur Nov 11 2024 Adithya Baglody <adithya.nagaraj.baglody@intel.com> - 1.0-4
- Updated the dracut module name.
- Remove initramfs from Requires.

* Thur Nov 07 2024 Adithya Baglody <adithya.nagaraj.baglody@intel.com> - 1.0-3
- Selected the correct TPM PCR to unseal.

* Thur Oct 30 2024 Adithya Baglody <adithya.nagaraj.baglody@intel.com> - 1.0-2
- Enable FDE setup script to dynamically select between 2 configurations.
  First is encryption of only user partition.
  Second config is FDE with dm-verity.
  Selection between configurations is set during the provisioning of Edge Microvisor Toolkit.

* Thur Sept 26 2024 Adithya Baglody <adithya.nagaraj.baglody@intel.com> - 1.0-1
- Original version for Edge Microvisor Toolkit.
