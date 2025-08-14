Summary:        Preempt RT Linux Kernel
Name:           kernel-rt
Version:        6.12.39
Release:        1%{?dist}
License:        GPLv2
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://www.kernel.org/pub/linux/kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.12.39.tar.gz
Source1:        config
Source3:        sha512hmac-openssl.sh
Source4:        emt-ca-20211013.pem
Source5:        cpupower
Source6:        cpupower.service

# Release tag: lts-v6.12.39-emt-250721T212915Z
# Intel not-upstreamed kernel features
#sriov
Patch0:         0001-drm-i915-mtl-Add-C10-table-for-HDMI-Clock-25175.sriov
Patch1:         0002-drm-i915-mtl-Copy-c10-phy-pll-sw-state-from-master-t.sriov
Patch2:         0003-drm-i915-guc-Define-MAX_DWORDS-for-CTB-HXG-Message.sriov
Patch3:         0004-drm-i915-call-taint_for_CI-on-FLR-failure.sriov
Patch4:         0005-drm-i915-huc-load-HuC-via-non-POR-GSC-engine-flow.sriov
Patch5:         0006-drm-i915-SR-IOV-Enabling-and-Support.sriov
Patch6:         0007-Revert-drm-i915-move-platform_engine_mask-and-memory.sriov
Patch7:         0008-drm-i915-gt-Enable-the-early-register-to-working-win.sriov
Patch8:         0009-drm-i915-gt-Modify-the-adls-mocs-table-same-as-tgl-m.sriov
Patch9:         0010-drm-i915-Bypass-gem_set_tiling-and-gem_get_tiling.sriov
Patch10:        0011-drm-i915-enable-CCS-on-DG1-and-TGL-for-testing.sriov
Patch11:        0012-drm-i915-force-VF-using-v70-GuC-API.sriov
Patch12:        0013-drm-i915-fix-regression-on-sriov-vf-failures-due-to-.sriov
Patch13:        0014-drm-i915-add-null-pointer-protection-inside-intel_fb.sriov
Patch14:        0015-drm-i915-use-the-original-Wa_14010685332-for-PCH_ADP.sriov
Patch15:        0016-drm-i915-fix-bitmap-clear-API-region-start-issue.sriov
Patch16:        0017-drm-i915-iov-Expose-early-runtime-registers-for-MTL.sriov
Patch17:        0018-drm-i915-gt-fix-empty-workaround-list-access-issue.sriov
Patch18:        0019-drm-i915-mtl-Add-module-parameter-override-for-Wa_16.sriov
Patch19:        0020-drm-i915-mtl-Provide-user-the-option-to-disable-ccs.sriov
Patch20:        0021-drm-i915-mtl-Turn-on-Wa_16019325821-Wa_14019159160-b.sriov
Patch21:        0022-drm-i915-pf-Use-GPU-to-set-PTE-owner.sriov
Patch22:        0023-drm-i915-pf-Use-GPU-to-set-PTE-owner-on-platforms-wi.sriov
Patch23:        0024-drm-i915-access-ddc-pointer-only-if-it-is-available.sriov
Patch24:        0025-drm-i915-guc-Upgrade-GuC-fw-version-to-70.20.0.sriov
Patch25:        0026-drm-i915-iov-Adding-runtime-reg-for-MTL-HuC-status.sriov
Patch26:        0027-drm-i915-guc-Upgrade-GuC-fw-version-to-70.29.2.sriov
Patch27:        0028-drm-i915-Re-add-enable_rc6-modparam.sriov
Patch28:        0032-drm-virtio-freeze-and-restore-hooks-to-support-suspe.sriov
Patch29:        0033-drm-virtio-save-and-restore-virtio_gpu_objects.sriov
Patch30:        0001-drm-virtio-Use-drm_gem_plane_helper_prepare_fb.patch
Patch31:        0034-drm-i915-pf-Introduce-i915_ggtt_save_ptes-and-i915_g.sriov
Patch32:        0035-drm-i915-iov-Introduce-VFs-shadow-copy-of-GGTT-on-PF.sriov
Patch33:        0036-drm-i915-iov-Shadow-GGTT-mock-selftestes.sriov
Patch34:        0037-drm-i915-gt-Don-t-support-GGTT-save-restore-via-BAR-.sriov
Patch35:        0038-drm-i915-pf-Add-helpers-for-saving-loading-GGTT-stat.sriov
Patch36:        0039-drm-i915-pf-Handle-VF-pause-complete-notification.sriov
Patch37:        0040-drm-i915-pf-Allow-to-save-restore-GuC-VF-state.sriov
Patch38:        0041-drm-i915-pf-Save-and-restore-VFs-state-during-S2idle.sriov
Patch39:        0042-drm-i915-pf-Skip-VF-save-restore-on-S2idle-S3-S4-if-.sriov
Patch40:        0043-drm-i915-pf-Start-use-shadow-GGTT-to-save-restore-du.sriov
Patch41:        0044-drm-i915-pf-Export-API-to-be-used-by-i915-vfio-pci.sriov
Patch42:        0045-drm-i915-iov-Flag-which-tells-whether-PAUSE-is-in-pr.sriov
Patch43:        0046-drm-i915-iov-Remember-run-state-on-suspend-and-resto.sriov
Patch44:        0047-drm-i915-pf-Pause-VF-before-restore-GuC-state-after-.sriov
Patch45:        0048-drm-i915-iov-fix-i915-sriov-build-issue.sriov
Patch46:        0001-drm-i915-CTB-TLB-invalidation-fix-on-VM.sriov
Patch47:        0002-vfio-i915-Add-vfio_pci-driver-for-Intel-graphics.sriov
Patch48:        0003-drm-i915-guc-Upgrade-GuC-fw-version-to-70.36.0.sriov
Patch49:        0001-drm-i915-Fix-logic-for-GUC-Process.sriov
Patch50:        0001-vfio-i915-Add-support-for-MMIO-save-restore.sriov
Patch51:        0002-drm-i915-SR-IOV-Save-Restore-Feature-support.sriov
Patch52:        0001-i915-Enable-w-a-16026508708.sriov
#security
Patch53:        0001-mei-bus-add-api-to-query-capabilities-of-ME-clien.security
Patch54:        0002-mei-virtio-virtualization-frontend-driver.security
Patch55:        0003-INTEL_DII-mei-avoid-reset-if-fw-is-down.security
Patch56:        0004-INTEL_DII-FIXME-mei-iaf-add-iaf-Intel-Accelerator.security
Patch57:        0005-INTEL_DII-mei-add-check-for-offline-bit-in-every-.security
Patch58:        0006-INTEL_DII-mei-add-empty-handlers-for-ops-function.security
Patch59:        0007-INTEL_DII-mei-gsc-add-fields-to-support-force-wak.security
Patch60:        0008-INTEL_DII-mei-add-waitqueue-for-device-state-chan.security
Patch61:        0009-INTEL_DII-mei-add-force-wake-workaround-infra.security
Patch62:        0010-INTEL_DII-mei-add-force-wake-workaround-in-init.security
Patch63:        0011-INTEL_DII-mei-add-force-wake-workaround-on-sessio.security
Patch64:        0012-INTEL_DII-mei-add-force-wake-workaround-in-runtim.security
Patch65:        0013-INTEL_DII-mei-add-force-wake-workaround-in-resume.security
Patch66:        0014-INTEL_DII-mei-disable-immediate-enum-if-forcewake.security
Patch67:        0015-INTEL_DII-mei-put-force-wake-in-error-flows.security
Patch68:        0016-INTEL_DII-mei-add-force-wake-callbacks-to-empty-h.security
Patch69:        0017-INTEL_DII-mei-optimize-force-wake-wait.security
Patch70:        0018-mei-me-apply-GSC-error-supression-to-systems-with.security
Patch71:        0019-INTEL_DII-mei-bus-fixup-disable-version-retrieval.security
#tgpio
Patch72:        0001-Revert-timekeeping-Add-function-to-convert-realtime-.tgpio
Patch73:        0002-Revert-x86-tsc-Remove-obsolete-ART-to-TSC-conversion.tgpio
Patch74:        0003-Revert-ice-ptp-Remove-convert_art_to_tsc.tgpio
Patch75:        0004-Revert-ALSA-hda-Remove-convert_art_to_tsc.tgpio
Patch76:        0005-Revert-stmmac-intel-Remove-convert_art_to_tsc.tgpio
Patch77:        0006-Revert-igc-Remove-convert_art_ns_to_tsc.tgpio
Patch78:        0007-Revert-e1000e-Replace-convert_art_to_tsc.tgpio
Patch79:        0008-Revert-x86-tsc-Provide-ART-base-clock-information-fo.tgpio
Patch80:        0009-Revert-timekeeping-Provide-infrastructure-for-conver.tgpio
Patch81:        0010-drivers-ptp-Add-Enhanced-handling-of-reserve-fields.tgpio
Patch82:        0011-drivers-ptp-Add-PEROUT2-ioctl-frequency-adjustment-i.tgpio
Patch83:        0012-drivers-ptp-Add-user-space-input-polling-interface.tgpio
Patch84:        0013-x86-tsc-Add-TSC-support-functions-to-support-ART-dri.tgpio
Patch85:        0014-drivers-ptp-Add-support-for-PMC-Time-Aware-GPIO-Driv.tgpio
Patch86:        0015-x86-core-TSC-reliable-kernel-arg-prevents-DQ-of-TSC-.tgpio
Patch87:        0016-mfd-intel-ehl-gpio-Introduce-MFD-framework-to-PSE-GP.tgpio
Patch88:        0017-TGPIO-Calling-power-management-calls-without-enterin.tgpio
Patch89:        0018-TGPIO-Fix-PSE-TGPIO-PTP-driver-ioctls-fail.tgpio
Patch90:        0019-Kernel-Argument-Bypassing-ART-Detection.tgpio
Patch91:        0020-GPIO-Fix-for-PSE-GPIO-generating-only-one-event-as-i.tgpio
Patch92:        0021-Added-TGPIO-pin-check-before-input-event-read.tgpio
Patch93:        0022-Added-an-Example-to-adjust-frequency-for-output.tgpio
Patch94:        0023-ptp-tgpio-PSE-TGPIO-crosststamp-counttstamp.tgpio
Patch95:        0024-ptp-Fixed-read-issue-on-PHC-with-zero-n_pins.tgpio
Patch96:        0025-ptp-S-W-workaround-for-PMC-TGPIO-h-w-bug.tgpio
Patch97:        0026-ptp-Fix-for-PSE-TGPIO-Oneshot-output-and-counttstamp.tgpio
Patch98:        0027-ptp-Fix-for-PSE-TGPIO-frequency-Adjustment-issue.tgpio
Patch99:        0028-tgpio-Fix-compilation-errors-for-PSE-TGPIO.tgpio
Patch100:       0029-Added-single-shot-output-mode-support-for-TGPIO.tgpio
Patch101:       0030-Added-an-example-to-poll-for-edges.tgpio
Patch102:       0031-Added-support-to-get-TGPIO-System-Clock-Offset.tgpio
Patch103:       0032-Added-single-shot-output-mode-option-for-TGPIO-pin.tgpio
Patch104:       0033-selftests-ptp-Added-COMPV-GPIO-Input-Mode-for-TGPIO.tgpio
Patch105:       0034-ptp-Introduce-PTP_PINDESC_INPUTPOLL-for-Intel-PMC-TG.tgpio
Patch106:       0035-drivers-ptp-Add-COMPV-GPIO-Mode-for-PSE-TGPIO.tgpio
Patch107:       0036-net-ice-fix-braces-around-scalar-initializer.tgpio
Patch108:       0037-ptp-Add-PTP_EVENT_COUNTER_MODE-in-v1-valid-flags.tgpio
Patch109:       0038-ptp-Enable-preempt-if-it-is-disabled.tgpio
Patch110:       0039-ptp-Generate-sqaure-wave-on-PSE-TGPIO.tgpio
Patch111:       0040-ptp-tgpio-Add-an-edge-if-the-output-signal-ends-high.tgpio
Patch112:       0041-ptp-pmc-tgpio-Initialize-variable-to-zero.tgpio
Patch113:       0042-ptp-tgpio-Fix-return-type-of-remove-function-in-tgpi.tgpio
Patch114:       0043-net-mlx5-reuse-convert_art_ns_to_tsc-to-convert-ART-.tgpio
#edac
Patch115:       0001-x86-mce-Add-MCACOD-code-for-generic-I-O-error.edac
Patch116:       0002-EDAC-ieh-Add-I-O-device-EDAC-driver-for-Intel-CPUs-wi.edac
Patch117:       0003-EDAC-ieh-Add-I-O-device-EDAC-support-for-Intel-Tiger-.edac
Patch118:       0004-EDAC-igen6-Add-registration-APIs-for-In-Band-ECC-erro.edac
Patch119:       0005-EDAC-i10nm-Print-DRAM-rules-debug-purpose.edac
Patch120:       0006-EDAC-skx_common-skx-i10nm-Make-skx_register_mci-indep.edac
Patch121:       0007-EDAC-skx_common-Prepare-skx_get_edac_list.edac
Patch122:       0008-EDAC-skx_common-Prepare-skx_set_hi_lo.edac
Patch123:       0009-EDAC-igen6-Add-Intel-Pnther-Lake-H-SoCs-support.edac
Patch124:       0002-EDAC-ie31200-Add-Kaby-Lake-S-dual-core-host-bridge-ID.edac
Patch125:       0006-EDAC-ie31200-Fix-the-3rd-parameter-name-of-populate_d.edac
Patch126:       0007-EDAC-ie31200-Simplify-the-pci_device_id-table.edac
Patch127:       0008-EDAC-ie31200-Make-the-memory-controller-resources-con.edac
Patch128:       0009-EDAC-ie31200-Make-struct-dimm_data-contain-decoded-in.edac
Patch129:       0010-EDAC-ie31200-Fold-the-two-channel-loops-into-one-loop.edac
Patch130:       0011-EDAC-ie31200-Break-up-ie31200_probe1.edac
Patch131:       0012-EDAC-ie31200-Add-Intel-Raptor-Lake-S-SoCs-support.edac
Patch132:       0013-EDAC-ie31200-Switch-Raptor-Lake-S-to-interrupt-mode.edac
Patch133:       0001-EDAC-ie31200-Add-two-Intel-SoCs-for-EDAC-support.edac
Patch134:       0002-ie31200-EDAC-Add-Intel-Bartlett-Lake-S-SoCs-support.edac
#tsn
Patch135:       0001-net-pcs-xpcs-enable-xpcs-reset-skipping.tsn
Patch136:       0002-net-stmmac-Bugfix-on-stmmac_interrupt-for-WOL.tsn
Patch137:       0003-net-phy-increase-gpy-loopback-test-delay.tsn
Patch138:       0004-net-stmmac-Resolve-poor-line-rate-after-switching-from.tsn
Patch139:       0005-net-phy-dp83867-perform-restart-AN-after-modifying-AN-.tsn
Patch140:       0006-stmmac-intel-Separate-ADL-N-and-RPL-P-device-ID-from-T.tsn
Patch141:       0007-net-stmmac-Adjust-mac_capabilities-for-Intel-mGbE-2.5G.tsn
Patch142:       0008-stmmac-intel-skip-xpcs-reset-for-2.5Gbps-on-Intel-Alde.tsn
Patch143:       0009-net-stmmac-add-check-for-2.5G-mode-to-prevent-MAC-capa.tsn
Patch144:       0010-stmmac-intel-Enable-PHY-WoL-in-ADL-N.tsn
Patch145:       0011-net-phy-reconfigure-PHY-WoL-when-WoL-option-is-enabled.tsn
Patch146:       0012-net-stmmac-fix-MAC-and-phylink-mismatch-issue-after-re.tsn
Patch147:       0013-net-stmmac-restructure-Rx-Tx-hardware-timestamping-fun.tsn
Patch148:       0014-net-stmmac-Add-per-packet-time-based-scheduling-for-XD.tsn
Patch149:       0015-net-stmmac-introduce-AF_XDP-ZC-RX-HW-timestamps.tsn
Patch150:       0016-net-stmmac-add-fsleep-in-HW-Rx-timestamp-checking-loop.tsn
Patch151:       0017-net-stmmac-select-PCS-negotiation-mode-according-to-th.tsn
Patch152:       0018-net-pcs-xpcs-re-initiate-clause-37-Auto-negotiation.tsn
Patch153:       0019-arch-x86-Add-IPC-mailbox-accessor-function-and-add-SoC.tsn
Patch154:       0020-net-stmmac-configure-SerDes-according-to-the-interface.tsn
Patch155:       0021-stmmac-intel-interface-switching-support-for-intel-pla.tsn
Patch156:       0022-net-stmmac-Set-mac_managed_pm-flag-from-stmmac-to-reso.tsn
Patch157:       0023-net-phylink-Add-module_exit.tsn
Patch158:       0024-net-stmmac-introduce-AF_XDP-ZC-TX-HW-timestamps.tsn
Patch159:       0025-net-sched-taprio-fix-too-early-schedules-switching.tsn
Patch160:       0026-net-sched-taprio-fix-cycle-time-adjustment-for-next-en.tsn
Patch161:       0027-net-sched-taprio-fix-impacted-fields-value-during-cycl.tsn
Patch162:       0028-net-sched-taprio-get-corrected-value-of-cycle_time-and.tsn
Patch163:       0029-xsk-add-txtime-field-in-xdp_desc-struct.tsn
Patch164:       0030-Revert-net-stmmac-silence-FPE-kernel-logs.tsn
Patch165:       0031-Revert-net-stmmac-support-fp-parameter-of-tc-taprio.tsn
Patch166:       0032-Revert-net-stmmac-support-fp-parameter-of-tc-mqprio.tsn
Patch167:       0033-Revert-net-stmmac-configure-FPE-via-ethtool-mm.tsn
Patch168:       0034-Revert-net-stmmac-refactor-FPE-verification-process.tsn
Patch169:       0035-Revert-net-stmmac-drop-stmmac_fpe_handshake.tsn
Patch170:       0036-Revert-net-stmmac-move-stmmac_fpe_cfg-to-stmmac_priv-d.tsn
Patch171:       0037-net-stmmac-add-FPE-preempt-setting-for-TxQ-preemptible.tsn
Patch172:       0038-taprio-Add-support-for-frame-preemption-offload.tsn
Patch173:       0039-net-stmmac-set-initial-EEE-policy-configuration.tsn
Patch174:       0040-net-phy-fix-phylib-s-dual-eee_enabled.tsn
Patch175:       0041-net-phy-ensure-that-genphy_c45_an_config_eee_aneg-sees.tsn
Patch176:       0042-net-phy-fix-phy_ethtool_set_eee-incorrectly-enabling-L.tsn
Patch177:       0001-igc-Set-the-RX-packet-buffer-size-for-TSN-mode.tsn
Patch178:       0002-igc-Only-dump-registers-if-configured-to-dump-HW-infor.tsn
Patch179:       0003-ethtool-Add-support-for-configuring-frame-preemption.tsn
Patch180:       0004-ethtool-Add-support-for-Frame-Preemption-verification.tsn
Patch181:       0005-igc-Add-support-for-enabling-frame-preemption-via-etht.tsn
Patch182:       0006-igc-Add-support-for-TC_SETUP_PREEMPT.tsn
Patch183:       0007-igc-Add-support-for-setting-frame-preemption-configura.tsn
Patch184:       0008-igc-Add-support-for-Frame-Preemption-verification.tsn
Patch185:       0009-igc-Add-support-for-exposing-frame-preemption-stats-re.tsn
Patch186:       0010-igc-Optimize-the-packet-buffer-utilization.tsn
Patch187:       0011-igc-Add-support-for-enabling-all-packets-to-be-receive.tsn
Patch188:       0012-igc-Add-support-for-DMA-timestamp-for-non-PTP-packets.tsn
Patch189:       0013-bpf-add-btf-register-unregister-API.tsn
Patch190:       0014-net-core-XDP-metadata-BTF-netlink-API.tsn
Patch191:       0015-rtnetlink-Fix-unchecked-return-value-of-dev_xdp_query_.tsn
Patch192:       0016-rtnetlink-Add-return-value-check.tsn
Patch193:       0017-tools-bpf-Query-XDP-metadata-BTF-ID.tsn
Patch194:       0018-tools-bpf-Add-xdp-set-command-for-md-btf.tsn
Patch195:       0019-igc-Add-BTF-based-metadata-for-XDP.tsn
Patch196:       0020-igc-Enable-HW-RX-Timestamp-for-AF_XDP-ZC.tsn
Patch197:       0021-igc-Take-care-of-DMA-timestamp-rollover.tsn
Patch198:       0022-igc-Add-SO_TXTIME-for-AF_XDP-ZC.tsn
Patch199:       0023-igc-Reodering-the-empty-packet-buffers-and-descriptors.tsn
Patch200:       0024-Revert-igc-Add-support-for-PTP-.getcyclesx64.tsn
Patch201:       0025-core-Introduce-netdev_tc_map_to_queue_mask.tsn
Patch202:       0026-taprio-Replace-tc_map_to_queue_mask.tsn
Patch203:       0027-mqprio-Add-support-for-frame-preemption-offload.tsn
Patch204:       0030-igc-Reduce-retry-count-to-a-more-reasonable-number.tsn
Patch205:       0001-igc-Enable-HW-TX-Timestamp-for-AF_XDP-ZC.tsn
Patch206:       0002-igc-Enable-trace-for-HW-TX-Timestamp-AF_XDP-ZC.tsn
Patch207:       0003-igc-Remove-the-CONFIG_DEBUG_MISC-condition-for-trace.tsn
Patch208:       0006-Revert-net-stmmac-set-initial-EEE-policy-configurati.tsn
Patch209:       0001-net-phy-Set-eee_cfg.eee_enabled-according-to-PHY.tsn
Patch210:       0001-Revert-net-stmmac-add-FPE-preempt-setting-for-TxQ-pree.tsn
Patch211:       0002-Reapply-net-stmmac-move-stmmac_fpe_cfg-to-stmmac_priv-.tsn
Patch212:       0003-Reapply-net-stmmac-drop-stmmac_fpe_handshake.tsn
Patch213:       0004-Reapply-net-stmmac-refactor-FPE-verification-process.tsn
Patch214:       0005-Reapply-net-stmmac-configure-FPE-via-ethtool-mm.tsn
Patch215:       0006-Reapply-net-stmmac-support-fp-parameter-of-tc-mqprio.tsn
Patch216:       0007-Reapply-net-stmmac-support-fp-parameter-of-tc-taprio.tsn
Patch217:       0008-Reapply-net-stmmac-silence-FPE-kernel-logs.tsn
#camera
Patch218:	0001-media-intel-ipu6-remove-buttress-ish-structure.camera
Patch219:	0001-media-i2c-Add-ar0234-camera-sensor-driver.camera
Patch220:	0002-media-i2c-add-support-for-lt6911uxe.camera
Patch221:	0003-INT3472-Support-LT6911UXE.camera
Patch222:	0004-upstream-Use-module-parameter-to-set-isys-freq.camera
Patch223:	0005-upstream-Use-module-parameter-to-set-psys-freq.camera
Patch224:	0006-media-pci-Enable-ISYS-reset.camera
Patch225:	0007-media-i2c-add-support-for-ar0234-and-lt6911uxe.camera
Patch226:	0008-driver-media-i2c-remove-useless-header-file.camera
Patch227:	0009-media-i2c-update-lt6911uxe-for-upstream-and-bug-fix.camera
Patch228:	0010-media-i2c-add-support-for-lt6911uxc.camera
Patch229:	0011-media-i2c-add-lt6911uxc-driver-and-enable-in-ipu-br.camera
Patch230:	0012-media-pci-intel-psys-driver.camera
Patch231:	0013-media-i2c-Remove-unused-variables-in-Lontium-driver.camera
Patch232:	0001-media-intel-ipu6-remove-buttress-ish-structure-1.camera
Patch233:	0002-media-pci-intel-include-psys-driver.camera
Patch234:	0003-Revert-media-ipu6-use-the-IPU6-DMA-mapping-APIs-to-.camera
Patch235:	0004-Revert-media-ipu6-remove-architecture-DMA-ops-depen.camera
Patch236:	0005-Revert-media-ipu6-not-override-the-dma_ops-of-devic.camera
Patch237:	0001-Reapply-media-ipu6-not-override-the-dma_ops-of-devi.camera
Patch238:	0002-Reapply-media-ipu6-remove-architecture-DMA-ops-depe.camera
Patch239:	0003-Reapply-media-ipu6-use-the-IPU6-DMA-mapping-APIs-to.camera
Patch240:	0001-media-pci-update-IPU6-PSYS-driver.camera
Patch241:	0002-media-i2c-update-lt6911uxc-driver-to-fix-COV-issue.camera
Patch242:	0003-lt6911-2-pads-linked-to-ipu-2-ports-for-split-mode.camera
Patch243:	0004-media-i2c-add-dv_timings-api-in-lt6911uxe.camera
Patch244:	0005-media-intel-ipu6-use-vc1-dma-for-MTL-and-ARL.camera
Patch245:	0006-media-i2c-some-changes-in-lt6911uxe.camera
Patch246:	0001-Revert-media-intel-ipu6-use-vc1-dma-for-MTL-and-ARL.camera
Patch247:	0002-media-i2c-update-format-in-irq-for-lt6911uxe.camera
Patch248:	0003-media-i2c-remove-unused-func-in-lt6911uxe.camera
Patch249:	0001-media-intel-ipu6-use-vc1-dma-for-MTL-and-ARL.camera
Patch250:	0002-media-ipu-Dma-sync-at-buffer_prepare-callback-as-DM.camera
Patch251:	0003-Support-IPU6-ISYS-FW-trace-dump-for-upstream-driver.camera
Patch252:	0004-Support-IPU6-PSYS-FW-trace-dump-for-upstream-driver.camera
Patch253:	0005-media-pci-The-order-of-return-buffers-should-be-FIF.camera
Patch254:	0006-media-i2c-fix-power-on-issue-for-on-board-LT6911UXC.camera
Patch255:	0007-media-i2c-fix-power-on-issue-for-on-board-LT6911UXE.camera
Patch256:	0001-media-pci-Modify-enble-disable-stream-in-CSI2.camera
Patch257:	0002-media-pci-Set-the-correct-SOF-for-different-stream.camera
Patch258:	0003-media-pci-support-imx390-for-6.11.0-rc3.camera
Patch259:	0004-i2c-media-fix-cov-issue.camera
Patch260:	0005-mv-ipu-acpi-module-to-linux-drivers.camera
Patch261:	0006-kernel-enable-VC-support-in-v4l2.camera
Patch262:	0007-media-pci-intel-support-PDATA-in-Kconfig-Makefile.camera
Patch263:	0008-media-pci-unregister-i2c-device-to-complete-ext_sub.camera
Patch264:	0009-media-pci-align-params-for-non-MIPI-split-and-split.camera
Patch265:	0010-media-pci-add-missing-if-for-PDATA.camera
Patch266:	0011-media-platform-fix-allyesconfig-build-error.camera
Patch267:	0012-media-pci-refine-PDATA-related-config.camera
Patch268:	0013-kernel-align-ACPI-PDATA-and-ACPI-fwnode-build-for-E.camera
Patch269:	0014-media-i2c-add-gmsl-isx031-support.camera
Patch270:	0015-media-i2c-add-support-for-isx031-max9296.camera
Patch271:	0016-fix-S4-issue-on-TWL.camera
Patch272:	0017-code-changes-for-link-frequency-and-sensor-physical.camera
#wwan
Patch273:	0001-Revert-bus-mhi-host-pci_generic-add-support-for-sc828.wwan
Patch274:	0002-wwan-add-SAHARA-device.wwan
Patch275:	0003-bus-mhi-host-allow-SBL-as-initial-EE.wwan
Patch276:	0004-drivers-bus-mhi-let-userspace-manage-xfp-fw-update-st.wwan
Patch277:	0005-wwan-add-NMEA-type.wwan
Patch278:	0006-drivers-bus-mhi-add-FN980-v2-support.wwan
Patch279:	0007-drivers-bus-mhi-add-FN990-NMEA-and-DIAG-in-SBL-device.wwan
Patch280:	0008-drivers-net-wwan-add-simple-DTR-driver.wwan
Patch281:	0009-drivers-bus-mhi-host-fix-recovery-process-when-modem-.wwan
Patch282:	0001-Revert-drivers-bus-mhi-host-fix-recovery-process-when.wwan
Patch283:	0002-Revert-drivers-net-wwan-add-simple-DTR-driver.wwan
Patch284:	0003-Revert-drivers-bus-mhi-add-FN990-NMEA-and-DIAG-in-SBL.wwan
Patch285:	0004-Revert-drivers-bus-mhi-add-FN980-v2-support.wwan
Patch286:	0005-Revert-wwan-add-NMEA-type.wwan
Patch287:	0006-Revert-drivers-bus-mhi-let-userspace-manage-xfp-fw-up.wwan
Patch288:	0007-Revert-bus-mhi-host-allow-SBL-as-initial-EE.wwan
Patch289:	0008-Revert-wwan-add-SAHARA-device.wwan
Patch290:	0009-Revert-Revert-bus-mhi-host-pci_generic-add-support-fo.wwan
#pmc_core
Patch291:	0001-platform-x86-intel-pmc-Add-Arrow-Lake-U-H-support.pmc_core
Patch292:	0002-platform-x86-intel-pmc-Add-Bartlett-Lake-support-to-.pmc_core
#lpss
Patch293:	0001-Added-spi_set_cs-for-more-stable-r-w-operations-in-S.lpss
Patch294:	0002-mtd-core-Don-t-fail-mtd_device_parse_register-if-OTP.lpss
Patch295:	0003-spi-intel-pci-Add-support-for-Arrow-Lake-H-SPI-seria.lpss
Patch296:	0004-spi-intel-Add-protected-and-locked-attributes.lpss
#preempt_rt patches backported
Patch297:	0001-Revert-sched-core-Remove-the-unnecessary-need_resche.rt
Patch298:	0001-hrtimer-Use-__raise_softirq_irqoff-to-raise-the-softirq.rt
Patch299:	0002-timers-Use-__raise_softirq_irqoff-to-raise-the-softirq.rt
Patch300:	0003-softirq-Use-a-dedicated-thread-for-timer-wakeups-on-PRE.rt
Patch301:	0004-serial-8250-Switch-to-nbcon-console.rt
Patch302:	0005-serial-8250-Revert-drop-lockdep-annotation-from-serial8.rt
Patch303:	0006-locking-rt-Remove-one-__cond_lock-in-RT-s-spin_trylock_.rt
Patch304:	0007-locking-rt-Add-sparse-annotation-for-RCU.rt
Patch305:	0008-locking-rt-Annotate-unlock-followed-by-lock-for-sparse.rt
Patch306:	0009-drm-i915-Use-preempt_disable-enable_rt-where-recommende.rt
Patch307:	0010-drm-i915-Don-t-disable-interrupts-on-PREEMPT_RT-during-.rt
Patch308:	0011-drm-i915-Don-t-check-for-atomic-context-on-PREEMPT_RT.rt
Patch309:	0012-drm-i915-Disable-tracing-points-on-PREEMPT_RT.rt
Patch310:	0013-drm-i915-gt-Use-spin_lock_irq-instead-of-local_irq_disa.rt
Patch311:	0014-drm-i915-Drop-the-irqs_disabled-check.rt
Patch312:	0015-drm-i915-guc-Consider-also-RCU-depth-in-busy-loop.rt
Patch313:	0016-Revert-drm-i915-Depend-on-PREEMPT_RT.rt
Patch314:	0017-sched-Add-TIF_NEED_RESCHED_LAZY-infrastructure.rt
Patch315:	0018-sched-Add-Lazy-preemption-model.rt
Patch316:	0019-sched-Enable-PREEMPT_DYNAMIC-for-PREEMPT_RT.rt
Patch317:	0020-sched-x86-Enable-Lazy-preemption.rt
Patch318:	0021-sched-Add-laziest-preempt-model.rt
Patch319:	0022-sched-Fixup-the-IS_ENABLED-check-for-PREEMPT_LAZY.rt
Patch320:	0023-tracing-Remove-TRACE_FLAG_IRQS_NOSUPPORT.rt
Patch321:	0024-tracing-Record-task-flag-NEED_RESCHED_LAZY.rt
Patch322:	0025-sysfs-Add-sys-kernel-realtime-entry.rt
Patch323:	0001-serial-8250-enable-original-console-by-default.rt
#drm
Patch324:	0001-drm-i915-enable-guc-submission-for-ADLs-by-default.drm
Patch325:	0001-drm-i915-disable-a-couple-of-RT-functions-if-RT-is-d.drm
Patch326:	0001-drm-i915-disable-dGPU-support-with-RT-kernel.drm
Patch327:	0001-i915-Update-GUC-to-v70.44.1-for-i915-platforms.drm
Patch328:	0001-Revert-drm-i915-disable-dGPU-support-with-RT-kernel.drm
Patch329:	0001-drm-i915-gt-Avoid-using-masked-workaround-for-CCS_MODE.drm
Patch330:	0002-drm-i915-gt-Move-the-CCS-mode-variable-to-a-global-pos.drm
Patch331:	0003-drm-i915-gt-Allow-the-creation-of-multi-mode-CCS-masks.drm
Patch332:	0004-drm-i915-gt-Refactor-uabi-engine-class-instance-list-c.drm
Patch333:	0005-drm-i915-gem-Mark-and-verify-UABI-engine-validity.drm
Patch334:	0006-drm-i915-gt-Introduce-for_each_enabled_engine-and-appl.drm
Patch335:	0007-drm-i915-gt-Manage-CCS-engine-creation-within-UABI-exp.drm
Patch336:	0008-drm-i915-gt-Remove-cslices-mask-value-from-the-CCS-str.drm
Patch337:	0009-drm-i915-gt-Expose-the-number-of-total-CCS-slices.drm
Patch338:	0010-drm-i915-gt-Store-engine-related-sysfs-kobjects.drm
Patch339:	0011-drm-i915-gt-Store-active-CCS-mask.drm
Patch340:	0012-drm-i915-Protect-access-to-the-UABI-engines-list-with-.drm
Patch341:	0013-drm-i915-gt-Isolate-single-sysfs-engine-file-creation.drm
Patch342:	0014-drm-i915-gt-Implement-creation-and-removal-routines-fo.drm
Patch343:	0015-drm-i915-gt-Allow-the-user-to-change-the-CCS-mode-thro.drm
Patch344:	0016-drm-i915-gt-Refactor-CCS-mode-handling-and-improve-app.drm
Patch345:	0017-drm-i915-no-waiting-for-page-flip-in-vpp-case.drm
#rapl
Patch346:	0001-powercap-intel_rapl-Add-support-for-Bartlett-Lake-pl.rapl
#misc
Patch347:	0001-Add-security.md-file.misc
#emt-eci
Patch348:	0057-kernel-trace-Add-DISALLOW_TRACE_PRINTK-make-option.patch
Patch349:	0058-Revert-scripts-remove-bin2c.patch
Patch350:	0059-extend-uio-driver-to-supports-msix.patch
Patch351:	0060-virtio-add-VIRTIO_PMD-support.patch
Patch352:	0061-virt-acrn-Introduce-interfaces-for-PIO-device.patch
Patch353:	0062-Add-hypercall-to-access-MSR.patch
Patch354:	0063-Revert-spi-Remove-unused-function-spi_busnum_to_mast.patch
Patch355:	0064-igc-add-CONFIG_IGC_TSN_TRACE-conditional-trace_print.patch
Patch356:	0065-stmmac_pci-add-CONFIG_STMMAC_TSN_TRACE-conditional-t.patch
Patch357:	0066-igb-prepare-for-AF_XDP-zero-copy-support.patch
Patch358:	0067-igb-Introduce-XSK-data-structures-and-helpers.patch
Patch359:	0068-igb-add-AF_XDP-zero-copy-Rx-support.patch
Patch360:	0069-igb-add-AF_XDP-zero-copy-Tx-support.patch
Patch361:	0070-igb-Add-BTF-based-metadata-for-XDP.patch
Patch362:	0071-ANDROID-trace-power-add-trace_clock_set_parent.patch
Patch363:	0072-ANDROID-trace-net-use-pK-for-kernel-pointers.patch
Patch364:	0073-ANDROID-trace-add-non-hierarchical-function_graph-op.patch
Patch365:	0074-virtio-fix-VIRTIO_PMD-support.patch
#emt-drm
Patch366:	0076-Revert-drm-xe-gt-Update-handling-of-xe_force_wake_ge.patch
Patch367:	0075-drm-xe-gsc-mei-interrupt-top-half-should-be-in-irq-d.patch
# EMT kernel configs
Patch368:	0001-Add-reference-kernel-config.patch
Patch369:	0002-Enable-more-kernel-options.patch
Patch370:	0003-Add-initial-kernel-config-for-RT.patch
Patch371:	0004-Update-RT-kernel-config.patch
Patch372:	0005-Enable-Disable-more-RT-kernel-config.patch
Patch373:	0006-config-enable-TSN-features.patch
Patch374:	0007-config-enable-DM_INTEGRITY-as-modules.patch
Patch375:	0008-Intel-config-rt-add-TGPIO-feature-configs-in-RT-kern.patch
Patch376:	0009-config-enable-RT-config-for-ECI.patch
Patch377:	0010-config-enable-GSC-and-PXE-for-HuC-support.patch
Patch378:	0011-Intel-config-add-SPI-I3C-configs-in-both-LTS-and-RT-.patch
Patch379:	0012-config-enable-FS_VERITY.patch
Patch380:	0013-Harden-the-kernel-config-from-compiler-perspective.patch
Patch381:	0014-Hardening-the-page-table-check-and-selinux-boot-para.patch
Patch382:	0015-Hardening-the-IO-related-kernel-config.patch
Patch383:	0016-Hardening-by-removeing-unnecessary-system-call.patch
Patch384:	0017-Hardening-the-misc-kernel-config.patch
Patch385:	0018-Hardening-the-kernel-for-x86-cpu-issues.patch
Patch386:	0019-Hardening-kernel-by-disabling-the-DEBUG-options.patch
Patch387:	0020-Hardening-kernel-by-enabling-kfence.patch
Patch388:	0021-Hardening-kernel-by-enabling-UBSAN.patch
Patch389:	0022-Hardening-the-kernel-memory-intialization.patch
Patch390:	0023-Enable-the-confidentiality-model-by-default.patch
Patch391:	0024-config-Switch-kernel-compression-from-gzip-to-zstd.patch
Patch392:	0025-Intel-config-disable-raid-0-1-10-456.patch
Patch393:	0026-Intel-config-disable-CONFIG_INFINIBAND_BNXT_RE.patch
Patch394:	0027-Intel-config-enable-CONFIG_UDMABUF-to-enable-EGL-dma.patch
Patch395:	0028-Intel-config-disable-io-uring-feature-to-avoid-secur.patch
Patch396:	0029-Intel-config-rt-harden-the-rt-kernel-config-from-com.patch
Patch397:	0030-Intel-config-rt-harden-the-page-table-check-and-seli.patch
Patch398:	0031-Intel-config-rt-harden-the-IO-related-kernel-config.patch
Patch399:	0032-Intel-config-rt-Remove-unused-system-call-to-avoid-s.patch
Patch400:	0033-Intel-config-rt-harden-the-misc-kernel-config.patch
Patch401:	0034-Intel-config-rt-harden-the-kernel-to-mitigate-x86-cp.patch
Patch402:	0035-Intel-config-rt-disable-the-DEBUG-options.patch
Patch403:	0036-Intel-config-rt-Enable-kfence-to-avoid-securit-risk.patch
Patch404:	0037-Intel-config-rt-Enable-UBSAN-feature.patch
Patch405:	0038-Intel-config-rt-Initialize-the-kernel-memory-to-avoi.patch
Patch406:	0039-Intel-config-rt-Enable-the-confidentiality-model-by-.patch
Patch407:	0040-Intel-config-disable-the-static-usermode-helper.patch
Patch408:	0041-Intel-config-disable-CONFIG_BTRFS_FS.patch
Patch409:	0042-config-restore-RT-CONFIG_HZ-to-1000.patch
Patch410:	0043-Intel-config-Enable-the-selinux-boot-param-and-devel.patch
Patch411:	0044-Intel-config-disable-CONFIG_TRIM_UNUSED_KSYMS.patch
Patch412:	0045-Intel-config-Enable-the-kernel-config-for-rasdaemon-.patch
Patch413:	0046-Intel-non-rt-config-Enable-the-support-for-trusted-c.patch
Patch414:	0047-iwlmei-enable-IWLMEI-in-rt-and-non-rt.patch
Patch415:	0048-Multi-OS-enable-android-binder-driver-for-CIC.patch
Patch416:	0049-Intel-config-enable-staging-and-android-ashmem.patch
Patch417:	0050-config-enable-xe-driver.patch
Patch418:	0051-config-rt-enable-CONFIG_UDMABUF.patch
Patch419:	0052-emt-config-disable-nvidia-framebuffer-driver.patch
Patch420:	0053-config-disable-kernel-module-signature.patch
Patch421:	0054-config-rt-enable-XE-driver.patch
Patch422:	0055-Enable-the-TSN-kernel-config.patch
Patch423:	0056-config-disable-random-structure-feature.patch
#CVE-2025-21751
Patch424:	CVE-2025-21751.patch
#CVE-2025-21709
Patch425:	CVE-2025-21709.patch
#CVE-2025-21807
Patch426:	CVE-2025-21807.patch
#CVE-2025-21817
Patch427:	CVE-2025-21817.patch
#CVE-2025-21884
Patch428:	CVE-2025-21884.patch
Patch429:	CVE-2025-21884-1.patch
#CVE-2025-22103
Patch430:	CVE-2025-22103.patch
#CVE-2025-22104
Patch431:	CVE-2025-22104.patch
#CVE-2025-22105
Patch432:	CVE-2025-22105.patch
Patch433:	CVE-2025-22105-1.patch
#CVE-2025-22106
Patch434:	CVE-2025-22106.patch
#CVE-2025-22108
Patch435:	CVE-2025-22108.patch
#CVE-2025-22111
Patch436:	CVE-2025-22111.patch
#CVE-2025-22113
Patch437:	CVE-2025-22113.patch
Patch438:	CVE-2025-22113-1.patch
#CVE-2025-22116
Patch439:	CVE-2025-22116.patch
#CVE-2025-22117
Patch440:	CVE-2025-22117.patch
#CVE-2025-22121
Patch441:	CVE-2025-22121.patch
Patch442:	CVE-2025-22121-1.patch
#CVE-2025-22124
Patch443:	CVE-2025-22124.patch
#CVE-2025-23131
Patch444:	CVE-2025-23131.patch
#CVE-2025-37746
Patch445:	CVE-2025-37746.patch
Patch446:	CVE-2025-37746-1.patch
#CVE-2025-37906
Patch447:	CVE-2025-37906.patch
#CVE-2025-38064
Patch448:	CVE-2025-38064.patch
Patch449:	CVE-2025-38064-1.patch
#CVE-2025-38041
Patch450:	CVE-2025-38041.patch
Patch451:	CVE-2025-38041-1.patch
Patch452:	CVE-2025-38041-2.patch
#CVE-2025-38029
Patch453:	CVE-2025-38029.patch
#CVE-2025-38351
Patch454:	CVE-2025-38351.patch
#CVE-2025-38311
Patch455:	CVE-2025-38311.patch
#CVE-2025-38306
Patch456:	CVE-2025-38306.patch
#CVE-2025-38248
Patch457:	CVE-2025-38248.patch
#CVE-2025-38234
Patch458:	CVE-2025-38234.patch
#CVE-2025-38207
Patch459:	CVE-2025-38207.patch
#CVE-2025-38137
Patch460:	CVE-2025-38137.patch
#CVE-2025-38105
Patch461:	CVE-2025-38105.patch

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
%setup -q -n linux-6.12.39
%autosetup -p1 -n linux-6.12.39 -N
patch -p1 --fuzz=3 --force < %{PATCH0}
patch -p1 --fuzz=3 --force < %{PATCH1}
patch -p1 --fuzz=3 --force < %{PATCH2}
patch -p1 --fuzz=3 --force < %{PATCH3}
patch -p1 --fuzz=3 --force < %{PATCH4}
patch -p1 --fuzz=3 --force < %{PATCH5}
patch -p1 --fuzz=3 --force < %{PATCH6}
patch -p1 --fuzz=3 --force < %{PATCH7}
patch -p1 --fuzz=3 --force < %{PATCH8}
patch -p1 --fuzz=3 --force < %{PATCH9}
patch -p1 --fuzz=3 --force < %{PATCH10}
patch -p1 --fuzz=3 --force < %{PATCH11}
patch -p1 --fuzz=3 --force < %{PATCH12}
patch -p1 --fuzz=3 --force < %{PATCH13}
patch -p1 --fuzz=3 --force < %{PATCH14}
patch -p1 --fuzz=3 --force < %{PATCH15}
patch -p1 --fuzz=3 --force < %{PATCH16}
patch -p1 --fuzz=3 --force < %{PATCH17}
patch -p1 --fuzz=3 --force < %{PATCH18}
patch -p1 --fuzz=3 --force < %{PATCH19}
patch -p1 --fuzz=3 --force < %{PATCH20}
patch -p1 --fuzz=3 --force < %{PATCH21}
patch -p1 --fuzz=3 --force < %{PATCH22}
patch -p1 --fuzz=3 --force < %{PATCH23}
patch -p1 --fuzz=3 --force < %{PATCH24}
patch -p1 --fuzz=3 --force < %{PATCH25}
patch -p1 --fuzz=3 --force < %{PATCH26}
patch -p1 --fuzz=3 --force < %{PATCH27}
patch -p1 --fuzz=3 --force < %{PATCH28}
patch -p1 --fuzz=3 --force < %{PATCH29}
patch -p1 --fuzz=3 --force < %{PATCH30}
patch -p1 --fuzz=3 --force < %{PATCH31}
patch -p1 --fuzz=3 --force < %{PATCH32}
patch -p1 --fuzz=3 --force < %{PATCH33}
patch -p1 --fuzz=3 --force < %{PATCH34}
patch -p1 --fuzz=3 --force < %{PATCH35}
patch -p1 --fuzz=3 --force < %{PATCH36}
patch -p1 --fuzz=3 --force < %{PATCH37}
patch -p1 --fuzz=3 --force < %{PATCH38}
patch -p1 --fuzz=3 --force < %{PATCH39}
patch -p1 --fuzz=3 --force < %{PATCH40}
patch -p1 --fuzz=3 --force < %{PATCH41}
patch -p1 --fuzz=3 --force < %{PATCH42}
patch -p1 --fuzz=3 --force < %{PATCH43}
patch -p1 --fuzz=3 --force < %{PATCH44}
patch -p1 --fuzz=3 --force < %{PATCH45}
patch -p1 --fuzz=3 --force < %{PATCH46}
patch -p1 --fuzz=3 --force < %{PATCH47}
patch -p1 --fuzz=3 --force < %{PATCH48}
patch -p1 --fuzz=3 --force < %{PATCH49}
patch -p1 --fuzz=3 --force < %{PATCH50}
patch -p1 --fuzz=3 --force < %{PATCH51}
patch -p1 --fuzz=3 --force < %{PATCH52}
patch -p1 --fuzz=3 --force < %{PATCH53}
patch -p1 --fuzz=3 --force < %{PATCH54}
patch -p1 --fuzz=3 --force < %{PATCH55}
patch -p1 --fuzz=3 --force < %{PATCH56}
patch -p1 --fuzz=3 --force < %{PATCH57}
patch -p1 --fuzz=3 --force < %{PATCH58}
patch -p1 --fuzz=3 --force < %{PATCH59}
patch -p1 --fuzz=3 --force < %{PATCH60}
patch -p1 --fuzz=3 --force < %{PATCH61}
patch -p1 --fuzz=3 --force < %{PATCH62}
patch -p1 --fuzz=3 --force < %{PATCH63}
patch -p1 --fuzz=3 --force < %{PATCH64}
patch -p1 --fuzz=3 --force < %{PATCH65}
patch -p1 --fuzz=3 --force < %{PATCH66}
patch -p1 --fuzz=3 --force < %{PATCH67}
patch -p1 --fuzz=3 --force < %{PATCH68}
patch -p1 --fuzz=3 --force < %{PATCH69}
patch -p1 --fuzz=3 --force < %{PATCH70}
patch -p1 --fuzz=3 --force < %{PATCH71}
patch -p1 --fuzz=3 --force < %{PATCH72}
patch -p1 --fuzz=3 --force < %{PATCH73}
patch -p1 --fuzz=3 --force < %{PATCH74}
patch -p1 --fuzz=3 --force < %{PATCH75}
patch -p1 --fuzz=3 --force < %{PATCH76}
patch -p1 --fuzz=3 --force < %{PATCH77}
patch -p1 --fuzz=3 --force < %{PATCH78}
patch -p1 --fuzz=3 --force < %{PATCH79}
patch -p1 --fuzz=3 --force < %{PATCH80}
patch -p1 --fuzz=3 --force < %{PATCH81}
patch -p1 --fuzz=3 --force < %{PATCH82}
patch -p1 --fuzz=3 --force < %{PATCH83}
patch -p1 --fuzz=3 --force < %{PATCH84}
patch -p1 --fuzz=3 --force < %{PATCH85}
patch -p1 --fuzz=3 --force < %{PATCH86}
patch -p1 --fuzz=3 --force < %{PATCH87}
patch -p1 --fuzz=3 --force < %{PATCH88}
patch -p1 --fuzz=3 --force < %{PATCH89}
patch -p1 --fuzz=3 --force < %{PATCH90}
patch -p1 --fuzz=3 --force < %{PATCH91}
patch -p1 --fuzz=3 --force < %{PATCH92}
patch -p1 --fuzz=3 --force < %{PATCH93}
patch -p1 --fuzz=3 --force < %{PATCH94}
patch -p1 --fuzz=3 --force < %{PATCH95}
patch -p1 --fuzz=3 --force < %{PATCH96}
patch -p1 --fuzz=3 --force < %{PATCH97}
patch -p1 --fuzz=3 --force < %{PATCH98}
patch -p1 --fuzz=3 --force < %{PATCH99}
patch -p1 --fuzz=3 --force < %{PATCH100}
patch -p1 --fuzz=3 --force < %{PATCH101}
patch -p1 --fuzz=3 --force < %{PATCH102}
patch -p1 --fuzz=3 --force < %{PATCH103}
patch -p1 --fuzz=3 --force < %{PATCH104}
patch -p1 --fuzz=3 --force < %{PATCH105}
patch -p1 --fuzz=3 --force < %{PATCH106}
patch -p1 --fuzz=3 --force < %{PATCH107}
patch -p1 --fuzz=3 --force < %{PATCH108}
patch -p1 --fuzz=3 --force < %{PATCH109}
patch -p1 --fuzz=3 --force < %{PATCH110}
patch -p1 --fuzz=3 --force < %{PATCH111}
patch -p1 --fuzz=3 --force < %{PATCH112}
patch -p1 --fuzz=3 --force < %{PATCH113}
patch -p1 --fuzz=3 --force < %{PATCH114}
patch -p1 --fuzz=3 --force < %{PATCH115}
patch -p1 --fuzz=3 --force < %{PATCH116}
patch -p1 --fuzz=3 --force < %{PATCH117}
patch -p1 --fuzz=3 --force < %{PATCH118}
patch -p1 --fuzz=3 --force < %{PATCH119}
patch -p1 --fuzz=3 --force < %{PATCH120}
patch -p1 --fuzz=3 --force < %{PATCH121}
patch -p1 --fuzz=3 --force < %{PATCH122}
patch -p1 --fuzz=3 --force < %{PATCH123}
patch -p1 --fuzz=3 --force < %{PATCH124}
patch -p1 --fuzz=3 --force < %{PATCH125}
patch -p1 --fuzz=3 --force < %{PATCH126}
patch -p1 --fuzz=3 --force < %{PATCH127}
patch -p1 --fuzz=3 --force < %{PATCH128}
patch -p1 --fuzz=3 --force < %{PATCH129}
patch -p1 --fuzz=3 --force < %{PATCH130}
patch -p1 --fuzz=3 --force < %{PATCH131}
patch -p1 --fuzz=3 --force < %{PATCH132}
patch -p1 --fuzz=3 --force < %{PATCH133}
patch -p1 --fuzz=3 --force < %{PATCH134}
patch -p1 --fuzz=3 --force < %{PATCH135}
patch -p1 --fuzz=3 --force < %{PATCH136}
patch -p1 --fuzz=3 --force < %{PATCH137}
patch -p1 --fuzz=3 --force < %{PATCH138}
patch -p1 --fuzz=3 --force < %{PATCH139}
patch -p1 --fuzz=3 --force < %{PATCH140}
patch -p1 --fuzz=3 --force < %{PATCH141}
patch -p1 --fuzz=3 --force < %{PATCH142}
patch -p1 --fuzz=3 --force < %{PATCH143}
patch -p1 --fuzz=3 --force < %{PATCH144}
patch -p1 --fuzz=3 --force < %{PATCH145}
patch -p1 --fuzz=3 --force < %{PATCH146}
patch -p1 --fuzz=3 --force < %{PATCH147}
patch -p1 --fuzz=3 --force < %{PATCH148}
patch -p1 --fuzz=3 --force < %{PATCH149}
patch -p1 --fuzz=3 --force < %{PATCH150}
patch -p1 --fuzz=3 --force < %{PATCH151}
patch -p1 --fuzz=3 --force < %{PATCH152}
patch -p1 --fuzz=3 --force < %{PATCH153}
patch -p1 --fuzz=3 --force < %{PATCH154}
patch -p1 --fuzz=3 --force < %{PATCH155}
patch -p1 --fuzz=3 --force < %{PATCH156}
patch -p1 --fuzz=3 --force < %{PATCH157}
patch -p1 --fuzz=3 --force < %{PATCH158}
patch -p1 --fuzz=3 --force < %{PATCH159}
patch -p1 --fuzz=3 --force < %{PATCH160}
patch -p1 --fuzz=3 --force < %{PATCH161}
patch -p1 --fuzz=3 --force < %{PATCH162}
patch -p1 --fuzz=3 --force < %{PATCH163}
patch -p1 --fuzz=3 --force < %{PATCH164}
patch -p1 --fuzz=3 --force < %{PATCH165}
patch -p1 --fuzz=3 --force < %{PATCH166}
patch -p1 --fuzz=3 --force < %{PATCH167}
patch -p1 --fuzz=3 --force < %{PATCH168}
patch -p1 --fuzz=3 --force < %{PATCH169}
patch -p1 --fuzz=3 --force < %{PATCH170}
patch -p1 --fuzz=3 --force < %{PATCH171}
patch -p1 --fuzz=3 --force < %{PATCH172}
patch -p1 --fuzz=3 --force < %{PATCH173}
patch -p1 --fuzz=3 --force < %{PATCH174}
patch -p1 --fuzz=3 --force < %{PATCH175}
patch -p1 --fuzz=3 --force < %{PATCH176}
patch -p1 --fuzz=3 --force < %{PATCH177}
patch -p1 --fuzz=3 --force < %{PATCH178}
patch -p1 --fuzz=3 --force < %{PATCH179}
patch -p1 --fuzz=3 --force < %{PATCH180}
patch -p1 --fuzz=3 --force < %{PATCH181}
patch -p1 --fuzz=3 --force < %{PATCH182}
patch -p1 --fuzz=3 --force < %{PATCH183}
patch -p1 --fuzz=3 --force < %{PATCH184}
patch -p1 --fuzz=3 --force < %{PATCH185}
patch -p1 --fuzz=3 --force < %{PATCH186}
patch -p1 --fuzz=3 --force < %{PATCH187}
patch -p1 --fuzz=3 --force < %{PATCH188}
patch -p1 --fuzz=3 --force < %{PATCH189}
patch -p1 --fuzz=3 --force < %{PATCH190}
patch -p1 --fuzz=3 --force < %{PATCH191}
patch -p1 --fuzz=3 --force < %{PATCH192}
patch -p1 --fuzz=3 --force < %{PATCH193}
patch -p1 --fuzz=3 --force < %{PATCH194}
patch -p1 --fuzz=3 --force < %{PATCH195}
patch -p1 --fuzz=3 --force < %{PATCH196}
patch -p1 --fuzz=3 --force < %{PATCH197}
patch -p1 --fuzz=3 --force < %{PATCH198}
patch -p1 --fuzz=3 --force < %{PATCH199}
patch -p1 --fuzz=3 --force < %{PATCH200}
patch -p1 --fuzz=3 --force < %{PATCH201}
patch -p1 --fuzz=3 --force < %{PATCH202}
patch -p1 --fuzz=3 --force < %{PATCH203}
patch -p1 --fuzz=3 --force < %{PATCH204}
patch -p1 --fuzz=3 --force < %{PATCH205}
patch -p1 --fuzz=3 --force < %{PATCH206}
patch -p1 --fuzz=3 --force < %{PATCH207}
patch -p1 --fuzz=3 --force < %{PATCH208}
patch -p1 --fuzz=3 --force < %{PATCH209}
patch -p1 --fuzz=3 --force < %{PATCH210}
patch -p1 --fuzz=3 --force < %{PATCH211}
patch -p1 --fuzz=3 --force < %{PATCH212}
patch -p1 --fuzz=3 --force < %{PATCH213}
patch -p1 --fuzz=3 --force < %{PATCH214}
patch -p1 --fuzz=3 --force < %{PATCH215}
patch -p1 --fuzz=3 --force < %{PATCH216}
patch -p1 --fuzz=3 --force < %{PATCH217}
patch -p1 --fuzz=3 --force < %{PATCH218}
patch -p1 --fuzz=3 --force < %{PATCH219}
patch -p1 --fuzz=3 --force < %{PATCH220}
patch -p1 --fuzz=3 --force < %{PATCH221}
patch -p1 --fuzz=3 --force < %{PATCH222}
patch -p1 --fuzz=3 --force < %{PATCH223}
patch -p1 --fuzz=3 --force < %{PATCH224}
patch -p1 --fuzz=3 --force < %{PATCH225}
patch -p1 --fuzz=3 --force < %{PATCH226}
patch -p1 --fuzz=3 --force < %{PATCH227}
patch -p1 --fuzz=3 --force < %{PATCH228}
patch -p1 --fuzz=3 --force < %{PATCH229}
patch -p1 --fuzz=3 --force < %{PATCH230}
patch -p1 --fuzz=3 --force < %{PATCH231}
patch -p1 --fuzz=3 --force < %{PATCH232}
patch -p1 --fuzz=3 --force < %{PATCH233}
patch -p1 --fuzz=3 --force < %{PATCH234}
patch -p1 --fuzz=3 --force < %{PATCH235}
patch -p1 --fuzz=3 --force < %{PATCH236}
patch -p1 --fuzz=3 --force < %{PATCH237}
patch -p1 --fuzz=3 --force < %{PATCH238}
patch -p1 --fuzz=3 --force < %{PATCH239}
patch -p1 --fuzz=3 --force < %{PATCH240}
patch -p1 --fuzz=3 --force < %{PATCH241}
patch -p1 --fuzz=3 --force < %{PATCH242}
patch -p1 --fuzz=3 --force < %{PATCH243}
patch -p1 --fuzz=3 --force < %{PATCH244}
patch -p1 --fuzz=3 --force < %{PATCH245}
patch -p1 --fuzz=3 --force < %{PATCH246}
patch -p1 --fuzz=3 --force < %{PATCH247}
patch -p1 --fuzz=3 --force < %{PATCH248}
patch -p1 --fuzz=3 --force < %{PATCH249}
patch -p1 --fuzz=3 --force < %{PATCH250}
patch -p1 --fuzz=3 --force < %{PATCH251}
patch -p1 --fuzz=3 --force < %{PATCH252}
patch -p1 --fuzz=3 --force < %{PATCH253}
patch -p1 --fuzz=3 --force < %{PATCH254}
patch -p1 --fuzz=3 --force < %{PATCH255}
patch -p1 --fuzz=3 --force < %{PATCH256}
patch -p1 --fuzz=3 --force < %{PATCH257}
patch -p1 --fuzz=3 --force < %{PATCH258}
patch -p1 --fuzz=3 --force < %{PATCH259}
patch -p1 --fuzz=3 --force < %{PATCH260}
patch -p1 --fuzz=3 --force < %{PATCH261}
patch -p1 --fuzz=3 --force < %{PATCH262}
patch -p1 --fuzz=3 --force < %{PATCH263}
patch -p1 --fuzz=3 --force < %{PATCH264}
patch -p1 --fuzz=3 --force < %{PATCH265}
patch -p1 --fuzz=3 --force < %{PATCH266}
patch -p1 --fuzz=3 --force < %{PATCH267}
patch -p1 --fuzz=3 --force < %{PATCH268}
patch -p1 --fuzz=3 --force < %{PATCH269}
patch -p1 --fuzz=3 --force < %{PATCH270}
patch -p1 --fuzz=3 --force < %{PATCH271}
patch -p1 --fuzz=3 --force < %{PATCH272}
patch -p1 --fuzz=3 --force < %{PATCH273}
patch -p1 --fuzz=3 --force < %{PATCH274}
patch -p1 --fuzz=3 --force < %{PATCH275}
patch -p1 --fuzz=3 --force < %{PATCH276}
patch -p1 --fuzz=3 --force < %{PATCH277}
patch -p1 --fuzz=3 --force < %{PATCH278}
patch -p1 --fuzz=3 --force < %{PATCH279}
patch -p1 --fuzz=3 --force < %{PATCH280}
patch -p1 --fuzz=3 --force < %{PATCH281}
patch -p1 --fuzz=3 --force < %{PATCH282}
patch -p1 --fuzz=3 --force < %{PATCH283}
patch -p1 --fuzz=3 --force < %{PATCH284}
patch -p1 --fuzz=3 --force < %{PATCH285}
patch -p1 --fuzz=3 --force < %{PATCH286}
patch -p1 --fuzz=3 --force < %{PATCH287}
patch -p1 --fuzz=3 --force < %{PATCH288}
patch -p1 --fuzz=3 --force < %{PATCH289}
patch -p1 --fuzz=3 --force < %{PATCH290}
patch -p1 --fuzz=3 --force < %{PATCH291}
patch -p1 --fuzz=3 --force < %{PATCH292}
patch -p1 --fuzz=3 --force < %{PATCH293}
patch -p1 --fuzz=3 --force < %{PATCH294}
patch -p1 --fuzz=3 --force < %{PATCH295}
patch -p1 --fuzz=3 --force < %{PATCH296}
patch -p1 --fuzz=3 --force < %{PATCH297}
patch -p1 --fuzz=3 --force < %{PATCH298}
patch -p1 --fuzz=3 --force < %{PATCH299}
patch -p1 --fuzz=3 --force < %{PATCH300}
patch -p1 --fuzz=3 --force < %{PATCH301}
patch -p1 --fuzz=3 --force < %{PATCH302}
patch -p1 --fuzz=3 --force < %{PATCH303}
patch -p1 --fuzz=3 --force < %{PATCH304}
patch -p1 --fuzz=3 --force < %{PATCH305}
patch -p1 --fuzz=3 --force < %{PATCH306}
patch -p1 --fuzz=3 --force < %{PATCH307}
patch -p1 --fuzz=3 --force < %{PATCH308}
patch -p1 --fuzz=3 --force < %{PATCH309}
patch -p1 --fuzz=3 --force < %{PATCH310}
patch -p1 --fuzz=3 --force < %{PATCH311}
patch -p1 --fuzz=3 --force < %{PATCH312}
patch -p1 --fuzz=3 --force < %{PATCH313}
patch -p1 --fuzz=3 --force < %{PATCH314}
patch -p1 --fuzz=3 --force < %{PATCH315}
patch -p1 --fuzz=3 --force < %{PATCH316}
patch -p1 --fuzz=3 --force < %{PATCH317}
patch -p1 --fuzz=3 --force < %{PATCH318}
patch -p1 --fuzz=3 --force < %{PATCH319}
patch -p1 --fuzz=3 --force < %{PATCH320}
patch -p1 --fuzz=3 --force < %{PATCH321}
patch -p1 --fuzz=3 --force < %{PATCH322}
patch -p1 --fuzz=3 --force < %{PATCH323}
patch -p1 --fuzz=3 --force < %{PATCH324}
patch -p1 --fuzz=3 --force < %{PATCH325}
patch -p1 --fuzz=3 --force < %{PATCH326}
patch -p1 --fuzz=3 --force < %{PATCH327}
patch -p1 --fuzz=3 --force < %{PATCH328}
patch -p1 --fuzz=3 --force < %{PATCH329}
patch -p1 --fuzz=3 --force < %{PATCH330}
patch -p1 --fuzz=3 --force < %{PATCH331}
patch -p1 --fuzz=3 --force < %{PATCH332}
patch -p1 --fuzz=3 --force < %{PATCH333}
patch -p1 --fuzz=3 --force < %{PATCH334}
patch -p1 --fuzz=3 --force < %{PATCH335}
patch -p1 --fuzz=3 --force < %{PATCH336}
patch -p1 --fuzz=3 --force < %{PATCH337}
patch -p1 --fuzz=3 --force < %{PATCH338}
patch -p1 --fuzz=3 --force < %{PATCH339}
patch -p1 --fuzz=3 --force < %{PATCH340}
patch -p1 --fuzz=3 --force < %{PATCH341}
patch -p1 --fuzz=3 --force < %{PATCH342}
patch -p1 --fuzz=3 --force < %{PATCH343}
patch -p1 --fuzz=3 --force < %{PATCH344}
patch -p1 --fuzz=3 --force < %{PATCH345}
patch -p1 --fuzz=3 --force < %{PATCH346}
patch -p1 --fuzz=3 --force < %{PATCH347}
patch -p1 --fuzz=3 --force < %{PATCH348}
patch -p1 --fuzz=3 --force < %{PATCH349}
patch -p1 --fuzz=3 --force < %{PATCH350}
patch -p1 --fuzz=3 --force < %{PATCH351}
patch -p1 --fuzz=3 --force < %{PATCH352}
patch -p1 --fuzz=3 --force < %{PATCH353}
patch -p1 --fuzz=3 --force < %{PATCH354}
patch -p1 --fuzz=3 --force < %{PATCH355}
patch -p1 --fuzz=3 --force < %{PATCH356}
patch -p1 --fuzz=3 --force < %{PATCH357}
patch -p1 --fuzz=3 --force < %{PATCH358}
patch -p1 --fuzz=3 --force < %{PATCH359}
patch -p1 --fuzz=3 --force < %{PATCH360}
patch -p1 --fuzz=3 --force < %{PATCH361}
patch -p1 --fuzz=3 --force < %{PATCH362}
patch -p1 --fuzz=3 --force < %{PATCH363}
patch -p1 --fuzz=3 --force < %{PATCH364}
patch -p1 --fuzz=3 --force < %{PATCH365}
patch -p1 --fuzz=3 --force < %{PATCH366}
patch -p1 --fuzz=3 --force < %{PATCH367}
patch -p1 --fuzz=3 --force < %{PATCH368}
patch -p1 --fuzz=3 --force < %{PATCH369}
patch -p1 --fuzz=3 --force < %{PATCH370}
patch -p1 --fuzz=3 --force < %{PATCH371}
patch -p1 --fuzz=3 --force < %{PATCH372}
patch -p1 --fuzz=3 --force < %{PATCH373}
patch -p1 --fuzz=3 --force < %{PATCH374}
patch -p1 --fuzz=3 --force < %{PATCH375}
patch -p1 --fuzz=3 --force < %{PATCH376}
patch -p1 --fuzz=3 --force < %{PATCH377}
patch -p1 --fuzz=3 --force < %{PATCH378}
patch -p1 --fuzz=3 --force < %{PATCH379}
patch -p1 --fuzz=3 --force < %{PATCH380}
patch -p1 --fuzz=3 --force < %{PATCH381}
patch -p1 --fuzz=3 --force < %{PATCH382}
patch -p1 --fuzz=3 --force < %{PATCH383}
patch -p1 --fuzz=3 --force < %{PATCH384}
patch -p1 --fuzz=3 --force < %{PATCH385}
patch -p1 --fuzz=3 --force < %{PATCH386}
patch -p1 --fuzz=3 --force < %{PATCH387}
patch -p1 --fuzz=3 --force < %{PATCH388}
patch -p1 --fuzz=3 --force < %{PATCH389}
patch -p1 --fuzz=3 --force < %{PATCH390}
patch -p1 --fuzz=3 --force < %{PATCH391}
patch -p1 --fuzz=3 --force < %{PATCH392}
patch -p1 --fuzz=3 --force < %{PATCH393}
patch -p1 --fuzz=3 --force < %{PATCH394}
patch -p1 --fuzz=3 --force < %{PATCH395}
patch -p1 --fuzz=3 --force < %{PATCH396}
patch -p1 --fuzz=3 --force < %{PATCH397}
patch -p1 --fuzz=3 --force < %{PATCH398}
patch -p1 --fuzz=3 --force < %{PATCH399}
patch -p1 --fuzz=3 --force < %{PATCH400}
patch -p1 --fuzz=3 --force < %{PATCH401}
patch -p1 --fuzz=3 --force < %{PATCH402}
patch -p1 --fuzz=3 --force < %{PATCH403}
patch -p1 --fuzz=3 --force < %{PATCH404}
patch -p1 --fuzz=3 --force < %{PATCH405}
patch -p1 --fuzz=3 --force < %{PATCH406}
patch -p1 --fuzz=3 --force < %{PATCH407}
patch -p1 --fuzz=3 --force < %{PATCH408}
patch -p1 --fuzz=3 --force < %{PATCH409}
patch -p1 --fuzz=3 --force < %{PATCH410}
patch -p1 --fuzz=3 --force < %{PATCH411}
patch -p1 --fuzz=3 --force < %{PATCH412}
patch -p1 --fuzz=3 --force < %{PATCH413}
patch -p1 --fuzz=3 --force < %{PATCH414}
patch -p1 --fuzz=3 --force < %{PATCH415}
patch -p1 --fuzz=3 --force < %{PATCH416}
patch -p1 --fuzz=3 --force < %{PATCH417}
patch -p1 --fuzz=3 --force < %{PATCH418}
patch -p1 --fuzz=3 --force < %{PATCH419}
patch -p1 --fuzz=3 --force < %{PATCH420}
patch -p1 --fuzz=3 --force < %{PATCH421}
patch -p1 --fuzz=3 --force < %{PATCH422}
patch -p1 --fuzz=3 --force < %{PATCH423}
patch -p1 --fuzz=3 --force < %{PATCH424}
patch -p1 --fuzz=3 --force < %{PATCH425}
patch -p1 --fuzz=3 --force < %{PATCH426}
patch -p1 --fuzz=3 --force < %{PATCH427}
patch -p1 --fuzz=3 --force < %{PATCH428}
patch -p1 --fuzz=3 --force < %{PATCH429}
patch -p1 --fuzz=3 --force < %{PATCH430}
patch -p1 --fuzz=3 --force < %{PATCH431}
patch -p1 --fuzz=3 --force < %{PATCH432}
patch -p1 --fuzz=3 --force < %{PATCH433}
patch -p1 --fuzz=3 --force < %{PATCH434}
patch -p1 --fuzz=3 --force < %{PATCH435}
patch -p1 --fuzz=3 --force < %{PATCH436}
patch -p1 --fuzz=3 --force < %{PATCH437}
patch -p1 --fuzz=3 --force < %{PATCH438}
patch -p1 --fuzz=3 --force < %{PATCH439}
patch -p1 --fuzz=3 --force < %{PATCH440}
patch -p1 --fuzz=3 --force < %{PATCH441}
patch -p1 --fuzz=3 --force < %{PATCH442}
patch -p1 --fuzz=3 --force < %{PATCH443}
patch -p1 --fuzz=3 --force < %{PATCH444}
patch -p1 --fuzz=3 --force < %{PATCH445}
patch -p1 --fuzz=3 --force < %{PATCH446}
patch -p1 --fuzz=3 --force < %{PATCH447}
patch -p1 --fuzz=3 --force < %{PATCH448}
patch -p1 --fuzz=3 --force < %{PATCH449}
patch -p1 --fuzz=3 --force < %{PATCH450}
patch -p1 --fuzz=3 --force < %{PATCH451}
patch -p1 --fuzz=3 --force < %{PATCH452}
patch -p1 --fuzz=3 --force < %{PATCH453}
patch -p1 --fuzz=3 --force < %{PATCH454}
patch -p1 --fuzz=3 --force < %{PATCH455}
patch -p1 --fuzz=3 --force < %{PATCH456}
patch -p1 --fuzz=3 --force < %{PATCH457}
patch -p1 --fuzz=3 --force < %{PATCH458}
patch -p1 --fuzz=3 --force < %{PATCH459}
patch -p1 --fuzz=3 --force < %{PATCH460}
patch -p1 --fuzz=3 --force < %{PATCH461}
# %patch 0 -p1
make mrproper

cp %{config_source} .config

# Add cert into kernel's trusted keyring
cp %{SOURCE4} certs/emt.pem
sed -i 's#CONFIG_SYSTEM_TRUSTED_KEYS=""#CONFIG_SYSTEM_TRUSTED_KEYS="certs/emt.pem"#' .config

cp .config current_config
sed -i 's/CONFIG_LOCALVERSION=""/CONFIG_LOCALVERSION="-%{release}"/' .config
make LC_ALL=  ARCH=%{arch} oldconfig

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
* Thu Aug 14 2025 Ren Jiaojiao <jiaojiaox.ren@intel.com> - 6.12.39-2
- Update kernel spec

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
