Summary:        Preempt RT Linux Kernel
Name:           kernel-rt
Version:        6.12.80
Release:        1%{?dist}
License:        GPLv2
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://www.kernel.org/pub/linux/kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.12.80.tar.gz
Source1:        config
Source3:        sha512hmac-openssl.sh
Source4:        emt-ca-20211013.pem
Source5:        cpupower
Source6:        cpupower.service


# Intel Kernel Patches
# Series file for v6.12.80 linux kernel
# 00d7934ffcc35 Linux 6.12.80
#sriov
Patch01001: 0001-drm-i915-mtl-Add-C10-table-for-HDMI-Clock-25175.sriov
Patch01002: 0002-drm-i915-mtl-Copy-c10-phy-pll-sw-state-from-master-t.sriov
Patch01003: 0003-drm-i915-guc-Define-MAX_DWORDS-for-CTB-HXG-Message.sriov
Patch01004: 0004-drm-i915-call-taint_for_CI-on-FLR-failure.sriov
Patch01005: 0005-drm-i915-huc-load-HuC-via-non-POR-GSC-engine-flow.sriov
Patch01006: 0006-drm-i915-SR-IOV-Enabling-and-Support.sriov
Patch01007: 0007-Revert-drm-i915-move-platform_engine_mask-and-memory.sriov
Patch01008: 0008-drm-i915-gt-Enable-the-early-register-to-working-win.sriov
Patch01009: 0009-drm-i915-gt-Modify-the-adls-mocs-table-same-as-tgl-m.sriov
Patch01010: 0010-drm-i915-Bypass-gem_set_tiling-and-gem_get_tiling.sriov
Patch01011: 0011-drm-i915-enable-CCS-on-DG1-and-TGL-for-testing.sriov
Patch01012: 0012-drm-i915-force-VF-using-v70-GuC-API.sriov
Patch01013: 0013-drm-i915-fix-regression-on-sriov-vf-failures-due-to-.sriov
Patch01014: 0014-drm-i915-add-null-pointer-protection-inside-intel_fb.sriov
Patch01015: 0015-drm-i915-use-the-original-Wa_14010685332-for-PCH_ADP.sriov
Patch01016: 0016-drm-i915-fix-bitmap-clear-API-region-start-issue.sriov
Patch01017: 0017-drm-i915-iov-Expose-early-runtime-registers-for-MTL.sriov
Patch01018: 0018-drm-i915-gt-fix-empty-workaround-list-access-issue.sriov
Patch01019: 0019-drm-i915-mtl-Add-module-parameter-override-for-Wa_16.sriov
Patch01020: 0020-drm-i915-mtl-Provide-user-the-option-to-disable-ccs.sriov
Patch01021: 0021-drm-i915-mtl-Turn-on-Wa_16019325821-Wa_14019159160-b.sriov
Patch01022: 0022-drm-i915-pf-Use-GPU-to-set-PTE-owner.sriov
Patch01023: 0023-drm-i915-pf-Use-GPU-to-set-PTE-owner-on-platforms-wi.sriov
Patch01024: 0024-drm-i915-access-ddc-pointer-only-if-it-is-available.sriov
Patch01025: 0025-drm-i915-guc-Upgrade-GuC-fw-version-to-70.20.0.sriov
Patch01026: 0026-drm-i915-iov-Adding-runtime-reg-for-MTL-HuC-status.sriov
Patch01027: 0027-drm-i915-guc-Upgrade-GuC-fw-version-to-70.29.2.sriov
Patch01028: 0028-drm-i915-Re-add-enable_rc6-modparam.sriov
Patch01029: 0032-drm-virtio-freeze-and-restore-hooks-to-support-suspe.sriov
Patch01030: 0033-drm-virtio-save-and-restore-virtio_gpu_objects.sriov
Patch01031: 0001-drm-virtio-Use-drm_gem_plane_helper_prepare_fb.patch
Patch01032: 0034-drm-i915-pf-Introduce-i915_ggtt_save_ptes-and-i915_g.sriov
Patch01033: 0035-drm-i915-iov-Introduce-VFs-shadow-copy-of-GGTT-on-PF.sriov
Patch01034: 0036-drm-i915-iov-Shadow-GGTT-mock-selftestes.sriov
Patch01035: 0037-drm-i915-gt-Don-t-support-GGTT-save-restore-via-BAR-.sriov
Patch01036: 0038-drm-i915-pf-Add-helpers-for-saving-loading-GGTT-stat.sriov
Patch01037: 0039-drm-i915-pf-Handle-VF-pause-complete-notification.sriov
Patch01038: 0040-drm-i915-pf-Allow-to-save-restore-GuC-VF-state.sriov
Patch01039: 0041-drm-i915-pf-Save-and-restore-VFs-state-during-S2idle.sriov
Patch01040: 0042-drm-i915-pf-Skip-VF-save-restore-on-S2idle-S3-S4-if-.sriov
Patch01041: 0043-drm-i915-pf-Start-use-shadow-GGTT-to-save-restore-du.sriov
Patch01042: 0044-drm-i915-pf-Export-API-to-be-used-by-i915-vfio-pci.sriov
Patch01043: 0045-drm-i915-iov-Flag-which-tells-whether-PAUSE-is-in-pr.sriov
Patch01044: 0046-drm-i915-iov-Remember-run-state-on-suspend-and-resto.sriov
Patch01045: 0047-drm-i915-pf-Pause-VF-before-restore-GuC-state-after-.sriov
Patch01046: 0048-drm-i915-iov-fix-i915-sriov-build-issue.sriov
Patch01047: 0001-drm-i915-CTB-TLB-invalidation-fix-on-VM.sriov
Patch01048: 0002-vfio-i915-Add-vfio_pci-driver-for-Intel-graphics.sriov
Patch01049: 0003-drm-i915-guc-Upgrade-GuC-fw-version-to-70.36.0.sriov
Patch01050: 0001-drm-i915-Fix-logic-for-GUC-Process.sriov
Patch01051: 0001-vfio-i915-Add-support-for-MMIO-save-restore.sriov
Patch01052: 0002-drm-i915-SR-IOV-Save-Restore-Feature-support.sriov
Patch01053: 0001-i915-Enable-w-a-16026508708.sriov
Patch01054: 0001-virtio-hookup-irq_get_affinity-callback.sriov
Patch01055: 0002-virtio-break-and-reset-virtio-devices-on-device_shut.sriov
Patch01056: 0003-virtgpu-don-t-reset-on-shutdown.sriov
Patch01057: 0004-drm-virtio-implement-virtio_gpu_shutdown.sriov
Patch01058: 0001-drm-virtio-Wait-until-the-control-and-cursor-queues-.sriov
Patch01059: 0001-drm-i915-move-sriov-selftest-buffer-out-of-stack.sriov
Patch01060: 0001-drm-i915-Do-not-advertise-about-CCS.sriov
Patch01061: 0001-Revert-drm-i915-Do-not-advertise-about-CCS.sriov
#security
Patch02001: 0001-mei-bus-add-api-to-query-capabilities-of-ME-clien.security
Patch02002: 0002-mei-virtio-virtualization-frontend-driver.security
Patch02003: 0003-INTEL_DII-mei-avoid-reset-if-fw-is-down.security
Patch02004: 0004-INTEL_DII-FIXME-mei-iaf-add-iaf-Intel-Accelerator.security
Patch02005: 0005-INTEL_DII-mei-add-check-for-offline-bit-in-every-.security
Patch02006: 0006-INTEL_DII-mei-add-empty-handlers-for-ops-function.security
Patch02007: 0007-INTEL_DII-mei-gsc-add-fields-to-support-force-wak.security
Patch02008: 0008-INTEL_DII-mei-add-waitqueue-for-device-state-chan.security
Patch02009: 0009-INTEL_DII-mei-add-force-wake-workaround-infra.security
Patch02010: 0010-INTEL_DII-mei-add-force-wake-workaround-in-init.security
Patch02011: 0011-INTEL_DII-mei-add-force-wake-workaround-on-sessio.security
Patch02012: 0012-INTEL_DII-mei-add-force-wake-workaround-in-runtim.security
Patch02013: 0013-INTEL_DII-mei-add-force-wake-workaround-in-resume.security
Patch02014: 0014-INTEL_DII-mei-disable-immediate-enum-if-forcewake.security
Patch02015: 0015-INTEL_DII-mei-put-force-wake-in-error-flows.security
Patch02016: 0016-INTEL_DII-mei-add-force-wake-callbacks-to-empty-h.security
Patch02017: 0017-INTEL_DII-mei-optimize-force-wake-wait.security
Patch02018: 0018-mei-me-apply-GSC-error-supression-to-systems-with.security
Patch02019: 0019-INTEL_DII-mei-bus-fixup-disable-version-retrieval.security
#tgpio
Patch03001: 0001-Revert-timekeeping-Add-function-to-convert-realtime-.tgpio
Patch03002: 0002-Revert-x86-tsc-Remove-obsolete-ART-to-TSC-conversion.tgpio
Patch03003: 0003-Revert-ice-ptp-Remove-convert_art_to_tsc.tgpio
Patch03004: 0004-Revert-ALSA-hda-Remove-convert_art_to_tsc.tgpio
Patch03005: 0005-Revert-stmmac-intel-Remove-convert_art_to_tsc.tgpio
Patch03006: 0006-Revert-igc-Remove-convert_art_ns_to_tsc.tgpio
Patch03007: 0007-Revert-e1000e-Replace-convert_art_to_tsc.tgpio
Patch03008: 0008-Revert-x86-tsc-Provide-ART-base-clock-information-fo.tgpio
Patch03009: 0009-Revert-timekeeping-Provide-infrastructure-for-conver.tgpio
Patch03010: 0010-drivers-ptp-Add-Enhanced-handling-of-reserve-fields.tgpio
Patch03011: 0011-drivers-ptp-Add-PEROUT2-ioctl-frequency-adjustment-i.tgpio
Patch03012: 0012-drivers-ptp-Add-user-space-input-polling-interface.tgpio
Patch03013: 0013-x86-tsc-Add-TSC-support-functions-to-support-ART-dri.tgpio
Patch03014: 0014-drivers-ptp-Add-support-for-PMC-Time-Aware-GPIO-Driv.tgpio
Patch03015: 0015-x86-core-TSC-reliable-kernel-arg-prevents-DQ-of-TSC-.tgpio
Patch03016: 0016-mfd-intel-ehl-gpio-Introduce-MFD-framework-to-PSE-GP.tgpio
Patch03017: 0017-TGPIO-Calling-power-management-calls-without-enterin.tgpio
Patch03018: 0018-TGPIO-Fix-PSE-TGPIO-PTP-driver-ioctls-fail.tgpio
Patch03019: 0019-Kernel-Argument-Bypassing-ART-Detection.tgpio
Patch03020: 0020-GPIO-Fix-for-PSE-GPIO-generating-only-one-event-as-i.tgpio
Patch03021: 0021-Added-TGPIO-pin-check-before-input-event-read.tgpio
Patch03022: 0022-Added-an-Example-to-adjust-frequency-for-output.tgpio
Patch03023: 0023-ptp-tgpio-PSE-TGPIO-crosststamp-counttstamp.tgpio
Patch03024: 0024-ptp-Fixed-read-issue-on-PHC-with-zero-n_pins.tgpio
Patch03025: 0025-ptp-S-W-workaround-for-PMC-TGPIO-h-w-bug.tgpio
Patch03026: 0026-ptp-Fix-for-PSE-TGPIO-Oneshot-output-and-counttstamp.tgpio
Patch03027: 0027-ptp-Fix-for-PSE-TGPIO-frequency-Adjustment-issue.tgpio
Patch03028: 0028-tgpio-Fix-compilation-errors-for-PSE-TGPIO.tgpio
Patch03029: 0029-Added-single-shot-output-mode-support-for-TGPIO.tgpio
Patch03030: 0030-Added-an-example-to-poll-for-edges.tgpio
Patch03031: 0031-Added-support-to-get-TGPIO-System-Clock-Offset.tgpio
Patch03032: 0032-Added-single-shot-output-mode-option-for-TGPIO-pin.tgpio
Patch03033: 0033-selftests-ptp-Added-COMPV-GPIO-Input-Mode-for-TGPIO.tgpio
Patch03034: 0034-ptp-Introduce-PTP_PINDESC_INPUTPOLL-for-Intel-PMC-TG.tgpio
Patch03035: 0035-drivers-ptp-Add-COMPV-GPIO-Mode-for-PSE-TGPIO.tgpio
Patch03036: 0036-net-ice-fix-braces-around-scalar-initializer.tgpio
Patch03037: 0037-ptp-Add-PTP_EVENT_COUNTER_MODE-in-v1-valid-flags.tgpio
Patch03038: 0038-ptp-Enable-preempt-if-it-is-disabled.tgpio
Patch03039: 0039-ptp-Generate-sqaure-wave-on-PSE-TGPIO.tgpio
Patch03040: 0040-ptp-tgpio-Add-an-edge-if-the-output-signal-ends-high.tgpio
Patch03041: 0041-ptp-pmc-tgpio-Initialize-variable-to-zero.tgpio
Patch03042: 0042-ptp-tgpio-Fix-return-type-of-remove-function-in-tgpi.tgpio
Patch03043: 0043-net-mlx5-reuse-convert_art_ns_to_tsc-to-convert-ART-.tgpio
#edac
Patch04001: 0001-x86-mce-Add-MCACOD-code-for-generic-I-O-error.edac
Patch04002: 0002-EDAC-ieh-Add-I-O-device-EDAC-driver-for-Intel-CPUs-wi.edac
Patch04003: 0003-EDAC-ieh-Add-I-O-device-EDAC-support-for-Intel-Tiger-.edac
Patch04004: 0004-EDAC-igen6-Add-registration-APIs-for-In-Band-ECC-erro.edac
Patch04005: 0005-EDAC-i10nm-Print-DRAM-rules-debug-purpose.edac
Patch04006: 0006-EDAC-skx_common-skx-i10nm-Make-skx_register_mci-indep.edac
Patch04007: 0007-EDAC-skx_common-Prepare-skx_get_edac_list.edac
Patch04008: 0008-EDAC-skx_common-Prepare-skx_set_hi_lo.edac
Patch04009: 0009-EDAC-igen6-Add-Intel-Pnther-Lake-H-SoCs-support.edac
Patch04010: 0002-EDAC-ie31200-Add-Kaby-Lake-S-dual-core-host-bridge-ID.edac
Patch04011: 0006-EDAC-ie31200-Fix-the-3rd-parameter-name-of-populate_d.edac
Patch04012: 0007-EDAC-ie31200-Simplify-the-pci_device_id-table.edac
Patch04013: 0008-EDAC-ie31200-Make-the-memory-controller-resources-con.edac
Patch04014: 0009-EDAC-ie31200-Make-struct-dimm_data-contain-decoded-in.edac
Patch04015: 0010-EDAC-ie31200-Fold-the-two-channel-loops-into-one-loop.edac
Patch04016: 0011-EDAC-ie31200-Break-up-ie31200_probe1.edac
Patch04017: 0012-EDAC-ie31200-Add-Intel-Raptor-Lake-S-SoCs-support.edac
Patch04018: 0013-EDAC-ie31200-Switch-Raptor-Lake-S-to-interrupt-mode.edac
Patch04019: 0001-EDAC-ie31200-Add-two-Intel-SoCs-for-EDAC-support.edac
Patch04020: 0002-ie31200-EDAC-Add-Intel-Bartlett-Lake-S-SoCs-support.edac
Patch04021: 0001-EDAC-igen6-Add-Intel-Amston-Lake-SoCs-support.edac
Patch04022: 0002-EDAC-igen6-Add-additional-Intel-Amston-Lake-SoC-compu.edac
Patch04023: 0001-EDAC-igen6-Initialize-edac_op_state-according-to-the-.edac
Patch04024: 0002-EDAC-igen6-Add-polling-support.edac
Patch04025: 0003-EDAC-igen6-Fix-the-flood-of-invalid-error-reports.edac
Patch04026: 0004-EDAC-igen6-Constify-struct-res_config.edac
Patch04027: 0005-EDAC-igen6-Skip-absent-memory-controllers.edac
Patch04028: 0006-EDAC-igen6-Fix-NULL-pointer-dereference.edac
#tsn
Patch05001: 0001-net-pcs-xpcs-enable-xpcs-reset-skipping.tsn
Patch05002: 0002-net-stmmac-Bugfix-on-stmmac_interrupt-for-WOL.tsn
Patch05003: 0003-net-phy-increase-gpy-loopback-test-delay.tsn
Patch05004: 0004-net-stmmac-Resolve-poor-line-rate-after-switching-from.tsn
Patch05005: 0005-net-phy-dp83867-perform-restart-AN-after-modifying-AN-.tsn
Patch05006: 0006-stmmac-intel-Separate-ADL-N-and-RPL-P-device-ID-from-T.tsn
Patch05007: 0007-net-stmmac-Adjust-mac_capabilities-for-Intel-mGbE-2.5G.tsn
Patch05008: 0008-stmmac-intel-skip-xpcs-reset-for-2.5Gbps-on-Intel-Alde.tsn
Patch05009: 0009-net-stmmac-add-check-for-2.5G-mode-to-prevent-MAC-capa.tsn
Patch05010: 0010-stmmac-intel-Enable-PHY-WoL-in-ADL-N.tsn
Patch05011: 0011-net-phy-reconfigure-PHY-WoL-when-WoL-option-is-enabled.tsn
Patch05012: 0012-net-stmmac-fix-MAC-and-phylink-mismatch-issue-after-re.tsn
Patch05013: 0013-net-stmmac-restructure-Rx-Tx-hardware-timestamping-fun.tsn
Patch05014: 0014-net-stmmac-Add-per-packet-time-based-scheduling-for-XD.tsn
Patch05015: 0015-net-stmmac-introduce-AF_XDP-ZC-RX-HW-timestamps.tsn
Patch05016: 0016-net-stmmac-add-fsleep-in-HW-Rx-timestamp-checking-loop.tsn
Patch05017: 0017-net-stmmac-select-PCS-negotiation-mode-according-to-th.tsn
Patch05018: 0018-net-pcs-xpcs-re-initiate-clause-37-Auto-negotiation.tsn
Patch05019: 0019-arch-x86-Add-IPC-mailbox-accessor-function-and-add-SoC.tsn
Patch05020: 0020-net-stmmac-configure-SerDes-according-to-the-interface.tsn
Patch05021: 0021-stmmac-intel-interface-switching-support-for-intel-pla.tsn
Patch05022: 0022-net-stmmac-Set-mac_managed_pm-flag-from-stmmac-to-reso.tsn
Patch05023: 0023-net-phylink-Add-module_exit.tsn
Patch05024: 0024-net-stmmac-introduce-AF_XDP-ZC-TX-HW-timestamps.tsn
Patch05025: 0025-net-sched-taprio-fix-too-early-schedules-switching.tsn
Patch05026: 0026-net-sched-taprio-fix-cycle-time-adjustment-for-next-en.tsn
Patch05027: 0027-net-sched-taprio-fix-impacted-fields-value-during-cycl.tsn
Patch05028: 0028-net-sched-taprio-get-corrected-value-of-cycle_time-and.tsn
Patch05029: 0029-xsk-add-txtime-field-in-xdp_desc-struct.tsn
Patch05030: 0030-Revert-net-stmmac-silence-FPE-kernel-logs.tsn
Patch05031: 0031-Revert-net-stmmac-support-fp-parameter-of-tc-taprio.tsn
Patch05032: 0032-Revert-net-stmmac-support-fp-parameter-of-tc-mqprio.tsn
Patch05033: 0033-Revert-net-stmmac-configure-FPE-via-ethtool-mm.tsn
Patch05034: 0034-Revert-net-stmmac-refactor-FPE-verification-process.tsn
Patch05035: 0035-Revert-net-stmmac-drop-stmmac_fpe_handshake.tsn
Patch05036: 0036-Revert-net-stmmac-move-stmmac_fpe_cfg-to-stmmac_priv-d.tsn
Patch05037: 0037-net-stmmac-add-FPE-preempt-setting-for-TxQ-preemptible.tsn
Patch05038: 0038-taprio-Add-support-for-frame-preemption-offload.tsn
Patch05039: 0039-net-stmmac-set-initial-EEE-policy-configuration.tsn
Patch05040: 0040-net-phy-fix-phylib-s-dual-eee_enabled.tsn
Patch05041: 0041-net-phy-ensure-that-genphy_c45_an_config_eee_aneg-sees.tsn
Patch05042: 0042-net-phy-fix-phy_ethtool_set_eee-incorrectly-enabling-L.tsn
Patch05043: 0001-igc-Set-the-RX-packet-buffer-size-for-TSN-mode.tsn
Patch05044: 0002-igc-Only-dump-registers-if-configured-to-dump-HW-infor.tsn
Patch05045: 0003-ethtool-Add-support-for-configuring-frame-preemption.tsn
Patch05046: 0004-ethtool-Add-support-for-Frame-Preemption-verification.tsn
Patch05047: 0005-igc-Add-support-for-enabling-frame-preemption-via-etht.tsn
Patch05048: 0006-igc-Add-support-for-TC_SETUP_PREEMPT.tsn
Patch05049: 0007-igc-Add-support-for-setting-frame-preemption-configura.tsn
Patch05050: 0008-igc-Add-support-for-Frame-Preemption-verification.tsn
Patch05051: 0009-igc-Add-support-for-exposing-frame-preemption-stats-re.tsn
Patch05052: 0010-igc-Optimize-the-packet-buffer-utilization.tsn
Patch05053: 0011-igc-Add-support-for-enabling-all-packets-to-be-receive.tsn
Patch05054: 0012-igc-Add-support-for-DMA-timestamp-for-non-PTP-packets.tsn
Patch05055: 0013-bpf-add-btf-register-unregister-API.tsn
Patch05056: 0014-net-core-XDP-metadata-BTF-netlink-API.tsn
Patch05057: 0015-rtnetlink-Fix-unchecked-return-value-of-dev_xdp_query_.tsn
Patch05058: 0016-rtnetlink-Add-return-value-check.tsn
Patch05059: 0017-tools-bpf-Query-XDP-metadata-BTF-ID.tsn
Patch05060: 0018-tools-bpf-Add-xdp-set-command-for-md-btf.tsn
Patch05061: 0019-igc-Add-BTF-based-metadata-for-XDP.tsn
Patch05062: 0020-igc-Enable-HW-RX-Timestamp-for-AF_XDP-ZC.tsn
Patch05063: 0021-igc-Take-care-of-DMA-timestamp-rollover.tsn
Patch05064: 0022-igc-Add-SO_TXTIME-for-AF_XDP-ZC.tsn
Patch05065: 0023-igc-Reodering-the-empty-packet-buffers-and-descriptors.tsn
Patch05066: 0024-Revert-igc-Add-support-for-PTP-.getcyclesx64.tsn
Patch05067: 0025-core-Introduce-netdev_tc_map_to_queue_mask.tsn
Patch05068: 0026-taprio-Replace-tc_map_to_queue_mask.tsn
Patch05069: 0027-mqprio-Add-support-for-frame-preemption-offload.tsn
Patch05070: 0030-igc-Reduce-retry-count-to-a-more-reasonable-number.tsn
Patch05071: 0001-igc-Enable-HW-TX-Timestamp-for-AF_XDP-ZC.tsn
Patch05072: 0002-igc-Enable-trace-for-HW-TX-Timestamp-AF_XDP-ZC.tsn
Patch05073: 0003-igc-Remove-the-CONFIG_DEBUG_MISC-condition-for-trace.tsn
Patch05074: 0006-Revert-net-stmmac-set-initial-EEE-policy-configurati.tsn
Patch05075: 0001-net-phy-Set-eee_cfg.eee_enabled-according-to-PHY.tsn
Patch05076: 0001-Revert-net-stmmac-add-FPE-preempt-setting-for-TxQ-pree.tsn
Patch05077: 0002-Reapply-net-stmmac-move-stmmac_fpe_cfg-to-stmmac_priv-.tsn
Patch05078: 0003-Reapply-net-stmmac-drop-stmmac_fpe_handshake.tsn
Patch05079: 0004-Reapply-net-stmmac-refactor-FPE-verification-process.tsn
Patch05080: 0005-Reapply-net-stmmac-configure-FPE-via-ethtool-mm.tsn
Patch05081: 0006-Reapply-net-stmmac-support-fp-parameter-of-tc-mqprio.tsn
Patch05082: 0007-Reapply-net-stmmac-support-fp-parameter-of-tc-taprio.tsn
Patch05083: 0008-Reapply-net-stmmac-silence-FPE-kernel-logs.tsn
#camera
Patch06001: 0001-media-intel-ipu6-remove-buttress-ish-structure.camera
Patch06002: 0001-media-i2c-Add-ar0234-camera-sensor-driver.camera
Patch06003: 0002-media-i2c-add-support-for-lt6911uxe.camera
Patch06004: 0003-INT3472-Support-LT6911UXE.camera
Patch06005: 0004-upstream-Use-module-parameter-to-set-isys-freq.camera
Patch06006: 0005-upstream-Use-module-parameter-to-set-psys-freq.camera
Patch06007: 0006-media-pci-Enable-ISYS-reset.camera
Patch06008: 0007-media-i2c-add-support-for-ar0234-and-lt6911uxe.camera
Patch06009: 0008-driver-media-i2c-remove-useless-header-file.camera
Patch06010: 0009-media-i2c-update-lt6911uxe-for-upstream-and-bug-fix.camera
Patch06011: 0010-media-i2c-add-support-for-lt6911uxc.camera
Patch06012: 0011-media-i2c-add-lt6911uxc-driver-and-enable-in-ipu-br.camera
Patch06013: 0012-media-pci-intel-psys-driver.camera
Patch06014: 0013-media-i2c-Remove-unused-variables-in-Lontium-driver.camera
Patch06015: 0001-media-intel-ipu6-remove-buttress-ish-structure-1.camera
Patch06016: 0002-media-pci-intel-include-psys-driver.camera
Patch06017: 0003-Revert-media-ipu6-use-the-IPU6-DMA-mapping-APIs-to-.camera
Patch06018: 0004-Revert-media-ipu6-remove-architecture-DMA-ops-depen.camera
Patch06019: 0005-Revert-media-ipu6-not-override-the-dma_ops-of-devic.camera
Patch06020: 0001-Reapply-media-ipu6-not-override-the-dma_ops-of-devi.camera
Patch06021: 0002-Reapply-media-ipu6-remove-architecture-DMA-ops-depe.camera
Patch06022: 0003-Reapply-media-ipu6-use-the-IPU6-DMA-mapping-APIs-to.camera
Patch06023: 0001-media-pci-update-IPU6-PSYS-driver.camera
Patch06024: 0002-media-i2c-update-lt6911uxc-driver-to-fix-COV-issue.camera
Patch06025: 0003-lt6911-2-pads-linked-to-ipu-2-ports-for-split-mode.camera
Patch06026: 0004-media-i2c-add-dv_timings-api-in-lt6911uxe.camera
Patch06027: 0005-media-intel-ipu6-use-vc1-dma-for-MTL-and-ARL.camera
Patch06028: 0006-media-i2c-some-changes-in-lt6911uxe.camera
Patch06029: 0001-Revert-media-intel-ipu6-use-vc1-dma-for-MTL-and-ARL.camera
Patch06030: 0002-media-i2c-update-format-in-irq-for-lt6911uxe.camera
Patch06031: 0003-media-i2c-remove-unused-func-in-lt6911uxe.camera
Patch06032: 0001-media-intel-ipu6-use-vc1-dma-for-MTL-and-ARL.camera
Patch06033: 0002-media-ipu-Dma-sync-at-buffer_prepare-callback-as-DM.camera
Patch06034: 0003-Support-IPU6-ISYS-FW-trace-dump-for-upstream-driver.camera
Patch06035: 0004-Support-IPU6-PSYS-FW-trace-dump-for-upstream-driver.camera
Patch06036: 0005-media-pci-The-order-of-return-buffers-should-be-FIF.camera
Patch06037: 0006-media-i2c-fix-power-on-issue-for-on-board-LT6911UXC.camera
Patch06038: 0007-media-i2c-fix-power-on-issue-for-on-board-LT6911UXE.camera
Patch06039: 0001-media-pci-Modify-enble-disable-stream-in-CSI2.camera
Patch06040: 0002-media-pci-Set-the-correct-SOF-for-different-stream.camera
Patch06041: 0003-media-pci-support-imx390-for-6.11.0-rc3.camera
Patch06042: 0004-i2c-media-fix-cov-issue.camera
Patch06043: 0005-mv-ipu-acpi-module-to-linux-drivers.camera
Patch06044: 0006-kernel-enable-VC-support-in-v4l2.camera
Patch06045: 0007-media-pci-intel-support-PDATA-in-Kconfig-Makefile.camera
Patch06046: 0008-media-pci-unregister-i2c-device-to-complete-ext_sub.camera
Patch06047: 0009-media-pci-align-params-for-non-MIPI-split-and-split.camera
Patch06048: 0010-media-pci-add-missing-if-for-PDATA.camera
Patch06049: 0011-media-platform-fix-allyesconfig-build-error.camera
Patch06050: 0012-media-pci-refine-PDATA-related-config.camera
Patch06051: 0013-kernel-align-ACPI-PDATA-and-ACPI-fwnode-build-for-E.camera
Patch06052: 0014-media-i2c-add-gmsl-isx031-support.camera
Patch06053: 0015-media-i2c-add-support-for-isx031-max9296.camera
Patch06054: 0016-fix-S4-issue-on-TWL.camera
Patch06055: 0017-code-changes-for-link-frequency-and-sensor-physical.camera
#wwan
Patch07001: 0001-Revert-bus-mhi-host-pci_generic-add-support-for-sc828.wwan
Patch07002: 0002-wwan-add-SAHARA-device.wwan
Patch07003: 0003-bus-mhi-host-allow-SBL-as-initial-EE.wwan
Patch07004: 0004-drivers-bus-mhi-let-userspace-manage-xfp-fw-update-st.wwan
Patch07005: 0005-wwan-add-NMEA-type.wwan
Patch07006: 0006-drivers-bus-mhi-add-FN980-v2-support.wwan
Patch07007: 0007-drivers-bus-mhi-add-FN990-NMEA-and-DIAG-in-SBL-device.wwan
Patch07008: 0008-drivers-net-wwan-add-simple-DTR-driver.wwan
Patch07009: 0009-drivers-bus-mhi-host-fix-recovery-process-when-modem-.wwan
Patch07010: 0001-Revert-drivers-bus-mhi-host-fix-recovery-process-when.wwan
Patch07011: 0002-Revert-drivers-net-wwan-add-simple-DTR-driver.wwan
Patch07012: 0003-Revert-drivers-bus-mhi-add-FN990-NMEA-and-DIAG-in-SBL.wwan
Patch07013: 0004-Revert-drivers-bus-mhi-add-FN980-v2-support.wwan
Patch07014: 0005-Revert-wwan-add-NMEA-type.wwan
Patch07015: 0006-Revert-drivers-bus-mhi-let-userspace-manage-xfp-fw-up.wwan
Patch07016: 0007-Revert-bus-mhi-host-allow-SBL-as-initial-EE.wwan
Patch07017: 0008-Revert-wwan-add-SAHARA-device.wwan
Patch07018: 0009-Revert-Revert-bus-mhi-host-pci_generic-add-support-fo.wwan
#pmc_core
Patch08001: 0001-platform-x86-intel-pmc-Add-Arrow-Lake-U-H-support.pmc_core
Patch08002: 0002-platform-x86-intel-pmc-Add-Bartlett-Lake-support-to-.pmc_core
Patch08003: 0001-platform-x86-intel-pmc-Fix-Arrow-Lake-U-H-NPU-PCI.pmc_core
#lpss
Patch09001: 0001-Added-spi_set_cs-for-more-stable-r-w-operations-in-S.lpss
Patch09002: 0002-mtd-core-Don-t-fail-mtd_device_parse_register-if-OTP.lpss
Patch09003: 0003-spi-intel-pci-Add-support-for-Arrow-Lake-H-SPI-seria.lpss
Patch09004: 0004-spi-intel-Add-protected-and-locked-attributes.lpss
#preempt_rt patches backported
Patch09005: 0001-Revert-sched-core-Remove-the-unnecessary-need_resche.rt
Patch09006: 0001-hrtimer-Use-__raise_softirq_irqoff-to-raise-the-softirq.rt
Patch09007: 0002-timers-Use-__raise_softirq_irqoff-to-raise-the-softirq.rt
Patch09008: 0003-softirq-Use-a-dedicated-thread-for-timer-wakeups-on-PRE.rt
Patch09009: 0004-serial-8250-Switch-to-nbcon-console.rt
Patch09010: 0005-serial-8250-Revert-drop-lockdep-annotation-from-serial8.rt
Patch09011: 0006-locking-rt-Remove-one-__cond_lock-in-RT-s-spin_trylock_.rt
Patch09012: 0007-locking-rt-Add-sparse-annotation-for-RCU.rt
Patch09013: 0008-locking-rt-Annotate-unlock-followed-by-lock-for-sparse.rt
Patch09014: 0009-drm-i915-Use-preempt_disable-enable_rt-where-recommende.rt
Patch09015: 0010-drm-i915-Don-t-disable-interrupts-on-PREEMPT_RT-during-.rt
Patch09016: 0011-drm-i915-Don-t-check-for-atomic-context-on-PREEMPT_RT.rt
Patch09017: 0012-drm-i915-Disable-tracing-points-on-PREEMPT_RT.rt
Patch09018: 0013-drm-i915-gt-Use-spin_lock_irq-instead-of-local_irq_disa.rt
Patch09019: 0014-drm-i915-Drop-the-irqs_disabled-check.rt
Patch09020: 0015-drm-i915-guc-Consider-also-RCU-depth-in-busy-loop.rt
Patch09021: 0016-Revert-drm-i915-Depend-on-PREEMPT_RT.rt
Patch09022: 0017-sched-Add-TIF_NEED_RESCHED_LAZY-infrastructure.rt
Patch09023: 0018-sched-Add-Lazy-preemption-model.rt
Patch09024: 0019-sched-Enable-PREEMPT_DYNAMIC-for-PREEMPT_RT.rt
Patch09025: 0020-sched-x86-Enable-Lazy-preemption.rt
Patch09026: 0021-sched-Add-laziest-preempt-model.rt
Patch09027: 0022-sched-Fixup-the-IS_ENABLED-check-for-PREEMPT_LAZY.rt
Patch09028: 0023-tracing-Remove-TRACE_FLAG_IRQS_NOSUPPORT.rt
Patch09029: 0024-tracing-Record-task-flag-NEED_RESCHED_LAZY.rt
Patch09030: 0025-sysfs-Add-sys-kernel-realtime-entry.rt
Patch09031: 0001-serial-8250-enable-original-console-by-default.rt
Patch09032: 0001-kernel-trace-Add-DISALLOW_TRACE_PRINTK-make-option.rt
Patch09033: 0002-Revert-scripts-remove-bin2c.rt
Patch09034: 0003-extend-uio-driver-to-supports-msix.rt
Patch09035: 0004-virtio-add-VIRTIO_PMD-support.rt
Patch09036: 0005-virt-acrn-Introduce-interfaces-for-PIO-device.rt
Patch09037: 0006-Add-hypercall-to-access-MSR.rt
Patch09038: 0007-Revert-spi-Remove-unused-function-spi_busnum_to_master.rt
Patch09039: 0008-igc-add-CONFIG_IGC_TSN_TRACE-conditional-trace_printk-u.rt
Patch09040: 0009-stmmac_pci-add-CONFIG_STMMAC_TSN_TRACE-conditional-trac.rt
Patch09041: 0010-igb-prepare-for-AF_XDP-zero-copy-support.rt
Patch09042: 0011-igb-Introduce-XSK-data-structures-and-helpers.rt
Patch09043: 0012-igb-add-AF_XDP-zero-copy-Rx-support.rt
Patch09044: 0013-igb-add-AF_XDP-zero-copy-Tx-support.rt
Patch09045: 0014-igb-Add-BTF-based-metadata-for-XDP.rt
Patch09046: 0015-ANDROID-trace-power-add-trace_clock_set_parent.rt
Patch09047: 0016-ANDROID-trace-net-use-pK-for-kernel-pointers.rt
Patch09048: 0017-ANDROID-trace-add-non-hierarchical-function_graph-optio.rt
Patch09049: 0018-virtio-fix-VIRTIO_PMD-support.rt
Patch09050: 0019-drm-i915-add-i915-perf-event-capacity.rt
Patch09051: 0020-drm-xe-pm-allow-xe-with-CONFIG_PM.rt
#drm
Patch10001: 0001-drm-i915-enable-guc-submission-for-ADLs-by-default.drm
Patch10002: 0001-drm-i915-disable-a-couple-of-RT-functions-if-RT-is-d.drm
Patch10003: 0001-drm-i915-disable-dGPU-support-with-RT-kernel.drm
Patch10004: 0001-i915-Update-GUC-to-v70.44.1-for-i915-platforms.drm
Patch10005: 0001-Revert-drm-i915-disable-dGPU-support-with-RT-kernel.drm
Patch10006: 0001-drm-i915-gt-Avoid-using-masked-workaround-for-CCS_MODE.drm
Patch10007: 0002-drm-i915-gt-Move-the-CCS-mode-variable-to-a-global-pos.drm
Patch10008: 0003-drm-i915-gt-Allow-the-creation-of-multi-mode-CCS-masks.drm
Patch10009: 0004-drm-i915-gt-Refactor-uabi-engine-class-instance-list-c.drm
Patch10010: 0005-drm-i915-gem-Mark-and-verify-UABI-engine-validity.drm
Patch10011: 0006-drm-i915-gt-Introduce-for_each_enabled_engine-and-appl.drm
Patch10012: 0007-drm-i915-gt-Manage-CCS-engine-creation-within-UABI-exp.drm
Patch10013: 0008-drm-i915-gt-Remove-cslices-mask-value-from-the-CCS-str.drm
Patch10014: 0009-drm-i915-gt-Expose-the-number-of-total-CCS-slices.drm
Patch10015: 0010-drm-i915-gt-Store-engine-related-sysfs-kobjects.drm
Patch10016: 0011-drm-i915-gt-Store-active-CCS-mask.drm
Patch10017: 0012-drm-i915-Protect-access-to-the-UABI-engines-list-with-.drm
Patch10018: 0013-drm-i915-gt-Isolate-single-sysfs-engine-file-creation.drm
Patch10019: 0014-drm-i915-gt-Implement-creation-and-removal-routines-fo.drm
Patch10020: 0015-drm-i915-gt-Allow-the-user-to-change-the-CCS-mode-thro.drm
Patch10021: 0016-drm-i915-gt-Refactor-CCS-mode-handling-and-improve-app.drm
Patch10022: 0017-drm-i915-no-waiting-for-page-flip-in-vpp-case.drm
Patch10023: 0001-Remove-unneeded-files.patch
Patch10024: 0001-i915-gt-Upgrade-GuC-70.44.1-70.49.4.drm
Patch10025: 0001-drm-i915-no-force-probe-needed-for-mtl-platform.drm
#rapl
Patch11001: 0001-powercap-intel_rapl-Add-support-for-Bartlett-Lake-pl.rapl
#misc
Patch12001: 0001-Add-security.md-file.misc
#iommu
Patch13001: 0001-driver-core-add-a-faux-bus-for-use-when-a-simple-dev.iommu
Patch13002: 0002-iommu-io-pgtable-arm-dynamically-allocate-selftest-d.iommu
#emt-drm
Patch14001: 0001-Revert-drm-xe-mmio-Avoid-double-adjust-in-64-bit-rea.patch
Patch14002: 0002-Revert-drm-xe-Switch-MMIO-interface-to-take-xe_mmio-.patch

#CVE-2025-21817
Patch15001: CVE-2025-21817.patch

#CVE-2025-22104
Patch15002: CVE-2025-22104.patch

#CVE-2025-22108
Patch15003: CVE-2025-22108.patch

#CVE-2025-23131
Patch15004: CVE-2025-23131.patch

#CVE-2025-37746
Patch15005: CVE-2025-37746.patch
Patch15006: CVE-2025-37746-1.patch

#CVE-2025-37906
Patch15007: CVE-2025-37906.patch

#CVE-2025-38041
Patch15008: CVE-2025-38041.patch
Patch15009: CVE-2025-38041-1.patch
Patch15010: CVE-2025-38041-2.patch

#CVE-2025-38029
Patch15011: CVE-2025-38029.patch

#CVE-2025-38311
Patch15012: CVE-2025-38311.patch

#CVE-2025-38207
Patch15013: CVE-2025-38207.patch

#CVE-2025-38137
Patch15014: CVE-2025-38137.patch

#CVE-2025-38199
Patch15015: CVE-2025-38199.patch

#CVE-2025-38140
Patch15016: CVE-2025-38140.patch

#CVE-2025-38132
Patch15017: CVE-2025-38132.patch
Patch15018: CVE-2025-38132-1.patch

#CVE-2025-37743
Patch15019: CVE-2025-37743.patch

#CVE-2025-23132
Patch15020: CVE-2025-23132.patch

#CVE-2025-22127
Patch15021: CVE-2025-22127.patch

#CVE-2025-22109
Patch15022: CVE-2025-22109.patch

#CVE-2025-21752
Patch15023: CVE-2025-21752.patch
Patch15024: CVE-2025-21752-1.patch

#CVE-2024-58095
Patch15025: CVE-2024-58095.patch

#CVE-2024-58094
Patch15026: CVE-2024-58094.patch

#CVE-2024-52560
Patch15027: CVE-2024-52560.patch
Patch15028: CVE-2024-52560-1.patch

#CVE-2025-38621
Patch15029: CVE-2025-38621.patch

#CVE-2025-39789
Patch15030: CVE-2025-39789.patch

#CVE-2025-39745
Patch15031: CVE-2025-39745.patch

#CVE-2025-39677
Patch15032: CVE-2025-39677.patch

#CVE-2025-39933
Patch15033: CVE-2025-39933.patch

#CVE-2025-39833
Patch15034: CVE-2025-39833.patch

#CVE-2025-39925
Patch15035: CVE-2025-39925.patch

#CVE-2025-39905
Patch15036: CVE-2025-39905.patch

#CVE-2025-39859
Patch15037: CVE-2025-39859.patch

#CVE-2025-39910
Patch15038: CVE-2025-39910.patch

#CVE-2025-40098
Patch15039: CVE-2025-40098.patch

#CVE-2025-40074
Patch15040: CVE-2025-40074.patch

#CVE-2025-40064
Patch15041: CVE-2025-40064.patch

#CVE-2025-40086
Patch15042: CVE-2025-40086.patch
Patch15043: CVE-2025-40086-1.patch

#CVE-2025-40168
Patch15044: CVE-2025-40168.patch

#CVE-2025-40139
Patch15045: CVE-2025-40139.patch

#CVE-2025-40136
Patch15046: CVE-2025-40136.patch

#CVE-2025-40130
Patch15047: CVE-2025-40130.patch

#CVE-2025-38656
Patch15048: CVE-2025-38656.patch
Patch15049: CVE-2025-38656-2.patch

#CVE-2025-38584
Patch15050: CVE-2025-38584.patch

#CVE-2025-68745
Patch15051: CVE-2025-68745.patch

#CVE-2025-68359
Patch15052: CVE-2025-68359.patch

#CVE-2025-68368
Patch15053: CVE-2025-68368.patch

#CVE-2025-68353
Patch15054: CVE-2025-68353.patch

#CVE-2025-68319
Patch15055: CVE-2025-68319.patch

#CVE-2025-68193
Patch15056: CVE-2025-68193.patch

#CVE-2025-40355
Patch15057: CVE-2025-40355.patch

#CVE-2025-40338
Patch15058: CVE-2025-40338.patch

#CVE-2025-68768
Patch15059: CVE-2025-68768.patch

#CVE-2025-71074
Patch15060: CVE-2025-71074.patch

#CVE-2025-71117
Patch15061: CVE-2025-71117.patch

#CVE-2026-23171
Patch15062: CVE-2026-23171.patch




#CVE-2026-23327
Patch15063: CVE-2026-23327.patch

#CVE-2026-23272
Patch15064: CVE-2026-23272.patch

#CVE-2026-23371
Patch15065: CVE-2026-23371.patch

#CVE-2026-23302
Patch15066: CVE-2026-23302.patch

#CVE-2026-23259
Patch15067: CVE-2026-23259.patch

#CVE-2026-23181
Patch15068: CVE-2026-23181.patch

#CVE-2025-71269
Patch15069: CVE-2025-71269.patch

#CVE-2025-71227
Patch15070: CVE-2025-71227_1.patch
Patch15071: CVE-2025-71227_2.patch

#CVE-2026-23473
Patch15072: CVE-2026-23473.patch

#CVE-2026-23442
Patch15073: CVE-2026-23442.patch

#CVE-2026-23394
Patch15074: CVE-2026-23394.patch

#CVE-2026-23389
Patch15075: CVE-2026-23389.patch

#CVE-2026-23374
Patch15076: CVE-2026-23374.patch
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
%setup -q -n linux-6.12.80
%autosetup -p1 -n linux-6.12.80
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

find . \( -name 'Makefile*' -o -name 'Kconfig*' -o -name '*.pl' \) | xargs sh -c 'cp --parents "$@" %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}' copy
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
%{_datadir}/perf-core/strace/groups/file
%{_datadir}/perf-core/strace/groups/string
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
* Mon Apr 20 2026 Lishan Liu <lishan.liu@intel.com> - 6.12.80-1
- Update kernel to 6.12.80-1

* Thu Feb 05 2026 Lishan Liu <lishan.liu@intel.com> - 6.12.67-1
- Update kernel to 6.12.67-1
- lts-v6.12.67-emt-cve-260128T180434Z

* Fri Jan 9 2026 Lishan Liu <lishan.liu@intel.com> - 6.12.61-2
- Update kernel to 6.12.61-2
- lts-v6.12.61-emt-cve-260106T193826Z
- Kenrel config update to support lontium audio

* Fri Jan 2 2026 Lishan Liu <lishan.liu@intel.com> - 6.12.61-1
- Update kernel to 6.12.61

* Thu Dec 11 2025 Lishan Liu <lishan.liu@intel.com> - 6.12.59-1
- Update kernel to 6.12.59

* Thu Nov 27 2025 Lishan Liu <lishan.liu@intel.com> - 6.12.55-2
- Update audio and virtio gpu kernel config

* Tue Nov 18 2025 Lishan Liu <lishan.liu@intel.com> - 6.12.55-1
- Update kernel to 6.12.55

* Fri Nov 14 2025 Lishan Liu <lishan.liu@intel.com> - 6.12.44-6
- Update audio support in kernel config

* Tue Nov 4 2025 Lishan Liu <lishan.liu@intel.com> - 6.12.44-5
- Update kernel config

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
