Summary:        Preempt RT Linux Kernel
Name:           kernel-rt
Version:        7.0.0
Release:        1%{?dist}
License:        GPLv2
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://www.kernel.org/pub/linux/kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v7.x/linux-7.0.tar.gz
Source1:        config
Source3:        sha512hmac-openssl.sh
Source4:        emt-ca-20211013.pem
Source5:        cpupower
Source6:        cpupower.service

# v7.0
#028ef9c96e96 Linux 7.0
# security
Patch01001: 0001-v7.0-rc3-Add-SECURITY.md-file.security
Patch01002: 0001-x86-bhi-x86-vmscape-Move-LFENCE-out-of-clear_bhb_.security
Patch01003: 0002-x86-bhi-Make-clear_bhb_loop-effective-on-newer-CP.security
Patch01004: 0003-x86-bhi-Rename-clear_bhb_loop-to-clear_bhb_loop_n.security
Patch01005: 0004-x86-vmscape-Rename-x86_ibpb_exit_to_user-to-x86_p.security
Patch01006: 0005-x86-vmscape-Move-mitigation-selection-to-a-switch.security
Patch01007: 0006-x86-vmscape-Use-write_ibpb-instead-of-indirect_br.security
Patch01008: 0007-x86-vmscape-Use-static_call-for-predictor-flush.security
Patch01009: 0008-x86-vmscape-Deploy-BHB-clearing-mitigation.security
Patch01010: 0009-x86-vmscape-Fix-conflicting-attack-vector-control.security
Patch01011: 0010-x86-vmscape-Add-cmdline-vmscape-on-to-override-at.security
Patch01012: 0001-x86-tboot-Add-support-for-parsing-DTPR-table-and-.security
Patch01013: 0002-iommu-vt-d-Disable-PMRs-and-skip-force-IOMMU-when.security
Patch01014: 0001-iommu-vt-d-cache-TPR-mappings-at-boot-to-fix-S3-r.security
# security issei
Patch01015: 0001-issei-initial-driver-skeleton.security
Patch01016: 0002-issei-add-firmware-and-host-clients-implementatio.security
Patch01017: 0003-issei-implement-main-thread-and-ham-messages.security
Patch01018: 0004-issei-add-heci-hardware-module.security
Patch01019: 0005-issei-add-runtime-pm.security
Patch01020: 0006-issei-host_client-add-dma-allocation-support.security
Patch01021: 0007-issei-add-driver-to-driver-interface.security
# security mei
Patch01022: 0001-mei-me-use-PCI_DEVICE_DATA-macro.security
Patch01023: 0002-mei-fix-idle-print-specifiers.security
Patch01024: 0003-mei-me-move-trace-into-firmware-status-read.security
Patch01025: 0004-mei-trace-print-return-value-of-pci_cfg_read.security
Patch01026: 0005-mei-convert-PCI-error-to-common-errno.security
Patch01027: 0006-mei-csc-support-controller-with-separate-PCI-devi.security
Patch01028: 0007-mei-csc-wake-device-while-reading-firmware-status.security
Patch01029: 0008-mei-bus-fix-device-leak.security
Patch01030: 0009-mei-bus-add-api-to-query-capabilities-of-ME-clien.security
Patch01031: 0010-mei-store-kind-as-enum.security
Patch01032: 0011-mei-expose-device-kind-for-ioe-device.security
Patch01033: 0012-mei-me-remove-comma-from-mei_cfg_idx-sentinel.security
Patch01034: 0013-mei-virtio-virtualization-frontend-driver.security
Patch01035: 0014-INTEL_DII-mei-avoid-reset-if-fw-is-down.security
Patch01036: 0015-INTEL_DII-mei-iaf-add-iaf-Intel-Accelerator-Fabri.security
Patch01037: 0016-mei-bus-TEST-add-client-dma-test-module.security
Patch01038: 0017-mei-me-add-nova-lake-point-H-DID.security
# storage
Patch02001: 0001-scsi-ufs-ufs-pci-Add-support-for-Intel-Nova-Lake.storage
Patch02002: 0001-PCI-vmd-Add-vmd_bus_enumeration-helper-function.storage
Patch02003: 0002-PCI-vmd-Add-vmd_configure_cfgbar-helper-function.storage
Patch02004: 0003-PCI-vmd-Add-vmd_configure_membar-and-vmd_configure.storage
Patch02005: 0004-PCI-vmd-Add-vmd_create_bus.storage
Patch02006: 0005-PCI-vmd-Replace-hardcoded-values-with-enum-and-def.storage
Patch02007: 0006-PCI-vmd-Convert-bus-and-busn_start-to-an-array.storage
Patch02008: 0007-PCI-vmd-Add-support-for-second-rootbus-under-VMD.storage
Patch02009: 0008-PCI-vmd-Add-workaround-for-bus-number-hardwired-to.storage
Patch02010: 0009-Add-VMD-Device-ID-for-NVL.storage
# perf
Patch03001: 0001-perf-x86-msr-Make-SMI-and-PPERF-on-by-default.perf
Patch03002: 0003-perf-x86-intel-Only-check-GP-counters-for-PEBS-constr.perf
Patch03003: 0004-perf-x86-intel-Restrict-PEBS_ENABLE-writes-to-PEBS-ca.perf
Patch03004: 0005-perf-x86-intel-Enable-large-PEBS-sampling-for-XMMs.perf
Patch03005: 0006-perf-x86-intel-Convert-x86_perf_regs-to-per-cpu-varia.perf
Patch03006: 0007-perf-Eliminate-duplicate-arch-specific-functions-defi.perf
Patch03007: 0008-perf-x86-Use-x86_perf_regs-in-the-x86-nmi-handler.perf
Patch03008: 0009-perf-x86-Introduce-x86-specific-x86_pmu_setup_regs_da.perf
Patch03009: 0010-x86-fpu-xstate-Add-xsaves_nmi-helper.perf
Patch03010: 0011-x86-fpu-Ensure-TIF_NEED_FPU_LOAD-is-set-after-saving-.perf
Patch03011: 0012-perf-Move-and-rename-has_extended_regs-for-ARCH-speci.perf
Patch03012: 0013-perf-x86-Enable-XMM-Register-Sampling-for-Non-PEBS-Ev.perf
Patch03013: 0014-perf-x86-Enable-XMM-register-sampling-for-REGS_USER-c.perf
Patch03014: 0015-perf-Add-sampling-support-for-SIMD-registers.perf
Patch03015: 0016-perf-x86-Enable-XMM-sampling-using-sample_simd_vec_re.perf
Patch03016: 0017-perf-x86-Enable-YMM-sampling-using-sample_simd_vec_re.perf
Patch03017: 0018-perf-x86-Enable-ZMM-sampling-using-sample_simd_vec_re.perf
Patch03018: 0019-perf-x86-Enable-OPMASK-sampling-using-sample_simd_pre.perf
Patch03019: 0020-perf-Enhance-perf_reg_validate-with-simd_enabled-argu.perf
Patch03020: 0021-perf-x86-Enable-eGPRs-sampling-using-sample_regs_-fie.perf
Patch03021: 0022-perf-x86-Enable-SSP-sampling-using-sample_regs_-field.perf
Patch03022: 0023-perf-x86-intel-Enable-PERF_PMU_CAP_SIMD_REGS-capabili.perf
Patch03023: 0024-perf-x86-intel-Enable-arch-PEBS-based-SIMD-eGPRs-SSP-.perf
Patch03024: 0025-perf-x86-Activate-back-to-back-NMI-detection-for-arch.perf
Patch03025: 0026-perf-headers-Sync-with-the-kernel-headers.perf
Patch03026: 0027-perf-regs-Support-x86-eGPRs-SSP-sampling.perf
Patch03027: 0028-perf-regs-Support-x86-SIMD-registers-sampling.perf
Patch03028: 0029-perf-regs-Enable-dumping-of-SIMD-registers.perf
Patch03029: 0034-perf-x86-Remove-helper-perf_events_lapic_init-from-x8.perf
Patch03030: 0035-perf-x86-Fix-typos-and-inconsistent-indents-in-perf_e.perf
Patch03031: 0036-KVM-x86-pmu-Only-map-generic-perf-events-for-fixed-co.perf
Patch03032: 0037-KVM-x86-pmu-Support-Intel-fixed-counter-3-on-mediated.perf
Patch03033: 0038-KVM-x86-pmu-Support-PERF_METRICS-MSR-in-mediated-vPMU.perf
Patch03034: 0039-KVM-x86-pmu-Insert-GP-for-invalid-architectural-PMU-M.perf
Patch03035: 0001-perf-core-allow-trace-events-to-be-accessed-from-any-.perf
# pmt
Patch04001: 0001-platform-x86-intel-vsec-Refactor-base_addr-handling.pmt
Patch04002: 0002-platform-x86-intel-vsec-Make-driver_data-info-const.pmt
Patch04003: 0003-platform-x86-intel-vsec-Decouple-add-link-helpers-from.pmt
Patch04004: 0004-platform-x86-intel-vsec-Switch-exported-helpers-from-p.pmt
Patch04005: 0005-platform-x86-intel-vsec-Return-real-error-codes-from-r.pmt
Patch04006: 0006-platform-x86-intel-vsec-Plumb-ACPI-PMT-discovery-table.pmt
Patch04007: 0007-platform-x86-intel-pmt-Add-pre-post-decode-hooks-aroun.pmt
Patch04008: 0008-platform-x86-intel-pmt-crashlog-Split-init-into-pre-de.pmt
Patch04009: 0009-platform-x86-intel-pmt-telemetry-Move-overlap-check-to.pmt
Patch04010: 0010-platform-x86-intel-pmt-Move-header-decode-into-common-.pmt
Patch04011: 0011-platform-x86-intel-pmt-Pass-discovery-index-instead-of.pmt
Patch04012: 0012-platform-x86-intel-pmt-Unify-header-fetch-and-add-ACPI.pmt
Patch04013: 0013-platform-x86-intel-pmc-Add-PMC-SSRAM-Kconfig-descripti.pmt
Patch04014: 0014-platform-x86-intel-pmc-Add-ACPI-PWRM-telemetry-driver-.pmt
Patch04015: 0015-platform-x86-intel-pmc-ssram-Rename-probe-and-PCI-ID-t.pmt
Patch04016: 0016-platform-x86-intel-pmc-ssram-Use-fixed-size-static-pmc.pmt
Patch04017: 0017-platform-x86-intel-pmc-ssram-Refactor-DEVID-PWRMBASE-e.pmt
Patch04018: 0018-platform-x86-intel-pmc-ssram-Add-PCI-platform-data.pmt
Patch04019: 0019-platform-x86-intel-pmc-ssram-Refactor-memory-barrier-f.pmt
Patch04020: 0020-platform-x86-intel-pmc-ssram-Add-ACPI-discovery-scaffo.pmt
Patch04021: 0021-platform-x86-intel-pmc-ssram-Make-PMT-registration-opt.pmt
Patch04022: 0022-platform-x86-intel-pmc-Add-NVL-PCI-IDs-for-SSRAM-telem.pmt
# gpio
Patch05001: 0001-gpio-Add-Intel-Nova-Lake-ACPI-GPIO-events-driver.gpio
# pmc_core
Patch06001: 0001-platform-x86-intel-pmc-Enable-PkgC-LTR-blocking-c.pmc_core
Patch06002: 0002-platform-x86-intel-pmc-Enable-Pkgc-blocking-resid.pmc_core
Patch06003: 0003-platform-x86-intel-pmc-Use-PCI-DID-for-PMC-SSRAM-.pmc_core
Patch06004: 0004-platform-x86-intel-pmc-Add-support-for-variable-D.pmc_core
Patch06005: 0005-platform-x86-intel-pmc-Retrieve-PMC-info-only-for.pmc_core
Patch06006: 0006-platform-x86-intel-pmc-Add-Nova-Lake-support-to-i.pmc_core
Patch06007: 0007-CONFLICT-Resolve-pmt_telem_find_and_register_endp.pmc_core
Patch06008: 0001-platform-x86-intel-pmc-Change-max-number-of-ppfea.pmc_core
Patch06009: 0001-platform-x86-intel-pmc-Update-NVL-PCDS_LPM_REQ_GU.pmc_core
# lpss
Patch07001: 0001-mfd-intel-lpss-Add-Intel-Nova-Lake-H-PCI-IDs.lpss
Patch07002: 0001-Added-spi_set_cs-for-more-stable-r-w-operations-in-SP.lpss
# i3c
Patch08001: 0001-i3c-mipi-i3c-hci-pci-Add-support-for-Intel-Nova-Lake-H.i3c
# ethernet
Patch09001: 0001-xfrm-esp-avoid-in-place-decrypt-on-shared-skb-fra.ethernet
Patch09002: 0002-rxrpc-Fix-potential-UAF-after-skb_unshare-failure.ethernet
Patch09003: 0003-rxrpc-Fix-conn-level-packet-handling-to-unshare-R.ethernet
Patch09004: 0004-rxrpc-Fix-re-decryption-of-RESPONSE-packets.ethernet
Patch09005: 0005-rxrpc-Fix-rxrpc_input_call_event-to-only-unshare-.ethernet
Patch09006: 0006-rxrpc-Also-unshare-DATA-RESPONSE-packets-when-pag.ethernet
Patch09007: 0001-igc-Only-dump-registers-if-configured-to-dump-HW-.ethernet
Patch09008: 0002-af_packet-Fix-wrong-timestamps-in-tcpdump.ethernet
Patch09009: 0003-igc-skip-RX-timestamp-header-for-frame-preemption.ethernet
Patch09010: 0004-igc-Add-support-for-DMA-timestamp-for-non-PTP-pac.ethernet
Patch09011: 0005-bpf-add-btf-register-unregister-API.ethernet
Patch09012: 0006-net-core-XDP-metadata-BTF-netlink-API.ethernet
Patch09013: 0007-rtnetlink-Fix-unchecked-return-value-of-dev_xdp_q.ethernet
Patch09014: 0008-rtnetlink-Add-return-value-check.ethernet
Patch09015: 0009-tools-bpf-Query-XDP-metadata-BTF-ID.ethernet
Patch09016: 0010-tools-bpf-Add-xdp-set-command-for-md-btf.ethernet
Patch09017: 0011-igc-Add-BTF-based-metadata-for-XDP.ethernet
Patch09018: 0012-igc-Enable-HW-RX-Timestamp-for-AF_XDP-ZC.ethernet
Patch09019: 0013-igc-Take-care-of-DMA-timestamp-rollover.ethernet
Patch09020: 0014-igc-Enable-HW-TX-Timestamp-for-AF_XDP-ZC.ethernet
Patch09021: 0015-igc-Enable-trace-for-HW-TX-Timestamp-AF_XDP-ZC.ethernet
Patch09022: 0016-igc-Remove-the-CONFIG_DEBUG_MISC-condition-for-tr.ethernet
Patch09023: 0017-igc-Remove-XDP-metadata-invalidation.ethernet
# audio
Patch10001: 0001-ASoC-Intel-soc-acpi-Add-entry-for-sof_es8336-in-NVL-.audio
Patch10002: 0001-ASoC-Intel-soc-acpi-Add-entry-for-HDMI_In-capture-su.audio
Patch10003: 0001-ASoC-Intel-soc-acpi-Add-entry-for-sof_rt5682-in-NVL-.audio
Patch10004: 0002-ASoC-Intel-sof_rt5682-Add-HDMI-In-capture-with-rt568.audio
Patch10005: 0001-ASoC-Intel-NVL-Add-entry-for-HDMI-In-capture-support.audio
# edac
Patch11001: 0001-EDAC-igen6-Fix-call-trace-due-to-missing-release.edac
Patch11002: 0002-EDAC-igen6-Fix-memory-topology-parsing-for-Panther-La.edac
Patch11003: 0003-EDAC-igen6-Add-one-Intel-Panther-Lake-H-SoC-support.edac
Patch11004: 0004-EDAC-igen6-Make-registers-for-detecting-IBECC-configu.edac
Patch11005: 0005-EDAC-igen6-Add-Intel-Nova-Lake-H-SoC-support.edac
# sriov
Patch12001: 0001-drm-xe-nvls-Enable-SRIOV-support-in-NVL-S.sriov
Patch12002: 0002-drm-sa-Split-drm_suballoc_new-into-SA-alloc-and-init.sriov
Patch12003: 0003-drm-xe-vf-Fix-fs_reclaim-warning-with-CCS-save-resto.sriov
Patch12004: 0004-drm-xe-sa-Add-lockdep-annotations-for-SA-manager-swa.sriov
Patch12005: 0005-drm-xe-Add-memory-pool-with-shadow-support.sriov
Patch12006: 0006-drm-xe-vf-Use-drm-mm-instead-of-drm-sa-for-CCS-read-.sriov
Patch12007: 0007-iommu-vt-d-Add-NVL-to-quirk-list-to-skip-TE-disablin.sriov
Patch12008: 0008-drm-virtio-freeze-and-restore-hooks-to-support-suspe.sriov
Patch12009: 0009-drm-virtio-save-and-restore-virtio_gpu_objects.sriov
Patch12010: 0010-drm-virtio-Wait-until-the-control-and-cursor-queues-.sriov
# conn
Patch13001: 0001-Bluetooth-btintel_pcie-Replace-snprintf-s-with-strscp.conn
Patch13002: 0002-Bluetooth-btintel_pcie-Use-struct_size-to-improve-hci.conn
Patch13003: 0003-Bluetooth-btintel-Add-support-for-hybrid-signature-fo.conn
Patch13004: 0004-Bluetooth-btintel-Replace-CNVi-id-with-hardware-varia.conn
Patch13005: 0005-Bluetooth-btintel-Add-support-for-Scorpious-Peak2-sup.conn
Patch13006: 0006-Bluetooth-btintel-Add-DSBR-support-for-ScP2-onwards.conn
Patch13007: 0007-Bluetooth-btintel_pcie-Add-support-for-exception-dump.conn
Patch13008: 0008-Bluetooth-btintel-Add-support-for-Scorpious-Peak2F-su.conn
Patch13009: 0009-Bluetooth-btintel_pcie-Add-support-for-exception-dump.conn
Patch13010: 0010-Bluetooth-btintel_pcie-Add-device-id-of-Scorpius-Peak.conn
Patch13011: 0011-Bluetooth-btintel_pcie-Add-device-id-of-Scorpious2-No.conn
Patch13012: 0012-Bluetooth-btintel_pci-Fix-btintel_pcie_read_hwexp-cod.conn
Patch13013: 0013-Bluetooth-btintel_pcie-Align-shared-DMA-memory-to-128.conn
Patch13014: 0014-Bluetooth-btintel_pcie-use-strscpy-to-copy-plain-stri.conn
Patch13015: 0015-Bluetooth-btintel_pcie-Support-Product-level-reset.conn
Patch13016: 0016-Bluetooth-btintel_pcie-treat-boot-stage-bit-12-as-war.conn
Patch13017: 0017-Bluetooth-btintel_pcie-Fix-incorrect-MAC-access-progr.conn
Patch13018: 0018-Bluetooth-btintel_pcie-Add-support-for-smart-trigger-.conn
# drm
Patch14001: 0001-drm-xe-nvls-Define-GuC-firmware-for-NVL-S.drm
Patch14002: 0001-drm-xe-Move-number-of-XeCore-fuse-registers-to-graphic.drm
Patch14003: 0002-drm-xe-xe3p_xpc-XeCore-mask-spans-four-registers.drm
Patch14004: 0003-drm-xe-xe3p_lpg-Add-support-for-graphics-IP-35.10.drm
Patch14005: 0004-drm-xe-xe3p_lpg-Add-initial-workarounds-for-graphics-v.drm
Patch14006: 0005-drm-xe-pat-Differentiate-between-primary-and-media-for.drm
Patch14007: 0006-drm-xe-xe3p_lpg-Add-new-PAT-table.drm
Patch14008: 0007-drm-xe-xe3p_lpg-Add-MCR-steering.drm
Patch14009: 0008-drm-xe-xe3p_lpg-Add-LRC-parsing-for-additional-RCS-eng.drm
Patch14010: 0009-drm-xe-xe3p_lpg-Disable-reporting-of-context-switch-st.drm
Patch14011: 0010-drm-xe-xe3p_lpg-Drop-unnecessary-tuning-settings.drm
Patch14012: 0011-drm-xe-xe3p_lpg-Extend-group-ID-mask-size.drm
Patch14013: 0012-drm-xe-xe3p_lpg-Update-LRC-sizes.drm
Patch14014: 0013-drm-xe-xe3p_lpg-Set-STLB-bank-hash-mode-to-4KB.drm
Patch14015: 0014-drm-xe-nvlp-Add-NVL-P-platform-definition.drm
Patch14016: 0015-drm-xe-nvlp-Attach-MOCS-table-for-nvlp.drm
Patch14017: 0016-drm-i915-nvlp-Hook-up-display-support.drm
Patch14018: 0017-drm-xe-nvlp-Bump-maximum-WOPCM-size.drm
Patch14019: 0018-drm-xe-Modify-stepping-info-directly-in-xe_step_-_get.drm
Patch14020: 0019-drm-xe-Drop-unused-IS_PLATFORM_STEP-and-IS_SUBPLATFORM.drm
Patch14021: 0020-drm-xe-nvlp-Read-platform-level-stepping-info.drm
Patch14022: 0021-drm-xe-rtp-Add-support-for-matching-platform-level-ste.drm
Patch14023: 0022-drm-xe-nvlp-Implement-Wa_14026539277.drm
Patch14024: 0023-drm-xe-xe3p-Drop-Wa_16028780921.drm
Patch14025: 0024-drm-xe-Translate-C-state-reset-value-into-RC6.drm
Patch14026: 0025-drm-xe-nvlp-Define-GuC-firmware-for-NVL-P.drm
Patch14027: 0026-drm-i915-cdclk-Extend-Wa_13012396614-to-Xe3p_LPD.drm
Patch14028: 0027-drm-xe-xe3p_xpc-Add-new-XeCore-fuse-registers-to-VF-ru.drm
Patch14029: 0028-drm-xe-xe3p_lpg-Add-Wa_14026781792.drm
Patch14030: 0029-drm-i915-fbc-remove-uint16-from-supported-FBC-formats-.drm
Patch14031: 0030-drm-xe-tuning-Apply-windower-hardware-filtering-settin.drm
Patch14032: 0031-drm-xe-xe3p_xpc-Drop-stale-MCR-steering-TODO-comment.drm
Patch14033: 0032-drm-xe-xe3p_lpg-flush-shrinker-bo-cachelines-manually.drm
Patch14034: 0033-drm-xe-pat-define-coh_mode-2way.drm
Patch14035: 0034-drm-xe-xe3p_lpg-Restrict-UAPI-to-enable-L2-flush-optim.drm
Patch14036: 0035-drm-xe-xe3p-Skip-TD-flush.drm
Patch14037: 0036-drm-xe-xe3p_lpg-Add-Wa_18044193044.drm
Patch14038: 0037-drm-xe-xe3p_lpg-Add-missing-indirect-ring-state-featur.drm
Patch14039: 0038-drm-xe-tuning-Stop-applying-CCCHKNREG1-tuning-from-Xe3.drm
Patch14040: 0039-drm-xe-tuning-Use-proper-register-offset-for-GAMSTLB_C.drm
Patch14041: 0040-drm-xe-Mark-ROW_CHICKEN5-as-a-masked-register.drm
Patch14042: 0041-drm-xe-sriov-Mark-NVL-as-SR-IOV-capable.drm
Patch14043: 0042-drm-xe-Add-Wa_14026578760.drm
Patch14044: 0043-drm-xe-nvls-Update-PCI-IDs.drm
Patch14045: 0001-drm-i915-xe3p_lpd-Extend-Type-C-flow-for-static-DDI-al.drm
Patch14046: 0001-drm-xe-guc-define-GuC-firmware-for-NVL-S.drm
# ipu
Patch15001: 0001-Add-New-Camera-sensor-Module.ipu
Patch15002: 0002-media-i2c-add-Maxim-GMSL2-3-serializer-and-deserialize.ipu
Patch15003: 0003-media-i2c-add-Maxim-GMSL2-3-serializer-framework.ipu
Patch15004: 0004-media-i2c-add-Maxim-GMSL2-3-deserializer-framework.ipu
Patch15005: 0005-media-i2c-maxim-serdes-add-MAX96717-driver.ipu
Patch15006: 0006-media-i2c-maxim-serdes-add-MAX96724-driver.ipu
Patch15007: 0007-media-i2c-maxim-serdes-add-MAX9296A-driver.ipu
Patch15008: 0008-media-i2c-max96717-Backport-to-v6.17.ipu
Patch15009: 0009-media-i2c-max_des-Fix-stream-mask-override-in-multi-st.ipu
Patch15010: 0010-media-i2c-max9296a-Fix-video-pipe-status-register-offs.ipu
Patch15011: 0011-media-i2c-max9296a-Fix-PHY-index-and-stream-ID-paramet.ipu
Patch15012: 0012-media-i2c-max9296a-Add-ACPI-ID.ipu
Patch15013: 0013-media-i2c-max9295a-Add-ACPI-ID.ipu
Patch15014: 0014-media-i2c-max96724-Add-ACPI-ID.ipu
Patch15015: 0015-media-i2c-max9296a-Move-use_atr-flag-to-deserializer-o.ipu
Patch15016: 0016-media-i2c-max96717-Guard-DT-pinctrl-ops-with-CONFIG_OF.ipu
Patch15017: 0017-media-i2c-max96724-Update-phy-to-id-mapping.ipu
Patch15018: 0018-media-i2c-max_serdes-Check-secondary-fwnode.ipu
Patch15019: 0019-media-i2c-maxim-serdes-Add-acpi_dev_clear_dependencies.ipu
Patch15020: 0020-maxim-serdes-max_des-Add-bus_handle-of-child-fwnode-in.ipu
Patch15021: 0021-maxim-serdes-max_ser-Add-bus_handle-of-child-fwnode-in.ipu
Patch15022: 0022-media-i2c-maxim-serdes-Add-V4L2_CID_LINK_FREQ-support.ipu
Patch15023: 0023-media-i2c-maxim-serdes-max96717-Add-VS_INDEPENDENT-mod.ipu
Patch15024: 0024-media-i2c-maxim-serdes-max_ser-Add-vc-id-into-pipe-sel.ipu
Patch15025: 0025-media-i2c-maxim-serdes-max_des-Dynamically-assign-acti.ipu
Patch15026: 0026-media-i2c-maxim-serdes-Retrieve-pipe-stream-autoselect.ipu
Patch15027: 0027-media-i2c-max_serdes-Fix-kernel-crash.ipu
Patch15028: 0028-media-i2c-maxim-serdes-max_des-Fix-stream-assign-issue.ipu
Patch15029: 0029-media-i2c-maxim-serdes-max_serdes-Update-pads-that-is-.ipu
Patch15030: 0030-maxim-serdes-Minor-fix-on-initialization-and-unused-va.ipu
Patch15031: 0031-dkms-add-kernel-7.0-support-and-align-IPU6-IPU7-patch-.ipu
Patch15032: 0032-fix-max-serdes-avoid-ACPI-NULL-deref-in-i2c-gate-detec.ipu
Patch15033: 0033-media-i2c-max9x-remove-DRIVER_VERSION_SUFFIX.ipu
Patch15034: 0034-staging-ipu7-Wait-back-firmware-message-buffers-when-t.ipu
Patch15035: 0035-staging-ipu7-reclaim-pending-fw-msg-buffers-by-stream_.ipu
Patch15036: 0036-media-ipu-Dma-sync-at-buffer_prepare-callback-as-DMA-i.ipu
Patch15037: 0037-patch-staging-add-ipu7-isys-reset-code-for-v7.0.ipu
Patch15038: 0038-patch-staging-add-enable-CONFIG_DEBUG_FS.ipu
Patch15039: 0039-patch-staging-add-enable-CONFIG_INTEL_IPU_ACPI.ipu
Patch15040: 0040-patch-staging-add-enable-ENABLE_FW_OFFLINE_LOGGER.ipu
Patch15041: 0041-patch-staging-add-patch-for-use-DPHY-as-the-default-ph.ipu
Patch15042: 0042-patch-staging-add-pacth-for-ipu7-Kconfig-Makefile.ipu
Patch15043: 0043-patch-staging-add-ipu7-isys-tpg-and-MGC-config.ipu
Patch15044: 0044-INT3472-Support-LT6911GXD.ipu
Patch15045: 0045-media-i2c-add-support-for-lt6911gxd.ipu
Patch15046: 0046-media-pci-enable-lt6911gxd-in-ipu-bridge.ipu
Patch15047: 0047-ipu-bridge-add-CPHY-support.ipu
Patch15048: 0048-max9x-add-config-in-makefile-kconfig.ipu
Patch15049: 0049-drivers-media-set-v4l2_subdev_enable_streams_api-true-.ipu
Patch15050: 0050-staging-ipu7-Update-IPU7-firmware-ABI-version-to-1.2.1.ipu
Patch15051: 0051-patch-staging-add-IPU8_PCI_ID-support.ipu
Patch15052: 0052-staging-ipu7-Add-IPU8-ABI-version-1.0.12.ipu
Patch15053: 0053-staging-ipu7-Define-gpreg_stride-for-different-IPU-ver.ipu
Patch15054: 0054-staging-media-ipu7-Fix-potential-NULL-pointer-derefere.ipu
Patch15055: 0055-staging-media-ipu7-set-skipframe-flag-when-frame-error.ipu
Patch15056: 0056-staging-ipu7-Add-more-insys-frame-format.ipu
Patch15057: 0057-media-mc-Add-INTERNAL-pad-flag.ipu
Patch15058: 0058-ipu-bridge-add-sensor.ipu
Patch15059: 0059-media-pci-ipu7-Add-D4XX-support-to-IPU7.ipu
Patch15060: 0060-media-ipu7-get-source-pad-according-to-csi2-ep-fwnode.ipu
Patch15061: 0061-media-ipu7-Clean-csi2-fwnode-ep-when-destroying-v4l2_a.ipu
Patch15062: 0062-media-ipu7-isys-let-v4l2-set-default-colorspace.ipu
Patch15063: 0063-media-ipu7-sync-psys-folder-from-ipu7-drivers.ipu
Patch15064: 0064-media-i2c-fix-compilation-config-issue.ipu
Patch15065: 0065-media-ipu-bridge-add-X86-dependency.ipu
Patch15066: 0001-ipu7-Wait-ipu-fw-requests-to-clear.ipu
Patch15067: 0002-staging-ipu7-add-isys-reset-feature.ipu
Patch15068: 0003-staging-ipu7-reclaim-pending-fw-msg-buffers-by-stream_.ipu
Patch15069: 0004-Apply-remaining-ipu7-driver-patches.ipu


%global security_hardening none
%global sha512hmac bash %{_sourcedir}/sha512hmac-openssl.sh
%define uname_r %{version}-%{release}

# find_debuginfo.sh arguments are set by default in rpm's macros.
# The default arguments regenerate the build-id for vmlinux in the
# debuginfo package causing a mismatch with the build-id for vmlinuz in
# the kernel package. Therefore, explicilty set the relevant default
# settings to prevent this behavior.
%undefine _unique_build_ids
%undefine _unique_debug_names
%global _missing_build_ids_terminate_build 1
%global _no_recompute_build_ids 1

%ifarch x86_64
%define arch x86_64
%define archdir x86
%define config_source %{SOURCE1}
%endif

%ifarch aarch64
%global __provides_exclude_from %{_libdir}/debug/.build-id/
%define arch arm64
%define archdir arm64
%define config_source %{SOURCE2}
%endif

BuildRequires:  audit-devel
BuildRequires:  bash
BuildRequires:  bc
BuildRequires:  build-essential
BuildRequires:  cpio
BuildRequires:  diffutils
BuildRequires:  dwarves
BuildRequires:  elfutils-libelf-devel
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  glib-devel
BuildRequires:  grub2-rpm-macros
BuildRequires:  kbd
BuildRequires:  kmod-devel
BuildRequires:  libcap-devel
BuildRequires:  libdnet-devel
BuildRequires:  libmspack-devel
BuildRequires:  libtraceevent-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  perl-devel
BuildRequires:  procps-ng-devel
BuildRequires:  python3-devel
BuildRequires:  sed
BuildRequires:  slang-devel
BuildRequires:  systemd-bootstrap-rpm-macros
%ifarch x86_64
BuildRequires:  pciutils-devel
%endif
Requires:       filesystem
Requires:       kmod
Requires(post): coreutils
Requires(postun): coreutils
%{?grub2_configuration_requires}
# When updating the config files it is important to sanitize them.
# Steps for updating a config file:
#  1. Extract the linux sources into a folder
#  2. Add the current config file to the folder
#  3. Run `make menuconfig` to edit the file (Manually editing is not recommended)
#  4. Save the config file
#  5. Copy the config file back into the kernel spec folder
#  6. Revert any undesired changes (GCC related changes, etc)
#  8. Build the kernel package
#  9. Apply the changes listed in the log file (if any) to the config file
#  10. Verify the rest of the config file looks ok
# If there are significant changes to the config file, disable the config check and build the
# kernel rpm. The final config file is included in /boot in the rpm.

%description
The kernel package contains the Linux kernel.

%package devel
Summary:        Kernel Dev
Group:          System Environment/Kernel
Requires:       %{name} = %{version}-%{release}
Requires:       gawk
Requires:       python3

%description devel
This package contains the Linux kernel dev files

%package drivers-accessibility
Summary:        Kernel accessibility modules
Group:          System Environment/Kernel
Requires:       %{name} = %{version}-%{release}

%description drivers-accessibility
This package contains the Linux kernel accessibility support

%package drivers-gpu
Summary:        Kernel gpu modules
Group:          System Environment/Kernel
Requires:       %{name} = %{version}-%{release}

%description drivers-gpu
This package contains the Linux kernel gpu support

%package drivers-sound
Summary:        Kernel Sound modules
Group:          System Environment/Kernel
Requires:       %{name} = %{version}-%{release}

%description drivers-sound
This package contains the Linux kernel sound support

%package docs
Summary:        Kernel docs
Group:          System Environment/Kernel
Requires:       python3

%description docs
This package contains the Linux kernel doc files

%package tools
Summary:        This package contains the 'perf' performance analysis tools for Linux kernel
Group:          System/Tools
Requires:       %{name} = %{version}-%{release}
Requires:       audit

%description tools
This package contains the 'perf' performance analysis tools for Linux kernel.

%package -n     python3-perf
Summary:        Python 3 extension for perf tools
Requires:       python3

%description -n python3-perf
This package contains the Python 3 extension for the 'perf' performance analysis tools for Linux kernel.

%package -n     bpftool
Summary:        Inspection and simple manipulation of eBPF programs and maps

%description -n bpftool
This package contains the bpftool, which allows inspection and simple
manipulation of eBPF programs and maps.

%prep
%define _default_patch_flags -p1 --fuzz=3 --force
%setup -q -n linux-7.0
%autosetup -p1 -n linux-7.0
# %patch 0 -p1
make mrproper

cp %{config_source} .config

# Add cert into kernel's trusted keyring
cp %{SOURCE4} certs/emt.pem
sed -i 's#CONFIG_SYSTEM_TRUSTED_KEYS=""#CONFIG_SYSTEM_TRUSTED_KEYS="certs/emt.pem"#' .config

cp .config current_config
sed -i 's/CONFIG_LOCALVERSION=""/CONFIG_LOCALVERSION="-%{release}"/' .config
make LC_ALL=  ARCH=%{arch} olddefconfig

# Verify the config files match
cp .config new_config
sed -i 's/CONFIG_LOCALVERSION=".*"/CONFIG_LOCALVERSION=""/' new_config
diff --unified new_config current_config > config_diff || true
if [ -s config_diff ]; then
    printf "\n\n\n\n\n\n\n\n"
    cat config_diff
    printf "\n\n\n\n\n\n\n\n"
    echo "Config file has unexpected changes"
    echo "Update config file to set changed values explicitly"

#  (DISABLE THIS IF INTENTIONALLY UPDATING THE CONFIG FILE)
#    exit 1
fi

%build
make VERBOSE=1 KBUILD_BUILD_VERSION="1" KBUILD_BUILD_HOST="EdgeMicrovisorToolkit" ARCH=%{arch} %{?_smp_mflags}

# Compile perf, python3-perf
make -C tools/perf PYTHON=%{python3} all

%ifarch x86_64
make -C tools turbostat cpupower
%endif

#Compile bpftool
make -C tools/bpf/bpftool

%define __modules_install_post \
for MODULE in `find %{buildroot}/lib/modules/%{uname_r} -name *.ko` ; do \
    ./scripts/sign-file sha512 certs/signing_key.pem certs/signing_key.x509 $MODULE \
    rm -f $MODULE.{sig,dig} \
    xz $MODULE \
    done \
%{nil}

# We want to compress modules after stripping. Extra step is added to
# the default __spec_install_post.
%define __spec_install_post\
    %{?__debug_package:%{__debug_install_post}}\
    %{__arch_install_post}\
    %{__os_install_post}\
    %{__modules_install_post}\
%{nil}

%install
install -vdm 755 %{buildroot}%{_sysconfdir}
install -vdm 700 %{buildroot}/boot
install -vdm 755 %{buildroot}%{_defaultdocdir}/linux-%{uname_r}
install -vdm 755 %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}
install -vdm 755 %{buildroot}%{_libdir}/debug/lib/modules/%{uname_r}

install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -c -m 644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/sysconfig/cpupower
install -d -m 755 %{buildroot}%{_unitdir}
install -c -m 644 %{SOURCE6} %{buildroot}%{_unitdir}/cpupower.service

make INSTALL_MOD_PATH=%{buildroot} modules_install

%ifarch x86_64
install -vm 600 arch/x86/boot/bzImage %{buildroot}/boot/vmlinuz-%{uname_r}
%endif

%ifarch aarch64
install -vm 600 arch/arm64/boot/Image %{buildroot}/boot/vmlinuz-%{uname_r}
%endif

# Restrict the permission on System.map-X file
install -vm 400 System.map %{buildroot}/boot/System.map-%{uname_r}
install -vm 600 .config %{buildroot}/boot/config-%{uname_r}
cp -r Documentation/*        %{buildroot}%{_defaultdocdir}/linux-%{uname_r}
install -vm 744 vmlinux %{buildroot}%{_libdir}/debug/lib/modules/%{uname_r}/vmlinux-%{uname_r}
# `perf test vmlinux` needs it
ln -s vmlinux-%{uname_r} %{buildroot}%{_libdir}/debug/lib/modules/%{uname_r}/vmlinux

cat > %{buildroot}/boot/linux-%{uname_r}.cfg << "EOF"
# GRUB Environment Block
mariner_cmdline=init=/lib/systemd/systemd ro loglevel=3 no-vmw-sta crashkernel=256M lockdown=integrity
mariner_linux=vmlinuz-%{uname_r}
mariner_initrd=initrd.img-%{uname_r}
EOF
chmod 600 %{buildroot}/boot/linux-%{uname_r}.cfg

# hmac sign the kernel for FIPS
%{sha512hmac} %{buildroot}/boot/vmlinuz-%{uname_r} | sed -e "s,$RPM_BUILD_ROOT,," > %{buildroot}/boot/.vmlinuz-%{uname_r}.hmac
cp %{buildroot}/boot/.vmlinuz-%{uname_r}.hmac %{buildroot}/lib/modules/%{uname_r}/.vmlinuz.hmac

# Register myself to initramfs
mkdir -p %{buildroot}/%{_localstatedir}/lib/initramfs/kernel
cat > %{buildroot}/%{_localstatedir}/lib/initramfs/kernel/%{uname_r} << "EOF"
--add-drivers "virtio_blk virtio-rng virtio_console virtio_crypto virtio_mem vmw_vsock_virtio_transport vmw_vsock_virtio_transport_common 9pnet_virtio vrf"
EOF

# Symlink /lib/modules/uname/vmlinuz to boot partition
ln -s /boot/vmlinuz-%{uname_r} %{buildroot}/lib/modules/%{uname_r}/vmlinuz

#    Cleanup dangling symlinks
rm -rf %{buildroot}/lib/modules/%{uname_r}/source
rm -rf %{buildroot}/lib/modules/%{uname_r}/build

find . -name Makefile* -o -name Kconfig* -o -name *.pl | xargs  sh -c 'cp --parents "$@" %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}' copy
find arch/%{archdir}/include include scripts -type f | xargs  sh -c 'cp --parents "$@" %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}' copy
find $(find arch/%{archdir} -name include -o -name scripts -type d) -type f | xargs  sh -c 'cp --parents "$@" %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}' copy
find arch/%{archdir}/include Module.symvers include scripts -type f | xargs  sh -c 'cp --parents "$@" %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}' copy
%ifarch x86_64
# CONFIG_STACK_VALIDATION=y requires objtool to build external modules
install -vsm 755 tools/objtool/objtool %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}/tools/objtool/
install -vsm 755 tools/objtool/fixdep %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}/tools/objtool/
%endif

cp .config %{buildroot}%{_prefix}/src/linux-headers-%{uname_r} # copy .config manually to be where it's expected to be
ln -sf "%{_prefix}/src/linux-headers-%{uname_r}" "%{buildroot}/lib/modules/%{uname_r}/build"
find %{buildroot}/lib/modules -name '*.ko' -print0 | xargs -0 chmod u+x

%ifarch aarch64
cp scripts/module.lds %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}/scripts/module.lds
%endif

# disable (JOBS=1) parallel build to fix this issue:
# fixdep: error opening depfile: ./.plugin_cfg80211.o.d: No such file or directory
# Linux version that was affected is 4.4.26
make -C tools JOBS=1 DESTDIR=%{buildroot} prefix=%{_prefix} perf_install

# Install python3-perf
make -C tools/perf DESTDIR=%{buildroot} prefix=%{_prefix} install-python_ext

# Install bpftool
make -C tools/bpf/bpftool DESTDIR=%{buildroot} prefix=%{_prefix} bash_compdir=%{_sysconfdir}/bash_completion.d/ mandir=%{_mandir} install

%ifarch x86_64
# Install turbostat cpupower
make -C tools DESTDIR=%{buildroot} prefix=%{_prefix} bash_compdir=%{_sysconfdir}/bash_completion.d/ mandir=%{_mandir} turbostat_install cpupower_install
%endif

# Remove trace (symlink to perf). This file causes duplicate identical debug symbols
rm -vf %{buildroot}%{_bindir}/trace

%triggerin -- initramfs
mkdir -p %{_localstatedir}/lib/rpm-state/initramfs/pending
touch %{_localstatedir}/lib/rpm-state/initramfs/pending/%{uname_r}
echo "initrd generation of kernel %{uname_r} will be triggered later" >&2

%triggerun -- initramfs
rm -rf %{_localstatedir}/lib/rpm-state/initramfs/pending/%{uname_r}
rm -rf /boot/initrd.img-%{uname_r}
echo "initrd of kernel %{uname_r} removed" >&2

%preun tools
%systemd_preun cpupower.service

%postun
if [ ! -e /boot/mariner.cfg ]
then
     ls /boot/linux-*.cfg 1> /dev/null 2>&1
     if [ $? -eq 0 ]
     then
          list=`ls -tu /boot/linux-*.cfg | head -n1`
          test -n "$list" && ln -sf "$list" /boot/mariner.cfg
     fi
fi
%grub2_postun

%postun tools
%systemd_postun cpupower.service

%post
/sbin/depmod -a %{uname_r}
ln -sf linux-%{uname_r}.cfg /boot/mariner.cfg
%grub2_post

%post drivers-accessibility
/sbin/depmod -a %{uname_r}

%post drivers-gpu
/sbin/depmod -a %{uname_r}

%post drivers-sound
/sbin/depmod -a %{uname_r}

%post tools
%systemd_post cpupower.service

%files
%defattr(-,root,root)
%license COPYING
%exclude %dir /usr/lib/debug
/boot/System.map-%{uname_r}
/boot/config-%{uname_r}
/boot/vmlinuz-%{uname_r}
/boot/.vmlinuz-%{uname_r}.hmac
%config(noreplace) /boot/linux-%{uname_r}.cfg
%config %{_localstatedir}/lib/initramfs/kernel/%{uname_r}
%defattr(0644,root,root)
/lib/modules/%{uname_r}/*
/lib/modules/%{uname_r}/.vmlinuz.hmac
%exclude /lib/modules/%{uname_r}/build
%exclude /lib/modules/%{uname_r}/kernel/drivers/accessibility
%exclude /lib/modules/%{uname_r}/kernel/drivers/gpu
%exclude /lib/modules/%{uname_r}/kernel/sound

%files docs
%defattr(-,root,root)
%{_defaultdocdir}/linux-%{uname_r}/*

%files devel
%defattr(-,root,root)
/lib/modules/%{uname_r}/build
%{_prefix}/src/linux-headers-%{uname_r}

%files drivers-accessibility
%defattr(-,root,root)
/lib/modules/%{uname_r}/kernel/drivers/accessibility

%files drivers-gpu
%defattr(-,root,root)
/lib/modules/%{uname_r}/kernel/drivers/gpu

%files drivers-sound
%defattr(-,root,root)
/lib/modules/%{uname_r}/kernel/sound

%files tools
%defattr(-,root,root)
%{_libexecdir}
%exclude %dir %{_libdir}/debug
%ifarch x86_64
%{_sbindir}/cpufreq-bench
%{_lib64dir}/libperf-jvmti.so
%{_libdir}/libcpupower.so*
%{_sysconfdir}/cpufreq-bench.conf
%{_sysconfdir}/cpupower-service.conf
%{_includedir}/cpuidle.h
%{_includedir}/cpufreq.h
%{_includedir}/powercap.h
%{_mandir}/man1/cpupower*.gz
%{_mandir}/man8/turbostat*.gz
%{_datadir}/locale/*/LC_MESSAGES/cpupower.mo
%{_datadir}/bash-completion/completions/cpupower
%endif
%ifarch aarch64
%{_libdir}/libperf-jvmti.so
%endif
%{_bindir}
%{_sysconfdir}/bash_completion.d/*
%{_docdir}/*
%{_includedir}/perf/perf_dlfilter.h
%{_unitdir}/cpupower.service
%config(noreplace) %{_sysconfdir}/sysconfig/cpupower

%files -n python3-perf
%{python3_sitearch}/*

%files -n bpftool
%{_sbindir}/bpftool
%{_sysconfdir}/bash_completion.d/bpftool

%changelog
* Mon Jul 6 2026 Lishan Liu <lishan.liu@intel.com> - 7.0.0-1
- Update kernel to mainline-preprod-v7.0-x86common-dev-emt-260713T072449Z

* Fri May 22 2026 Lishan Liu <lishan.liu@intel.com> - 6.18.23-1
- Update kernel to 6.18.23-1

* Wed May 13 2026 Lishan Liu <lishan.liu@intel.com> - 6.18.20-2
- Remove patch 0068-drm-i915-no-waiting-for-page-flip-in-vpp-case.drm

* Wed Apr 29 2026 Lishan Liu <lishan.liu@intel.com> - 6.18.20-1
- Update kernel to 6.18.20-1
- lts-v6.18.20-emt-cve-260417T093242Z
- enable TGPIO kernel config

* Mon Mar 16 2026 Lishan Liu <lishan.liu@intel.com> - 6.18.15-1
- Update kernel to 6.18.15-1
- lts-v6.18.15-emt-260310T050801Z

* Sun Feb 01 2026 Lishan Liu <lishan.liu@intel.com> - 6.17.11-2
- Update kernel to 6.17.11-2
- mainline-v6.17.11-emt-overlay-cve-260128T080735Z

* Thu Jan 15 2026 Lishan Liu <lishan.liu@intel.com> - 6.17.11-1
- Update kernel to mainline-v6.17.11-emt-260108T031458Z

* Mon Dec 1 2025 Lishan Liu <lishan.liu@intel.com> - 6.17.0-3
- Update kernel to mainline-tracking-pre-prod-v6.17-linux-251118T134731Z

* Tue Nov 25 2025 Lishan Liu <lishan.liu@intel.com> - 6.17.0-2
- Bump release version for rebase

* Thu Oct 30 2025 Lishan Liu <lishan.liu@intel.com> - 6.17.0-1
- Upgate kernel to 6.17.0

* Tue Nov 18 2025 Lishan Liu <lishan.liu@intel.com> - 6.12.55-1
- Update kernel to 6.12.55

* Fri Nov 14 2025 Lishan Liu <lishan.liu@intel.com> - 6.12.44-6
- Update audio support in kernel config

* Tue Nov 4 2025 Lishan Liu <lishan.liu@intel.com> - 6.12.44-5
- Update kernel config

* Thu Oct 30 2025 Lishan Liu <lishan.liu@intel.com> - 6.17.0-1
- Upgate kernel to 6.17.0

* Thu Oct 23 2025 Lishan Liu <lishan.liu@intel.com> - 6.12.44-4
- Revert to working kernel config

* Fri Oct 10 2025 Zhang Baoli <baoli.zhang@intel.com> - 6.12.44-3
- Fix ISO mouse detection and cmdline params in non-rt kernel

* Tue Sep 30 2025 Zhang Baoli <baoli.zhang@intel.com> - 6.12.44-2
- Fix the boot failure of ISO and raw image

* Tue Sep 09 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.44-1
- Update kernel to 6.12.44

* Thu Jul 24 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.39-1
- Update kernel to 6.12.39

* Thu Jul 10 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.35-2
- Update kernel to 6.12.35

* Fri Jul 04 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.35-1
- Update kernel to 6.12.35

* Thu Jun 19 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.33-1
- Update kernel to 6.12.33

* Wed Mar 28 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.30-1
- Update kernel to 6.12.30

* Thu Mar 22 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.28-1
- Update kernel to 6.12.28

* Mon Apr 21 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.23-1
- Update kernel to 6.12.23

* Thu Mar 27 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.20-1
- Update kernel to 6.12.20

* Thu Mar 20 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.19-1
- Update kernel to 6.12.19

* Mon Mar 03 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.15-1
- Update kernel to 6.12.15

* Wed Feb 19 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.12-1
- Update kernel to 6.12.12

* Mon Dec 30 2024 Junxiao Chang <junxiao.chang@intel.com> - 6.6.63-6
- Revert back to original packaging for GPU drivers

* Tue Dec 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 6.6.63-5
- Updated initial changelog entry.

* Tue Dec 24 2024 Junxiao Chang <junxiao.chang@intel.com> - 6.6.63-4
- Adding i915 kernel module package.

* Tue Dec 17 2024 Lishan Liu <lishan.liu@intel.com> - 6.6.63-3
- Change RT kernel CONFIG_HZ to 1000.

* Tue Dec 12 2024 Swee Yee Fonn <swee.yee.fonn@intel.com> - 6.6.63-2
- Enable kernel to use ZSTD compression instead of GZIP.

* Tue Dec 10 2024 Man jiahua <jiahuax.man@intel.com> - 6.6.63-1
- Update RT kernel version to 6.6.63-rt46.

* Mon Nov 04 2024 Man jiahua <jiahuax.man@intel.com> - 6.6.58-1
- Update RT kernel version to 6.6.58-rt45.

* Wed Oct 16 2024 Man jiahua <jiahuax.man@intel.com> - 6.6.53-1
- Update RT kernel version to 6.6.53-rt44.

* Thu Sep 26 2024 Shi Qingdong <qingdong.shi@intel.com> - 6.6.52-1
- Update RT kernel version to 6.6.52-rt43.

* Mon Sep 23 2024 Man jiahua <jiahuax.man@intel.com> - 6.6.49-1
- Update RT kernel version to 6.6.49-rt41.

* Fri Sep 6 2024 Shi Qingdong <qingdong.shi@intel.com> - 6.6.48-1
- Update RT kernel version to 6.6.48-rt40.

* Fri Aug 9 2024 Zhou Furong <furong.zhon@intel.com> - 6.6.43.2
- Update RT kernel config.

* Mon Aug 5 2024 Zhou Furong <furong.zhon@intel.com> - 6.6.43.1
- Initial RT version based on 6.6.43-rt38.

* Tue Jul 23 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 6.6.35.3
- Fix initrd generation issue

* Tue Jul 9 2024 Zhou Furong <furong.zhon@intel.com> - 6.6.35.2
- Update kernel source link and enable kernel option VPU/QAT/ICE

* Tue Jul 2 2024 Zhou Furong <furong.zhou@intel.com> - 6.6.35-1
- Initial Edge Microvisor Toolkit import from Azure Linux (license: MIT). License verified.
- Updated for Edge Microvisor Toolkit
