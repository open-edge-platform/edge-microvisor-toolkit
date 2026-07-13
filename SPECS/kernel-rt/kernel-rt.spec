Summary:        Preempt RT Linux Kernel
Name:           kernel-rt
Version:        6.18.33
Release:        1%{?dist}
License:        GPLv2
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://www.kernel.org/pub/linux/kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.18.33.tar.gz
Source1:        config
Source3:        sha512hmac-openssl.sh
Source4:        emt-ca-20211013.pem
Source5:        cpupower
Source6:        cpupower.service

# Intel Kernel Patches
# Series file for v6.18.33 linux kernel
# 83657f4189612 Linux 6.18.33
# security
Patch01001: 0001-Add-security.md-file.security
Patch01002: 0002-Add-updated-TPR-TXT-Protected-Regions-support-to-.security
Patch01003: 0001-mei-bus-fix-device-leak.security
Patch01004: 0002-mei-bus-add-api-to-query-capabilities-of-ME-clien.security
Patch01005: 0003-mei-expose-device-kind-for-ioe-device.security
Patch01006: 0004-mei-virtio-virtualization-frontend-driver.security
Patch01007: 0005-INTEL_DII-mei-avoid-reset-if-fw-is-down.security
Patch01008: 0006-INTEL_DII-mei-iaf-add-iaf-Intel-Accelerator-Fabri.security
Patch01009: 0007-INTEL_DII-mei-add-check-for-offline-bit-in-every-.security
Patch01010: 0008-INTEL_DII-mei-add-empty-handlers-for-ops-function.security
Patch01011: 0001-issei-initial-driver-skeleton.security
Patch01012: 0002-issei-add-firmware-and-host-clients-implementatio.security
Patch01013: 0003-issei-implement-main-thread-and-ham-messages.security
Patch01014: 0004-issei-add-heci-hardware-module.security
Patch01015: 0005-issei-update-MAINTAINERS-file.security
Patch01016: 0006-issei-host_client-add-dma-allocation-support.security
Patch01017: 0007-issei-add-driver-to-driver-interface.security
Patch01018: 0001-tpm-restore-timeout-for-key-creation-commands.security
Patch01019: 0001-iommu-vt-d-cache-TPR-mappings-at-boot-to-fix-S3-r.security
# preempt-rt
Patch02001: 0001-drm-i915-Use-preempt_disable-enable_rt-where-recommende.rt
Patch02002: 0002-drm-i915-Don-t-disable-interrupts-on-PREEMPT_RT-during-.rt
Patch02003: 0003-drm-i915-Disable-tracing-points-on-PREEMPT_RT.rt
Patch02004: 0004-drm-i915-gt-Use-spin_lock_irq-instead-of-local_irq_disa.rt
Patch02005: 0005-drm-i915-Drop-the-irqs_disabled-check.rt
Patch02006: 0006-drm-i915-guc-Consider-also-RCU-depth-in-busy-loop.rt
Patch02007: 0007-drm-i915-Consider-RCU-read-section-as-atomic.rt
Patch02008: 0008-Revert-drm-i915-Depend-on-PREEMPT_RT.rt
Patch02009: 0009-sysfs-Add-sys-kernel-realtime-entry.rt
Patch02010: 0001-drm-i915-adding-i915-parameter-to-disable-stolen-memory.rt
Patch02011: 0001-sched-adding-option-to-disable-timer-migration-in-isola.rt
Patch02012: 0002-drm-xe-adding-parameter-to-disable-stolen-memory.rt
Patch02013: 0002-efi-adding-dynamic-enable-efi-service-interface.rt
Patch02014: 0003-drm-i915-add-i915-perf-event-capacity.rt
# rapl
Patch03001: 0003-cpuidle-Add-sanity-check-for-exit-latency-and-target-.rapl
Patch03002: 0004-cpuidle-teo-Use-this_cpu_ptr-where-possible.rapl
Patch03003: 0006-cpuidle-governors-teo-Drop-redundant-function-paramet.rapl
Patch03004: 0007-cpuidle-governors-teo-Use-s64-consistently-in-teo_upd.rapl
Patch03005: 0008-cpuidle-governors-teo-Decay-metrics-below-DECAY_SHIFT.rapl
Patch03006: 0010-cpuidle-governors-teo-Rework-the-handling-of-tick-wak.rapl
Patch03007: 0011-cpuidle-governors-teo-Fix-tick_intercepts-handling-in.rapl
Patch03008: 0012-cpuidle-governors-teo-Simplify-intercepts-based-state.rapl
Patch03009: 0013-powercap-intel_rapl-Prepare-read_raw-interface-for-at.rapl
Patch03010: 0014-powercap-intel_rapl-Enable-MSR-based-RAPL-PMU-support.rapl
Patch03011: 0015-cpuidle-governors-teo-Add-missing-space-to-the-descri.rapl
Patch03012: 0016-cpuidle-Update-header-inclusion.rapl
Patch03013: 0017-cpuidle-Warn-instead-of-bailing-out-if-target-residen.rapl
# turbo
Patch04001: 0002-tools-power-turbostat-Add-Wildcat-Lake-and-Nova-Lake.turbo
Patch04002: 0003-tools-power-turbostat-Refactor-added-column-header-p.turbo
Patch04003: 0004-tools-power-turbostat-Refactor-added-counter-value-p.turbo
Patch04004: 0005-tools-power-turbostat.8-Update-example.turbo
Patch04005: 0006-tools-power-turbostat-Refactor-floating-point-printo.turbo
Patch04006: 0007-tools-power-turbostat-Remove-dead-code.turbo
Patch04007: 0008-tools-power-turbostat-Add-LLC-stats.turbo
Patch04008: 0009-tools-power-turbostat-Set-per_cpu_msr_sum-to-NULL-af.turbo
Patch04009: 0010-tools-power-turbostat-Add-run-time-MSR-driver-probe.turbo
Patch04010: 0011-tools-power-x86_energy_perf_policy-Add-Android-MSR-d.turbo
Patch04011: 0012-tools-power-x86_energy_perf_policy-Simplify-Android-.turbo
Patch04012: 0013-tools-power-x86_energy_perf_policy-Fix-format-string.turbo
Patch04013: 0014-tools-power-x86_energy_perf_policy-Fix-potential-NUL.turbo
Patch04014: 0015-tools-power-turbostat-Validate-RAPL-MSRs-for-AWS-Nit.turbo
Patch04015: 0016-tools-power-turbostat-Enhance-perf-probe.turbo
Patch04016: 0017-tools-power-turbostat-Validate-APERF-access-for-VMWA.turbo
Patch04017: 0018-tools-power-turbostat-Print-nan-for-out-of-range-per.turbo
Patch04018: 0019-tools-power-turbostat-Print-percentages-in-8-columns.turbo
Patch04019: 0020-tools-power-turbostat-Print-wide-names-only-for-RAW-.turbo
Patch04020: 0021-tools-power-turbostat-version-2025.12.02.turbo
# ethernet
Patch05001: 0001-igc-Only-dump-registers-if-configured-to-dump-HW-.ethernet
Patch05002: 0002-af_packet-Fix-wrong-timestamps-in-tcpdump.ethernet
Patch05003: 0001-igc-Add-support-for-DMA-timestamp-for-non-PTP-pac.ethernet
Patch05004: 0002-bpf-add-btf-register-unregister-API.ethernet
Patch05005: 0003-net-core-XDP-metadata-BTF-netlink-API.ethernet
Patch05006: 0004-rtnetlink-Fix-unchecked-return-value-of-dev_xdp_q.ethernet
Patch05007: 0005-rtnetlink-Add-return-value-check.ethernet
Patch05008: 0006-tools-bpf-Query-XDP-metadata-BTF-ID.ethernet
Patch05009: 0007-tools-bpf-Add-xdp-set-command-for-md-btf.ethernet
Patch05010: 0008-igc-Add-BTF-based-metadata-for-XDP.ethernet
Patch05011: 0009-igc-Enable-HW-RX-Timestamp-for-AF_XDP-ZC.ethernet
Patch05012: 0010-igc-Take-care-of-DMA-timestamp-rollover.ethernet
Patch05013: 0011-igc-Enable-HW-TX-Timestamp-for-AF_XDP-ZC.ethernet
Patch05014: 0012-igc-Enable-trace-for-HW-TX-Timestamp-AF_XDP-ZC.ethernet
Patch05015: 0013-igc-Remove-the-CONFIG_DEBUG_MISC-condition-for-tr.ethernet
Patch05016: 0014-igc-Remove-XDP-metadata-invalidation.ethernet
Patch05017: 0001-net-pcs-xpcs-enable-xpcs-reset-skipping.ethernet
Patch05018: 0002-net-stmmac-Bugfix-on-stmmac_interrupt-for-WOL.ethernet
Patch05019: 0003-net-phy-increase-gpy-loopback-test-delay.ethernet
Patch05020: 0004-net-stmmac-Resolve-poor-line-rate-after-switching.ethernet
Patch05021: 0005-net-phy-dp83867-perform-restart-AN-after-modifyin.ethernet
Patch05022: 0006-net-stmmac-Adjust-mac_capabilities-for-Intel-mGbE.ethernet
Patch05023: 0007-stmmac-intel-skip-xpcs-reset-for-2.5Gbps-on-Intel.ethernet
Patch05024: 0008-net-stmmac-add-check-for-2.5G-mode-to-prevent-MAC.ethernet
Patch05025: 0009-stmmac-intel-Enable-PHY-WoL-in-ADL-N.ethernet
Patch05026: 0010-net-phy-reconfigure-PHY-WoL-when-WoL-option-is-en.ethernet
Patch05027: 0011-net-stmmac-Set-mac_managed_pm-flag-from-stmmac-to.ethernet
Patch05028: 0012-net-phylink-Add-module_exit.ethernet
Patch05029: 0013-net-stmmac-restructure-Rx-Tx-hardware-timestampin.ethernet
Patch05030: 0014-net-stmmac-introduce-AF_XDP-ZC-RX-HW-timestamps.ethernet
Patch05031: 0015-net-stmmac-add-fsleep-in-HW-Rx-timestamp-checking.ethernet
Patch05032: 0016-net-stmmac-introduce-AF_XDP-ZC-TX-HW-timestamps.ethernet
Patch05033: 0017-net-phy-Set-eee_cfg.eee_enabled-according-to-PHY.ethernet
Patch05034: 0018-net-stmmac-intel-Initialize-plat-phy_interfaces-i.ethernet
Patch05035: 0001-Revert-net-stmmac-Adjust-mac_capabilities-for-Int.ethernet
Patch05036: 0002-net-stmmac-Adjust-mac_capabilities-for-Intel-mGbE.ethernet
Patch05037: 0003-net-stmmac-Update-default_an_inband-before-assign.ethernet
Patch05038: 0001-igc-skip-RX-timestamp-header-for-frame-preemption.ethernet
# nmi
Patch06001: 0001-KVM-VMX-Enable-support-for-secondary-VM-exit-controls.nmi
Patch06002: 0002-KVM-VMX-Initialize-VM-entry-exit-FRED-controls-in-vmcs.nmi
Patch06003: 0003-KVM-VMX-Disable-FRED-if-FRED-consistency-checks-fail.nmi
Patch06004: 0004-x86-cea-Prefix-event-stack-names-with-ESTACK_.nmi
Patch06005: 0005-x86-cea-Use-array-indexing-to-simplify-exception-stack.nmi
Patch06006: 0006-x86-cea-Export-__this_cpu_ist_top_va-to-KVM.nmi
Patch06007: 0007-KVM-VMX-Initialize-VMCS-FRED-fields.nmi
Patch06008: 0008-KVM-VMX-Set-FRED-MSR-intercepts.nmi
Patch06009: 0009-KVM-VMX-Save-restore-guest-FRED-RSP0.nmi
Patch06010: 0010-KVM-VMX-Add-support-for-saving-and-restoring-FRED-MSRs.nmi
Patch06011: 0011-KVM-x86-Add-a-helper-to-detect-if-FRED-is-enabled-for-.nmi
Patch06012: 0012-KVM-VMX-Virtualize-FRED-event_data.nmi
Patch06013: 0013-KVM-VMX-Virtualize-FRED-nested-exception-tracking.nmi
Patch06014: 0014-KVM-x86-Save-restore-the-nested-flag-of-an-exception.nmi
Patch06015: 0015-KVM-x86-Mark-CR4.FRED-as-not-reserved.nmi
Patch06016: 0016-KVM-VMX-Dump-FRED-context-in-dump_vmcs.nmi
Patch06017: 0017-KVM-x86-Advertise-support-for-FRED.nmi
Patch06018: 0018-KVM-nVMX-Enable-support-for-secondary-VM-exit-controls.nmi
Patch06019: 0019-KVM-nVMX-Handle-FRED-VMCS-fields-in-nested-VMX-context.nmi
Patch06020: 0020-KVM-nVMX-Validate-FRED-related-VMCS-fields.nmi
Patch06021: 0021-KVM-nVMX-Guard-SHADOW_FIELD_R-OW-macros-with-VMX-featu.nmi
Patch06022: 0022-KVM-nVMX-Enable-VMX-FRED-controls.nmi
Patch06023: 0023-KVM-selftests-Run-debug_regs-test-with-FRED-enabled.nmi
Patch06024: 0024-KVM-selftests-Add-a-new-VM-guest-mode-to-run-user-leve.nmi
Patch06025: 0025-KVM-selftests-Add-fred-exception-tests.nmi
Patch06026: 0026-KVM-selftests-Add-the-2nd-VM-exit-controls-MSR-to-the-.nmi
Patch06027: 0027-task_stack.h-Add-a-new-helper-task_empty_stack_pointer.nmi
Patch06028: 0028-x86-fred-Allow-variable-sized-event-frame.nmi
Patch06029: 0029-x86-Remove-the-padding-space-at-top-of-the-init-stack.nmi
Patch06030: 0030-x86-fred-Provide-separate-IRQ-vs.-NMI-wrappers-for-ent.nmi
Patch06031: 0031-x86-fred-Pass-event-data-to-the-NMI-entry-point-from-K.nmi
Patch06032: 0032-x86-cpufeatures-Add-the-CPUID-feature-bit-for-NMI-sour.nmi
Patch06033: 0033-x86-nmi-Extend-the-registration-interface-to-include-t.nmi
Patch06034: 0034-x86-nmi-Assign-and-register-NMI-source-vectors.nmi
Patch06035: 0035-x86-nmi-Add-support-to-handle-NMIs-with-source-informa.nmi
Patch06036: 0036-x86-nmi-Prepare-for-the-new-NMI-source-vector-encoding.nmi
Patch06037: 0037-x86-nmi-Enable-NMI-source-for-IPIs-delivered-as-NMIs.nmi
Patch06038: 0038-perf-x86-Enable-NMI-source-reporting-for-perfmon.nmi
Patch06039: 0039-x86-nmi-Print-source-information-with-the-unknown-NMI-.nmi
Patch06040: 0040-x86-nmi-Include-source-information-in-NMI-handler-trac.nmi
Patch06041: 0041-KVM-VMX-Implement-NMI-source-injection.nmi
Patch06042: 0042-KVM-x86-Advise-NMI-Source-to-user-space.nmi
Patch06043: 0043-x86-fred-Enable-FRED-by-default.nmi
Patch06044: 0044-fixup-KVM-VMX-Handle-MCs-on-VM-Enter-TD-Enter-outside-.nmi
# drm
Patch07001: 0001-drm-xe-xe_vm-bypass-vm_bind-failure-as-wa-to-enable-hw.drm
Patch07002: 0002-drm-virtio-freeze-and-restore-hooks-to-support-suspend.drm
Patch07003: 0003-drm-virtio-save-and-restore-virtio_gpu_objects.drm
Patch07004: 0001-drm-xe-Upgrade-PTL-and-BMG-GuC-to-70.55.3-MTL-LNL-DG2-.drm
Patch07005: 0001-i915-gt-Upgrade-GuCs-accordingly-to-20260110-baselin.drm
Patch07006: 0001-i915-gt-GuC-for-legacy-platform.drm
Patch07007: 0001-i915-and-xe-gt-Update-GuC-versions-accordingly.drm
Patch07008: 0001-drm-i915-mtl-Add-C10-table-for-HDMI-Clock-25175.drm
Patch07009: 0002-drm-i915-mtl-Copy-c10-phy-pll-sw-state-from-master-to-.drm
Patch07010: 0003-drm-i915-guc-Define-MAX_DWORDS-for-CTB-HXG-Message.drm
Patch07011: 0004-drm-i915-call-taint_for_CI-on-FLR-failure.drm
Patch07012: 0005-drm-i915-huc-load-HuC-via-non-POR-GSC-engine-flow.drm
Patch07013: 0006-drm-i915-SR-IOV-Enabling-and-Support.drm
Patch07014: 0007-Revert-drm-i915-move-platform_engine_mask-and-memory_r.drm
Patch07015: 0008-drm-i915-gt-Enable-the-early-register-to-working-winVM.drm
Patch07016: 0009-drm-i915-gt-Modify-the-adls-mocs-table-same-as-tgl-moc.drm
Patch07017: 0010-drm-i915-Bypass-gem_set_tiling-and-gem_get_tiling.drm
Patch07018: 0011-drm-i915-enable-CCS-on-DG1-and-TGL-for-testing.drm
Patch07019: 0012-drm-i915-force-VF-using-v70-GuC-API.drm
Patch07020: 0013-drm-i915-fix-regression-on-sriov-vf-failures-due-to-ne.drm
Patch07021: 0014-drm-i915-use-the-original-Wa_14010685332-for-PCH_ADP.drm
Patch07022: 0015-drm-i915-fix-bitmap-clear-API-region-start-issue.drm
Patch07023: 0016-drm-i915-iov-Expose-early-runtime-registers-for-MTL.drm
Patch07024: 0017-drm-i915-gt-fix-empty-workaround-list-access-issue.drm
Patch07025: 0018-drm-i915-mtl-Add-module-parameter-override-for-Wa_1601.drm
Patch07026: 0019-drm-i915-mtl-Provide-user-the-option-to-disable-ccs.drm
Patch07027: 0020-drm-i915-mtl-Turn-on-Wa_16019325821-Wa_14019159160-by-.drm
Patch07028: 0021-drm-i915-pf-Use-GPU-to-set-PTE-owner.drm
Patch07029: 0022-drm-i915-pf-Use-GPU-to-set-PTE-owner-on-platforms-with.drm
Patch07030: 0023-drm-i915-access-ddc-pointer-only-if-it-is-available.drm
Patch07031: 0024-drm-i915-iov-Adding-runtime-reg-for-MTL-HuC-status.drm
Patch07032: 0025-drm-i915-Re-add-enable_rc6-modparam.drm
Patch07033: 0026-drm-virtio-use-the-fence-for-every-plane-update.drm
Patch07034: 0027-drm-virtio-freeze-and-restore-hooks-to-support-suspend.drm
Patch07035: 0028-drm-virtio-save-and-restore-virtio_gpu_objects.drm
Patch07036: 0029-drm-i915-pf-Introduce-i915_ggtt_save_ptes-and-i915_ggt.drm
Patch07037: 0030-drm-i915-iov-Introduce-VFs-shadow-copy-of-GGTT-on-PF.drm
Patch07038: 0031-drm-i915-iov-Shadow-GGTT-mock-selftestes.drm
Patch07039: 0032-drm-i915-gt-Don-t-support-GGTT-save-restore-via-BAR-fo.drm
Patch07040: 0033-drm-i915-pf-Add-helpers-for-saving-loading-GGTT-state.drm
Patch07041: 0034-drm-i915-pf-Handle-VF-pause-complete-notification.drm
Patch07042: 0035-drm-i915-pf-Allow-to-save-restore-GuC-VF-state.drm
Patch07043: 0036-drm-i915-pf-Save-and-restore-VFs-state-during-S2idle-S.drm
Patch07044: 0037-drm-i915-pf-Skip-VF-save-restore-on-S2idle-S3-S4-if-it.drm
Patch07045: 0038-drm-i915-pf-Start-use-shadow-GGTT-to-save-restore-duri.drm
Patch07046: 0039-drm-i915-pf-Export-API-to-be-used-by-i915-vfio-pci.drm
Patch07047: 0040-drm-i915-iov-Flag-which-tells-whether-PAUSE-is-in-prog.drm
Patch07048: 0041-drm-i915-iov-Remember-run-state-on-suspend-and-restore.drm
Patch07049: 0042-drm-i915-pf-Pause-VF-before-restore-GuC-state-after-su.drm
Patch07050: 0043-drm-i915-iov-fix-i915-sriov-build-issue.drm
Patch07051: 0044-drm-i915-enable-guc-submission-for-ADLs-by-default.drm
Patch07052: 0045-drm-i915-CTB-TLB-invalidation-fix-on-VM.drm
Patch07053: 0046-vfio-i915-Add-vfio_pci-driver-for-Intel-graphics.drm
Patch07054: 0047-i915-Enable-w-a-16026508708.drm
Patch07055: 0048-drm-i915-disable-a-couple-of-RT-functions-if-RT-is-dis.drm
Patch07056: 0049-drm-i915-Fix-logic-for-GUC-Process.drm
Patch07057: 0050-vfio-i915-Add-support-for-MMIO-save-restore.drm
Patch07058: 0051-drm-i915-SR-IOV-Save-Restore-Feature-support.drm
Patch07059: 0052-drm-i915-gt-Avoid-using-masked-workaround-for-CCS_MODE.drm
Patch07060: 0053-drm-i915-gt-Move-the-CCS-mode-variable-to-a-global-pos.drm
Patch07061: 0054-drm-i915-gt-Allow-the-creation-of-multi-mode-CCS-masks.drm
Patch07062: 0055-drm-i915-gt-Refactor-uabi-engine-class-instance-list-c.drm
Patch07063: 0056-drm-i915-gem-Mark-and-verify-UABI-engine-validity.drm
Patch07064: 0057-drm-i915-gt-Introduce-for_each_enabled_engine-and-appl.drm
Patch07065: 0058-drm-i915-gt-Manage-CCS-engine-creation-within-UABI-exp.drm
Patch07066: 0059-drm-i915-gt-Remove-cslices-mask-value-from-the-CCS-str.drm
Patch07067: 0060-drm-i915-gt-Expose-the-number-of-total-CCS-slices.drm
Patch07068: 0061-drm-i915-gt-Store-engine-related-sysfs-kobjects.drm
Patch07069: 0062-drm-i915-gt-Store-active-CCS-mask.drm
Patch07070: 0063-drm-i915-Protect-access-to-the-UABI-engines-list-with-.drm
Patch07071: 0064-drm-i915-gt-Isolate-single-sysfs-engine-file-creation.drm
Patch07072: 0065-drm-i915-gt-Implement-creation-and-removal-routines-fo.drm
Patch07073: 0066-drm-i915-gt-Allow-the-user-to-change-the-CCS-mode-thro.drm
Patch07074: 0067-drm-i915-gt-Refactor-CCS-mode-handling-and-improve-app.drm
Patch07075: 0068-drm-i915-no-waiting-for-page-flip-in-vpp-case.drm
Patch07076: 0069-drm-i915-move-sriov-selftest-buffer-out-of-stack.drm
Patch07077: 0001-drm-virtio-Wait-until-the-control-and-cursor-queues-ar.drm
Patch07078: 0002-virtio-gpu-reset-attachment-state-during-resource-rest.drm
Patch07079: 0001-Add-display-error-fatal-masking-to-earlier-stage-and-a.drm
Patch07080: 0001-Revert-drm-i915-no-waiting-for-page-flip-in-vpp-case.drm
Patch07081: 0001-drm-i915-bios-Update-reading-panel-rotation-from-VBT.drm
Patch07082: 0001-drm-xe-display-Always-use-system-memory-on-PREEMPT_RT-.drm
Patch07083: 0002-drm-xe-display-Prefer-not-to-allocate-a-framebuffers-i.drm
Patch07084: 0003-drm-vblank_work-Add-methods-to-schedule-vblank_work-in.drm
Patch07085: 0004-drm-vblank-Add-a-2-stage-version-of-drm_crtc_arm_vblan.drm
Patch07086: 0005-drm-intel-display-Make-intel_crtc_arm_vblank_event-sta.drm
Patch07087: 0006-drm-intel-display-Convert-vblank-event-handling-to-2-s.drm
Patch07088: 0007-drm-i915-display-Move-vblank-put-until-after-critical-.drm
Patch07089: 0008-drm-i915-display-Remove-locking-from-intel_vblank_evad.drm
Patch07090: 0009-drm-i915-display-Handle-vlv-dsi-workaround-in-scanline.drm
Patch07091: 0010-drm-i915-gt-Add-a-spinlock-to-prevent-starvation-of-ir.drm
Patch07092: 0011-drm-i915-disable-PMU-events-on-PREEMPT_RT.drm
# edac
Patch08001: 0003-EDAC-igen6-Fix-masks-of-MCHBAR-TOM-TOUUD-registers.edac
Patch08002: 0001-x86-mce-Add-MCACOD-code-for-generic-I-O-error.edac
Patch08003: 0002-EDAC-ieh-Add-I-O-device-EDAC-driver-for-Intel-CPUs-wi.edac
Patch08004: 0003-EDAC-ieh-Add-I-O-device-EDAC-support-for-Intel-Tiger-.edac
Patch08005: 0004-EDAC-igen6-Add-registration-APIs-for-In-Band-ECC-erro.edac
Patch08006: 0005-FIXUP-Add-argument-to-register_nmi_handler-thanks-to-.edac
Patch08007: 0001-EDAC-igen6-Fix-call-trace-due-to-missing-release.edac
Patch08008: 0002-EDAC-igen6-Fix-memory-topology-parsing-for-Panther-La.edac
Patch08009: 0003-EDAC-igen6-Add-one-Intel-Panther-Lake-H-SoC-support.edac
Patch08010: 0004-EDAC-igen6-Fix-runtime-field-extraction-for-lts-6.18.edac
Patch08011: 0001-EDAC-igen6-Add-Intel-Starfire-SoCs-support.edac
# perf
Patch09001: 0001-perf-x86-intel-cstate-Add-Pantherlake-support.perf
Patch09002: 0002-perf-x86-intel-uncore-Move-uncore-discovery-init-stru.perf
Patch09003: 0003-perf-x86-intel-uncore-Support-per-platform-discovery-.perf
Patch09004: 0004-perf-x86-intel-uncore-Remove-has_generic_discovery_ta.perf
Patch09005: 0005-perf-x86-intel-uncore-Add-IMH-PMON-support-for-Diamon.perf
Patch09006: 0006-perf-x86-intel-uncore-Add-CBB-PMON-support-for-Diamon.perf
Patch09007: 0007-perf-x86-intel-uncore-Add-domain-global-init-callback.perf
Patch09008: 0008-perf-x86-intel-uncore-Add-freerunning-event-descripto.perf
Patch09009: 0009-perf-x86-intel-uncore-Support-IIO-free-running-counte.perf
Patch09010: 0010-perf-x86-intel-uncore-Support-uncore-constraint-range.perf
Patch09011: 0011-perf-x86-intel-uncore-Update-DMR-uncore-constraints-p.perf
Patch09012: 0012-perf-pmu-Relax-uncore-wildcard-matching-to-allow-nume.perf
Patch09013: 0013-perf-x86-intel-uncore-Add-missing-PMON-units-for-Pant.perf
Patch09014: 0001-perf-x86-intel-uncore-Refine-global-control-handling-.perf
Patch09015: 0001-perf-x86-intel-Initialize-architectural-PEBS.perf
Patch09016: 0002-perf-x86-intel-ds-Factor-out-PEBS-record-processing-c.perf
Patch09017: 0003-perf-x86-intel-ds-Factor-out-PEBS-group-processing-co.perf
Patch09018: 0004-perf-x86-intel-Process-arch-PEBS-records-or-record-fr.perf
Patch09019: 0005-perf-x86-intel-Allocate-arch-PEBS-buffer-and-initiali.perf
Patch09020: 0006-perf-x86-intel-Update-dyn_constraint-base-on-PEBS-eve.perf
Patch09021: 0007-perf-x86-intel-Setup-PEBS-data-configuration-and-enab.perf
Patch09022: 0008-perf-x86-intel-Add-counter-group-support-for-arch-PEB.perf
Patch09023: 0009-perf-x86-intel-Check-PEBS-dyn_constraints.perf
Patch09024: 0010-perf-x86-intel-Optimize-PEBS-extended-config.perf
Patch09025: 0011-perf-x86-intel-Fix-and-clean-up-intel_pmu_drain_arch_.perf
Patch09026: 0012-perf-x86-intel-Enable-large-PEBS-sampling-for-XMMs.perf
Patch09027: 0013-perf-x86-intel-Convert-x86_perf_regs-to-per-cpu-varia.perf
Patch09028: 0014-perf-Eliminate-duplicate-arch-specific-functions-defi.perf
Patch09029: 0015-perf-x86-Use-x86_perf_regs-in-the-x86-nmi-handler.perf
Patch09030: 0016-x86-fpu-Ensure-TIF_NEED_FPU_LOAD-is-set-after-saving-.perf
Patch09031: 0017-x86-fpu-xstate-Add-xsaves_nmi-helper.perf
Patch09032: 0018-perf-Move-and-rename-has_extended_regs-for-arch-speci.perf
Patch09033: 0019-perf-x86-Enable-XMM-Register-Sampling-for-Non-PEBS-Ev.perf
Patch09034: 0020-perf-x86-Enable-XMM-register-sampling-for-REGS_USER-c.perf
Patch09035: 0021-perf-Add-perf_event_attr-config4.perf
Patch09036: 0022-perf-Add-sampling-support-for-SIMD-registers.perf
Patch09037: 0023-perf-x86-Support-XMM-sampling-using-sample_simd_vec_r.perf
Patch09038: 0024-perf-x86-Support-YMM-sampling-using-sample_simd_vec_r.perf
Patch09039: 0025-perf-x86-Support-ZMM-sampling-using-sample_simd_vec_r.perf
Patch09040: 0026-perf-x86-Support-OPMASK-sampling-using-sample_simd_pr.perf
Patch09041: 0027-perf-Enhance-perf_reg_validate-with-simd_enabled-argu.perf
Patch09042: 0028-perf-x86-Support-eGPRs-sampling-using-sample_regs_-fi.perf
Patch09043: 0029-perf-x86-Support-SSP-sampling-using-sample_regs_-fiel.perf
Patch09044: 0030-perf-x86-intel-Support-arch-PEBS-based-SIMD-eGPRs-SSP.perf
Patch09045: 0031-perf-x86-intel-Enable-PERF_PMU_CAP_SIMD_REGS-capabili.perf
Patch09046: 0032-perf-perf_regs-Switch-from-arch-string-to-int-e_machi.perf
Patch09047: 0033-perf-regs-Refactor-use-of-arch__sample_reg_masks-to-p.perf
Patch09048: 0034-perf-perf_regs-Accurately-compute-register-names-for-.perf
Patch09049: 0035-perf-arch-Update-arch-headers-to-use-relative-UAPI-pa.perf
Patch09050: 0036-perf-regs-Remove-__weak-attributive-arch__xxx_reg_mas.perf
Patch09051: 0037-perf-regs-Remove-__weak-attributive-arch_sdt_arg_pars.perf
Patch09052: 0038-perf-regs-Support-x86-eGPRs-SSP-sampling.perf
Patch09053: 0039-perf-regs-Support-x86-SIMD-registers-sampling.perf
Patch09054: 0040-perf-regs-Enable-dumping-of-SIMD-registers.perf
Patch09055: 0041-tools-headers-Sync-UAPI-headers-and-fix-perf-build-fo.perf
# pmt
Patch10001: 0001-platform-x86-intel-vsec-Add-support-for-Wildcat-Lake.pmt
Patch10002: 0001-platform-x86-intel-pmc-Add-support-for-multiple-DMU-GU.pmt
Patch10003: 0002-platform-x86-intel-pmc-Add-DMU-GUID-to-Arrow-Lake-U-H.pmt
Patch10004: 0003-platform-x86-intel-pmc-Rename-PMC-index-variable-to-pm.pmt
Patch10005: 0004-platform-x86-intel-pmc-Relocate-lpm_req_guid-to-pmc_re.pmt
Patch10006: 0005-platform-x86-intel-pmc-Remove-redundant-has_die_c6-var.pmt
Patch10007: 0006-platform-x86-intel-pmc-Enable-SSRAM-support-for-Wildca.pmt
# audio
Patch11001: 0001-ASoC-Intel-sof_rt5682-Add-quirk-override-support.audio
Patch11002: 0002-ASoC-SOF-Intel-hda-Only-check-SSP-MCLK-mask-in-case-.audio
Patch11003: 0001-soundwire-fix-bug-in-sdw_add_element_group_count-fou.audio
Patch11004: 0001-ASoC-SOF-Don-t-print-the-monolithic-topology-name-if.audio
Patch11005: 0002-ASoC-soc-acpi-make-some-variables-of-acpi-adr-and-li.audio
Patch11006: 0003-ASoC-soc_sdw_utils-add-name_prefix-to-asoc_sdw_codec.audio
Patch11007: 0004-ASoC-Intel-export-sof_sdw_get_tplg_files.audio
Patch11008: 0005-ASoC-soc_sdw_utils-export-asoc_sdw_get_dai_type.audio
Patch11009: 0006-ASoC-SOF-add-platform-name-into-sof_intel_dsp_desc.audio
Patch11010: 0007-ASoC-SOF-don-t-check-the-existence-of-dummy-topology.audio
Patch11011: 0008-ASoC-SOF-Intel-use-sof_sdw-as-default-SDW-machine-dr.audio
Patch11012: 0009-ASoC-sof-function-topology-lib-escalate-the-log-when.audio
# lpss
Patch12001: 0001-Added-spi_set_cs-for-more-stable-r-w-operations-in.lpss
# cpuidle
Patch13001: 0001-intel_idle-Add-Panther-Lake-C-states-table.cpuidle
Patch13002: 0001-x86-cpu-Add-Intel-CPU-model-number-for-rugged-Pant.cpuidle
# kvm
Patch14001: 0001-Revert-x86-fred-Enable-FRED-by-default.kvm
# tgpio
Patch15001: 0001-pps-add-platform-driver-for-Intel-Timed-IO-TIO-hardw.tgpio
Patch15002: 0002-pps-generators-convert-pps_gen_tio-to-auxiliary-driv.tgpio
Patch15003: 0003-pps-add-optional-driver-controlled-polling-interface.tgpio
Patch15004: 0004-pps-store-const-pps_source_info-pointer-in-core-inst.tgpio
Patch15005: 0005-pps-clients-add-support-for-Intel-Timed-IO-PPS-clien.tgpio
Patch15006: 0001-pps-clients-pps-ldisc-fix-lifetime-of-pps_source_inf.tgpio
# ipu
Patch16001: 0001-Add-IPU6-headers.ipu
Patch16002: 0002-Add-serdes-drivers.ipu
Patch16003: 0003-Add-IPU6-PSYS-drivers.ipu
Patch16004: 0004-Add-IPU-ACPI-drivers.ipu
Patch16005: 0005-media-ipu6-Use-module-parameter-to-set-isys-freq.ipu
Patch16006: 0006-media-ipu6-Use-module-parameter-to-set-psys-freq.ipu
Patch16007: 0007-media-ipu6-Enable-ISYS-reset.ipu
Patch16008: 0008-media-ipu6-Use-vc1-DMA.ipu
Patch16009: 0009-media-ipu6-Use-DMA-sync-in-buffer_prepare-callback.ipu
Patch16010: 0010-media-i2c-Add-ar0234-camera-sensor-driver.ipu
Patch16011: 0011-media-i2c-Add-lt6911uxc-driver.ipu
Patch16012: 0012-media-lt6911-2-pads-linked-to-ipu-2-ports-for-split-mo.ipu
Patch16013: 0013-platform-x86-enable-ADL-RPL-int3472-control-logic-type.ipu
Patch16014: 0014-media-pci-The-order-of-return-buffers-should-be-FIFO.ipu
Patch16015: 0015-media-pci-Add-is_support_vc-for-IPU_ISYS_RESET.ipu
Patch16016: 0016-Modify-enable-disable-stream-in-CSI2.ipu
Patch16017: 0017-media-pci-Set-the-correct-SOF-for-different-stream.ipu
Patch16018: 0018-media-pci-support-imx390-for-6.18.3.ipu
Patch16019: 0019-i2c-media-fix-cov-issue.ipu
Patch16020: 0020-mv-ipu-acpi-module-to-linux-drivers.ipu
Patch16021: 0021-kernel-enable-VC-support-in-v4l2.ipu
Patch16022: 0022-media-pci-intel-support-PDATA-in-Kconfig-Makefile.ipu
Patch16023: 0023-media-pci-unregister-i2c-device-to-complete-ext_subdev.ipu
Patch16024: 0024-media-pci-align-params-for-non-MIPI-split-and-split-ca.ipu
Patch16025: 0025-Apply-IPU6-patch-0053-add-missing-if-for-PDATA.ipu
Patch16026: 0026-media-platform-fix-allyesconfig-build-error.ipu
Patch16027: 0027-Apply-IPU6-patch-0055-refine-PDATA-related-config.ipu
Patch16028: 0028-kernel-align-ACPI-PDATA-and-ACPI-fwnode-build-for-ECG.ipu
Patch16029: 0029-media-i2c-add-gmsl-isx031-support.ipu
Patch16030: 0030-media-ipu-invalidate-MMU-TLB-in-dma-buffers-creation.ipu
Patch16031: 0031-Add-IPU-PSYS-driver-compilation.ipu
Patch16032: 0032-Add-psys-driver-and-i2c-sensor.ipu
Patch16033: 0033-Add-ISX301-and-MAX9X-sensor.ipu
Patch16034: 0034-Modify-Kconfig-Makefile-and-ACPI-data.ipu
Patch16035: 0035-Modify-isys-and-isys-abi-driver-for-ipu7.ipu
Patch16036: 0036-Update-acpi-acpi-pdata-and-serdes-pdata.ipu
Patch16037: 0037-media-ipu-invalidate-MMU-TLB-in-dma-buffers-creation.ipu
Patch16038: 0038-media-ipu7-ignore-interrupts-when-device-is-suspended.ipu
Patch16039: 0039-media-ipu-Dma-sync-at-buffer_prepare-callback-as-DMA-i.ipu
Patch16040: 0040-media-ipu7-update-CDPHY-register-settings.ipu
Patch16041: 0041-Resolve-conflicts-after-adding-ipu7-isys-reset-code.ipu
Patch16042: 0042-Enable-Intel-IPU-ACPI-config.ipu
Patch16043: 0043-Add-patch-for-ipu7-Makefile.ipu
Patch16044: 0044-Add-Lontium-sensor-support-for-ipu7.ipu
Patch16045: 0045-Enable-Lontium-sensor-for-ipu7-in-IPU-bridge.ipu
Patch16046: 0046-Resolve-delta-between-VTG-new-changes-and-IPU6-6.18-ba.ipu
Patch16047: 0047-Enable-max9x-and-isx031-sensors.ipu
Patch16048: 0048-Update-IPU7-firmware-ABI-version-to-1.2.1.20251215_224.ipu
Patch16049: 0049-Enable-ipu8-pci-id-support.ipu
Patch16050: 0050-Add-ipu8-abi-new-version.ipu
Patch16051: 0051-Define-gpreg_stride-for-different-IPU-versions.ipu
Patch16052: 0052-Fix-lt6911gxd-enumeration-issue-on-ipu7.ipu
Patch16053: 0001-Extending-sleep-period-for-RESET-operation.ipu
Patch16054: 0002-Add-AR0234-HID.ipu
Patch16055: 0001-IPU7-release-for-iot-I2C-sensors-update.ipu
Patch16056: 0002-IPU7-release-for-iot-Update-IPU-camera-enumeration.ipu
Patch16057: 0001-media-i2c-max96724-Enable-clk-on-PHY0-for-2x4-D-PHY.ipu
# selftests
Patch17001: 0001-selftests-pps-add-common-test-framework-for-Inte.selftests
Patch17002: 0002-selftests-pps-self-tests-for-the-Intel-Timed-IO-.selftests
Patch17003: 0003-selftests-pps-self-tests-for-the-Intel-Timed-IO-.selftests
Patch17004: 0004-selftests-pps-self-tests-for-the-Intel-Timed-IO-.selftests
Patch17005: 0005-selftests-pps-skip-remaining-tests-when-Module-V.selftests
# sriov
Patch18001: 0001-vfio-i915-Add-default-handler-for-.match_token_uuid.sriov
Patch18002: 0001-drm-xe-vf-Improve-getting-clean-NULL-context.sriov
Patch18003: 0002-drm-xe-Add-PR_CTR_CTRL-THRSH-register-definitions.sriov
Patch18004: 0003-drm-xe-Add-MI_SEMAPHORE_WAIT-command-definition.sriov
Patch18005: 0001-drm-i915-vf-Remove-prelim-IOV-state-sysfs-nodes.sriov
# pmc_core
Patch19001: 0001-cpufreq-intel_pstate-Use-HYBRID_SCALING_FACTOR_AD.pmc_core
Patch19002: 0001-cpufreq-intel_pstate-Add-and-use-hybrid_get_cpu_t.pmc_core
Patch19003: 0002-cpufreq-intel_pstate-Use-correct-scaling-factor-o.pmc_core
Patch19004: 0001-platform-x86-intel-pmc-Add-Panther-Lake-R-support.pmc_core
#CVE-2026-23377
Patch20001: CVE-2026-23377.patch

#CVE-2026-23374
Patch20002: CVE-2026-23374.patch

#CVE-2026-23371
Patch20003: CVE-2026-23371.patch
Patch20004: CVE-2026-23371_2.patch

#CVE-2026-23327
Patch20005: CVE-2026-23327.patch

#CVE-2026-23459
Patch20006: CVE-2026-23459.patch

#CVE-2026-31420
Patch20007: CVE-2026-31420.patch

#CVE-2026-31560
Patch20008: CVE-2026-31560_1.patch
Patch20009: CVE-2026-31560_2.patch

#CVE-2026-31688
Patch20010: CVE-2026-31688.patch

#CVE-2026-31777
Patch20011: CVE-2026-31777.patch

#CVE-2026-43009
Patch20012: CVE-2026-43009.patch

#CVE-2026-43022
Patch20013: CVE-2026-43022.patch

#CVE-2026-43095
Patch20014: CVE-2026-43095.patch

#CVE-2026-43115
Patch20015: CVE-2026-43115_1.patch
Patch20016: CVE-2026-43115_2.patch

#CVE-2026-43299
Patch20017: CVE-2026-43299.patch

#CVE-2026-43308
Patch20018: CVE-2026-43308.patch

#CVE-2026-43344
Patch20019: CVE-2026-43344.patch

#CVE-2026-43391
Patch20020: CVE-2026-43391.patch

#CVE-2026-43414
Patch20021: CVE-2026-43414.patch

#CVE-2026-46252
Patch20022: CVE-2026-46252.patch

#CVE-2026-46244
Patch20023: CVE-2026-46244.patch

#CVE-2026-46243
Patch20024: CVE-2026-46243.patch

#CVE-2026-46216
Patch20025: CVE-2026-46216.patch

#CVE-2026-46203
Patch20026: CVE-2026-46203.patch

#CVE-2026-46153
Patch20027: CVE-2026-46153_1.patch
Patch20028: CVE-2026-46153_2.patch

#CVE-2026-46017
Patch20029: CVE-2026-46017.patch

#CVE-2026-46008
Patch20030: CVE-2026-46008.patch

#CVE-2026-45963
Patch20031: CVE-2026-45963.patch

#CVE-2026-45961
Patch20032: CVE-2026-45961.patch

#CVE-2026-45945
Patch20033: CVE-2026-45945.patch

#CVE-2025-71313
Patch20034: CVE-2025-71313.patch

#CVE-2026-46130
Patch20035: CVE-2026-46130.patch

#CVE-2026-45901
Patch20036: CVE-2026-45901.patch

#CVE-2026-45897
Patch20037: CVE-2026-45897.patch

#CVE-2025-71306
Patch20038: CVE-2025-71306_1.patch
Patch20039: CVE-2025-71306_2.patch

#CVE-2026-45850
Patch20040: CVE-2026-45850.patch

#CVE-2026-45930
Patch20041: CVE-2026-45930.patch


# End of Patch Section

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
%setup -q -n linux-6.18.33
%autosetup -p1 -n linux-6.18.33
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
* Mon Jul 13 2026 Lishan Liu <lishan.liu@intel.com> - 6.18.33-1
- Update kernel to 6.18.33-1

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
