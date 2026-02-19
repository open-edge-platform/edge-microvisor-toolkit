Summary:        Preempt RT Linux Kernel
Name:           kernel-rt
Version:        6.17.11
Release:        3%{?dist}
License:        GPLv2
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://www.kernel.org/pub/linux/kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.17.11.tar.gz
Source1:        config
Source3:        sha512hmac-openssl.sh
Source4:        emt-ca-20211013.pem
Source5:        cpupower
Source6:        cpupower.service

# Intel not-upstreamed kernel features
# v6.17.11
#5439375ca698 Linux 6.17.11
# security
Patch01001: 0001-Add-security.md-file.security
Patch01002: 0001-issei-initial-driver-skeleton.security
Patch01003: 0002-issei-add-firmware-and-host-clients-implementatio.security
Patch01004: 0003-issei-implement-main-thread-and-ham-messages.security
Patch01005: 0004-issei-add-heci-hardware-module.security
Patch01006: 0005-issei-update-MAINTAINERS-file.security
Patch01007: 0001-Add-updated-TPR-TXT-Protected-Regions-support-to-.security
# lpss
Patch02001: 0001-PCI-Apply-ASPM-L1-latency-quirk-to-Intel-DG2-Audio-en.lpss
Patch02002: 0002-PCI-portdrv-Do-not-require-an-interrupt-for-all-AER-c.lpss
Patch02003: 0003-PCI-Add-sysfs-attribute-for-disabling-PCIe-link-to-do.lpss
Patch02004: 0004-ACPI-hotplug-PCI-Take-runtime-PM-autosuspend-into-acc.lpss
Patch02005: 0005-spi-intel-pci-Add-support-for-Arrow-Lake-H-SPI-serial.lpss
Patch02006: 0006-mtd-core-Don-t-fail-mtd_device_parse_register-if-OTP-.lpss
Patch02007: 0007-spi-intel-Add-support-for-Intel-Wildcat-Lake-SPI-seri.lpss
Patch02008: 0008-spi-intel-Add-support-for-128M-component-density.lpss
Patch02009: 0010-i2c-i801-Add-support-for-Intel-Wildcat-Lake-U.lpss
Patch02010: 0011-i2c-designware-Preliminary-SMBus-support.lpss
Patch02011: 0001-Added-spi_set_cs-for-more-stable-r-w-operations-in-SP.lpss
# drm
Patch03001: 0001-drm-virtio-freeze-and-restore-hooks-to-support-suspend.drm
Patch03002: 0002-drm-virtio-save-and-restore-virtio_gpu_objects.drm
Patch03003: 0001-drm-xe-Upgrade-XE-GuC-to-the-latest-upstream.drm
Patch03004: 0001-drm-xe-Upgrade-PTL-and-BMG-GuC-to-70.55.3-MTL-LNL-DG2-.drm
# sriov
Patch04001: 0001-drm-xe-xe_vm-bypass-vm_bind-failure-as-wa-to-enable-.sriov
Patch04002: 0001-drm-virtio-Wait-until-the-control-and-cursor-queues-.sriov
# edac
Patch05001: 0002-EDAC-skx_common-skx-Use-configuration-data-not-global.edac
Patch05002: 0003-EDAC-skx_common-Move-mc_mapping-to-be-a-field-inside-.edac
Patch05003: 0004-EDAC-skx_common-Swap-memory-controller-index-mapping.edac
Patch05004: 0005-EDAC-skx_common-Make-skx_dev-imc-a-flexible-array.edac
Patch05005: 0006-EDAC-skx_common-Remove-redundant-upper-bound-check-fo.edac
Patch05006: 0007-EDAC-i10nm-Reallocate-skx_dev-list-if-preconfigured-c.edac
Patch05007: 0008-EDAC-skx_common-Remove-unused-NUM-_IMC-macros.edac
Patch05008: 0009-x86-mce-Add-MCACOD-code-for-generic-I-O-error.edac
Patch05009: 0010-EDAC-ieh-Add-I-O-device-EDAC-driver-for-Intel-CPUs-wi.edac
Patch05010: 0011-EDAC-ieh-Add-I-O-device-EDAC-support-for-Intel-Tiger-.edac
Patch05011: 0012-EDAC-igen6-Add-registration-APIs-for-In-Band-ECC-erro.edac
Patch05012: 0001-EDAC-igen6-Add-more-Intel-Panther-Lake-H-SoCs-support.edac
# perf
Patch06001: 0001-perf-x86-msr-Make-SMI-and-PPERF-on-by-default.perf
Patch06002: 0002-perf-x86-intel-Add-a-check-for-dynamic-constraints.perf
Patch06003: 0005-perf-x86-Check-if-cpuc-events-pointer-exists-before-a.perf
Patch06004: 0006-perf-x86-Add-PERF_CAP_PEBS_TIMING_INFO-flag.perf
Patch06005: 0007-perf-x86-intel-Change-macro-GLOBAL_CTRL_EN_PERF_METRI.perf
Patch06006: 0009-perf-x86-Remove-helper-perf_events_lapic_init-from-x8.perf
Patch06007: 0010-perf-x86-intel-Fix-typo-in-comments-of-intel_put_even.perf
Patch06008: 0011-perf-x86-Fix-typos-and-inconsistent-indents-in-perf_e.perf
Patch06009: 0012-perf-x86-intel-Print-more-information-in-x86_pmu_show.perf
Patch06010: 0013-perf-x86-intel-Initialize-architectural-PEBS.perf
Patch06011: 0014-perf-x86-intel-ds-Factor-out-PEBS-record-processing-c.perf
Patch06012: 0015-perf-x86-intel-ds-Factor-out-PEBS-group-processing-co.perf
Patch06013: 0016-perf-x86-intel-Process-arch-PEBS-records-or-record-fr.perf
Patch06014: 0017-perf-x86-intel-Allocate-arch-PEBS-buffer-and-initiali.perf
Patch06015: 0018-perf-x86-intel-Update-dyn_constranit-base-on-PEBS-eve.perf
Patch06016: 0019-perf-x86-intel-Setup-PEBS-data-configuration-and-enab.perf
Patch06017: 0020-perf-x86-intel-Add-counter-group-support-for-arch-PEB.perf
Patch06018: 0021-perf-x86-intel-Support-SSP-register-capturing-for-arc.perf
Patch06019: 0022-perf-core-Support-to-capture-higher-width-vector-regi.perf
Patch06020: 0023-perf-x86-intel-Support-arch-PEBS-vector-registers-gro.perf
Patch06021: 0024-perf-tools-Support-to-show-SSP-register.perf
Patch06022: 0025-perf-tools-Enhance-arch__intr-user_reg_mask-helpers.perf
Patch06023: 0026-perf-tools-Enhance-sample_regs_user-intr-to-capture-m.perf
Patch06024: 0027-perf-tools-Support-to-capture-more-vector-registers-x.perf
Patch06025: 0028-perf-tools-tests-Add-vector-registers-PEBS-sampling-t.perf
Patch06026: 0029-perf-x86-intel-Add-PMU-support-for-WildcatLake.perf
Patch06027: 0031-perf-evsel-Update-the-hint-for-the-usage-of-the-load-.perf
Patch06028: 0032-perf-x86-intel-cstate-Add-Clearwater-Forrest-support.perf
Patch06029: 0033-KVM-x86-pmu-Correct-typo-_COUTNERS-to-_COUNTERS.perf
Patch06030: 0034-KVM-selftests-Add-timing_info-bit-support-in-vmx_pmu_.perf
Patch06031: 0035-KVM-Selftests-Validate-more-arch-events-in-pmu_counte.perf
Patch06032: 0036-KVM-selftests-Relax-precise-event-count-validation-as.perf
Patch06033: 0037-KVM-selftests-Relax-branches-event-count-check-for-ev.perf
Patch06034: 0039-KVM-x86-Add-kvm_icr_to_lapic_irq-helper-to-allow-for-.perf
Patch06035: 0040-KVM-x86-Only-allow-fast-IPIs-in-fastpath-WRMSR-X2APIC.perf
Patch06036: 0041-KVM-x86-Drop-semi-arbitrary-restrictions-on-IPI-type-.perf
Patch06037: 0042-KVM-x86-Unconditionally-handle-MSR_IA32_TSC_DEADLINE-.perf
Patch06038: 0043-KVM-x86-Acquire-SRCU-in-WRMSR-fastpath-iff-instructio.perf
Patch06039: 0044-KVM-x86-Unconditionally-grab-data-from-EDX-EAX-in-WRM.perf
Patch06040: 0045-KVM-x86-Fold-WRMSR-fastpath-helpers-into-the-main-han.perf
Patch06041: 0046-KVM-x86-pmu-Move-kvm_init_pmu_capability-to-pmu.c.perf
Patch06042: 0047-KVM-x86-pmu-Add-wrappers-for-counting-emulated-instru.perf
Patch06043: 0048-KVM-x86-pmu-Calculate-set-of-to-be-emulated-PMCs-at-t.perf
Patch06044: 0049-KVM-x86-pmu-Rename-pmc_speculative_in_use-to-pmc_is_l.perf
Patch06045: 0050-KVM-x86-pmu-Open-code-pmc_event_is_allowed-in-its-cal.perf
Patch06046: 0051-KVM-x86-pmu-Drop-redundant-check-on-PMC-being-globall.perf
Patch06047: 0052-KVM-x86-pmu-Drop-redundant-check-on-PMC-being-locally.perf
Patch06048: 0053-KVM-x86-pmu-Rename-check_pmu_event_filter-to-pmc_is_e.perf
Patch06049: 0054-KVM-x86-Push-acquisition-of-SRCU-in-fastpath-into-kvm.perf
Patch06050: 0055-KVM-x86-Add-a-fastpath-handler-for-INVD.perf
Patch06051: 0056-perf-Skip-pmu_ctx-based-on-event_type.perf
Patch06052: 0057-perf-Add-generic-exclude_guest-support.perf
Patch06053: 0058-perf-Move-security_perf_event_free-call-to-__free_eve.perf
Patch06054: 0059-perf-Add-APIs-to-create-release-mediated-guest-vPMUs.perf
Patch06055: 0060-perf-Clean-up-perf-ctx-time.perf
Patch06056: 0061-perf-Add-a-EVENT_GUEST-flag.perf
Patch06057: 0062-perf-Add-APIs-to-load-put-guest-mediated-PMU-context.perf
Patch06058: 0063-perf-core-x86-Register-a-new-vector-for-handling-medi.perf
Patch06059: 0064-perf-x86-Switch-LVTPC-to-from-mediated-PMI-vector-on-.perf
Patch06060: 0065-perf-x86-core-Do-not-set-bit-width-for-unavailable-co.perf
Patch06061: 0066-perf-x86-core-Plumb-mediated-PMU-capability-from-x86_.perf
Patch06062: 0067-perf-x86-intel-Support-PERF_PMU_CAP_MEDIATED_VPMU.perf
Patch06063: 0068-perf-x86-amd-Support-PERF_PMU_CAP_MEDIATED_VPMU-for-A.perf
Patch06064: 0069-KVM-VMX-Setup-canonical-VMCS-config-prior-to-kvm_x86_.perf
Patch06065: 0070-KVM-SVM-Check-pmu-version-not-enable_pmu-when-getting.perf
Patch06066: 0071-KVM-Add-a-simplified-wrapper-for-registering-perf-cal.perf
Patch06067: 0072-KVM-x86-pmu-Snapshot-host-i.e.-perf-s-reported-PMU-ca.perf
Patch06068: 0073-KVM-x86-pmu-Start-stubbing-in-mediated-PMU-support.perf
Patch06069: 0074-KVM-x86-pmu-Implement-Intel-mediated-PMU-requirements.perf
Patch06070: 0075-KVM-x86-pmu-Implement-AMD-mediated-PMU-requirements.perf
Patch06071: 0076-KVM-x86-pmu-Register-PMI-handler-for-mediated-vPMU.perf
Patch06072: 0077-KVM-x86-Rename-vmx_vmentry-vmexit_ctrl-helpers.perf
Patch06073: 0078-KVM-x86-pmu-Move-PMU_CAP_-FW_WRITES-LBR_FMT-into-msr-.perf
Patch06074: 0079-KVM-x86-Rework-KVM_REQ_MSR_FILTER_CHANGED-into-a-gene.perf
Patch06075: 0080-KVM-x86-Use-KVM_REQ_RECALC_INTERCEPTS-to-react-to-CPU.perf
Patch06076: 0081-KVM-VMX-Add-helpers-to-toggle-change-a-bit-in-VMCS-ex.perf
Patch06077: 0082-KVM-x86-pmu-Disable-RDPMC-interception-for-compatible.perf
Patch06078: 0083-KVM-x86-pmu-Load-save-GLOBAL_CTRL-via-entry-exit-fiel.perf
Patch06079: 0084-KVM-x86-pmu-Use-BIT_ULL-instead-of-open-coded-equival.perf
Patch06080: 0085-KVM-x86-pmu-Move-initialization-of-valid-PMCs-bitmask.perf
Patch06081: 0086-KVM-x86-pmu-Restrict-GLOBAL_-CTRL-STATUS-fixed-PMCs-a.perf
Patch06082: 0087-KVM-x86-pmu-Disable-interception-of-select-PMU-MSRs-f.perf
Patch06083: 0088-KVM-x86-pmu-Bypass-perf-checks-when-emulating-mediate.perf
Patch06084: 0089-KVM-x86-pmu-Introduce-eventsel_hw-to-prepare-for-pmu-.perf
Patch06085: 0090-KVM-x86-pmu-Reprogram-mediated-PMU-event-selectors-on.perf
Patch06086: 0091-KVM-x86-pmu-Always-stuff-GuestOnly-1-HostOnly-0-for-m.perf
Patch06087: 0092-KVM-x86-pmu-Load-put-mediated-PMU-context-when-enteri.perf
Patch06088: 0093-KVM-x86-pmu-Disallow-emulation-in-the-fastpath-if-med.perf
Patch06089: 0094-KVM-x86-pmu-Handle-emulated-instruction-for-mediated-.perf
Patch06090: 0095-KVM-nVMX-Add-macros-to-simplify-nested-MSR-intercepti.perf
Patch06091: 0096-KVM-nVMX-Disable-PMU-MSR-interception-as-appropriate-.perf
Patch06092: 0097-KVM-nSVM-Disable-PMU-MSR-interception-as-appropriate-.perf
Patch06093: 0098-KVM-x86-pmu-Expose-enable_mediated_pmu-parameter-to-u.perf
Patch06094: 0099-KVM-x86-pmu-Elide-WRMSRs-when-loading-guest-PMCs-if-v.perf
Patch06095: 0001-KVM-x86-pmu-Fix-the-warning-in-perf_get_x86_pmu_capab.perf
# cet
Patch07001: 0001-KVM-x86-Rename-kvm_-g-s-et_msr-to-show-that-they-emula.cet
Patch07002: 0002-KVM-x86-Use-double-underscore-read-write-MSR-helpers-a.cet
Patch07003: 0003-KVM-x86-Add-kvm_msr_-read-write-helpers.cet
Patch07004: 0004-KVM-x86-Manually-clear-MPX-state-only-on-INIT.cet
Patch07005: 0005-KVM-x86-Zero-XSTATE-components-on-INIT-by-iterating-ov.cet
Patch07006: 0006-KVM-x86-Introduce-KVM_-G-S-ET_ONE_REG-uAPIs-support.cet
Patch07007: 0007-KVM-x86-Report-XSS-as-to-be-saved-if-there-are-support.cet
Patch07008: 0008-KVM-x86-Refresh-CPUID-on-write-to-guest-MSR_IA32_XSS.cet
Patch07009: 0009-KVM-x86-Initialize-kvm_caps.supported_xss.cet
Patch07010: 0010-KVM-x86-Load-guest-FPU-state-when-access-XSAVE-managed.cet
Patch07011: 0011-KVM-x86-Add-fault-checks-for-guest-CR4.CET-setting.cet
Patch07012: 0012-KVM-x86-Report-KVM-supported-CET-MSRs-as-to-be-saved.cet
Patch07013: 0013-KVM-VMX-Introduce-CET-VMCS-fields-and-control-bits.cet
Patch07014: 0014-KVM-x86-Enable-guest-SSP-read-write-interface-with-new.cet
Patch07015: 0015-KVM-VMX-Emulate-read-and-write-to-CET-MSRs.cet
Patch07016: 0016-KVM-x86-Save-and-reload-SSP-to-from-SMRAM.cet
Patch07017: 0017-KVM-VMX-Set-up-interception-for-CET-MSRs.cet
Patch07018: 0018-KVM-VMX-Set-host-constant-supervisor-states-to-VMCS-fi.cet
Patch07019: 0019-KVM-x86-Don-t-emulate-instructions-guarded-by-CET.cet
Patch07020: 0020-KVM-x86-Enable-CET-virtualization-for-VMX-and-advertis.cet
Patch07021: 0021-KVM-nVMX-Virtualize-NO_HW_ERROR_CODE_CC-for-L1-event-i.cet
Patch07022: 0022-KVM-nVMX-Enable-CET-support-for-nested-guest.cet
Patch07023: 0023-KVM-nVMX-Add-consistency-checks-for-CR0.WP-and-CR4.CET.cet
Patch07024: 0024-KVM-nVMX-Add-consistency-checks-for-CET-states.cet
# nmi
Patch08001: 0001-KVM-VMX-Add-host-MSR-read-write-helpers-to-consolidate.nmi
Patch08002: 0002-KVM-VMX-Add-support-for-the-secondary-VM-exit-controls.nmi
Patch08003: 0003-KVM-VMX-Initialize-VM-entry-exit-FRED-controls-in-vmcs.nmi
Patch08004: 0004-KVM-VMX-Disable-FRED-if-FRED-consistency-checks-fail.nmi
Patch08005: 0005-x86-cea-Export-an-API-to-get-per-CPU-exception-stacks-.nmi
Patch08006: 0006-KVM-VMX-Initialize-VMCS-FRED-fields.nmi
Patch08007: 0007-KVM-VMX-Set-FRED-MSR-intercepts.nmi
Patch08008: 0008-KVM-VMX-Save-restore-guest-FRED-RSP0.nmi
Patch08009: 0009-KVM-VMX-Add-support-for-FRED-context-save-restore.nmi
Patch08010: 0010-KVM-x86-Add-a-helper-to-detect-if-FRED-is-enabled-for-.nmi
Patch08011: 0011-KVM-VMX-Virtualize-FRED-event_data.nmi
Patch08012: 0012-KVM-VMX-Virtualize-FRED-nested-exception-tracking.nmi
Patch08013: 0013-KVM-x86-Save-restore-the-nested-flag-of-an-exception.nmi
Patch08014: 0014-KVM-x86-Mark-CR4.FRED-as-not-reserved.nmi
Patch08015: 0015-KVM-VMX-Dump-FRED-context-in-dump_vmcs.nmi
Patch08016: 0016-KVM-x86-Advertise-support-for-FRED.nmi
Patch08017: 0017-KVM-nVMX-Add-support-for-the-secondary-VM-exit-control.nmi
Patch08018: 0018-KVM-nVMX-Add-FRED-VMCS-fields-to-nested-VMX-context-ha.nmi
Patch08019: 0019-KVM-nVMX-Add-FRED-related-VMCS-field-checks.nmi
Patch08020: 0020-KVM-nVMX-Add-prerequisites-to-SHADOW_FIELD_R-OW-macros.nmi
Patch08021: 0021-KVM-nVMX-Allow-VMX-FRED-controls.nmi
Patch08022: 0022-x86-fred-Enable-FRED-by-default.nmi
Patch08023: 0023-x86-entry-fred-Simply-push-__KERNEL_CS.nmi
Patch08024: 0024-KVM-selftests-Run-debug_regs-test-with-FRED-enabled.nmi
Patch08025: 0025-KVM-selftests-Add-a-new-VM-guest-mode-to-run-user-leve.nmi
Patch08026: 0026-KVM-selftests-Add-fred-exception-tests.nmi
Patch08027: 0027-KVM-selftests-Add-the-2nd-VM-exit-controls-MSR-to-the-.nmi
Patch08028: 0028-task_stack.h-Add-a-new-helper-task_empty_stack_pointer.nmi
Patch08029: 0029-x86-fred-Allow-variable-sized-event-frame.nmi
Patch08030: 0030-x86-Remove-the-padding-space-at-top-of-the-init-stack.nmi
Patch08031: 0031-x86-fred-Provide-separate-IRQ-vs.-NMI-wrappers-for-ent.nmi
Patch08032: 0032-x86-fred-Pass-event-data-to-the-NMI-entry-point-from-K.nmi
Patch08033: 0033-x86-cpufeatures-Add-the-CPUID-feature-bit-for-NMI-sour.nmi
Patch08034: 0034-x86-nmi-Extend-the-registration-interface-to-include-t.nmi
Patch08035: 0035-x86-nmi-Assign-and-register-NMI-source-vectors.nmi
Patch08036: 0036-x86-nmi-Add-support-to-handle-NMIs-with-source-informa.nmi
Patch08037: 0037-x86-nmi-Prepare-for-the-new-NMI-source-vector-encoding.nmi
Patch08038: 0038-x86-nmi-Enable-NMI-source-for-IPIs-delivered-as-NMIs.nmi
Patch08039: 0039-perf-x86-Enable-NMI-source-reporting-for-perfmon.nmi
Patch08040: 0040-x86-nmi-Print-source-information-with-the-unknown-NMI-.nmi
Patch08041: 0041-x86-nmi-Include-source-information-in-NMI-handler-trac.nmi
Patch08042: 0042-KVM-VMX-Implement-NMI-source-injection.nmi
Patch08043: 0043-KVM-x86-Advise-NMI-Source-to-user-space.nmi
Patch08044: 0044-EDAC-ieh-Fix-a-compile-error.nmi
Patch08045: 0001-x86-fred-Revert-x86-fred-Enable-FRED-by-default.nmi
# ipu
Patch09001: 0001-media-ipu7-IPU7-driver-release-for-PTL-Beta-v6.17-iot.ipu
Patch09002: 0002-INT3472-Support-LT6911GXD.ipu
Patch09003: 0003-media-i2c-add-support-for-lt6911gxd.ipu
Patch09004: 0004-media-pci-enable-lt6911gxd-in-ipu-bridge.ipu
Patch09005: 0005-ipu-bridge-add-CPHY-support.ipu
Patch09006: 0006-media-ipu-Dma-sync-at-buffer_prepare-callback-as-DMA-i.ipu
Patch09007: 0007-staging-media-ipu7-remove-from-the-Makefile-Kconfig.ipu
Patch09008: 0008-media-pci-Enable-IPU7-in-Makefile-Kconfig.ipu
Patch09009: 0009-max9x-add-config-in-makefile-kconfig.ipu
Patch09010: 0010-drivers-media-set-v4l2_subdev_enable_streams_api-true-.ipu
Patch09011: 0011-ipu7-media-Fix-allyesconfig-allmodconfig.ipu
Patch09012: 0001-IPU7-media-pci-Add-platform-data-config.ipu
Patch09013: 0001-media-i2c-max9x-fix-S3-S4-error-for-max9x.ipu
Patch09014: 0002-media-i2c-max9x-uniform-serdes-driver-compilation.ipu
Patch09015: 0001-Revert-media-i2c-max9x-uniform-serdes-driver-compilati.ipu
Patch09016: 0002-Revert-media-i2c-max9x-fix-S3-S4-error-for-max9x.ipu
Patch09017: 0001-Remove-IPU7-drivers-from-pci-directory.ipu
Patch09018: 0002-patch-staging-add-ipu7-isys-reset-code.ipu
Patch09019: 0003-patch-staging-add-enbaled-IPU8_INSYS_NEW_ABI.ipu
Patch09020: 0004-patch-staging-add-enable-CONFIG_DEBUG_FS.ipu
Patch09021: 0005-patch-staging-add-enable-CONFIG_INTEL_IPU_ACPI.ipu
Patch09022: 0006-patch-staging-add-enable-ENABLE_FW_OFFLINE_LOGGER.ipu
Patch09023: 0007-patch-staging-add-patch-for-use-DPHY-as-the-default-ph.ipu
Patch09024: 0008-media-ipu-invalidate-MMU-TLB-in-dma-buffers-creation.ipu
Patch09025: 0009-patch-staging-add-fixup-some-PCI-probe-and-release-iss.ipu
Patch09026: 0010-patch-staging-add-IPU8_PCI_ID-support.ipu
Patch09027: 0011-patch-staging-add-patch-for-ipu7-Kconfig-Makefile.ipu
Patch09028: 0012-media-ipu-Update-firmware-ABI-version-to-1.2.1.2025121.ipu
Patch09029: 0013-patch-staging-add-ipu7-isys-tpg-and-MGC-config.ipu
Patch09030: 0014-media-ipu-Dma-sync-at-buffer_prepare-callback-as-DMA-i.ipu
Patch09031: 0015-media-ipu7-update-CDPHY-register-settings.ipu
Patch09032: 0016-Port-over-IPU-ACPI-drivers-changes-from-VTG-github-rep.ipu
Patch09033: 0017-Copy-ACPI-header-files-from-VTG-IPU7-IPU6-repo.ipu
Patch09034: 0018-IPU7-PSYS-driver-addition.ipu
Patch09035: 0019-porting-gmsl-isx031-code-between-PTL-IPU7-beta-release.ipu
Patch09036: 0020-Update-lt6911gxd-sensor-driver-to-fix-timeout-issue-af.ipu
Patch09037: 0021-Update-compilation-path-for-IPU7-drivers.ipu
Patch09038: 0001-i2c-add-identifier-for-ATR-and-MUX-adapters.ipu
Patch09039: 0002-i2c-i2c-core-acpi-clear-dependency-for-MUX-or-ATR-adap.ipu
Patch09040: 0003-i2c-atr-Add-fwnode-handling.ipu
Patch09041: 0004-media-v4l2-async-Fix-error-handling-on-steps-after-fin.ipu
Patch09042: 0005-media-mc-Add-INTERNAL-pad-flag.ipu
Patch09043: 0006-i2c-atr-Remove-COMPILE_TEST-check.ipu
# tbt
Patch10001: 0002-thunderbolt-Make-XDomain-lane-bonding-comply-with-the-.tbt
Patch10002: 0003-net-thunderbolt-Allow-changing-MTU-of-the-device.tbt
Patch10003: 0004-thunderbolt-Add-Kconfig-option-to-disable-PCIe-tunneli.tbt
# pmc_core
Patch11001: 0001-platform-x86-intel-pmc-Add-Wildcat-Lake-support-t.pmc_core
# i3c
Patch12001: 0002-i3c-master-Add-helpers-for-DMA-mapping-and-bounce-buff.i3c
Patch12002: 0003-i3c-mipi-i3c-hci-Use-core-helpers-for-DMA-mapping-and-.i3c
Patch12003: 0004-i3c-mipi-i3c-hci-Use-physical-device-pointer-with-DMA-.i3c
Patch12004: 0005-i3c-mipi-i3c-hci-Use-own-DMA-bounce-buffer-management-.i3c
Patch12005: 0006-i3c-mipi-i3c-hci-Change-interrupt-status-prints-to-dev.i3c
Patch12006: 0007-i3c-mipi-i3c-hci-Remove-nonexistent-ring-interrupt.i3c
Patch12007: 0008-i3c-mipi-i3c-hci-Uniform-ring-number-printouts.i3c
Patch12008: 0009-i3c-mipi-i3c-hci-Remove-function-enter-DBG-printouts.i3c
Patch12009: 0010-i3c-mipi-i3c-hci-Convert-remaining-DBG-prints-to-dev_d.i3c
Patch12010: 0002-platform-x86-intel-pmc-Add-Wildcat-Lake-support-t.pmc_core
# ethernet
Patch13001: 0001-igc-Only-dump-registers-if-configured-to-dump-HW-.ethernet
Patch13002: 0002-igc-Add-support-for-DMA-timestamp-for-non-PTP-pac.ethernet
Patch13003: 0003-bpf-add-btf-register-unregister-API.ethernet
Patch13004: 0004-net-core-XDP-metadata-BTF-netlink-API.ethernet
Patch13005: 0005-rtnetlink-Fix-unchecked-return-value-of-dev_xdp_q.ethernet
Patch13006: 0006-rtnetlink-Add-return-value-check.ethernet
Patch13007: 0007-tools-bpf-Query-XDP-metadata-BTF-ID.ethernet
Patch13008: 0008-tools-bpf-Add-xdp-set-command-for-md-btf.ethernet
Patch13009: 0009-igc-Add-BTF-based-metadata-for-XDP.ethernet
Patch13010: 0010-igc-Enable-HW-RX-Timestamp-for-AF_XDP-ZC.ethernet
Patch13011: 0011-igc-Take-care-of-DMA-timestamp-rollover.ethernet
Patch13012: 0014-igc-Enable-HW-TX-Timestamp-for-AF_XDP-ZC.ethernet
Patch13013: 0015-igc-Enable-trace-for-HW-TX-Timestamp-AF_XDP-ZC.ethernet
Patch13014: 0016-igc-Remove-the-CONFIG_DEBUG_MISC-condition-for-tr.ethernet
Patch13015: 0017-af_packet-Fix-wrong-timestamps-in-tcpdump.ethernet
Patch13016: 0001-igc-Reduce-TSN-TX-packet-buffer-from-7KB-to-5KB-p.ethernet
Patch13017: 0001-igc-fix-race-condition-in-TX-timestamp-read-for-r.ethernet
Patch13018: 0001-igc-Remove-XDP-metadata-invalidation.ethernet
# audio
Patch14001: 0001-ASoC-SOF-Intel-hda-Only-check-SSP-MCLK-mask-in-case-.audio
Patch14002: 0001-ASoC-Intel-sof_rt5682-Add-quirk-override-support.audio
# rt
Patch15001: 0001-mei-gsc-add-dependency-on-Xe-driver.rt
Patch15002: 0002-drm-me-gsc-mei-interrupt-top-half-should-be-in-irq-disa.rt
Patch15003: 0001-drm-i915-Use-preempt_disable-enable_rt-where-recommende.rt
Patch15004: 0002-drm-i915-Don-t-disable-interrupts-on-PREEMPT_RT-during-.rt
Patch15005: 0003-drm-i915-Don-t-check-for-atomic-context-on-PREEMPT_RT.rt
Patch15006: 0004-drm-i915-Disable-tracing-points-on-PREEMPT_RT.rt
Patch15007: 0005-drm-i915-gt-Use-spin_lock_irq-instead-of-local_irq_disa.rt
Patch15008: 0006-drm-i915-Drop-the-irqs_disabled-check.rt
Patch15009: 0007-drm-i915-guc-Consider-also-RCU-depth-in-busy-loop.rt
Patch15010: 0008-drm-i915-Consider-RCU-read-section-as-atomic.rt
Patch15011: 0009-Revert-drm-i915-Depend-on-PREEMPT_RT.rt
# thermal
Patch16001: 0001-thermal-intel-int340x-Remove-redundant-acpi_has_me.thermal
Patch16002: 0002-thermal-intel-int340x-Add-support-for-power-slider.thermal
Patch16003: 0003-thermal-intel-int340x-Enable-power-slider-interfac.thermal
Patch16004: 0004-thermal-intel-int340x-Add-module-parameter-for-bal.thermal
Patch16005: 0005-thermal-intel-int340x-Add-module-parameter-to-chan.thermal
Patch16006: 0006-thermal-gov_step_wise-Clean-up-local-variable-init.thermal
Patch16007: 0007-thermal-gov_step_wise-Clarify-cooling-logic-descri.thermal
Patch16008: 0008-thermal-testing-Rearrange-variable-declarations-in.thermal
Patch16009: 0009-thermal-hwmon-replace-deprecated-strcpy-with-strsc.thermal
Patch16010: 0010-thermal-intel-int340x-Power-Slider-Validate-slider.thermal
Patch16011: 0011-platform-x86-intel-hid-Add-Nova-Lake-support.thermal
# uncore-frequency
Patch17001: 0001-platform-x86-intel-uncore-freq-Add-additi.uncore-frequency
#CVE-2025-68265
Patch18001: CVE-2025-68265.patch

#CVE-2025-68263
Patch18002: CVE-2025-68263.patch

#CVE-2025-68255
Patch18003: CVE-2025-68255.patch

#CVE-2025-68256
Patch18004: CVE-2025-68256.patch

#CVE-2025-68281
Patch18005: CVE-2025-68281.patch

#CVE-2025-68262
Patch18006: CVE-2025-68262.patch

#CVE-2025-68261
Patch18007: CVE-2025-68261.patch

#CVE-2025-68259
Patch18008: CVE-2025-68259.patch

#CVE-2025-68254
Patch18009: CVE-2025-68254.patch

#CVE-2025-68264
Patch18010: CVE-2025-68264.patch

#CVE-2025-68325
Patch18011: CVE-2025-68325.patch

#CVE-2025-68323
Patch18012: CVE-2025-68323.patch

#CVE-2025-68749
Patch18013: CVE-2025-68749.patch

#CVE-2025-68745
Patch18014: CVE-2025-68745.patch

#CVE-2025-68349
Patch18015: CVE-2025-68349.patch

#CVE-2025-68366
Patch18016: CVE-2025-68366.patch

#CVE-2025-68744
Patch18017: CVE-2025-68744.patch

#CVE-2025-68363
Patch18018: CVE-2025-68363.patch

#CVE-2025-68379
Patch18019: CVE-2025-68379.patch

#CVE-2025-68375
Patch18020: CVE-2025-68375.patch

#CVE-2025-68736
Patch18021: CVE-2025-68736.patch

#CVE-2025-68732
Patch18022: CVE-2025-68732.patch

#CVE-2025-68730
Patch18023: CVE-2025-68730.patch

#CVE-2025-68733
Patch18024: CVE-2025-68733.patch

#CVE-2025-68333
Patch18025: CVE-2025-68333.patch

#CVE-2025-68336
Patch18026: CVE-2025-68336.patch

#CVE-2025-68345
Patch18027: CVE-2025-68345.patch

#CVE-2025-68346
Patch18028: CVE-2025-68346.patch

#CVE-2025-68347
Patch18029: CVE-2025-68347.patch

#CVE-2025-68348
Patch18030: CVE-2025-68348.patch

#CVE-2025-68353
Patch18031: CVE-2025-68353.patch

#CVE-2025-68358
Patch18032: CVE-2025-68358.patch

#CVE-2025-68337
Patch18033: CVE-2025-68337.patch

#CVE-2025-68354
Patch18034: CVE-2025-68354.patch

#CVE-2025-68359
Patch18035: CVE-2025-68359.patch

#CVE-2025-68741
Patch18036: CVE-2025-68741.patch

#CVE-2025-68368
Patch18037: CVE-2025-68368.patch

#CVE-2025-68371
Patch18038: CVE-2025-68371.patch

#CVE-2025-68373
Patch18039: CVE-2025-68373.patch
Patch18040: CVE-2025-68373-2.patch

#CVE-2025-68740
Patch18041: CVE-2025-68740.patch

#CVE-2025-68374
Patch18042: CVE-2025-68374.patch

#CVE-2025-68742
Patch18043: CVE-2025-68742.patch

#CVE-2025-68743
Patch18044: CVE-2025-68743.patch

#CVE-2025-68724
Patch18045: CVE-2025-68724.patch

#CVE-2025-68378
Patch18046: CVE-2025-68378.patch

#CVE-2025-68725
Patch18047: CVE-2025-68725.patch

#CVE-2025-68372
Patch18048: CVE-2025-68372.patch

#CVE-2026-23007
Patch18049: CVE-2026-23007.patch

#CVE-2026-23008
Patch18050: CVE-2026-23008.patch

#CVE-2026-23009
Patch18051: CVE-2026-23009.patch

#CVE-2026-23012
Patch18052: CVE-2026-23012.patch

#CVE-2026-22993
Patch18053: CVE-2026-22993.patch

#CVE-2026-22987
Patch18054: CVE-2026-22987.patch

#CVE-2026-22981
Patch18055: CVE-2026-22981.patch

#CVE-2025-71161
Patch18056: CVE-2025-71161.patch

#CVE-2025-71117
Patch18057: CVE-2025-71117.patch

#CVE-2025-71128
Patch18058: CVE-2025-71128.patch

#CVE-2025-71139
Patch18059: CVE-2025-71139-1.patch
Patch18060: CVE-2025-71139-2.patch

#CVE-2025-71142
Patch18061: CVE-2025-71142.patch

#CVE-2025-71115
Patch18062: CVE-2025-71115.patch

#CVE-2025-71090
Patch18063: CVE-2025-71090.patch

#CVE-2025-71070
Patch18064: CVE-2025-71070-1.patch
Patch18065: CVE-2025-71070-2.patch

#CVE-2025-71074
Patch18066: CVE-2025-71074.patch

#CVE-2025-68823
Patch18067: CVE-2025-68823.patch

#CVE-2025-68807
Patch18068: CVE-2025-68807.patch

#CVE-2025-68805
Patch18069: CVE-2025-68805.patch

#CVE-2025-68791
Patch18070: CVE-2025-68791.patch

#CVE-2025-68768
Patch18071: CVE-2025-68768-1.patch
Patch18072: CVE-2025-68768-2.patch
Patch18073: CVE-2025-68768-3.patch

#CVE-2025-68764
Patch18074: CVE-2025-68764.patch

#CVE-2025-68762
Patch18075: CVE-2025-68762.patch

#CVE-2025-68759
Patch18076: CVE-2025-68759.patch

#CVE-2025-68756
Patch18077: CVE-2025-68756.patch

#CVE-2025-68753
Patch18078: CVE-2025-68753.patch

#CVE-2025-68752
Patch18079: CVE-2025-68752.patch

#CVE-2026-23004
Patch18080: CVE-2026-23004.patch

#CVE-2026-22985
Patch18081: CVE-2026-22985-1.patch
Patch18082: CVE-2026-22985-2.patch

# End of Patch section

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
%setup -q -n linux-6.17.11
%autosetup -p1 -n linux-6.17.11
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
* Thu Feb 19 2026 Lishan Liu <lishan.liu@intel.com> - 6.17.11-3
- Kernel config update for TCP plus TCSS ports

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
