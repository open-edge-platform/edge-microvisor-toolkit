# Extensions and Patches

Edge Microvisor Toolkit leverages a collection of extensions and patches
to provide more versatile deployment options and optimizations for Intel® silicon based AI
solutions at the edge. Read on to learn more about the components and kernel patchsets
used in the toolkit.

## Extensions

Deploying of Edge Microvisor Toolkit with Lightweight Kubernetes (K3s)
requires additional extensions which are downloaded as docker images. Below is
a list of components essential for scaled deployment of the toolkit.

### Multus CNI

A Container Network Interface (CNI) plugin for Kubernetes that enables you to
attach multiple network interfaces to Kubernetes pods, which usually have only
one network interface. For more details, refer to the
[GitHub page](https://github.com/k8snetworkplumbingwg/multus-cni).

### Intel Device Plugins for Kubernetes

Intel GPU plugin provides access to discrete and integrated Intel GPU devices
supported by the host kernel. It enables offloading compute operations of
Kubernetes workload to GPU devices. It may be beneficial in such use cases as
media transcoding and analytics, cloud gaming, AI training and inference.
For more details, refer to the
[GitHub page](https://github.com/intel/intel-device-plugins-for-kubernetes/blob/main/cmd/gpu_plugin/README.md).

### Calico

- **CNI Plugin**

  [A plugin](https://github.com/projectcalico/calico/tree/master/cni-plugin)
  that enables you to use Calico for deployments based on Container
  Network Interface (CNI). It is available as a
  [docker image](https://hub.docker.com/r/calico/cni).

- **Node**

  [A CNI plugin](https://github.com/projectcalico/calico/tree/master/node)
  that enables you to create a Layer 3 network for Kubernetes
  pods and assign a unique IP address for each. Node is available as a
  [docker image](https://hub.docker.com/r/calico/node/)

- **Kube controllers**

  [A set of controllers](https://github.com/projectcalico/calico/tree/master/kube-controllers)
  that monitor the resources in the Kubernetes API (network,
  policies, nodes) and adjust Calico's CNI configuration. Kube controllers are
  available as a [docker image](https://hub.docker.com/r/calico/kube-controllers).


## Patches

Below is a list of
[Intel not-upstreamed kernel features](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/SPECS/kernel/kernel.spec).\
Check the following quilt patchsets:

- [PREEMPT_RT](#preempt_rt)
- [Time-Sensitive Networking (TSN)](#time-sensitive-networking-tsn)
- [SR-IOV](#sr-iov)
- [DRM](#drm)

### PREEMPT_RT

- 0001-Revert-sched-core-Remove-the-unnecessary-need_resche.rt
- 0001-hrtimer-Use-__raise_softirq_irqoff-to-raise-the-softirq.rt
- 0002-timers-Use-__raise_softirq_irqoff-to-raise-the-softirq.rt
- 0003-softirq-Use-a-dedicated-thread-for-timer-wakeups-on-PRE.rt
- 0004-serial-8250-Switch-to-nbcon-console.rt
- 0005-serial-8250-Revert-drop-lockdep-annotation-from-serial8.rt
- 0006-locking-rt-Remove-one-__cond_lock-in-RT-s-spin_trylock_.rt
- 0007-locking-rt-Add-sparse-annotation-for-RCU.rt
- 0008-locking-rt-Annotate-unlock-followed-by-lock-for-sparse.rt
- 0009-drm-i915-Use-preempt_disable-enable_rt-where-recommende.rt
- 0010-drm-i915-Don-t-disable-interrupts-on-PREEMPT_RT-during-.rt
- 0011-drm-i915-Don-t-check-for-atomic-context-on-PREEMPT_RT.rt
- 0012-drm-i915-Disable-tracing-points-on-PREEMPT_RT.rt
- 0013-drm-i915-gt-Use-spin_lock_irq-instead-of-local_irq_disa.rt
- 0014-drm-i915-Drop-the-irqs_disabled-check.rt
- 0015-drm-i915-guc-Consider-also-RCU-depth-in-busy-loop.rt
- 0016-Revert-drm-i915-Depend-on-PREEMPT_RT.rt
- 0017-sched-Add-TIF_NEED_RESCHED_LAZY-infrastructure.rt
- 0018-sched-Add-Lazy-preemption-model.rt
- 0019-sched-Enable-PREEMPT_DYNAMIC-for-PREEMPT_RT.rt
- 0020-sched-x86-Enable-Lazy-preemption.rt
- 0021-sched-Add-laziest-preempt-model.rt
- 0022-sched-Fixup-the-IS_ENABLED-check-for-PREEMPT_LAZY.rt
- 0023-tracing-Remove-TRACE_FLAG_IRQS_NOSUPPORT.rt
- 0024-tracing-Record-task-flag-NEED_RESCHED_LAZY.rt
- 0025-sysfs-Add-sys-kernel-realtime-entry.rt
- 0001-serial-8250-enable-original-console-by-default.rt
- 0001-kernel-trace-Add-DISALLOW_TRACE_PRINTK-make-option.rt
- 0002-Revert-scripts-remove-bin2c.rt
- 0003-extend-uio-driver-to-supports-msix.rt
- 0004-virtio-add-VIRTIO_PMD-support.rt
- 0005-virt-acrn-Introduce-interfaces-for-PIO-device.rt
- 0006-Add-hypercall-to-access-MSR.rt
- 0007-Revert-spi-Remove-unused-function-spi_busnum_to_master.rt
- 0008-igc-add-CONFIG_IGC_TSN_TRACE-conditional-trace_printk-u.rt
- 0009-stmmac_pci-add-CONFIG_STMMAC_TSN_TRACE-conditional-trac.rt
- 0010-igb-prepare-for-AF_XDP-zero-copy-support.rt
- 0011-igb-Introduce-XSK-data-structures-and-helpers.rt
- 0012-igb-add-AF_XDP-zero-copy-Rx-support.rt
- 0013-igb-add-AF_XDP-zero-copy-Tx-support.rt
- 0014-igb-Add-BTF-based-metadata-for-XDP.rt
- 0015-ANDROID-trace-power-add-trace_clock_set_parent.rt
- 0016-ANDROID-trace-net-use-pK-for-kernel-pointers.rt
- 0017-ANDROID-trace-add-non-hierarchical-function_graph-optio.rt
- 0018-virtio-fix-VIRTIO_PMD-support.rt
- 0019-drm-i915-add-i915-perf-event-capacity.rt
- 0020-drm-xe-pm-allow-xe-with-CONFIG_PM.rt

### Time-Sensitive Networking (TSN)

- 0001-net-pcs-xpcs-enable-xpcs-reset-skipping.tsn
- 0002-net-stmmac-Bugfix-on-stmmac_interrupt-for-WOL.tsn
- 0003-net-phy-increase-gpy-loopback-test-delay.tsn
- 0004-net-stmmac-Resolve-poor-line-rate-after-switching-from.tsn
- 0005-net-phy-dp83867-perform-restart-AN-after-modifying-AN-.tsn
- 0006-stmmac-intel-Separate-ADL-N-and-RPL-P-device-ID-from-T.tsn
- 0007-net-stmmac-Adjust-mac_capabilities-for-Intel-mGbE-2.5G.tsn
- 0008-stmmac-intel-skip-xpcs-reset-for-2.5Gbps-on-Intel-Alde.tsn
- 0009-net-stmmac-add-check-for-2.5G-mode-to-prevent-MAC-capa.tsn
- 0010-stmmac-intel-Enable-PHY-WoL-in-ADL-N.tsn
- 0011-net-phy-reconfigure-PHY-WoL-when-WoL-option-is-enabled.tsn
- 0012-net-stmmac-fix-MAC-and-phylink-mismatch-issue-after-re.tsn
- 0013-net-stmmac-restructure-Rx-Tx-hardware-timestamping-fun.tsn
- 0014-net-stmmac-Add-per-packet-time-based-scheduling-for-XD.tsn
- 0015-net-stmmac-introduce-AF_XDP-ZC-RX-HW-timestamps.tsn
- 0016-net-stmmac-add-fsleep-in-HW-Rx-timestamp-checking-loop.tsn
- 0017-net-stmmac-select-PCS-negotiation-mode-according-to-th.tsn
- 0018-net-pcs-xpcs-re-initiate-clause-37-Auto-negotiation.tsn
- 0019-arch-x86-Add-IPC-mailbox-accessor-function-and-add-SoC.tsn
- 0020-net-stmmac-configure-SerDes-according-to-the-interface.tsn
- 0021-stmmac-intel-interface-switching-support-for-intel-pla.tsn
- 0022-net-stmmac-Set-mac_managed_pm-flag-from-stmmac-to-reso.tsn
- 0023-net-phylink-Add-module_exit.tsn
- 0024-net-stmmac-introduce-AF_XDP-ZC-TX-HW-timestamps.tsn
- 0025-net-sched-taprio-fix-too-early-schedules-switching.tsn
- 0026-net-sched-taprio-fix-cycle-time-adjustment-for-next-en.tsn
- 0027-net-sched-taprio-fix-impacted-fields-value-during-cycl.tsn
- 0028-net-sched-taprio-get-corrected-value-of-cycle_time-and.tsn
- 0029-xsk-add-txtime-field-in-xdp_desc-struct.tsn
- 0030-Revert-net-stmmac-silence-FPE-kernel-logs.tsn
- 0031-Revert-net-stmmac-support-fp-parameter-of-tc-taprio.tsn
- 0032-Revert-net-stmmac-support-fp-parameter-of-tc-mqprio.tsn
- 0033-Revert-net-stmmac-configure-FPE-via-ethtool-mm.tsn
- 0034-Revert-net-stmmac-refactor-FPE-verification-process.tsn
- 0035-Revert-net-stmmac-drop-stmmac_fpe_handshake.tsn
- 0036-Revert-net-stmmac-move-stmmac_fpe_cfg-to-stmmac_priv-d.tsn
- 0037-net-stmmac-add-FPE-preempt-setting-for-TxQ-preemptible.tsn
- 0038-taprio-Add-support-for-frame-preemption-offload.tsn
- 0039-net-stmmac-set-initial-EEE-policy-configuration.tsn
- 0040-net-phy-fix-phylib-s-dual-eee_enabled.tsn
- 0041-net-phy-ensure-that-genphy_c45_an_config_eee_aneg-sees.tsn
- 0042-net-phy-fix-phy_ethtool_set_eee-incorrectly-enabling-L.tsn
- 0001-igc-Set-the-RX-packet-buffer-size-for-TSN-mode.tsn
- 0002-igc-Only-dump-registers-if-configured-to-dump-HW-infor.tsn
- 0003-ethtool-Add-support-for-configuring-frame-preemption.tsn
- 0004-ethtool-Add-support-for-Frame-Preemption-verification.tsn
- 0005-igc-Add-support-for-enabling-frame-preemption-via-etht.tsn
- 0006-igc-Add-support-for-TC_SETUP_PREEMPT.tsn
- 0007-igc-Add-support-for-setting-frame-preemption-configura.tsn
- 0008-igc-Add-support-for-Frame-Preemption-verification.tsn
- 0009-igc-Add-support-for-exposing-frame-preemption-stats-re.tsn
- 0010-igc-Optimize-the-packet-buffer-utilization.tsn
- 0011-igc-Add-support-for-enabling-all-packets-to-be-receive.tsn
- 0012-igc-Add-support-for-DMA-timestamp-for-non-PTP-packets.tsn
- 0013-bpf-add-btf-register-unregister-API.tsn
- 0014-net-core-XDP-metadata-BTF-netlink-API.tsn
- 0015-rtnetlink-Fix-unchecked-return-value-of-dev_xdp_query_.tsn
- 0016-rtnetlink-Add-return-value-check.tsn
- 0017-tools-bpf-Query-XDP-metadata-BTF-ID.tsn
- 0018-tools-bpf-Add-xdp-set-command-for-md-btf.tsn
- 0019-igc-Add-BTF-based-metadata-for-XDP.tsn
- 0020-igc-Enable-HW-RX-Timestamp-for-AF_XDP-ZC.tsn
- 0021-igc-Take-care-of-DMA-timestamp-rollover.tsn
- 0022-igc-Add-SO_TXTIME-for-AF_XDP-ZC.tsn
- 0023-igc-Reodering-the-empty-packet-buffers-and-descriptors.tsn
- 0024-Revert-igc-Add-support-for-PTP-.getcyclesx64.tsn
- 0025-core-Introduce-netdev_tc_map_to_queue_mask.tsn
- 0026-taprio-Replace-tc_map_to_queue_mask.tsn
- 0027-mqprio-Add-support-for-frame-preemption-offload.tsn
- 0030-igc-Reduce-retry-count-to-a-more-reasonable-number.tsn
- 0001-igc-Enable-HW-TX-Timestamp-for-AF_XDP-ZC.tsn
- 0002-igc-Enable-trace-for-HW-TX-Timestamp-AF_XDP-ZC.tsn
- 0003-igc-Remove-the-CONFIG_DEBUG_MISC-condition-for-trace.tsn
- 0006-Revert-net-stmmac-set-initial-EEE-policy-configurati.tsn
- 0001-net-phy-Set-eee_cfg.eee_enabled-according-to-PHY.tsn
- 0001-Revert-net-stmmac-add-FPE-preempt-setting-for-TxQ-pree.tsn
- 0002-Reapply-net-stmmac-move-stmmac_fpe_cfg-to-stmmac_priv-.tsn
- 0003-Reapply-net-stmmac-drop-stmmac_fpe_handshake.tsn
- 0004-Reapply-net-stmmac-refactor-FPE-verification-process.tsn
- 0005-Reapply-net-stmmac-configure-FPE-via-ethtool-mm.tsn
- 0006-Reapply-net-stmmac-support-fp-parameter-of-tc-mqprio.tsn
- 0007-Reapply-net-stmmac-support-fp-parameter-of-tc-taprio.tsn
- 0008-Reapply-net-stmmac-silence-FPE-kernel-logs.tsn

### SR-IOV

- 0001-drm-i915-mtl-Add-C10-table-for-HDMI-Clock-25175.sriov
- 0002-drm-i915-mtl-Copy-c10-phy-pll-sw-state-from-master-t.sriov
- 0003-drm-i915-guc-Define-MAX_DWORDS-for-CTB-HXG-Message.sriov
- 0004-drm-i915-call-taint_for_CI-on-FLR-failure.sriov
- 0005-drm-i915-huc-load-HuC-via-non-POR-GSC-engine-flow.sriov
- 0006-drm-i915-SR-IOV-Enabling-and-Support.sriov
- 0007-Revert-drm-i915-move-platform_engine_mask-and-memory.sriov
- 0008-drm-i915-gt-Enable-the-early-register-to-working-win.sriov
- 0009-drm-i915-gt-Modify-the-adls-mocs-table-same-as-tgl-m.sriov
- 0010-drm-i915-Bypass-gem_set_tiling-and-gem_get_tiling.sriov
- 0011-drm-i915-enable-CCS-on-DG1-and-TGL-for-testing.sriov
- 0012-drm-i915-force-VF-using-v70-GuC-API.sriov
- 0013-drm-i915-fix-regression-on-sriov-vf-failures-due-to-.sriov
- 0014-drm-i915-add-null-pointer-protection-inside-intel_fb.sriov
- 0015-drm-i915-use-the-original-Wa_14010685332-for-PCH_ADP.sriov
- 0016-drm-i915-fix-bitmap-clear-API-region-start-issue.sriov
- 0017-drm-i915-iov-Expose-early-runtime-registers-for-MTL.sriov
- 0018-drm-i915-gt-fix-empty-workaround-list-access-issue.sriov
- 0019-drm-i915-mtl-Add-module-parameter-override-for-Wa_16.sriov
- 0020-drm-i915-mtl-Provide-user-the-option-to-disable-ccs.sriov
- 0021-drm-i915-mtl-Turn-on-Wa_16019325821-Wa_14019159160-b.sriov
- 0022-drm-i915-pf-Use-GPU-to-set-PTE-owner.sriov
- 0023-drm-i915-pf-Use-GPU-to-set-PTE-owner-on-platforms-wi.sriov
- 0024-drm-i915-access-ddc-pointer-only-if-it-is-available.sriov
- 0025-drm-i915-guc-Upgrade-GuC-fw-version-to-70.20.0.sriov
- 0026-drm-i915-iov-Adding-runtime-reg-for-MTL-HuC-status.sriov
- 0027-drm-i915-guc-Upgrade-GuC-fw-version-to-70.29.2.sriov
- 0028-drm-i915-Re-add-enable_rc6-modparam.sriov
- 0032-drm-virtio-freeze-and-restore-hooks-to-support-suspe.sriov
- 0033-drm-virtio-save-and-restore-virtio_gpu_objects.sriov
- 0001-drm-virtio-Use-drm_gem_plane_helper_prepare_fb.patch
- 0034-drm-i915-pf-Introduce-i915_ggtt_save_ptes-and-i915_g.sriov
- 0035-drm-i915-iov-Introduce-VFs-shadow-copy-of-GGTT-on-PF.sriov
- 0036-drm-i915-iov-Shadow-GGTT-mock-selftestes.sriov
- 0037-drm-i915-gt-Don-t-support-GGTT-save-restore-via-BAR-.sriov
- 0038-drm-i915-pf-Add-helpers-for-saving-loading-GGTT-stat.sriov
- 0039-drm-i915-pf-Handle-VF-pause-complete-notification.sriov
- 0040-drm-i915-pf-Allow-to-save-restore-GuC-VF-state.sriov
- 0041-drm-i915-pf-Save-and-restore-VFs-state-during-S2idle.sriov
- 0042-drm-i915-pf-Skip-VF-save-restore-on-S2idle-S3-S4-if-.sriov
- 0043-drm-i915-pf-Start-use-shadow-GGTT-to-save-restore-du.sriov
- 0044-drm-i915-pf-Export-API-to-be-used-by-i915-vfio-pci.sriov
- 0045-drm-i915-iov-Flag-which-tells-whether-PAUSE-is-in-pr.sriov
- 0046-drm-i915-iov-Remember-run-state-on-suspend-and-resto.sriov
- 0047-drm-i915-pf-Pause-VF-before-restore-GuC-state-after-.sriov
- 0048-drm-i915-iov-fix-i915-sriov-build-issue.sriov
- 0001-drm-i915-CTB-TLB-invalidation-fix-on-VM.sriov
- 0002-vfio-i915-Add-vfio_pci-driver-for-Intel-graphics.sriov
- 0003-drm-i915-guc-Upgrade-GuC-fw-version-to-70.36.0.sriov
- 0001-drm-i915-Fix-logic-for-GUC-Process.sriov
- 0001-vfio-i915-Add-support-for-MMIO-save-restore.sriov
- 0002-drm-i915-SR-IOV-Save-Restore-Feature-support.sriov
- 0001-i915-Enable-w-a-16026508708.sriov
- 0001-virtio-hookup-irq_get_affinity-callback.sriov
- 0002-virtio-break-and-reset-virtio-devices-on-device_shut.sriov
- 0003-virtgpu-don-t-reset-on-shutdown.sriov
- 0004-drm-virtio-implement-virtio_gpu_shutdown.sriov
- 0001-drm-virtio-Wait-until-the-control-and-cursor-queues-.sriov
- 0001-drm-i915-move-sriov-selftest-buffer-out-of-stack.sriov
- 0001-drm-i915-Do-not-advertise-about-CCS.sriov
- 0001-Revert-drm-i915-Do-not-advertise-about-CCS.sriov

### DRM

- 0001-drm-i915-enable-guc-submission-for-ADLs-by-default.drm
- 0001-drm-i915-disable-a-couple-of-RT-functions-if-RT-is-d.drm
- 0001-drm-i915-disable-dGPU-support-with-RT-kernel.drm
- 0001-i915-Update-GUC-to-v70.44.1-for-i915-platforms.drm
- 0001-Revert-drm-i915-disable-dGPU-support-with-RT-kernel.drm
- 0001-drm-i915-gt-Avoid-using-masked-workaround-for-CCS_MODE.drm
- 0002-drm-i915-gt-Move-the-CCS-mode-variable-to-a-global-pos.drm
- 0003-drm-i915-gt-Allow-the-creation-of-multi-mode-CCS-masks.drm
- 0004-drm-i915-gt-Refactor-uabi-engine-class-instance-list-c.drm
- 0005-drm-i915-gem-Mark-and-verify-UABI-engine-validity.drm
- 0006-drm-i915-gt-Introduce-for_each_enabled_engine-and-appl.drm
- 0007-drm-i915-gt-Manage-CCS-engine-creation-within-UABI-exp.drm
- 0008-drm-i915-gt-Remove-cslices-mask-value-from-the-CCS-str.drm
- 0009-drm-i915-gt-Expose-the-number-of-total-CCS-slices.drm
- 0010-drm-i915-gt-Store-engine-related-sysfs-kobjects.drm
- 0011-drm-i915-gt-Store-active-CCS-mask.drm
- 0012-drm-i915-Protect-access-to-the-UABI-engines-list-with-.drm
- 0013-drm-i915-gt-Isolate-single-sysfs-engine-file-creation.drm
- 0014-drm-i915-gt-Implement-creation-and-removal-routines-fo.drm
- 0015-drm-i915-gt-Allow-the-user-to-change-the-CCS-mode-thro.drm
- 0016-drm-i915-gt-Refactor-CCS-mode-handling-and-improve-app.drm
- 0017-drm-i915-no-waiting-for-page-flip-in-vpp-case.drm
- 0001-Remove-unneeded-files.patch
- 0001-i915-gt-Upgrade-GuC-70.44.1-70.49.4.drm
- 0001-drm-i915-no-force-probe-needed-for-mtl-platform.drm
