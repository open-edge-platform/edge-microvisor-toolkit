Summary:        Preempt RT Linux Kernel
Name:           kernel-rt
Version:        6.12.59
Release:        1%{?dist}
License:        GPLv2
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://www.kernel.org/pub/linux/kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.12.59.tar.gz
Source1:        config
Source3:        sha512hmac-openssl.sh
Source4:        emt-ca-20211013.pem
Source5:        cpupower
Source6:        cpupower.service


# Intel not-upstreamed kernel features
# d5dc97879a97 Linux 6.12.59
#sriov
Patch0: 0001-drm-i915-mtl-Add-C10-table-for-HDMI-Clock-25175.sriov
Patch1: 0002-drm-i915-mtl-Copy-c10-phy-pll-sw-state-from-master-t.sriov
Patch2: 0003-drm-i915-guc-Define-MAX_DWORDS-for-CTB-HXG-Message.sriov
Patch3: 0004-drm-i915-call-taint_for_CI-on-FLR-failure.sriov
Patch4: 0005-drm-i915-huc-load-HuC-via-non-POR-GSC-engine-flow.sriov
Patch5: 0006-drm-i915-SR-IOV-Enabling-and-Support.sriov
Patch6: 0007-Revert-drm-i915-move-platform_engine_mask-and-memory.sriov
Patch7: 0008-drm-i915-gt-Enable-the-early-register-to-working-win.sriov
Patch8: 0009-drm-i915-gt-Modify-the-adls-mocs-table-same-as-tgl-m.sriov
Patch9: 0010-drm-i915-Bypass-gem_set_tiling-and-gem_get_tiling.sriov
Patch10: 0011-drm-i915-enable-CCS-on-DG1-and-TGL-for-testing.sriov
Patch11: 0012-drm-i915-force-VF-using-v70-GuC-API.sriov
Patch12: 0013-drm-i915-fix-regression-on-sriov-vf-failures-due-to-.sriov
Patch13: 0014-drm-i915-add-null-pointer-protection-inside-intel_fb.sriov
Patch14: 0015-drm-i915-use-the-original-Wa_14010685332-for-PCH_ADP.sriov
Patch15: 0016-drm-i915-fix-bitmap-clear-API-region-start-issue.sriov
Patch16: 0017-drm-i915-iov-Expose-early-runtime-registers-for-MTL.sriov
Patch17: 0018-drm-i915-gt-fix-empty-workaround-list-access-issue.sriov
Patch18: 0019-drm-i915-mtl-Add-module-parameter-override-for-Wa_16.sriov
Patch19: 0020-drm-i915-mtl-Provide-user-the-option-to-disable-ccs.sriov
Patch20: 0021-drm-i915-mtl-Turn-on-Wa_16019325821-Wa_14019159160-b.sriov
Patch21: 0022-drm-i915-pf-Use-GPU-to-set-PTE-owner.sriov
Patch22: 0023-drm-i915-pf-Use-GPU-to-set-PTE-owner-on-platforms-wi.sriov
Patch23: 0024-drm-i915-access-ddc-pointer-only-if-it-is-available.sriov
Patch24: 0025-drm-i915-guc-Upgrade-GuC-fw-version-to-70.20.0.sriov
Patch25: 0026-drm-i915-iov-Adding-runtime-reg-for-MTL-HuC-status.sriov
Patch26: 0027-drm-i915-guc-Upgrade-GuC-fw-version-to-70.29.2.sriov
Patch27: 0028-drm-i915-Re-add-enable_rc6-modparam.sriov
Patch28: 0032-drm-virtio-freeze-and-restore-hooks-to-support-suspe.sriov
Patch29: 0033-drm-virtio-save-and-restore-virtio_gpu_objects.sriov
Patch30: 0001-drm-virtio-Use-drm_gem_plane_helper_prepare_fb.patch
Patch31: 0034-drm-i915-pf-Introduce-i915_ggtt_save_ptes-and-i915_g.sriov
Patch32: 0035-drm-i915-iov-Introduce-VFs-shadow-copy-of-GGTT-on-PF.sriov
Patch33: 0036-drm-i915-iov-Shadow-GGTT-mock-selftestes.sriov
Patch34: 0037-drm-i915-gt-Don-t-support-GGTT-save-restore-via-BAR-.sriov
Patch35: 0038-drm-i915-pf-Add-helpers-for-saving-loading-GGTT-stat.sriov
Patch36: 0039-drm-i915-pf-Handle-VF-pause-complete-notification.sriov
Patch37: 0040-drm-i915-pf-Allow-to-save-restore-GuC-VF-state.sriov
Patch38: 0041-drm-i915-pf-Save-and-restore-VFs-state-during-S2idle.sriov
Patch39: 0042-drm-i915-pf-Skip-VF-save-restore-on-S2idle-S3-S4-if-.sriov
Patch40: 0043-drm-i915-pf-Start-use-shadow-GGTT-to-save-restore-du.sriov
Patch41: 0044-drm-i915-pf-Export-API-to-be-used-by-i915-vfio-pci.sriov
Patch42: 0045-drm-i915-iov-Flag-which-tells-whether-PAUSE-is-in-pr.sriov
Patch43: 0046-drm-i915-iov-Remember-run-state-on-suspend-and-resto.sriov
Patch44: 0047-drm-i915-pf-Pause-VF-before-restore-GuC-state-after-.sriov
Patch45: 0048-drm-i915-iov-fix-i915-sriov-build-issue.sriov
Patch46: 0001-drm-i915-CTB-TLB-invalidation-fix-on-VM.sriov
Patch47: 0002-vfio-i915-Add-vfio_pci-driver-for-Intel-graphics.sriov
Patch48: 0003-drm-i915-guc-Upgrade-GuC-fw-version-to-70.36.0.sriov
Patch49: 0001-drm-i915-Fix-logic-for-GUC-Process.sriov
Patch50: 0001-vfio-i915-Add-support-for-MMIO-save-restore.sriov
Patch51: 0002-drm-i915-SR-IOV-Save-Restore-Feature-support.sriov
Patch52: 0001-i915-Enable-w-a-16026508708.sriov
Patch53: 0001-virtio-hookup-irq_get_affinity-callback.sriov
Patch54: 0002-virtio-break-and-reset-virtio-devices-on-device_shut.sriov
Patch55: 0003-virtgpu-don-t-reset-on-shutdown.sriov
Patch56: 0004-drm-virtio-implement-virtio_gpu_shutdown.sriov
Patch57: 0001-drm-virtio-Wait-until-the-control-and-cursor-queues-.sriov
Patch58: 0001-drm-i915-move-sriov-selftest-buffer-out-of-stack.sriov
Patch59: 0001-drm-i915-Do-not-advertise-about-CCS.sriov
#security
Patch60: 0001-mei-bus-add-api-to-query-capabilities-of-ME-clien.security
Patch61: 0002-mei-virtio-virtualization-frontend-driver.security
Patch62: 0003-INTEL_DII-mei-avoid-reset-if-fw-is-down.security
Patch63: 0004-INTEL_DII-FIXME-mei-iaf-add-iaf-Intel-Accelerator.security
Patch64: 0005-INTEL_DII-mei-add-check-for-offline-bit-in-every-.security
Patch65: 0006-INTEL_DII-mei-add-empty-handlers-for-ops-function.security
Patch66: 0007-INTEL_DII-mei-gsc-add-fields-to-support-force-wak.security
Patch67: 0008-INTEL_DII-mei-add-waitqueue-for-device-state-chan.security
Patch68: 0009-INTEL_DII-mei-add-force-wake-workaround-infra.security
Patch69: 0010-INTEL_DII-mei-add-force-wake-workaround-in-init.security
Patch70: 0011-INTEL_DII-mei-add-force-wake-workaround-on-sessio.security
Patch71: 0012-INTEL_DII-mei-add-force-wake-workaround-in-runtim.security
Patch72: 0013-INTEL_DII-mei-add-force-wake-workaround-in-resume.security
Patch73: 0014-INTEL_DII-mei-disable-immediate-enum-if-forcewake.security
Patch74: 0015-INTEL_DII-mei-put-force-wake-in-error-flows.security
Patch75: 0016-INTEL_DII-mei-add-force-wake-callbacks-to-empty-h.security
Patch76: 0017-INTEL_DII-mei-optimize-force-wake-wait.security
Patch77: 0018-mei-me-apply-GSC-error-supression-to-systems-with.security
Patch78: 0019-INTEL_DII-mei-bus-fixup-disable-version-retrieval.security
#tgpio
Patch79: 0001-Revert-timekeeping-Add-function-to-convert-realtime-.tgpio
Patch80: 0002-Revert-x86-tsc-Remove-obsolete-ART-to-TSC-conversion.tgpio
Patch81: 0003-Revert-ice-ptp-Remove-convert_art_to_tsc.tgpio
Patch82: 0004-Revert-ALSA-hda-Remove-convert_art_to_tsc.tgpio
Patch83: 0005-Revert-stmmac-intel-Remove-convert_art_to_tsc.tgpio
Patch84: 0006-Revert-igc-Remove-convert_art_ns_to_tsc.tgpio
Patch85: 0007-Revert-e1000e-Replace-convert_art_to_tsc.tgpio
Patch86: 0008-Revert-x86-tsc-Provide-ART-base-clock-information-fo.tgpio
Patch87: 0009-Revert-timekeeping-Provide-infrastructure-for-conver.tgpio
Patch88: 0010-drivers-ptp-Add-Enhanced-handling-of-reserve-fields.tgpio
Patch89: 0011-drivers-ptp-Add-PEROUT2-ioctl-frequency-adjustment-i.tgpio
Patch90: 0012-drivers-ptp-Add-user-space-input-polling-interface.tgpio
Patch91: 0013-x86-tsc-Add-TSC-support-functions-to-support-ART-dri.tgpio
Patch92: 0014-drivers-ptp-Add-support-for-PMC-Time-Aware-GPIO-Driv.tgpio
Patch93: 0015-x86-core-TSC-reliable-kernel-arg-prevents-DQ-of-TSC-.tgpio
Patch94: 0016-mfd-intel-ehl-gpio-Introduce-MFD-framework-to-PSE-GP.tgpio
Patch95: 0017-TGPIO-Calling-power-management-calls-without-enterin.tgpio
Patch96: 0018-TGPIO-Fix-PSE-TGPIO-PTP-driver-ioctls-fail.tgpio
Patch97: 0019-Kernel-Argument-Bypassing-ART-Detection.tgpio
Patch98: 0020-GPIO-Fix-for-PSE-GPIO-generating-only-one-event-as-i.tgpio
Patch99: 0021-Added-TGPIO-pin-check-before-input-event-read.tgpio
Patch100: 0022-Added-an-Example-to-adjust-frequency-for-output.tgpio
Patch101: 0023-ptp-tgpio-PSE-TGPIO-crosststamp-counttstamp.tgpio
Patch102: 0024-ptp-Fixed-read-issue-on-PHC-with-zero-n_pins.tgpio
Patch103: 0025-ptp-S-W-workaround-for-PMC-TGPIO-h-w-bug.tgpio
Patch104: 0026-ptp-Fix-for-PSE-TGPIO-Oneshot-output-and-counttstamp.tgpio
Patch105: 0027-ptp-Fix-for-PSE-TGPIO-frequency-Adjustment-issue.tgpio
Patch106: 0028-tgpio-Fix-compilation-errors-for-PSE-TGPIO.tgpio
Patch107: 0029-Added-single-shot-output-mode-support-for-TGPIO.tgpio
Patch108: 0030-Added-an-example-to-poll-for-edges.tgpio
Patch109: 0031-Added-support-to-get-TGPIO-System-Clock-Offset.tgpio
Patch110: 0032-Added-single-shot-output-mode-option-for-TGPIO-pin.tgpio
Patch111: 0033-selftests-ptp-Added-COMPV-GPIO-Input-Mode-for-TGPIO.tgpio
Patch112: 0034-ptp-Introduce-PTP_PINDESC_INPUTPOLL-for-Intel-PMC-TG.tgpio
Patch113: 0035-drivers-ptp-Add-COMPV-GPIO-Mode-for-PSE-TGPIO.tgpio
Patch114: 0036-net-ice-fix-braces-around-scalar-initializer.tgpio
Patch115: 0037-ptp-Add-PTP_EVENT_COUNTER_MODE-in-v1-valid-flags.tgpio
Patch116: 0038-ptp-Enable-preempt-if-it-is-disabled.tgpio
Patch117: 0039-ptp-Generate-sqaure-wave-on-PSE-TGPIO.tgpio
Patch118: 0040-ptp-tgpio-Add-an-edge-if-the-output-signal-ends-high.tgpio
Patch119: 0041-ptp-pmc-tgpio-Initialize-variable-to-zero.tgpio
Patch120: 0042-ptp-tgpio-Fix-return-type-of-remove-function-in-tgpi.tgpio
Patch121: 0043-net-mlx5-reuse-convert_art_ns_to_tsc-to-convert-ART-.tgpio
#edac
Patch122: 0001-x86-mce-Add-MCACOD-code-for-generic-I-O-error.edac
Patch123: 0002-EDAC-ieh-Add-I-O-device-EDAC-driver-for-Intel-CPUs-wi.edac
Patch124: 0003-EDAC-ieh-Add-I-O-device-EDAC-support-for-Intel-Tiger-.edac
Patch125: 0004-EDAC-igen6-Add-registration-APIs-for-In-Band-ECC-erro.edac
Patch126: 0005-EDAC-i10nm-Print-DRAM-rules-debug-purpose.edac
Patch127: 0006-EDAC-skx_common-skx-i10nm-Make-skx_register_mci-indep.edac
Patch128: 0007-EDAC-skx_common-Prepare-skx_get_edac_list.edac
Patch129: 0008-EDAC-skx_common-Prepare-skx_set_hi_lo.edac
Patch130: 0009-EDAC-igen6-Add-Intel-Pnther-Lake-H-SoCs-support.edac
Patch131: 0002-EDAC-ie31200-Add-Kaby-Lake-S-dual-core-host-bridge-ID.edac
Patch132: 0006-EDAC-ie31200-Fix-the-3rd-parameter-name-of-populate_d.edac
Patch133: 0007-EDAC-ie31200-Simplify-the-pci_device_id-table.edac
Patch134: 0008-EDAC-ie31200-Make-the-memory-controller-resources-con.edac
Patch135: 0009-EDAC-ie31200-Make-struct-dimm_data-contain-decoded-in.edac
Patch136: 0010-EDAC-ie31200-Fold-the-two-channel-loops-into-one-loop.edac
Patch137: 0011-EDAC-ie31200-Break-up-ie31200_probe1.edac
Patch138: 0012-EDAC-ie31200-Add-Intel-Raptor-Lake-S-SoCs-support.edac
Patch139: 0013-EDAC-ie31200-Switch-Raptor-Lake-S-to-interrupt-mode.edac
Patch140: 0001-EDAC-ie31200-Add-two-Intel-SoCs-for-EDAC-support.edac
Patch141: 0002-ie31200-EDAC-Add-Intel-Bartlett-Lake-S-SoCs-support.edac
Patch142: 0001-EDAC-igen6-Add-Intel-Amston-Lake-SoCs-support.edac
Patch143: 0002-EDAC-igen6-Add-additional-Intel-Amston-Lake-SoC-compu.edac
Patch144: 0001-EDAC-igen6-Initialize-edac_op_state-according-to-the-.edac
Patch145: 0002-EDAC-igen6-Add-polling-support.edac
Patch146: 0003-EDAC-igen6-Fix-the-flood-of-invalid-error-reports.edac
Patch147: 0004-EDAC-igen6-Constify-struct-res_config.edac
Patch148: 0005-EDAC-igen6-Skip-absent-memory-controllers.edac
Patch149: 0006-EDAC-igen6-Fix-NULL-pointer-dereference.edac
#tsn
Patch150: 0001-net-pcs-xpcs-enable-xpcs-reset-skipping.tsn
Patch151: 0002-net-stmmac-Bugfix-on-stmmac_interrupt-for-WOL.tsn
Patch152: 0003-net-phy-increase-gpy-loopback-test-delay.tsn
Patch153: 0004-net-stmmac-Resolve-poor-line-rate-after-switching-from.tsn
Patch154: 0005-net-phy-dp83867-perform-restart-AN-after-modifying-AN-.tsn
Patch155: 0006-stmmac-intel-Separate-ADL-N-and-RPL-P-device-ID-from-T.tsn
Patch156: 0007-net-stmmac-Adjust-mac_capabilities-for-Intel-mGbE-2.5G.tsn
Patch157: 0008-stmmac-intel-skip-xpcs-reset-for-2.5Gbps-on-Intel-Alde.tsn
Patch158: 0009-net-stmmac-add-check-for-2.5G-mode-to-prevent-MAC-capa.tsn
Patch159: 0010-stmmac-intel-Enable-PHY-WoL-in-ADL-N.tsn
Patch160: 0011-net-phy-reconfigure-PHY-WoL-when-WoL-option-is-enabled.tsn
Patch161: 0012-net-stmmac-fix-MAC-and-phylink-mismatch-issue-after-re.tsn
Patch162: 0013-net-stmmac-restructure-Rx-Tx-hardware-timestamping-fun.tsn
Patch163: 0014-net-stmmac-Add-per-packet-time-based-scheduling-for-XD.tsn
Patch164: 0015-net-stmmac-introduce-AF_XDP-ZC-RX-HW-timestamps.tsn
Patch165: 0016-net-stmmac-add-fsleep-in-HW-Rx-timestamp-checking-loop.tsn
Patch166: 0017-net-stmmac-select-PCS-negotiation-mode-according-to-th.tsn
Patch167: 0018-net-pcs-xpcs-re-initiate-clause-37-Auto-negotiation.tsn
Patch168: 0019-arch-x86-Add-IPC-mailbox-accessor-function-and-add-SoC.tsn
Patch169: 0020-net-stmmac-configure-SerDes-according-to-the-interface.tsn
Patch170: 0021-stmmac-intel-interface-switching-support-for-intel-pla.tsn
Patch171: 0022-net-stmmac-Set-mac_managed_pm-flag-from-stmmac-to-reso.tsn
Patch172: 0023-net-phylink-Add-module_exit.tsn
Patch173: 0024-net-stmmac-introduce-AF_XDP-ZC-TX-HW-timestamps.tsn
Patch174: 0025-net-sched-taprio-fix-too-early-schedules-switching.tsn
Patch175: 0026-net-sched-taprio-fix-cycle-time-adjustment-for-next-en.tsn
Patch176: 0027-net-sched-taprio-fix-impacted-fields-value-during-cycl.tsn
Patch177: 0028-net-sched-taprio-get-corrected-value-of-cycle_time-and.tsn
Patch178: 0029-xsk-add-txtime-field-in-xdp_desc-struct.tsn
Patch179: 0030-Revert-net-stmmac-silence-FPE-kernel-logs.tsn
Patch180: 0031-Revert-net-stmmac-support-fp-parameter-of-tc-taprio.tsn
Patch181: 0032-Revert-net-stmmac-support-fp-parameter-of-tc-mqprio.tsn
Patch182: 0033-Revert-net-stmmac-configure-FPE-via-ethtool-mm.tsn
Patch183: 0034-Revert-net-stmmac-refactor-FPE-verification-process.tsn
Patch184: 0035-Revert-net-stmmac-drop-stmmac_fpe_handshake.tsn
Patch185: 0036-Revert-net-stmmac-move-stmmac_fpe_cfg-to-stmmac_priv-d.tsn
Patch186: 0037-net-stmmac-add-FPE-preempt-setting-for-TxQ-preemptible.tsn
Patch187: 0038-taprio-Add-support-for-frame-preemption-offload.tsn
Patch188: 0039-net-stmmac-set-initial-EEE-policy-configuration.tsn
Patch189: 0040-net-phy-fix-phylib-s-dual-eee_enabled.tsn
Patch190: 0041-net-phy-ensure-that-genphy_c45_an_config_eee_aneg-sees.tsn
Patch191: 0042-net-phy-fix-phy_ethtool_set_eee-incorrectly-enabling-L.tsn
Patch192: 0001-igc-Set-the-RX-packet-buffer-size-for-TSN-mode.tsn
Patch193: 0002-igc-Only-dump-registers-if-configured-to-dump-HW-infor.tsn
Patch194: 0003-ethtool-Add-support-for-configuring-frame-preemption.tsn
Patch195: 0004-ethtool-Add-support-for-Frame-Preemption-verification.tsn
Patch196: 0005-igc-Add-support-for-enabling-frame-preemption-via-etht.tsn
Patch197: 0006-igc-Add-support-for-TC_SETUP_PREEMPT.tsn
Patch198: 0007-igc-Add-support-for-setting-frame-preemption-configura.tsn
Patch199: 0008-igc-Add-support-for-Frame-Preemption-verification.tsn
Patch200: 0009-igc-Add-support-for-exposing-frame-preemption-stats-re.tsn
Patch201: 0010-igc-Optimize-the-packet-buffer-utilization.tsn
Patch202: 0011-igc-Add-support-for-enabling-all-packets-to-be-receive.tsn
Patch203: 0012-igc-Add-support-for-DMA-timestamp-for-non-PTP-packets.tsn
Patch204: 0013-bpf-add-btf-register-unregister-API.tsn
Patch205: 0014-net-core-XDP-metadata-BTF-netlink-API.tsn
Patch206: 0015-rtnetlink-Fix-unchecked-return-value-of-dev_xdp_query_.tsn
Patch207: 0016-rtnetlink-Add-return-value-check.tsn
Patch208: 0017-tools-bpf-Query-XDP-metadata-BTF-ID.tsn
Patch209: 0018-tools-bpf-Add-xdp-set-command-for-md-btf.tsn
Patch210: 0019-igc-Add-BTF-based-metadata-for-XDP.tsn
Patch211: 0020-igc-Enable-HW-RX-Timestamp-for-AF_XDP-ZC.tsn
Patch212: 0021-igc-Take-care-of-DMA-timestamp-rollover.tsn
Patch213: 0022-igc-Add-SO_TXTIME-for-AF_XDP-ZC.tsn
Patch214: 0023-igc-Reodering-the-empty-packet-buffers-and-descriptors.tsn
Patch215: 0024-Revert-igc-Add-support-for-PTP-.getcyclesx64.tsn
Patch216: 0025-core-Introduce-netdev_tc_map_to_queue_mask.tsn
Patch217: 0026-taprio-Replace-tc_map_to_queue_mask.tsn
Patch218: 0027-mqprio-Add-support-for-frame-preemption-offload.tsn
Patch219: 0030-igc-Reduce-retry-count-to-a-more-reasonable-number.tsn
Patch220: 0001-igc-Enable-HW-TX-Timestamp-for-AF_XDP-ZC.tsn
Patch221: 0002-igc-Enable-trace-for-HW-TX-Timestamp-AF_XDP-ZC.tsn
Patch222: 0003-igc-Remove-the-CONFIG_DEBUG_MISC-condition-for-trace.tsn
Patch223: 0006-Revert-net-stmmac-set-initial-EEE-policy-configurati.tsn
Patch224: 0001-net-phy-Set-eee_cfg.eee_enabled-according-to-PHY.tsn
Patch225: 0001-Revert-net-stmmac-add-FPE-preempt-setting-for-TxQ-pree.tsn
Patch226: 0002-Reapply-net-stmmac-move-stmmac_fpe_cfg-to-stmmac_priv-.tsn
Patch227: 0003-Reapply-net-stmmac-drop-stmmac_fpe_handshake.tsn
Patch228: 0004-Reapply-net-stmmac-refactor-FPE-verification-process.tsn
Patch229: 0005-Reapply-net-stmmac-configure-FPE-via-ethtool-mm.tsn
Patch230: 0006-Reapply-net-stmmac-support-fp-parameter-of-tc-mqprio.tsn
Patch231: 0007-Reapply-net-stmmac-support-fp-parameter-of-tc-taprio.tsn
Patch232: 0008-Reapply-net-stmmac-silence-FPE-kernel-logs.tsn
#camera
Patch233: 0001-media-intel-ipu6-remove-buttress-ish-structure.camera
Patch234: 0001-media-i2c-Add-ar0234-camera-sensor-driver.camera
Patch235: 0002-media-i2c-add-support-for-lt6911uxe.camera
Patch236: 0003-INT3472-Support-LT6911UXE.camera
Patch237: 0004-upstream-Use-module-parameter-to-set-isys-freq.camera
Patch238: 0005-upstream-Use-module-parameter-to-set-psys-freq.camera
Patch239: 0006-media-pci-Enable-ISYS-reset.camera
Patch240: 0007-media-i2c-add-support-for-ar0234-and-lt6911uxe.camera
Patch241: 0008-driver-media-i2c-remove-useless-header-file.camera
Patch242: 0009-media-i2c-update-lt6911uxe-for-upstream-and-bug-fix.camera
Patch243: 0010-media-i2c-add-support-for-lt6911uxc.camera
Patch244: 0011-media-i2c-add-lt6911uxc-driver-and-enable-in-ipu-br.camera
Patch245: 0012-media-pci-intel-psys-driver.camera
Patch246: 0013-media-i2c-Remove-unused-variables-in-Lontium-driver.camera
Patch247: 0001-media-intel-ipu6-remove-buttress-ish-structure-1.camera
Patch248: 0002-media-pci-intel-include-psys-driver.camera
Patch249: 0003-Revert-media-ipu6-use-the-IPU6-DMA-mapping-APIs-to-.camera
Patch250: 0004-Revert-media-ipu6-remove-architecture-DMA-ops-depen.camera
Patch251: 0005-Revert-media-ipu6-not-override-the-dma_ops-of-devic.camera
Patch252: 0001-Reapply-media-ipu6-not-override-the-dma_ops-of-devi.camera
Patch253: 0002-Reapply-media-ipu6-remove-architecture-DMA-ops-depe.camera
Patch254: 0003-Reapply-media-ipu6-use-the-IPU6-DMA-mapping-APIs-to.camera
Patch255: 0001-media-pci-update-IPU6-PSYS-driver.camera
Patch256: 0002-media-i2c-update-lt6911uxc-driver-to-fix-COV-issue.camera
Patch257: 0003-lt6911-2-pads-linked-to-ipu-2-ports-for-split-mode.camera
Patch258: 0004-media-i2c-add-dv_timings-api-in-lt6911uxe.camera
Patch259: 0005-media-intel-ipu6-use-vc1-dma-for-MTL-and-ARL.camera
Patch260: 0006-media-i2c-some-changes-in-lt6911uxe.camera
Patch261: 0001-Revert-media-intel-ipu6-use-vc1-dma-for-MTL-and-ARL.camera
Patch262: 0002-media-i2c-update-format-in-irq-for-lt6911uxe.camera
Patch263: 0003-media-i2c-remove-unused-func-in-lt6911uxe.camera
Patch264: 0001-media-intel-ipu6-use-vc1-dma-for-MTL-and-ARL.camera
Patch265: 0002-media-ipu-Dma-sync-at-buffer_prepare-callback-as-DM.camera
Patch266: 0003-Support-IPU6-ISYS-FW-trace-dump-for-upstream-driver.camera
Patch267: 0004-Support-IPU6-PSYS-FW-trace-dump-for-upstream-driver.camera
Patch268: 0005-media-pci-The-order-of-return-buffers-should-be-FIF.camera
Patch269: 0006-media-i2c-fix-power-on-issue-for-on-board-LT6911UXC.camera
Patch270: 0007-media-i2c-fix-power-on-issue-for-on-board-LT6911UXE.camera
Patch271: 0001-media-pci-Modify-enble-disable-stream-in-CSI2.camera
Patch272: 0002-media-pci-Set-the-correct-SOF-for-different-stream.camera
Patch273: 0003-media-pci-support-imx390-for-6.11.0-rc3.camera
Patch274: 0004-i2c-media-fix-cov-issue.camera
Patch275: 0005-mv-ipu-acpi-module-to-linux-drivers.camera
Patch276: 0006-kernel-enable-VC-support-in-v4l2.camera
Patch277: 0007-media-pci-intel-support-PDATA-in-Kconfig-Makefile.camera
Patch278: 0008-media-pci-unregister-i2c-device-to-complete-ext_sub.camera
Patch279: 0009-media-pci-align-params-for-non-MIPI-split-and-split.camera
Patch280: 0010-media-pci-add-missing-if-for-PDATA.camera
Patch281: 0011-media-platform-fix-allyesconfig-build-error.camera
Patch282: 0012-media-pci-refine-PDATA-related-config.camera
Patch283: 0013-kernel-align-ACPI-PDATA-and-ACPI-fwnode-build-for-E.camera
Patch284: 0014-media-i2c-add-gmsl-isx031-support.camera
Patch285: 0015-media-i2c-add-support-for-isx031-max9296.camera
Patch286: 0016-fix-S4-issue-on-TWL.camera
Patch287: 0017-code-changes-for-link-frequency-and-sensor-physical.camera
#wwan
Patch288: 0001-Revert-bus-mhi-host-pci_generic-add-support-for-sc828.wwan
Patch289: 0002-wwan-add-SAHARA-device.wwan
Patch290: 0003-bus-mhi-host-allow-SBL-as-initial-EE.wwan
Patch291: 0004-drivers-bus-mhi-let-userspace-manage-xfp-fw-update-st.wwan
Patch292: 0005-wwan-add-NMEA-type.wwan
Patch293: 0006-drivers-bus-mhi-add-FN980-v2-support.wwan
Patch294: 0007-drivers-bus-mhi-add-FN990-NMEA-and-DIAG-in-SBL-device.wwan
Patch295: 0008-drivers-net-wwan-add-simple-DTR-driver.wwan
Patch296: 0009-drivers-bus-mhi-host-fix-recovery-process-when-modem-.wwan
Patch297: 0001-Revert-drivers-bus-mhi-host-fix-recovery-process-when.wwan
Patch298: 0002-Revert-drivers-net-wwan-add-simple-DTR-driver.wwan
Patch299: 0003-Revert-drivers-bus-mhi-add-FN990-NMEA-and-DIAG-in-SBL.wwan
Patch300: 0004-Revert-drivers-bus-mhi-add-FN980-v2-support.wwan
Patch301: 0005-Revert-wwan-add-NMEA-type.wwan
Patch302: 0006-Revert-drivers-bus-mhi-let-userspace-manage-xfp-fw-up.wwan
Patch303: 0007-Revert-bus-mhi-host-allow-SBL-as-initial-EE.wwan
Patch304: 0008-Revert-wwan-add-SAHARA-device.wwan
Patch305: 0009-Revert-Revert-bus-mhi-host-pci_generic-add-support-fo.wwan
#pmc_core
Patch306: 0001-platform-x86-intel-pmc-Add-Arrow-Lake-U-H-support.pmc_core
Patch307: 0002-platform-x86-intel-pmc-Add-Bartlett-Lake-support-to-.pmc_core
Patch308: 0001-platform-x86-intel-pmc-Fix-Arrow-Lake-U-H-NPU-PCI.pmc_core
#lpss
Patch309: 0001-Added-spi_set_cs-for-more-stable-r-w-operations-in-S.lpss
Patch310: 0002-mtd-core-Don-t-fail-mtd_device_parse_register-if-OTP.lpss
Patch311: 0003-spi-intel-pci-Add-support-for-Arrow-Lake-H-SPI-seria.lpss
Patch312: 0004-spi-intel-Add-protected-and-locked-attributes.lpss
#preempt_rt patches backported
Patch313: 0001-Revert-sched-core-Remove-the-unnecessary-need_resche.rt
Patch314: 0001-hrtimer-Use-__raise_softirq_irqoff-to-raise-the-softirq.rt
Patch315: 0002-timers-Use-__raise_softirq_irqoff-to-raise-the-softirq.rt
Patch316: 0003-softirq-Use-a-dedicated-thread-for-timer-wakeups-on-PRE.rt
Patch317: 0004-serial-8250-Switch-to-nbcon-console.rt
Patch318: 0005-serial-8250-Revert-drop-lockdep-annotation-from-serial8.rt
Patch319: 0006-locking-rt-Remove-one-__cond_lock-in-RT-s-spin_trylock_.rt
Patch320: 0007-locking-rt-Add-sparse-annotation-for-RCU.rt
Patch321: 0008-locking-rt-Annotate-unlock-followed-by-lock-for-sparse.rt
Patch322: 0009-drm-i915-Use-preempt_disable-enable_rt-where-recommende.rt
Patch323: 0010-drm-i915-Don-t-disable-interrupts-on-PREEMPT_RT-during-.rt
Patch324: 0011-drm-i915-Don-t-check-for-atomic-context-on-PREEMPT_RT.rt
Patch325: 0012-drm-i915-Disable-tracing-points-on-PREEMPT_RT.rt
Patch326: 0013-drm-i915-gt-Use-spin_lock_irq-instead-of-local_irq_disa.rt
Patch327: 0014-drm-i915-Drop-the-irqs_disabled-check.rt
Patch328: 0015-drm-i915-guc-Consider-also-RCU-depth-in-busy-loop.rt
Patch329: 0016-Revert-drm-i915-Depend-on-PREEMPT_RT.rt
Patch330: 0017-sched-Add-TIF_NEED_RESCHED_LAZY-infrastructure.rt
Patch331: 0018-sched-Add-Lazy-preemption-model.rt
Patch332: 0019-sched-Enable-PREEMPT_DYNAMIC-for-PREEMPT_RT.rt
Patch333: 0020-sched-x86-Enable-Lazy-preemption.rt
Patch334: 0021-sched-Add-laziest-preempt-model.rt
Patch335: 0022-sched-Fixup-the-IS_ENABLED-check-for-PREEMPT_LAZY.rt
Patch336: 0023-tracing-Remove-TRACE_FLAG_IRQS_NOSUPPORT.rt
Patch337: 0024-tracing-Record-task-flag-NEED_RESCHED_LAZY.rt
Patch338: 0025-sysfs-Add-sys-kernel-realtime-entry.rt
Patch339: 0001-serial-8250-enable-original-console-by-default.rt
Patch340: 0001-kernel-trace-Add-DISALLOW_TRACE_PRINTK-make-option.rt
Patch341: 0002-Revert-scripts-remove-bin2c.rt
Patch342: 0003-extend-uio-driver-to-supports-msix.rt
Patch343: 0004-virtio-add-VIRTIO_PMD-support.rt
Patch344: 0005-virt-acrn-Introduce-interfaces-for-PIO-device.rt
Patch345: 0006-Add-hypercall-to-access-MSR.rt
Patch346: 0007-Revert-spi-Remove-unused-function-spi_busnum_to_master.rt
Patch347: 0008-igc-add-CONFIG_IGC_TSN_TRACE-conditional-trace_printk-u.rt
Patch348: 0009-stmmac_pci-add-CONFIG_STMMAC_TSN_TRACE-conditional-trac.rt
Patch349: 0010-igb-prepare-for-AF_XDP-zero-copy-support.rt
Patch350: 0011-igb-Introduce-XSK-data-structures-and-helpers.rt
Patch351: 0012-igb-add-AF_XDP-zero-copy-Rx-support.rt
Patch352: 0013-igb-add-AF_XDP-zero-copy-Tx-support.rt
Patch353: 0014-igb-Add-BTF-based-metadata-for-XDP.rt
Patch354: 0015-ANDROID-trace-power-add-trace_clock_set_parent.rt
Patch355: 0016-ANDROID-trace-net-use-pK-for-kernel-pointers.rt
Patch356: 0017-ANDROID-trace-add-non-hierarchical-function_graph-optio.rt
Patch357: 0018-virtio-fix-VIRTIO_PMD-support.rt
Patch358: 0019-drm-i915-add-i915-perf-event-capacity.rt
Patch359: 0020-drm-xe-pm-allow-xe-with-CONFIG_PM.rt
#drm
Patch360: 0001-drm-i915-enable-guc-submission-for-ADLs-by-default.drm
Patch361: 0001-drm-i915-disable-a-couple-of-RT-functions-if-RT-is-d.drm
Patch362: 0001-drm-i915-disable-dGPU-support-with-RT-kernel.drm
Patch363: 0001-i915-Update-GUC-to-v70.44.1-for-i915-platforms.drm
Patch364: 0001-Revert-drm-i915-disable-dGPU-support-with-RT-kernel.drm
Patch365: 0001-drm-i915-gt-Avoid-using-masked-workaround-for-CCS_MODE.drm
Patch366: 0002-drm-i915-gt-Move-the-CCS-mode-variable-to-a-global-pos.drm
Patch367: 0003-drm-i915-gt-Allow-the-creation-of-multi-mode-CCS-masks.drm
Patch368: 0004-drm-i915-gt-Refactor-uabi-engine-class-instance-list-c.drm
Patch369: 0005-drm-i915-gem-Mark-and-verify-UABI-engine-validity.drm
Patch370: 0006-drm-i915-gt-Introduce-for_each_enabled_engine-and-appl.drm
Patch371: 0007-drm-i915-gt-Manage-CCS-engine-creation-within-UABI-exp.drm
Patch372: 0008-drm-i915-gt-Remove-cslices-mask-value-from-the-CCS-str.drm
Patch373: 0009-drm-i915-gt-Expose-the-number-of-total-CCS-slices.drm
Patch374: 0010-drm-i915-gt-Store-engine-related-sysfs-kobjects.drm
Patch375: 0011-drm-i915-gt-Store-active-CCS-mask.drm
Patch376: 0012-drm-i915-Protect-access-to-the-UABI-engines-list-with-.drm
Patch377: 0013-drm-i915-gt-Isolate-single-sysfs-engine-file-creation.drm
Patch378: 0014-drm-i915-gt-Implement-creation-and-removal-routines-fo.drm
Patch379: 0015-drm-i915-gt-Allow-the-user-to-change-the-CCS-mode-thro.drm
Patch380: 0016-drm-i915-gt-Refactor-CCS-mode-handling-and-improve-app.drm
Patch381: 0017-drm-i915-no-waiting-for-page-flip-in-vpp-case.drm
Patch382: 0001-Remove-unneeded-files.patch
Patch383: 0001-i915-gt-Upgrade-GuC-70.44.1-70.49.4.drm
#rapl
Patch384: 0001-powercap-intel_rapl-Add-support-for-Bartlett-Lake-pl.rapl
#misc
Patch385: 0001-Add-security.md-file.misc
#iommu
Patch386: 0001-driver-core-add-a-faux-bus-for-use-when-a-simple-dev.iommu
Patch387: 0002-iommu-io-pgtable-arm-dynamically-allocate-selftest-d.iommu
#emt-drm
Patch388: 0075-drm-xe-gsc-mei-interrupt-top-half-should-be-in-irq-d.patch
#CVE-2025-21709
Patch389: CVE-2025-21709.patch
#CVE-2025-21817
Patch390: CVE-2025-21817.patch
#CVE-2025-22104
Patch391: CVE-2025-22104.patch
#CVE-2025-22108
Patch392: CVE-2025-22108.patch
#CVE-2025-22111
Patch393: CVE-2025-22111.patch
#CVE-2025-22116
Patch394: CVE-2025-22116.patch
#CVE-2025-22117
Patch395: CVE-2025-22117.patch
#CVE-2025-23131
Patch396: CVE-2025-23131.patch
#CVE-2025-37746
Patch397: CVE-2025-37746.patch
Patch398: CVE-2025-37746-1.patch
#CVE-2025-37906
Patch399: CVE-2025-37906.patch
#CVE-2025-38041
Patch400: CVE-2025-38041.patch
Patch401: CVE-2025-38041-1.patch
Patch402: CVE-2025-38041-2.patch
#CVE-2025-38029
Patch403: CVE-2025-38029.patch
#CVE-2025-38311
Patch404: CVE-2025-38311.patch
#CVE-2025-38248
Patch405: CVE-2025-38248.patch
#CVE-2025-38234
Patch406: CVE-2025-38234.patch
#CVE-2025-38207
Patch407: CVE-2025-38207.patch
#CVE-2025-38137
Patch408: CVE-2025-38137.patch
#CVE-2025-40325
Patch409: CVE-2025-40325.patch
#CVE-2025-38284
Patch410: CVE-2025-38284.patch
Patch411: CVE-2025-38284-1.patch
Patch412: CVE-2025-38284-2.patch
#CVE-2025-38199
Patch413: CVE-2025-38199.patch
#CVE-2025-38140
Patch414: CVE-2025-38140.patch
#CVE-2025-38132
Patch415: CVE-2025-38132.patch
Patch416: CVE-2025-38132-1.patch
#CVE-2025-37743
Patch417: CVE-2025-37743.patch
#CVE-2025-23132
Patch418: CVE-2025-23132.patch
#CVE-2025-22127
Patch419: CVE-2025-22127.patch
#CVE-2025-22109
Patch420: CVE-2025-22109.patch
#CVE-2025-21752
Patch421: CVE-2025-21752.patch
Patch422: CVE-2025-21752-1.patch
#CVE-2024-58095
Patch423: CVE-2024-58095.patch
#CVE-2024-58094
Patch424: CVE-2024-58094.patch
#CVE-2024-52560
Patch425: CVE-2024-52560.patch
Patch426: CVE-2024-52560-1.patch
#CVE-2025-38621
Patch427: CVE-2025-38621.patch
#CVE-2025-38627
Patch428: CVE-2025-38627.patch
#CVE-2025-39789
Patch429: CVE-2025-39789.patch
#CVE-2025-39764
Patch430: CVE-2025-39764.patch
#CVE-2025-39745
Patch431: CVE-2025-39745.patch
#CVE-2025-39677
Patch432: CVE-2025-39677.patch
#CVE-2025-39933
Patch433: CVE-2025-39933.patch
#CVE-2025-39833
Patch434: CVE-2025-39833.patch
#CVE-2025-39925
Patch435: CVE-2025-39925.patch
#CVE-2025-39905
Patch436: CVE-2025-39905.patch
#CVE-2025-39859
Patch437: CVE-2025-39859.patch
#CVE-2025-39910
Patch438: CVE-2025-39910.patch
#CVE-2025-40098
Patch439: CVE-2025-40098.patch
#CVE-2025-40075
Patch440: CVE-2025-40075.patch
Patch441: CVE-2025-40075-1.patch
#CVE-2025-40074
Patch442: CVE-2025-40074.patch
#CVE-2025-40064
Patch443: CVE-2025-40064.patch
#CVE-2025-40086
Patch444: CVE-2025-40086.patch
Patch445: CVE-2025-40086-1.patch
#CVE-2025-40168
Patch446: CVE-2025-40168.patch
#CVE-2025-40170
Patch447: CVE-2025-40170.patch
#CVE-2025-40164
Patch448: CVE-2025-40164.patch
#CVE-2025-40158
Patch449: CVE-2025-40158.patch
#CVE-2025-40149
Patch450: CVE-2025-40149.patch
#CVE-2025-40147
Patch451: CVE-2025-40147.patch
#CVE-2025-40139
Patch452: CVE-2025-40139.patch
#CVE-2025-40136
Patch453: CVE-2025-40136.patch
#CVE-2025-40135
Patch454: CVE-2025-40135.patch
#CVE-2025-40130
Patch455: CVE-2025-40130.patch
#CVE-2025-38656
Patch456: CVE-2025-38656.patch
Patch457: CVE-2025-38656-2.patch
#CVE-2025-38591
Patch458: CVE-2025-38591.patch
#CVE-2025-38584
Patch459: CVE-2025-38584.patch
# CVE Patches

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
%setup -q -n linux-6.12.59
%autosetup -p1 -n linux-6.12.59
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
