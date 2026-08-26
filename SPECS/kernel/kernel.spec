Summary:        Linux Kernel
Name:           kernel
Version:        6.18.41
Release:        1%{?dist}
License:        GPLv2
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://www.kernel.org/pub/linux/kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.18.41.tar.gz
Source1:        config
Source3:        sha512hmac-openssl.sh
Source4:        emt-ca-20211013.pem
Source5:        cpupower
Source6:        cpupower.service

# Intel Kernel Patches
# Series file for v6.18.41 linux kernel
# 2fe596715f840 Linux 6.18.41
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
Patch01018: 0001-iommu-vt-d-cache-TPR-mappings-at-boot-to-fix-S3-r.security
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
Patch03014: 0001-powercap-intel_rapl-Remove-incorrect-CPU-check-in-PMU.rapl
Patch03015: 0002-powercap-intel_rapl-Expose-all-package-CPUs-in-PMU-cp.rapl
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
Patch05038: 0001-Revert-igc-Enable-HW-TX-Timestamp-for-AF_XDP-ZC.ethernet
Patch05039: 0002-Revert-igc-Take-care-of-DMA-timestamp-rollover.ethernet
Patch05040: 0003-Revert-igc-Add-support-for-DMA-timestamp-for-non-.ethernet
Patch05041: 0004-igc-Add-support-for-DMA-timestamp-for-non-PTP-pac.ethernet
Patch05042: 0005-igc-Take-care-of-DMA-timestamp-rollover.ethernet
Patch05043: 0006-igc-Enable-HW-TX-Timestamp-for-AF_XDP-ZC.ethernet
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
Patch08007: 0002-EDAC-igen6-Fix-memory-topology-parsing-for-Panther-La.edac
Patch08008: 0003-EDAC-igen6-Add-one-Intel-Panther-Lake-H-SoC-support.edac
Patch08009: 0004-EDAC-igen6-Fix-runtime-field-extraction-for-lts-6.18.edac
Patch08010: 0001-EDAC-igen6-Add-Intel-Starfire-SoCs-support.edac
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
Patch09056: 0001-perf-x86-intel-Add-PMU-support-for-WildcatLake.perf
Patch09057: 0002-perf-x86-intel-Add-Airmont-NP.perf
# pmt
Patch10001: 0001-platform-x86-intel-vsec-Add-support-for-Wildcat-Lake.pmt
Patch10002: 0002-platform-x86-intel-pmc-Add-DMU-GUID-to-Arrow-Lake-U-H.pmt
Patch10003: 0005-platform-x86-intel-pmc-Remove-redundant-has_die_c6-var.pmt
Patch10004: 0006-platform-x86-intel-pmc-Enable-SSRAM-support-for-Wildca.pmt
# audio
Patch11001: 0001-ASoC-Intel-sof_rt5682-Add-quirk-override-support.audio
Patch11002: 0002-ASoC-SOF-Intel-hda-Only-check-SSP-MCLK-mask-in-case-.audio
Patch11003: 0001-ASoC-SOF-Don-t-print-the-monolithic-topology-name-if.audio
Patch11004: 0002-ASoC-soc-acpi-make-some-variables-of-acpi-adr-and-li.audio
Patch11005: 0003-ASoC-soc_sdw_utils-add-name_prefix-to-asoc_sdw_codec.audio
Patch11006: 0004-ASoC-Intel-export-sof_sdw_get_tplg_files.audio
Patch11007: 0005-ASoC-soc_sdw_utils-export-asoc_sdw_get_dai_type.audio
Patch11008: 0006-ASoC-SOF-add-platform-name-into-sof_intel_dsp_desc.audio
Patch11009: 0007-ASoC-SOF-don-t-check-the-existence-of-dummy-topology.audio
Patch11010: 0008-ASoC-SOF-Intel-use-sof_sdw-as-default-SDW-machine-dr.audio
Patch11011: 0009-ASoC-sof-function-topology-lib-escalate-the-log-when.audio
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
Patch16058: 0001-media-ipu7-fix-psys-probe-failure-due-to-unregistered-.ipu
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
Patch18006: 0001-drm-i915-vf-Add-fake-watchdog-to-get-clean-NULL-cont.sriov
Patch18007: 0001-drm-xe-guc-Upgrade-GuC-PTL-BMG-and-LNL-following-01..sriov
Patch18008: 0001-vfio-i915-fix-double-free-issue-in-i915-vfio-driver.sriov
Patch18009: 0002-drm-i915-iov-fix-sriov-bounds-check-issue.sriov
# pmc_core
Patch19001: 0001-cpufreq-intel_pstate-Use-HYBRID_SCALING_FACTOR_AD.pmc_core
Patch19002: 0001-platform-x86-intel-pmc-Add-Panther-Lake-R-support.pmc_core
# camera
Patch20001: 0001-media-i2c-add-I2C_ATR-config.camera
# thermal
Patch21001: 0001-platform-x86-intel-uncore-freq-Add-support-for-rug.thermal
Patch21002: 0002-powercap-intel_rapl-Add-rugged-Panther-Lake-suppor.thermal
Patch21003: 0003-thermal-intel-intel_tcc_cooling-Add-rugged-Panther.thermal
Patch21004: 0004-tools-power-turbostat-Add-rugged-Panther-Lake-supp.thermal
#CVE-2026-23377
Patch22001: CVE-2026-23377.patch

#CVE-2026-23374
Patch22002: CVE-2026-23374.patch



#CVE-2026-23459
Patch22003: CVE-2026-23459.patch



#CVE-2026-31688
Patch22004: CVE-2026-31688.patch

#CVE-2026-31777
Patch22005: CVE-2026-31777.patch

#CVE-2026-43009
Patch22006: CVE-2026-43009.patch


#CVE-2026-43095
Patch22007: CVE-2026-43095.patch

#CVE-2026-43115
Patch22008: CVE-2026-43115_1.patch
Patch22009: CVE-2026-43115_2.patch

#CVE-2026-43299
Patch22010: CVE-2026-43299.patch

#CVE-2026-43308
Patch22011: CVE-2026-43308.patch

#CVE-2026-43344
Patch22012: CVE-2026-43344.patch

#CVE-2026-43391
Patch22013: CVE-2026-43391.patch

#CVE-2026-43414
Patch22014: CVE-2026-43414.patch






#CVE-2026-46153
Patch22015: CVE-2026-46153_1.patch
Patch22016: CVE-2026-46153_2.patch

#CVE-2026-46017
Patch22017: CVE-2026-46017.patch

#CVE-2026-46008
Patch22018: CVE-2026-46008.patch

#CVE-2026-45963
Patch22019: CVE-2026-45963.patch

#CVE-2026-45961
Patch22020: CVE-2026-45961.patch


#CVE-2025-71313
Patch22021: CVE-2025-71313.patch

#CVE-2026-46130
Patch22022: CVE-2026-46130.patch

#CVE-2026-45901
Patch22023: CVE-2026-45901.patch

#CVE-2026-45897
Patch22024: CVE-2026-45897.patch

#CVE-2025-71306
Patch22025: CVE-2025-71306_1.patch
Patch22026: CVE-2025-71306_2.patch

#CVE-2026-46302
Patch22027: CVE-2026-46302.patch

#CVE-2026-52965
Patch22028: CVE-2026-52965.patch

#CVE-2026-52949
Patch22029: CVE-2026-52949.patch

#CVE-2026-52956
Patch22030: CVE-2026-52956.patch

#CVE-2026-52960
Patch22031: CVE-2026-52960.patch

#CVE-2026-52988
Patch22032: CVE-2026-52988_1.patch
Patch22033: CVE-2026-52988_2.patch

#CVE-2026-53008
Patch22034: CVE-2026-53008.patch

#CVE-2026-53007
Patch22035: CVE-2026-53007.patch

#CVE-2026-53009
Patch22036: CVE-2026-53009.patch

#CVE-2026-53078
Patch22037: CVE-2026-53078.patch

#CVE-2026-53089
Patch22038: CVE-2026-53089.patch

#CVE-2026-53090
Patch22039: CVE-2026-53090.patch

#CVE-2026-53091
Patch22040: CVE-2026-53091.patch

#CVE-2026-53106
Patch22041: CVE-2026-53106.patch

#CVE-2026-53124
Patch22042: CVE-2026-53124.patch

#CVE-2026-63839
Patch22043: CVE-2026-63839.patch

#CVE-2026-63858
# NOTE: 2 commits already satisfied by baseline CVE-2026-52988 (CVE-2026-52988_1.patch, CVE-2026-52988_2.patch)
Patch22044: CVE-2026-63858.patch

#CVE-2026-63872
Patch22045: CVE-2026-63872.patch

#CVE-2026-63977
Patch22046: CVE-2026-63977_1.patch
Patch22047: CVE-2026-63977_2.patch

#CVE-2026-64523
Patch22048: CVE-2026-64523.patch

#CVE-2026-63978
Patch22049: CVE-2026-63978.patch

#CVE-2026-63979
Patch22050: CVE-2026-63979_1.patch
Patch22051: CVE-2026-63979_2.patch
Patch22052: CVE-2026-63979_3.patch
Patch22053: CVE-2026-63979_4.patch
Patch22054: CVE-2026-63979_5.patch

#CVE-2026-64013
Patch22055: CVE-2026-64013.patch

#CVE-2026-64017
Patch22056: CVE-2026-64017.patch

#CVE-2026-64019
Patch22057: CVE-2026-64019_1.patch
Patch22058: CVE-2026-64019_2.patch

#CVE-2026-64020
Patch22059: CVE-2026-64020.patch

#CVE-2026-64057
Patch22060: CVE-2026-64057.patch

#CVE-2026-64067
Patch22061: CVE-2026-64067.patch

#CVE-2026-64068
Patch22062: CVE-2026-64068.patch

#CVE-2026-64117
Patch22063: CVE-2026-64117_1.patch
Patch22064: CVE-2026-64117_2.patch

#CVE-2026-64160
Patch22065: CVE-2026-64160_1.patch
Patch22066: CVE-2026-64160_2.patch

#CVE-2026-64159
Patch22067: CVE-2026-64159.patch

#CVE-2026-64283
Patch22068: CVE-2026-64283_1.patch
Patch22069: CVE-2026-64283_2.patch

#CVE-2026-64388
Patch22070: CVE-2026-64388.patch

#CVE-2026-64400
Patch22071: CVE-2026-64400.patch

#CVE-2026-64561
Patch22072: CVE-2026-64561.patch

#CVE-2026-64562
Patch22073: CVE-2026-64562.patch

#CVE-2026-64564
Patch22074: CVE-2026-64564.patch

#CVE-2026-64567
Patch22075: CVE-2026-64567.patch

#CVE-2026-64568
Patch22076: CVE-2026-64568.patch

#CVE-2026-64569
Patch22077: CVE-2026-64569.patch

#CVE-2026-64570
Patch22078: CVE-2026-64570.patch

#CVE-2026-64571
Patch22079: CVE-2026-64571.patch

#CVE-2026-64572
Patch22080: CVE-2026-64572.patch

#CVE-2026-64574
Patch22081: CVE-2026-64574.patch

#CVE-2026-64575
Patch22082: CVE-2026-64575.patch

#CVE-2026-64576
Patch22083: CVE-2026-64576.patch

#CVE-2026-64579
Patch22084: CVE-2026-64579.patch

#CVE-2026-64580
Patch22085: CVE-2026-64580.patch

#CVE-2026-64581
Patch22086: CVE-2026-64581.patch

#CVE-2026-64584
Patch22087: CVE-2026-64584.patch




# End of Patch Section

%global security_hardening none
%global sha512hmac bash %{_sourcedir}/sha512hmac-openssl.sh
%global mstflintver 4.28.0
%define uname_r %{version}-%{release}
%define mariner_version 3

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
BuildRequires:  procps-ng-devel
BuildRequires:  python3-devel
BuildRequires:  sed
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
Obsoletes:      linux-dev

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
%setup -q -n linux-6.18.41
%autosetup -p1 -n linux-6.18.41
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

# hmac sign the kernel for FIPS
%{sha512hmac} %{buildroot}/boot/vmlinuz-%{uname_r} | sed -e "s,$RPM_BUILD_ROOT,," > %{buildroot}/boot/.vmlinuz-%{uname_r}.hmac
cp %{buildroot}/boot/.vmlinuz-%{uname_r}.hmac %{buildroot}/lib/modules/%{uname_r}/.vmlinuz.hmac

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
rm -rf /boot/initramfs-%{uname_r}.img
echo "initrd of kernel %{uname_r} removed" >&2

%preun tools
%systemd_preun cpupower.service

%postun
%grub2_postun

%postun tools
%systemd_postun cpupower.service

%post
/sbin/depmod -a %{uname_r}
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
* Thu Aug 20 2026 Lishan Liu <lishan.liu@intel.com> - 6.18.41-1
- Update kernel to 6.18.41-1

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

* Tue Sep 30 2025 Zhang Baoli <baoli.zhang@intel.com> -6.12.44-2
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

* Thu May 22 2025 Mun Chun Yep <mun.chun.yep@intel.com> - 6.12.23-3
- bump to sync for kernel-uki

* Thu May 15 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 6.12.23-2
- bump to sync for kernel-uki

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
- Upgrade version for Edge Microvisor Toolkit.

* Fri Jan 17 2025 Man jiahua <jiahuax.man@intel.com> - 6.6.71-1
- Update kernel to 6.6.71

* Mon Dec 30 2024 Junxiao Chang <junxiao.chang@intel.com> - 6.6.66-6
- Revert back to original packaging for GPU drivers

* Mon Dec 30 2024 Anuj Mittal <anuj.mittal@intel.com> - 6.6.66-5
- Reenable SELINUX_BOOTPARAM and DEVELOP

* Thu Dec 26 2024 Anuj Mittal <anuj.mittal@intel.com> - 6.6.66-4
- Disable CONFIG_STATIC_USERMODEHELPER to ensure autoload of modules

* Mon Dec 23 2024 Junxiao Chang <junxiao.chang@intel.com> - 6.6.66-3
- Adding i915 kernel module package

* Mon Dec 23 2024 Anuj Mittal <anuj.mittal@intel.com> - 6.6.66-2
- Update config signature

* Fri Dec 20 2024 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.6.66-1
- Update kernel to 6.6.66

* Tue Dec 12 2024 Swee Yee Fonn <swee.yee.fonn@intel.com> - 6.6.63-2
- Enable kernel to use ZSTD compression instead of GZIP.

* Thu Dec 05 2024 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.6.63-1
- Update kernel to 6.6.63

* Mon Nov 25 2024 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.6.62-2
- Update kernel to 6.6.62

* Fri Nov 22 2024 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.6.62-1
- Update kernel to 6.6.62

* Tue Oct 15 2024 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.6.53-1
- Update kernel to 6.6.53

* Thu Sep 26 2024 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.6.52-1
- Update kernel to 6.6.52

* Mon Sep 23 2024 Shi Qingdong <qingdong.shi@intel.com> - 6.6.49-1
- Update kernel to 6.6.49

* Fri Sep 06 2024 Shi Qingdong <qingdong.shi@intel.com> - 6.6.48-1
- Update kernel to 6.6.48

* Thu Aug 01 2024 Shi Qingdong <qingdong.shi@intel.com> - 6.6.43.1
- Update kernel to 6.6.43. 

* Wed Aug 07 2024 Thien Trung Vuong <tvuong@microsoft.com> - 6.6.43.1-6
- Rebuild UKI with new initrd

* Tue Aug 06 2024 Chris Co <chrco@microsoft.com> - 6.6.43.1-5
- Enable USB_TMC

* Sat Aug 03 2024 Chris Co <chrco@microsoft.com> - 6.6.43.1-4
- Enable MPTCP

* Thu Aug 01 2024 Rachel Menge <rachelmenge@microsoft.com> - 6.6.43.1-3
- Enable EVM

* Wed Jul 31 2024 Chris Co <chrco@microsoft.com> - 6.6.43.1-2
- Enable FS_VERITY
- Enable IPE LSM

* Tue Jul 30 2024 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 6.6.43.1-1
- Auto-upgrade to 6.6.43.1

* Tue Jul 30 2024 Chris Co <chrco@microsoft.com> - 6.6.39.1-2
- Enable DMI_SYSFS as module
- Enable EROFS_FS as module
- Enable DM_VERITY_VERIFY_ROOTHASH_SIG_SECONDARY_KEYRING
- Enable IMA_ARCH_POLICY
- Enable INTEGRITY_MACHINE_KEYRING

* Fri Jul 26 2024 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 6.6.39.1-1
- Auto-upgrade to 6.6.39.1

* Tue Jul 16 2024 Kelsey Steele <kelseysteele@microsoft.com> - 6.6.35.1-6
- config_aarch64: Convert selected configs to modules

* Wed Jul 10 2024 Thien Trung Vuong <tvuong@microsoft.com> - 6.6.35.1-5
- Bump release to match kernel-uki

* Fri Jul 05 2024 Gary Swalling <gaswal@microsoft.com> - 6.6.35.1-4
- Enable SECONDARY_TRUSTED_KEYRING

* Mon Jul 01 2024 Rachel Menge <rachelmenge@microsoft.com> - 6.6.35.1-3
- disable KEXEC and LEGACY_TIOCSTI

* Fri Jun 28 2024 Rachel Menge <rachelmenge@microsoft.com> - 6.6.35.1-2
- Enable LCOW boot and POD creation configs

* Tue Jun 25 2024 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 6.6.35.1-1
- Auto-upgrade to 6.6.35.1

* Wed Jun 12 2024 Dan Streetman <ddstreet@microsoft.com> - 6.6.29.1-6
- include i18n (kbd package) in UKI, to provide loadkeys binary so
  systemd-vconsole-setup works

* Tue Jun 11 2024 Juan Camposeco <juanarturoc@microsoft.com> - 6.6.29.1-5
- Add patch to enable mstflint kernel driver 4.28.0-1

* Fri May 31 2024 Thien Trung Vuong <tvuong@microsoft.com> - 6.6.29.1-4
- Enable CONFIG_AMD_MEM_ENCRYPT, CONFIG_SEV_GUEST

* Fri May 03 2024 Rachel Menge <rachelmenge@microsoft.com> - 6.6.29.1-3
- Enable CONFIG_IGC module

* Fri May 03 2024 Rachel Menge <rachelmenge@microsoft.com> - 6.6.29.1-2
- Remove XFS v4

* Wed May 01 2024 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 6.6.29.1-1
- Auto-upgrade to 6.6.29.1

* Mon Apr 29 2024 Sriram Nambakam <snambakam@microsoft.com> - 6.6.22.1-3
- Remove CONFIG_NF_CONNTRACK_PROCFS
- Remove CONFIG_TRACE_IRQFLAGS
- Remove CONFIG_TRACE_IRQFLAGS_NMI
- Remove CONFIG_IRQSOFF_TRACER
- Remove CONFIG_PREEMPTIRQ_TRACEPOINTS

* Wed Mar 27 2024 Cameron Baird <cameronbaird@microsoft.com> - 6.6.22.1-2
- Change aarch64 config to produce hv, xen, virtio as modules
- to support dracut initramfs generation on arm64 VM systems

* Mon Mar 25 2024 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 6.6.22.1-1
- Auto-upgrade to 6.6.22.1

* Tue Mar 19 2024 Dan Streetman <ddstreet@microsoft.com> - 6.6.14.1-5
- remove unnecessary 10_kernel.cfg grub config file

* Wed Mar 06 2024 Chris Gunn <chrisgun@microsoft.com> - 6.6.14.1-4
- Remove /var/lib/initramfs/kernel files.

* Fri Feb 23 2024 Chris Gunn <chrisgun@microsoft.com> - 6.6.14.1-3
- Call dracut instead of mkinitrd
- Rename initrd.img-<kver> to initramfs-<kver>.img

* Tue Feb 20 2024 Cameron Baird <cameronbaird@microsoft.com> - 6.6.14.1-2
- Remove legacy /boot/mariner.cfg
- Introduce /etc/default/grub.d/10_kernel.cfg

* Fri Feb 09 2024 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 6.6.14.1-1
- Auto-upgrade to 6.6.14.1
- Enable support for latency based cgroup IO protection
- Enable ZRAM module
- Enable Broadcom MPI3 Storage Controller Device Driver module

* Thu Feb 01 2024 Vince Perri <viperri@microsoft.com> - 6.6.12.1-3
- Config changes to converge kernel-hci config with kernel
- Remove no-vmw-sta kernel argument inherited from Photon OS

* Sat Jan 27 11:07:05 EST 2024 Dan Streetman <ddstreet@ieee.org> - 6.6.12.1-2
- use "bootstrap" systemd macros

* Fri Jan 26 2024 Rachel Menge <rachelmenge@microsoft.com> - 6.6.12.1-1
- Upgrade to 6.6.12.1

* Wed Jan 17 2024 Pawel Winogrodzki <pawelwi@microsoft.com> - 6.6.2.1-3
- Bump release to match kernel-headers.

* Thu Dec 14 2023 Rachel Menge <rachelmenge@microsoft.com> - 6.6.2.1-2
- Add cpupower.service to kernel-tools
- Enable user-based event tracing
- Enable CONFIG_BPF_LSM (Thien Trung Vuong <tvuong@microsoft.com>)
- Enable CUSE module (Juan Camposeco <juanarturoc@microsoft.com>)
- Add IOMMU configs for aarch64 (David Daney <daviddaney@microsoft.com>)
- Set selinux as default LSM
- Enable CONFIG_X86_IOPL_IOPERM

* Wed Dec 13 2023 Rachel Menge <rachelmenge@microsoft.com> - 6.6.2.1-1
- Upgrade to 6.6.2.1
- Add libtraceevent-devel to BuildRequires

* Thu Dec 07 2023 Rachel Menge <rachelmenge@microsoft.com> - 6.1.58.1-3
- Update 6.1 to have parity with ARM configs for 5.15

* Fri Dec 01 2023 Cameron Baird <cameronbaird@microsoft.com> - 6.1.58.1-2
- Remove loglevel=3, causing kernel to boot with the config-defined value,
    CONSOLE_LOGLEVEL_DEFAULT.

* Fri Oct 27 2023 Rachel Menge <rachelmenge@microsoft.com> - 6.1.58.1-1
- Upgrade to 6.1.58.1
- Remove support for imx8 dtb subpackage
- Add patch for perf_bpf_test_add_nonnull_argument
- Add cpio BuildRequires
- Ensure parity with 2.0 kernel configs

* Mon Oct 23 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.135.1-2
- Enable CONFIG_BINFMT_MISC

* Tue Oct 17 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.135.1-1
- Auto-upgrade to 5.15.135.1

* Tue Sep 26 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.133.1-1
- Auto-upgrade to 5.15.133.1
- Remove CONFIG_NET_CLS_RSVP and CONFIG_NET_CLS_RSVP6 that don't apply to the new version

* Thu Sep 21 2023 Cameron Baird <cameronbaird@microsoft.com> - 5.15.131.1-3
- Call grub2-mkconfig to regenerate configs only if the user has
    previously used grub2-mkconfig for boot configuration.

* Wed Sep 20 2023 Jon Slobodzian <joslobo@microsoft.com> - 5.15.131.1-2
- Recompile with stack-protection fixed gcc version (CVE-2023-4039)

* Fri Sep 08 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.131.1-1
- Auto-upgrade to 5.15.131.1

* Mon Aug 14 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.126.1-1
- Auto-upgrade to 5.15.126.1

* Thu Aug 10 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.125.1-2
- Enable CONFIG_BLK_DEV_NBD module

* Wed Aug 09 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.125.1-1
- Auto-upgrade to 5.15.125.1

* Tue Aug 01 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.123.1-1
- Auto-upgrade to 5.15.123.1

* Fri Jul 28 2023 Juan Camposeco <juanarturoc@microsoft.com> - 5.15.122.1-2
- Enable Mellanox DPU drivers and configurations, ARM64 only

* Wed Jul 26 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.122.1-1
- Auto-upgrade to 5.15.122.1

* Wed Jun 28 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.118.1-1
- Auto-upgrade to 5.15.118.1

* Tue Jun 20 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.116.1-2
- Enable CONFIG_IP_VS_MH module

* Tue Jun 13 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.116.1-1
- Auto-upgrade to 5.15.116.1

* Wed May 24 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.112.1-2
- Enable CONFIG_NVME_MULTIPATH with patch to set default to off

* Tue May 23 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.112.1-1
- Auto-upgrade to 5.15.112.1

* Mon May 15 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.111.1-1
- Auto-upgrade to 5.15.111.1

* Mon May 15 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.110.1-5
- Revert CONFIG_NVME_MULTIPATH

* Tue May 09 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.110.1-4
- Enable CONFIG_EDAC_SKX

* Thu May 04 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.110.1-3
- Enable HWMON support, RAS_CEC, and BLK_DEV_IO_TRACE

* Wed May 03 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.110.1-2
- Enable CONFIG_NVME_MULTIPATH

* Mon May 01 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.110.1-1
- Auto-upgrade to 5.15.110.1

* Thu Apr 27 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.107.1-4
- Enable DRM_AMDGPU module

* Wed Apr 26 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.107.1-3
- Enable Dell drivers and supporting config options
- Enable TLS

* Wed Apr 19 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.107.1-2
- Disable rpm's debuginfo defaults which regenerate build-ids

* Tue Apr 18 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.107.1-1
- Auto-upgrade to 5.15.107.1

* Tue Apr 11 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.102.1-5
- Enable CONFIG_HIST_TRIGGERS

* Wed Mar 29 2023 Kanika Nema <kanikanema@microsoft.com> - 5.15.102.1-4
- Enable nvme-tcp and nvme-rdma modules

* Wed Mar 29 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.102.1-3
- Enable CONFIG_NET_CLS_FLOWER module

* Wed Mar 22 2023 Thien Trung Vuong <tvuong@microsoft.com> - 5.15.102.1-2
- Enable Wireguard module

* Tue Mar 14 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.102.1-1
- Auto-upgrade to 5.15.102.1

* Mon Mar 06 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.98.1-1
- Auto-upgrade to 5.15.98.1

* Sat Feb 25 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.95.1-1
- Auto-upgrade to 5.15.95.1

* Wed Feb 22 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.94.1-1
- Auto-upgrade to 5.15.94.1

* Wed Feb 15 2023 Rachel Menge <rachelmenge@microsoft.com> - 5.15.92.1-3
- Install vmlinux as root executable for debuginfo

* Thu Feb 09 2023 Minghe Ren <mingheren@microsoft.com> - 5.15.92.1-2
- Disable CONFIG_INIT_ON_FREE_DEFAULT_ON

* Mon Feb 06 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.92.1-1
- Auto-upgrade to 5.15.92.1

* Wed Jan 25 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.90.1-1
- Auto-upgrade to 5.15.90.1

* Sat Jan 14 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.87.1-1
- Auto-upgrade to 5.15.87.1

* Sat Jan 07 2023 nick black <niblack@microsoft.com> - 5.15.86.1-2
- Add several missing BuildRequires (w/ Rachel Menge)

* Tue Jan 03 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.86.1-1
- Auto-upgrade to 5.15.86.1

* Fri Dec 23 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.85.1-1
- Auto-upgrade to 5.15.85.1

* Mon Dec 19 2022 Betty Lakes <bettylakes@microsoft.com> - 5.15.82.1-2
- Turn on Generic Target Core Mod

* Tue Dec 13 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.82.1-1
- Auto-upgrade to 5.15.82.1

* Wed Dec 07 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.81.1-1
- Auto-upgrade to 5.15.81.1

* Mon Dec 05 2022 Betty Lakes <bettylakes@microsoft.com> - 5.15.80.1-2
- Turn on hibernation and its dependencies

* Tue Nov 29 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.80.1-1
- Auto-upgrade to 5.15.80.1

* Fri Nov 18 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.79.1-1
- Auto-upgrade to 5.15.79.1

* Tue Nov 08 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.77.1-1
- Auto-upgrade to 5.15.77.1

* Wed Oct 26 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.15.74.1-3
- Turn on Configs for different TCP algorithms

* Mon Oct 24 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.15.74.1-2
- Package gpu kernel modules in new package kernel-drivers-gpu

* Wed Oct 19 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.74.1-1
- Upgrade to 5.15.74.1

* Fri Oct 07 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.72.1-1
- Upgrade to 5.15.72.1

* Tue Sep 27 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.70.1-1
- Upgrade to 5.15.70.1

* Mon Sep 26 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.69.1-1
- Upgrade to 5.15.69.1

* Thu Sep 22 2022 Chris Co <chrco@microsoft.com> - 5.15.67.1-4
- Enable SCSI logging facility

* Tue Sep 20 2022 Chris Co <chrco@microsoft.com> - 5.15.67.1-3
- Enable 32-bit time syscall support

* Fri Sep 16 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.15.67.1-2
- Enable CONFIG_NETFILTER_XT_TARGET_TRACE as a module

* Thu Sep 15 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.67.1-1
- Upgrade to 5.15.67.1

* Thu Sep 15 2022 Adit Jha <aditjha@microsoft.com> - 5.15.63.1-4
- Setting vfat module in kernel config to Y to be baked in

* Tue Sep 13 2022 Saul Paredes <saulparedes@microsoft.com> - 5.15.63.1-3
- Adjust crashkernel param to crash, dump memory to a file, and recover correctly

* Tue Sep 06 2022 Nikola Bojanic <t-nbojanic@microsoft.com> - 5.15.63.1-2
- Enable CRIU support: https://criu.org/Linux_kernel

* Mon Aug 29 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.63.1-1
- Upgrade to 5.15.63.1

* Wed Aug 17 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.15.60.2-1
- Upgrade to 5.15.60.2 to fix arm64 builds

* Tue Aug 02 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.15.57.1-3
- Turn on CONFIG_SECURITY_LANDLOCK

* Mon Aug 01 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.15.57.1-2
- Turn on CONFIG_BLK_DEV_ZONED

* Tue Jul 26 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.57.1-1
- Upgrade to 5.15.57.1

* Fri Jul 22 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.15.55.1-1
- Upgrade to 5.15.55.1

* Thu Jul 21 2022 Henry Li <lihl@microsoft.com> - 5.15.48.1-6
- Add turbostat and cpupower to kernel-tools

* Fri Jul 08 2022 Francis Laniel <flaniel@linux.microsoft.com> - 5.15.48.1-5
- Add back CONFIG_FTRACE_SYSCALLS to enable eBPF CO-RE syscalls tracers.
- Add CONFIG_IKHEADERS=m to enable eBPF standard tracers.

* Mon Jun 27 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 5.15.48.1-4
- Remove 'quiet' from commandline to enable verbose log

* Mon Jun 27 2022 Henry Beberman <henry.beberman@microsoft.com> - 5.15.48.1-3
- Enable CONFIG_VIRTIO_FS=m and CONFIG_FUSE_DAX=y
- Symlink /lib/modules/uname/vmlinuz to /boot/vmlinuz-uname to improve compat with scripts seeking the kernel.

* Wed Jun 22 2022 Max Brodeur-Urbas <maxbr@microsoft.com> - 5.15.48.1-2
- Enabling Vgem driver in config.

* Fri Jun 17 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 5.15.48.1-1
- Update source to 5.15.48.1

* Tue Jun 14 2022 Pawel Winogrodzki <pawelwi@microsoft.com> - 5.15.45.1-2
- Moving ".config" update and check steps into the %%prep section.

* Thu Jun 09 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.15.45.1-1
- Update source to 5.15.45.1
- Address CVE-2022-32250 with a nopatch

* Mon Jun 06 2022 Max Brodeur-Urbas <maxbr@microsoft.com> - 5.15.41.1-4
- Compiling ptp_kvm driver as a module

* Wed Jun 01 2022 Pawel Winogrodzki <pawelwi@microsoft.com> - 5.15.41.1-3
- Enabling "LIVEPATCH" config option.

* Thu May 26 2022 Minghe Ren <mingheren@microsoft.com> - 5.15.41.1-2
- Disable SMACK kernel configuration

* Tue May 24 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.15.41.1-1
- Update source to 5.15.41.1
- Nopatch CVE-2020-35501, CVE-2022-28893, CVE-2022-29581

* Mon May 23 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 5.15.37.1-3
- Fix configs to bring down initrd boot time

* Mon May 16 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 5.15.37.1-2
- Fix cdrom, hyperv-mouse, kexec and crash-on-demand config in aarch64

* Mon May 09 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 5.15.37.1-1
- Update source to 5.15.37.1
- Nopatch CVE-2021-4095, CVE-2022-0500, CVE-2022-0998, CVE-2022-28796, CVE-2022-29582,
    CVE-2022-1048, CVE-2022-1195, CVE-2022-1353, CVE-2022-29968, CVE-2022-1015
- Enable IFB config

* Tue Apr 19 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.15.34.1-1
- Update source to 5.15.34.1
- Clean up nopatches in Patch list, no longer needed for CVE automation
- Nopatch CVE-2022-28390, CVE-2022-28389, CVE-2022-28388, CVE-2022-28356, CVE-2022-0435,
    CVE-2021-4202, CVE-2022-27950, CVE-2022-0433, CVE-2022-0494, CVE-2022-0330, CVE-2022-0854,
    CVE-2021-4197, CVE-2022-29156

* Tue Apr 19 2022 Max Brodeur-Urbas <maxbr@microsoft.com> - 5.15.32.1-3
- Remove kernel lockdown config from grub envblock

* Tue Apr 12 2022 Andrew Phelps <anphel@microsoft.com> - 5.15.32.1-2
- Remove trace symlink from _bindir
- Exclude files and directories under the debug folder from kernel and kernel-tools packages
- Remove BR for xerces-c-devel

* Fri Apr 08 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 5.15.32.1-1
- Update source to 5.15.32.1
- Address CVES: 2022-0516, 2022-26878, 2022-27223, 2022-24958, 2022-0742,
  2022-1011, 2022-26490, 2021-4002
- Enable MANA driver config
- Address CVEs 2022-0995, 2022-1055, 2022-27666

* Tue Apr 05 2022 Henry Li <lihl@microsoft.com> - 5.15.26.1-4
- Add Dell devices support

* Mon Mar 28 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.15.26.1-3
- Remove hardcoded mariner.pem from configs and instead insert during
  the build phase

* Mon Mar 14 2022 Vince Perri <viperri@microsoft.com> - 5.15.26.1-2
- Add support for compressed firmware

* Tue Mar 08 2022 cameronbaird <cameronbaird@microsoft.com> - 5.15.26.1-1
- Update source to 5.15.26.1
- Address CVES: 2022-0617, 2022-25375, 2022-25258, 2021-4090, 2022-25265,
  2021-45402, 2022-0382, 2022-0185, 2021-44879, 2022-24959, 2022-0264,
  2022-24448, 2022-24122, 2021-20194, 2022-0847, 1999-0524, 2008-4609,
  2010-0298, 2010-4563, 2011-0640, 2022-0492, 2021-3743, 2022-26966

* Mon Mar 07 2022 George Mileka <gmileka@microsoft.com> - 5.15.18.1-5
- Enabled vfio noiommu.

* Fri Feb 25 2022 Henry Li <lihl@microsoft.com> - 5.15.18.1-4
- Enable CONFIG_DEVMEM, CONFIG_STRICT_DEVMEM and CONFIG_IO_STRICT_DEVMEM

* Thu Feb 24 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.15.18.1-3
- CONFIG_BPF_UNPRIV_DEFAULT_OFF=y

* Thu Feb 24 2022 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.15.18.1-2
- Add usbip required kernel configs CONFIG_USBIP_CORE CONFIG_USBIP_VHCI_HCD

* Mon Feb 07 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.15.18.1-1
- Update source to 5.15.18.1
- Address CVE-2010-0309, CVE-2018-1000026, CVE-2018-16880, CVE-2019-3016,
  CVE-2019-3819, CVE-2019-3887, CVE-2020-25672, CVE-2021-3564, CVE-2021-45095,
  CVE-2021-45469, CVE-2021-45480

* Thu Feb 03 2022 Henry Li <lihl@microsoft.com> - 5.15.2.1-5
- Enable CONFIG_X86_SGX and CONFIG_X86_SGX_KVM

* Wed Feb 02 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.15.2.1-4
- Add libperf-jvmti.so to tools package

* Thu Jan 27 2022 Daniel Mihai <dmihai@microsoft.com> - 5.15.2.1-3
- Enable kdb frontend for kgdb

* Sun Jan 23 2022 Chris Co <chrco@microsoft.com> - 5.15.2.1-2
- Rotate Mariner cert

* Thu Jan 06 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.15.2.1-1
- Update source to 5.15.2.1

* Tue Jan 04 2022 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.10.78.1-3
- Add provides exclude for debug build-id for aarch64 to generate debuginfo rpm
- Fix missing brackets for __os_install_post.

* Tue Dec 28 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.10.78.1-2
- Enable CONFIG_COMPAT kernel configs

* Tue Nov 23 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.78.1-1
- Update source to 5.10.78.1
- Address CVE-2021-43267, CVE-2021-42739, CVE-2021-42327, CVE-2021-43389
- Add patch to fix SPDX-License-Identifier in headers

* Mon Nov 15 2021 Thomas Crain <thcrain@microsoft.com> - 5.10.74.1-4
- Add python3-perf subpackage and add python3-devel to build-time requirements
- Exclude accessibility modules from main package to avoid subpackage conflict
- Remove redundant License tag from bpftool subpackage

* Thu Nov 04 2021 Andrew Phelps <anphel@microsoft.com> - 5.10.74.1-3
- Update configs for gcc 11.2.0 and binutils 2.37 updates

* Tue Oct 26 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.74.1-2
- Update configs for eBPF support
- Add dwarves Build-requires

* Tue Oct 19 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.74.1-1
- Update source to 5.10.74.1
- Address CVE-2021-41864, CVE-2021-42252
- License verified

* Thu Oct 07 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.69.1-1
- Update source to 5.10.69.1
- Address CVE-2021-38300, CVE-2021-41073, CVE-2021-3653, CVE-2021-42008

* Wed Sep 22 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.64.1-2
- Enable CONFIG_NET_VRF
- Add vrf to drivers argument for dracut

* Mon Sep 20 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.64.1-1
- Update source to 5.10.64.1

* Fri Sep 17 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.60.1-1
- Remove cn from dracut drivers argument
- Update source to 5.10.60.1
- Address CVE-2021-38166, CVE-2021-38205, CVE-2021-3573
  CVE-2021-37576, CVE-2021-34556, CVE-2021-35477, CVE-2021-28691,
  CVE-2021-3564, CVE-2020-25639, CVE-2021-29657, CVE-2021-38199,
  CVE-2021-38201, CVE-2021-38202, CVE-2021-38207, CVE-2021-38204,
  CVE-2021-38206, CVE-2021-38208, CVE-2021-38200, CVE-2021-38203,
  CVE-2021-38160, CVE-2021-3679, CVE-2021-38198, CVE-2021-38209,
  CVE-2021-3655
- Add patch to fix VDSO in HyperV

* Thu Sep 09 2021 Muhammad Falak <mwani@microsoft.com> - 5.10.52.1-2
- Export `bpftool` subpackage

* Tue Jul 20 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.52.1-1
- Update source to 5.10.52.1
- Address CVE-2021-35039, CVE-2021-33909

* Mon Jul 19 2021 Chris Co <chrco@microsoft.com> - 5.10.47.1-2
- Enable CONFIG_CONNECTOR and CONFIG_PROC_EVENTS

* Tue Jul 06 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.47.1-1
- Update source to 5.10.47.1
- Address CVE-2021-34693, CVE-2021-33624

* Wed Jun 30 2021 Chris Co <chrco@microsoft.com> - 5.10.42.1-4
- Enable legacy mcelog config

* Tue Jun 22 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.10.42.1-3
- Enable CONFIG_IOSCHED_BFQ and CONFIG_BFQ_GROUP_IOSCHED configs

* Wed Jun 16 2021 Chris Co <chrco@microsoft.com> - 5.10.42.1-2
- Enable CONFIG_CROSS_MEMORY_ATTACH

* Tue Jun 08 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.42.1-1
- Update source to 5.10.42.1
- Address CVE-2021-33200

* Thu Jun 03 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.37.1-2
- Address CVE-2020-25672

* Fri May 28 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.37.1-1
- Update source to 5.10.37.1
- Address CVE-2021-23134, CVE-2021-29155, CVE-2021-31829, CVE-2021-31916,
  CVE-2021-32399, CVE-2021-33033, CVE-2021-33034, CVE-2021-3483
  CVE-2021-3501, CVE-2021-3506

* Thu May 27 2021 Chris Co <chrco@microsoft.com> - 5.10.32.1-7
- Set lockdown=integrity by default

* Wed May 26 2021 Chris Co <chrco@microsoft.com> - 5.10.32.1-6
- Add Mariner cert into the trusted kernel keyring

* Tue May 25 2021 Daniel Mihai <dmihai@microsoft.com> - 5.10.32.1-5
- Enable kernel debugger

* Thu May 20 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.10.32.1-4
- Bump release number to match kernel-signed update

* Mon May 17 2021 Andrew Phelps <anphel@microsoft.com> - 5.10.32.1-3
- Update CONFIG_LD_VERSION for binutils 2.36.1
- Remove build-id match check

* Thu May 13 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.32.1-2
- Add CONFIG_AS_HAS_LSE_ATOMICS=y

* Mon May 03 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.32.1-1
- Update source to 5.10.32.1
- Address CVE-2021-23133, CVE-2021-29154, CVE-2021-30178

* Thu Apr 22 2021 Chris Co <chrco@microsoft.com> - 5.10.28.1-4
- Disable CONFIG_EFI_DISABLE_PCI_DMA. It can cause boot issues on some hardware.

* Mon Apr 19 2021 Chris Co <chrco@microsoft.com> - 5.10.28.1-3
- Bump release number to match kernel-signed update

* Thu Apr 15 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.28.1-2
- Address CVE-2021-29648

* Thu Apr 08 2021 Chris Co <chrco@microsoft.com> - 5.10.28.1-1
- Update source to 5.10.28.1
- Update uname_r define to match the new value derived from the source
- Address CVE-2020-27170, CVE-2020-27171, CVE-2021-28375, CVE-2021-28660,
  CVE-2021-28950, CVE-2021-28951, CVE-2021-28952, CVE-2021-28971,
  CVE-2021-28972, CVE-2021-29266, CVE-2021-28964, CVE-2020-35508,
  CVE-2020-16120, CVE-2021-29264, CVE-2021-29265, CVE-2021-29646,
  CVE-2021-29647, CVE-2021-29649, CVE-2021-29650, CVE-2021-30002

* Fri Mar 26 2021 Daniel Mihai <dmihai@microsoft.com> - 5.10.21.1-4
- Enable CONFIG_CRYPTO_DRBG_HASH, CONFIG_CRYPTO_DRBG_CTR

* Thu Mar 18 2021 Chris Co <chrco@microsoft.com> - 5.10.21.1-3
- Address CVE-2021-27365, CVE-2021-27364, CVE-2021-27363
- Enable CONFIG_FANOTIFY_ACCESS_PERMISSIONS

* Wed Mar 17 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.10.21.1-2
- Disable QAT kernel configs

* Thu Mar 11 2021 Chris Co <chrco@microsoft.com> - 5.10.21.1-1
- Update source to 5.10.21.1
- Add virtio drivers to be installed into initrd
- Address CVE-2021-26930, CVE-2020-35499, CVE-2021-26931, CVE-2021-26932

* Fri Mar 05 2021 Chris Co <chrco@microsoft.com> - 5.10.13.1-4
- Enable kernel lockdown config

* Thu Mar 04 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.10.13.1-3
- Add configs for CONFIG_BNXT bnxt_en and MSR drivers

* Mon Feb 22 2021 Thomas Crain <thcrain@microsoft.com> - 5.10.13.1-2
- Add configs for speakup and uinput drivers
- Add kernel-drivers-accessibility subpackage

* Thu Feb 18 2021 Chris Co <chrco@microsoft.com> - 5.10.13.1-1
- Update source to 5.10.13.1
- Remove patch to publish efi tpm event log on ARM. Present in updated source.
- Remove patch for arm64 hyperv support. Present in updated source.
- Account for new module.lds location on aarch64
- Remove CONFIG_GCC_PLUGIN_RANDSTRUCT
- Add CONFIG_SCSI_SMARTPQI=y

* Thu Feb 11 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.91-5
- Add configs to enable tcrypt in FIPS mode

* Tue Feb 09 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.91-4
- Use OpenSSL to perform HMAC calc

* Thu Jan 28 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.91-3
- Add configs for userspace crypto support
- HMAC calc the kernel for FIPS

* Wed Jan 27 2021 Daniel McIlvaney <damcilva@microsoft.com> - 5.4.91-2
- Enable dm-verity boot support with FEC

* Wed Jan 20 2021 Chris Co <chrco@microsoft.com> - 5.4.91-1
- Update source to 5.4.91
- Address CVE-2020-29569, CVE-2020-28374, CVE-2020-36158
- Remove patch to fix GUI installer crash. Fixed in updated source.

* Tue Jan 12 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.4.83-4
- Add imx8mq support

* Sat Jan 09 2021 Andrew Phelps <anphel@microsoft.com> - 5.4.83-3
- Add patch to fix GUI installer crash

* Mon Dec 28 2020 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.83-2
- Address CVE-2020-27777

* Tue Dec 15 2020 Henry Beberman <henry.beberman@microsoft.com> - 5.4.83-1
- Update source to 5.4.83
- Address CVE-2020-14351, CVE-2020-14381, CVE-2020-25656, CVE-2020-25704,
  CVE-2020-29534, CVE-2020-29660, CVE-2020-29661

* Fri Dec 04 2020 Chris Co <chrco@microsoft.com> - 5.4.81-1
- Update source to 5.4.81
- Remove patch for kexec in HyperV. Integrated in 5.4.81.
- Address CVE-2020-25705, CVE-2020-15436, CVE-2020-28974, CVE-2020-29368,
  CVE-2020-29369, CVE-2020-29370, CVE-2020-29374, CVE-2020-29373, CVE-2020-28915,
  CVE-2020-28941, CVE-2020-27675, CVE-2020-15437, CVE-2020-29371, CVE-2020-29372,
  CVE-2020-27194, CVE-2020-27152

* Wed Nov 25 2020 Chris Co <chrco@microsoft.com> - 5.4.72-5
- Add patch to publish efi tpm event log on ARM

* Mon Nov 23 2020 Chris Co <chrco@microsoft.com> - 5.4.72-4
- Apply patch to fix kexec in HyperV

* Mon Nov 16 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.72-3
- Disable kernel config SLUB_DEBUG_ON due to tcp throughput perf impact

* Tue Nov 10 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.72-2
- Enable kernel configs for Arm64 HyperV, Ampere and Cavium SoCs support

* Mon Oct 26 2020 Chris Co <chrco@microsoft.com> - 5.4.72-1
- Update source to 5.4.72
- Remove patch to support CometLake e1000e ethernet. Integrated in 5.4.72.
- Add license file
- Lint spec
- Address CVE-2018-1000026, CVE-2018-16880, CVE-2020-12464, CVE-2020-12465,
  CVE-2020-12659, CVE-2020-15780, CVE-2020-14356, CVE-2020-14386, CVE-2020-25645,
  CVE-2020-25643, CVE-2020-25211, CVE-2020-25212, CVE-2008-4609, CVE-2020-14331,
  CVE-2010-0298, CVE-2020-10690, CVE-2020-25285, CVE-2020-10711, CVE-2019-3887,
  CVE-2020-14390, CVE-2019-19338, CVE-2019-20810, CVE-2020-10766, CVE-2020-10767,
  CVE-2020-10768, CVE-2020-10781, CVE-2020-12768, CVE-2020-14314, CVE-2020-14385,
  CVE-2020-25641, CVE-2020-26088, CVE-2020-10942, CVE-2020-12826, CVE-2019-3016,
  CVE-2019-3819, CVE-2020-16166, CVE-2020-11608, CVE-2020-11609, CVE-2020-25284,
  CVE-2020-12888, CVE-2017-8244, CVE-2017-8245, CVE-2017-8246, CVE-2009-4484,
  CVE-2015-5738, CVE-2007-4998, CVE-2010-0309, CVE-2011-0640, CVE-2020-12656,
  CVE-2011-2519, CVE-1999-0656, CVE-2010-4563, CVE-2019-20794, CVE-1999-0524

* Fri Oct 16 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.51-11
- Enable QAT kernel configs

* Fri Oct 02 2020 Chris Co <chrco@microsoft.com> - 5.4.51-10
- Address CVE-2020-10757, CVE-2020-12653, CVE-2020-12657, CVE-2010-3865,
  CVE-2020-11668, CVE-2020-12654, CVE-2020-24394, CVE-2020-8428

* Fri Oct 02 2020 Chris Co <chrco@microsoft.com> - 5.4.51-9
- Fix aarch64 build error

* Wed Sep 30 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.51-8
- Update postun script to deal with removal in case of another installed kernel.

* Fri Sep 25 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.51-7
- Enable Mellanox kernel configs

* Wed Sep 23 2020 Daniel McIlvaney <damcilva@microsoft.com> - 5.4.51-6
- Enable CONFIG_IMA (measurement only) and associated configs

* Thu Sep 03 2020 Daniel McIlvaney <damcilva@microsoft.com> - 5.4.51-5
- Add code to check for missing config flags in the checked in configs

* Thu Sep 03 2020 Chris Co <chrco@microsoft.com> - 5.4.51-4
- Apply additional kernel hardening configs

* Thu Sep 03 2020 Chris Co <chrco@microsoft.com> - 5.4.51-3
- Bump release number due to kernel-signed-<arch> package update
- Minor aarch64 config and changelog cleanup

* Tue Sep 01 2020 Chris Co <chrco@microsoft.com> - 5.4.51-2
- Update source hash

* Wed Aug 19 2020 Chris Co <chrco@microsoft.com> - 5.4.51-1
- Update source to 5.4.51
- Enable DXGKRNL config
- Address CVE-2020-11494, CVE-2020-11565, CVE-2020-12655, CVE-2020-12771,
  CVE-2020-13974, CVE-2020-15393, CVE-2020-8647, CVE-2020-8648, CVE-2020-8649,
  CVE-2020-9383, CVE-2020-11725

* Wed Aug 19 2020 Chris Co <chrco@microsoft.com> - 5.4.42-12
- Remove the signed package depends

* Tue Aug 18 2020 Chris Co <chrco@microsoft.com> - 5.4.42-11
- Remove signed subpackage

* Mon Aug 17 2020 Chris Co <chrco@microsoft.com> - 5.4.42-10
- Enable BPF, PC104, userfaultfd, SLUB sysfs, SMC, XDP sockets monitoring configs

* Fri Aug 07 2020 Mateusz Malisz <mamalisz@microsoft.com> - 5.4.42-9
- Add crashkernel=128M to the kernel cmdline
- Update config to support kexec and kexec_file_load

* Tue Aug 04 2020 Pawel Winogrodzki <pawelwi@microsoft.com> - 5.4.42-8
- Updating "KBUILD_BUILD_VERSION" and "KBUILD_BUILD_HOST" with correct
  distribution name.

* Wed Jul 22 2020 Chris Co <chrco@microsoft.com> - 5.4.42-7
- Address CVE-2020-8992, CVE-2020-12770, CVE-2020-13143, CVE-2020-11884

* Fri Jul 17 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.42-6
- Enable CONFIG_MLX5_CORE_IPOIB and CONFIG_INFINIBAND_IPOIB config flags

* Fri Jul 17 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.42-5
- Adding XDP config flag

* Thu Jul 09 2020 Anand Muthurajan <anandm@microsoft.com> - 5.4.42-4
- Enable CONFIG_QED, CONFIG_QEDE, CONFIG_QED_SRIOV and CONFIG_QEDE_VXLAN flags

* Wed Jun 24 2020 Chris Co <chrco@microsoft.com> - 5.4.42-3
- Regenerate input config files

* Fri Jun 19 2020 Chris Co <chrco@microsoft.com> - 5.4.42-2
- Add kernel-secure subpackage and macros for adding offline signed kernels

* Fri Jun 12 2020 Chris Co <chrco@microsoft.com> - 5.4.42-1
- Update source to 5.4.42

* Thu Jun 11 2020 Chris Co <chrco@microsoft.com> - 5.4.23-17
- Enable PAGE_POISONING configs
- Disable PROC_KCORE config
- Enable RANDOM_TRUST_CPU config for x86_64

* Fri Jun 05 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.23-16
- Adding BPF config flags

* Thu Jun 04 2020 Chris Co <chrco@microsoft.com> - 5.4.23-15
- Add config support for USB video class devices

* Wed Jun 03 2020 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.23-14
- Add CONFIG_CRYPTO_XTS=y to config.

* Wed Jun 03 2020 Chris Co <chrco@microsoft.com> - 5.4.23-13
- Add patch to support CometLake e1000e ethernet
- Remove drivers-gpu subpackage
- Inline the initramfs trigger and postun source files
- Remove rpi3 dtb and ls1012 dtb subpackages

* Wed May 27 2020 Chris Co <chrco@microsoft.com> - 5.4.23-12
- Update arm64 security configs
- Disable devmem in x86_64 config

* Tue May 26 2020 Daniel Mihai <dmihai@microsoft.com> - 5.4.23-11
- Disabled Reliable Datagram Sockets protocol (CONFIG_RDS).

* Fri May 22 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.23-10
- Change /boot directory permissions to 600.

* Thu May 21 2020 Chris Co <chrco@microsoft.com> - 5.4.23-9
- Update x86_64 security configs

* Wed May 20 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.23-8
- Adding InfiniBand config flags

* Mon May 11 2020 Anand Muthurajan <anandm@microsoft.com> - 5.4.23-7
- Adding PPP config flags

* Tue Apr 28 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.23-6
- Renaming Linux-PAM to pam

* Tue Apr 28 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.23-5
- Renaming linux to kernel

* Tue Apr 14 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.23-4
- Remove linux-aws and linux-esx references.
- Remove kat_build usage.
- Remove ENA module.

* Fri Apr 10 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.23-3
- Remove xml-security-c dependency.

* Wed Apr 08 2020 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.23-2
- Remove toybox and only use coreutils for requires.

* Tue Dec 10 2019 Chris Co <chrco@microsoft.com> - 5.4.23-1
- Update to Microsoft Linux Kernel 5.4.23
- Remove patches
- Update ENA module to 2.1.2 to work with Linux 5.4.23
- Remove xr module
- Remove Xen tmem module from dracut module list to fix initramfs creation
- Add patch to fix missing trans_pgd header in aarch64 build

* Fri Oct 11 2019 Henry Beberman <hebeberm@microsoft.com> - 4.19.52-8
- Enable Hyper-V TPM in config

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> - 4.19.52-7
- Initial CBL-Mariner import from Photon (license: Apache2).

* Thu Jul 25 2019 Keerthana K <keerthanak@vmware.com> - 4.19.52-6
- Fix postun scriplet.

* Thu Jul 11 2019 Keerthana K <keerthanak@vmware.com> - 4.19.52-5
- Enable kernel configs necessary for BPF Compiler Collection (BCC).

* Wed Jul 10 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.52-4
- Deprecate linux-aws-tools in favor of linux-tools.

* Tue Jul 02 2019 Alexey Makhalov <amakhalov@vmware.com> - 4.19.52-3
- Fix 9p vsock 16bit port issue.

* Thu Jun 20 2019 Tapas Kundu <tkundu@vmware.com> - 4.19.52-2
- Enabled CONFIG_I2C_CHARDEV to support lm-sensors

* Mon Jun 17 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.52-1
- Update to version 4.19.52
- Fix CVE-2019-12456, CVE-2019-12379, CVE-2019-12380, CVE-2019-12381,
- CVE-2019-12382, CVE-2019-12378, CVE-2019-12455

* Tue May 28 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.40-3
- Change default I/O scheduler to 'deadline' to fix performance issue.

* Tue May 14 2019 Keerthana K <keerthanak@vmware.com> - 4.19.40-2
- Fix to parse through /boot folder and update symlink (/boot/photon.cfg) if
- mulitple kernels are installed and current linux kernel is removed.

* Tue May 07 2019 Ajay Kaher <akaher@vmware.com> - 4.19.40-1
- Update to version 4.19.40

* Thu Apr 11 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.32-3
- Update config_aarch64 to fix ARM64 build.

* Fri Mar 29 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.32-2
- Fix CVE-2019-10125

* Wed Mar 27 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.32-1
- Update to version 4.19.32

* Thu Mar 14 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.29-1
- Update to version 4.19.29

* Tue Mar 05 2019 Ajay Kaher <akaher@vmware.com> - 4.19.26-1
- Update to version 4.19.26

* Thu Feb 21 2019 Him Kalyan Bordoloi <bordoloih@vmware.com> - 4.19.15-3
- Fix CVE-2019-8912

* Thu Jan 24 2019 Alexey Makhalov <amakhalov@vmware.com> - 4.19.15-2
- Add WiFi (ath10k), sensors (i2c,spi), usb support for NXP LS1012A board.

* Tue Jan 15 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.15-1
- Update to version 4.19.15

* Fri Jan 11 2019 Srinidhi Rao <srinidhir@vmware.com> - 4.19.6-7
- Add Network support for NXP LS1012A board.

* Wed Jan 09 2019 Ankit Jain <ankitja@vmware.com> - 4.19.6-6
- Enable following for x86_64 and aarch64:
-  Enable Kernel Address Space Layout Randomization.
-  Enable CONFIG_SECURITY_NETWORK_XFRM

* Fri Jan 04 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.6-5
- Enable AppArmor by default.

* Wed Jan 02 2019 Alexey Makhalov <amakhalov@vmware.com> - 4.19.6-4
- .config: added Compulab fitlet2 device drivers
- .config_aarch64: added gpio sysfs support
- renamed -sound to -drivers-sound

* Tue Jan 01 2019 Ajay Kaher <akaher@vmware.com> - 4.19.6-3
- .config: Enable CONFIG_PCI_HYPERV driver

* Wed Dec 19 2018 Srinidhi Rao <srinidhir@vmware.com> - 4.19.6-2
- Add NXP LS1012A support.

* Mon Dec 10 2018 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.6-1
- Update to version 4.19.6

* Fri Dec 07 2018 Alexey Makhalov <amakhalov@vmware.com> - 4.19.1-3
- .config: added qmi wwan module

* Mon Nov 12 2018 Ajay Kaher <akaher@vmware.com> - 4.19.1-2
- Fix config_aarch64 for 4.19.1

* Mon Nov 05 2018 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.1-1
- Update to version 4.19.1

* Tue Oct 16 2018 Him Kalyan Bordoloi <bordoloih@vmware.com> - 4.18.9-5
- Change in config to enable drivers for zigbee and GPS

* Fri Oct 12 2018 Ajay Kaher <akaher@vmware.com> - 4.18.9-4
- Enable LAN78xx for aarch64 rpi3

* Fri Oct 5 2018 Ajay Kaher <akaher@vmware.com> - 4.18.9-3
- Fix config_aarch64 for 4.18.9
- Add module.lds for aarch64

* Wed Oct 03 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.18.9-2
- Use updated steal time accounting patch.
- .config: Enable CONFIG_CPU_ISOLATION and a few networking options
- that got accidentally dropped in the last update.

* Mon Oct 1 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.18.9-1
- Update to version 4.18.9

* Tue Sep 25 2018 Ajay Kaher <akaher@vmware.com> - 4.14.67-2
- Build hang (at make oldconfig) fix in config_aarch64

* Wed Sep 19 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.14.67-1
- Update to version 4.14.67

* Tue Sep 18 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.14.54-7
- Add rdrand-based RNG driver to enhance kernel entropy.

* Sun Sep 02 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.14.54-6
- Add full retpoline support by building with retpoline-enabled gcc.

* Thu Aug 30 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.14.54-5
- Apply out-of-tree patches needed for AppArmor.

* Wed Aug 22 2018 Alexey Makhalov <amakhalov@vmware.com> - 4.14.54-4
- Fix overflow kernel panic in rsi driver.
- .config: enable BT stack, enable GPIO sysfs.
- Add Exar USB serial driver.

* Fri Aug 17 2018 Ajay Kaher <akaher@vmware.com> - 4.14.54-3
- Enabled USB PCI in config_aarch64
- Build hang (at make oldconfig) fix in config_aarch64

* Thu Jul 19 2018 Alexey Makhalov <amakhalov@vmware.com> - 4.14.54-2
- .config: usb_serial_pl2303=m,wlan=y,can=m,gpio=y,pinctrl=y,iio=m

* Mon Jul 09 2018 Him Kalyan Bordoloi <bordoloih@vmware.com> - 4.14.54-1
- Update to version 4.14.54

* Fri Jan 26 2018 Alexey Makhalov <amakhalov@vmware.com> - 4.14.8-2
- Added vchiq entry to rpi3 dts
- Added dtb-rpi3 subpackage

* Fri Dec 22 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.14.8-1
- Version update

* Wed Dec 13 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.66-4
- KAT build support

* Thu Dec 07 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.66-3
- Aarch64 support

* Tue Dec 05 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.66-2
- Sign and compress modules after stripping. fips=1 requires signed modules

* Mon Dec 04 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.66-1
- Version update

* Tue Nov 21 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.64-1
- Version update

* Mon Nov 06 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.60-1
- Version update

* Wed Oct 11 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.53-3
- Add patch "KVM: Don't accept obviously wrong gsi values via
    KVM_IRQFD" to fix CVE-2017-1000252.

* Tue Oct 10 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.53-2
- Build hang (at make oldconfig) fix.

* Thu Oct 05 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.53-1
- Version update

* Mon Oct 02 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.52-3
- Allow privileged CLONE_NEWUSER from nested user namespaces.

* Mon Oct 02 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.52-2
- Fix CVE-2017-11472 (ACPICA: Namespace: fix operand cache leak)

* Mon Oct 02 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.52-1
- Version update

* Mon Sep 18 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.47-2
- Requires coreutils or toybox

* Mon Sep 04 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.47-1
- Fix CVE-2017-11600

* Tue Aug 22 2017 Anish Swaminathan <anishs@vmware.com> - 4.9.43-2
- Add missing xen block drivers

* Mon Aug 14 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.43-1
- Version update
- [feature] new sysctl option unprivileged_userns_clone

* Wed Aug 09 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.41-2
- Fix CVE-2017-7542
- [bugfix] Added ccm,gcm,ghash,lzo crypto modules to avoid
    panic on modprobe tcrypt

* Mon Aug 07 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.41-1
- Version update

* Fri Aug 04 2017 Bo Gan <ganb@vmware.com> - 4.9.38-6
- Fix initramfs triggers

* Tue Aug 01 2017 Anish Swaminathan <anishs@vmware.com> - 4.9.38-5
- Allow some algorithms in FIPS mode
- Reverts 284a0f6e87b0721e1be8bca419893902d9cf577a and backports
- bcf741cb779283081db47853264cc94854e7ad83 in the kernel tree
- Enable additional NF features

* Fri Jul 21 2017 Anish Swaminathan <anishs@vmware.com> - 4.9.38-4
- Add patches in Hyperv codebase

* Fri Jul 21 2017 Anish Swaminathan <anishs@vmware.com> - 4.9.38-3
- Add missing hyperv drivers

* Thu Jul 20 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.38-2
- Disable scheduler beef up patch

* Tue Jul 18 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.38-1
- Fix CVE-2017-11176 and CVE-2017-10911

* Mon Jul 03 2017 Xiaolin Li <xiaolinl@vmware.com> - 4.9.34-3
- Add libdnet-devel, kmod-devel and libmspack-devel to BuildRequires

* Thu Jun 29 2017 Divya Thaluru <dthaluru@vmware.com> - 4.9.34-2
- Added obsolete for deprecated linux-dev package

* Wed Jun 28 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.34-1
- [feature] 9P FS security support
- [feature] DM Delay target support
- Fix CVE-2017-1000364 ("stack clash") and CVE-2017-9605

* Thu Jun 8 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.31-1
- Fix CVE-2017-8890, CVE-2017-9074, CVE-2017-9075, CVE-2017-9076
    CVE-2017-9077 and CVE-2017-9242
- [feature] IPV6 netfilter NAT table support

* Fri May 26 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.30-1
- Added ENA driver for AMI
- Fix CVE-2017-7487 and CVE-2017-9059

* Wed May 17 2017 Vinay Kulkarni <kulkarniv@vmware.com> - 4.9.28-2
- Enable IPVLAN module.

* Tue May 16 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.28-1
- Version update

* Wed May 10 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.27-1
- Version update

* Sun May 7 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.26-1
- Version update
- Removed version suffix from config file name

* Thu Apr 27 2017 Bo Gan <ganb@vmware.com> - 4.9.24-2
- Support dynamic initrd generation

* Tue Apr 25 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.24-1
- Fix CVE-2017-6874 and CVE-2017-7618.
- Fix audit-devel BuildRequires.
- .config: build nvme and nvme-core in kernel.

* Mon Mar 6 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.13-2
- .config: NSX requirements for crypto and netfilter

* Tue Feb 28 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.13-1
- Update to linux-4.9.13 to fix CVE-2017-5986 and CVE-2017-6074

* Thu Feb 09 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.9-1
- Update to linux-4.9.9 to fix CVE-2016-10153, CVE-2017-5546,
    CVE-2017-5547, CVE-2017-5548 and CVE-2017-5576.
- .config: added CRYPTO_FIPS support.

* Tue Jan 10 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.2-1
- Update to linux-4.9.2 to fix CVE-2016-10088
- Move linux-tools.spec to linux.spec as -tools subpackage

* Mon Dec 19 2016 Xiaolin Li <xiaolinl@vmware.com> - 4.9.0-2
- BuildRequires Linux-PAM-devel

* Mon Dec 12 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.9.0-1
- Update to linux-4.9.0
- Add paravirt stolen time accounting feature (from linux-esx),
    but disable it by default (no-vmw-sta cmdline parameter)

* Thu Dec  8 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.35-3
- net-packet-fix-race-condition-in-packet_set_ring.patch
    to fix CVE-2016-8655

* Wed Nov 30 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.35-2
- Expand `uname -r` with release number
- Check for build-id matching
- Added syscalls tracing support
- Compress modules

* Mon Nov 28 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.35-1
- Update to linux-4.4.35
- vfio-pci-fix-integer-overflows-bitmask-check.patch
    to fix CVE-2016-9083

* Tue Nov 22 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.31-4
- net-9p-vsock.patch

* Thu Nov 17 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.31-3
- tty-prevent-ldisc-drivers-from-re-using-stale-tty-fields.patch
    to fix CVE-2015-8964

* Tue Nov 15 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.31-2
- .config: add cgrup_hugetlb support
- .config: add netfilter_xt_{set,target_ct} support
- .config: add netfilter_xt_match_{cgroup,ipvs} support

* Thu Nov 10 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.31-1
- Update to linux-4.4.31

* Fri Oct 21 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.26-1
- Update to linux-4.4.26

* Wed Oct 19 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-6
- net-add-recursion-limit-to-GRO.patch
- scsi-arcmsr-buffer-overflow-in-arcmsr_iop_message_xfer.patch

* Tue Oct 18 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-5
- ipip-properly-mark-ipip-GRO-packets-as-encapsulated.patch
- tunnels-dont-apply-GRO-to-multiple-layers-of-encapsulation.patch

* Mon Oct  3 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-4
- Package vmlinux with PROGBITS sections in -debuginfo subpackage

* Tue Sep 27 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-3
- .config: CONFIG_IP_SET_HASH_{IPMARK,MAC}=m

* Tue Sep 20 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-2
- Add -release number for /boot/* files
- Use initrd.img with version and release number
- Rename -dev subpackage to -devel

* Wed Sep  7 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-1
- Update to linux-4.4.20
- apparmor-fix-oops-validate-buffer-size-in-apparmor_setprocattr.patch
- keys-fix-asn.1-indefinite-length-object-parsing.patch

* Thu Aug 25 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-11
- vmxnet3 patches to bumpup a version to 1.4.8.0

* Wed Aug 10 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-10
- Added VSOCK-Detach-QP-check-should-filter-out-non-matching-QPs.patch
- .config: pmem hotplug + ACPI NFIT support
- .config: enable EXPERT mode, disable UID16 syscalls

* Thu Jul 07 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-9
- .config: pmem + fs_dax support

* Fri Jun 17 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-8
- patch: e1000e-prevent-div-by-zero-if-TIMINCA-is-zero.patch
- .config: disable rt group scheduling - not supported by systemd

* Wed Jun 15 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.4.8-7
- fixed the capitalization for - System.map

* Thu May 26 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-6
- patch: REVERT-sched-fair-Beef-up-wake_wide.patch

* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> - 4.4.8-5
- GA - Bump release of all rpms

* Mon May 23 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.4.8-4
- Fixed generation of debug symbols for kernel modules & vmlinux.

* Mon May 23 2016 Divya Thaluru <dthaluru@vmware.com> - 4.4.8-3
- Added patches to fix CVE-2016-3134, CVE-2016-3135

* Wed May 18 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.4.8-2
- Enabled CONFIG_UPROBES in config as needed by ktap

* Wed May 04 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-1
- Update to linux-4.4.8
- Added net-Drivers-Vmxnet3-set-... patch

* Tue May 03 2016 Vinay Kulkarni <kulkarniv@vmware.com> - 4.2.0-27
- Compile Intel GigE and VMXNET3 as part of kernel.

* Thu Apr 28 2016 Nick Shi <nshi@vmware.com> - 4.2.0-26
- Compile cramfs.ko to allow mounting cramfs image

* Tue Apr 12 2016 Vinay Kulkarni <kulkarniv@vmware.com> - 4.2.0-25
- Revert network interface renaming disable in kernel.

* Tue Mar 29 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-24
- Support kmsg dumping to vmware.log on panic
- sunrpc: xs_bind uses ip_local_reserved_ports

* Mon Mar 28 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-23
- Enabled Regular stack protection in Linux kernel in config

* Thu Mar 17 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-22
- Restrict the permissions of the /boot/System.map-X file

* Fri Mar 04 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-21
- Patch: SUNRPC: Do not reuse srcport for TIME_WAIT socket.

* Wed Mar 02 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-20
- Patch: SUNRPC: Ensure that we wait for connections to complete
    before retrying

* Fri Feb 26 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-19
- Disable watchdog under VMware hypervisor.

* Thu Feb 25 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-18
- Added rpcsec_gss_krb5 and nfs_fscache

* Mon Feb 22 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-17
- Added sysctl param to control weighted_cpuload() behavior

* Thu Feb 18 2016 Divya Thaluru <dthaluru@vmware.com> - 4.2.0-16
- Disabling network renaming

* Sun Feb 14 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-15
- veth patch: don’t modify ip_summed

* Thu Feb 11 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-14
- Full tickless -> idle tickless + simple CPU time accounting
- SLUB -> SLAB
- Disable NUMA balancing
- Disable stack protector
- No build_forced no-CBs CPUs
- Disable Expert configuration mode
- Disable most of debug features from 'Kernel hacking'

* Mon Feb 08 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-13
- Double tcp_mem limits, patch is added.

* Wed Feb 03 2016 Anish Swaminathan <anishs@vmware.com> -  4.2.0-12
- Fixes for CVE-2015-7990/6937 and CVE-2015-8660.

* Tue Jan 26 2016 Anish Swaminathan <anishs@vmware.com> - 4.2.0-11
- Revert CONFIG_HZ=250

* Fri Jan 22 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-10
- Fix for CVE-2016-0728

* Wed Jan 13 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-9
- CONFIG_HZ=250

* Tue Jan 12 2016 Mahmoud Bassiouny <mbassiouny@vmware.com> - 4.2.0-8
- Remove rootfstype from the kernel parameter.

* Mon Jan 04 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-7
- Disabled all the tracing options in kernel config.
- Disabled preempt.
- Disabled sched autogroup.

* Thu Dec 17 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-6
- Enabled kprobe for systemtap & disabled dynamic function tracing in config

* Fri Dec 11 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-5
- Added oprofile kernel driver sub-package.

* Fri Nov 13 2015 Mahmoud Bassiouny <mbassiouny@vmware.com> - 4.2.0-4
- Change the linux image directory.

* Wed Nov 11 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-3
- Added the build essential files in the dev sub-package.

* Mon Nov 09 2015 Vinay Kulkarni <kulkarniv@vmware.com> - 4.2.0-2
- Enable Geneve module support for generic kernel.

* Fri Oct 23 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-1
- Upgraded the generic linux kernel to version 4.2.0 & and updated timer handling to full tickless mode.

* Tue Sep 22 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.0.9-5
- Added driver support for frame buffer devices and ACPI

* Wed Sep 2 2015 Alexey Makhalov <amakhalov@vmware.com> - 4.0.9-4
- Added mouse ps/2 module.

* Fri Aug 14 2015 Alexey Makhalov <amakhalov@vmware.com> - 4.0.9-3
- Use photon.cfg as a symlink.

* Thu Aug 13 2015 Alexey Makhalov <amakhalov@vmware.com> - 4.0.9-2
- Added environment file(photon.cfg) for grub.

* Wed Aug 12 2015 Sharath George <sharathg@vmware.com> - 4.0.9-1
- Upgrading kernel version.

* Wed Aug 12 2015 Alexey Makhalov <amakhalov@vmware.com> - 3.19.2-5
- Updated OVT to version 10.0.0.
- Rename -gpu-drivers to -drivers-gpu in accordance to directory structure.
- Added -sound package/

* Tue Aug 11 2015 Anish Swaminathan<anishs@vmware.com> - 3.19.2-4
- Removed Requires dependencies.

* Fri Jul 24 2015 Harish Udaiya Kumar <hudaiyakumar@gmail.com> - 3.19.2-3
- Updated the config file to include graphics drivers.

* Mon May 18 2015 Touseef Liaqat <tliaqat@vmware.com> - 3.13.3-2
- Update according to UsrMove.

* Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> - 3.13.3-1
- Initial build. First version
