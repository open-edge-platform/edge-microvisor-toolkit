Summary:        Linux Kernel
Name:           kernel
Version:        6.12.61
Release:        1%{?dist}
License:        GPLv2
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://www.kernel.org/pub/linux/kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.12.61.tar.gz
Source1:        config
Source3:        sha512hmac-openssl.sh
Source4:        emt-ca-20211013.pem
Source5:        cpupower
Source6:        cpupower.service


# Intel not-upstreamed kernel features
# Series file for v6.12.61 linux kernel
# dcbeffaf66d03 Linux 6.12.61
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
Patch384: 0001-drm-i915-no-force-probe-needed-for-mtl-platform.drm
#rapl
Patch385: 0001-powercap-intel_rapl-Add-support-for-Bartlett-Lake-pl.rapl
#misc
Patch386: 0001-Add-security.md-file.misc
#iommu
Patch387: 0001-driver-core-add-a-faux-bus-for-use-when-a-simple-dev.iommu
Patch388: 0002-iommu-io-pgtable-arm-dynamically-allocate-selftest-d.iommu
#emt-drm
Patch389: 0075-drm-xe-gsc-mei-interrupt-top-half-should-be-in-irq-d.patch
#CVE-2025-21709
Patch390: CVE-2025-21709.patch

#CVE-2025-21817
Patch391: CVE-2025-21817.patch

#CVE-2025-22104
Patch392: CVE-2025-22104.patch

#CVE-2025-22108
Patch393: CVE-2025-22108.patch

#CVE-2025-22111
Patch394: CVE-2025-22111.patch

#CVE-2025-22116
Patch395: CVE-2025-22116.patch

#CVE-2025-22117
Patch396: CVE-2025-22117.patch

#CVE-2025-23131
Patch397: CVE-2025-23131.patch

#CVE-2025-37746
Patch398: CVE-2025-37746.patch
Patch399: CVE-2025-37746-1.patch

#CVE-2025-37906
Patch400: CVE-2025-37906.patch

#CVE-2025-38041
Patch401: CVE-2025-38041.patch
Patch402: CVE-2025-38041-1.patch
Patch403: CVE-2025-38041-2.patch

#CVE-2025-38029
Patch404: CVE-2025-38029.patch

#CVE-2025-38311
Patch405: CVE-2025-38311.patch

#CVE-2025-38248
Patch406: CVE-2025-38248.patch

#CVE-2025-38234
Patch407: CVE-2025-38234.patch

#CVE-2025-38207
Patch408: CVE-2025-38207.patch

#CVE-2025-38137
Patch409: CVE-2025-38137.patch

#CVE-2025-40325
Patch410: CVE-2025-40325.patch

#CVE-2025-38284
Patch411: CVE-2025-38284.patch
Patch412: CVE-2025-38284-1.patch
Patch413: CVE-2025-38284-2.patch

#CVE-2025-38199
Patch414: CVE-2025-38199.patch

#CVE-2025-38140
Patch415: CVE-2025-38140.patch

#CVE-2025-38132
Patch416: CVE-2025-38132.patch
Patch417: CVE-2025-38132-1.patch

#CVE-2025-37743
Patch418: CVE-2025-37743.patch

#CVE-2025-23132
Patch419: CVE-2025-23132.patch

#CVE-2025-22127
Patch420: CVE-2025-22127.patch

#CVE-2025-22109
Patch421: CVE-2025-22109.patch

#CVE-2025-21752
Patch422: CVE-2025-21752.patch
Patch423: CVE-2025-21752-1.patch

#CVE-2024-58095
Patch424: CVE-2024-58095.patch

#CVE-2024-58094
Patch425: CVE-2024-58094.patch

#CVE-2024-52560
Patch426: CVE-2024-52560.patch
Patch427: CVE-2024-52560-1.patch

#CVE-2025-38621
Patch428: CVE-2025-38621.patch

#CVE-2025-38627
Patch429: CVE-2025-38627.patch

#CVE-2025-39789
Patch430: CVE-2025-39789.patch

#CVE-2025-39764
Patch431: CVE-2025-39764.patch

#CVE-2025-39745
Patch432: CVE-2025-39745.patch

#CVE-2025-39677
Patch433: CVE-2025-39677.patch

#CVE-2025-39933
Patch434: CVE-2025-39933.patch

#CVE-2025-39833
Patch435: CVE-2025-39833.patch

#CVE-2025-39925
Patch436: CVE-2025-39925.patch

#CVE-2025-39905
Patch437: CVE-2025-39905.patch

#CVE-2025-39859
Patch438: CVE-2025-39859.patch

#CVE-2025-39910
Patch439: CVE-2025-39910.patch

#CVE-2025-40098
Patch440: CVE-2025-40098.patch

#CVE-2025-40075
Patch441: CVE-2025-40075.patch
Patch442: CVE-2025-40075-1.patch

#CVE-2025-40074
Patch443: CVE-2025-40074.patch

#CVE-2025-40064
Patch444: CVE-2025-40064.patch

#CVE-2025-40086
Patch445: CVE-2025-40086.patch
Patch446: CVE-2025-40086-1.patch

#CVE-2025-40168
Patch447: CVE-2025-40168.patch

#CVE-2025-40170
Patch448: CVE-2025-40170.patch

#CVE-2025-40164
Patch449: CVE-2025-40164.patch

#CVE-2025-40158
Patch450: CVE-2025-40158.patch

#CVE-2025-40149
Patch451: CVE-2025-40149.patch

#CVE-2025-40147
Patch452: CVE-2025-40147.patch

#CVE-2025-40139
Patch453: CVE-2025-40139.patch

#CVE-2025-40136
Patch454: CVE-2025-40136.patch

#CVE-2025-40135
Patch455: CVE-2025-40135.patch

#CVE-2025-40130
Patch456: CVE-2025-40130.patch

#CVE-2025-38656
Patch457: CVE-2025-38656.patch
Patch458: CVE-2025-38656-2.patch

#CVE-2025-38591
Patch459: CVE-2025-38591.patch

#CVE-2025-38584
Patch460: CVE-2025-38584.patch

#CVE-2025-40215
Patch461: CVE-2025-40215.patch

# CVE Patches

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
%setup -q -n linux-6.12.61
%autosetup -p1 -n linux-6.12.61
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
