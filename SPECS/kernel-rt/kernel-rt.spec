Summary:        Preempt RT Linux Kernel
Name:           kernel-rt
Version:        6.18.15
Release:        1%{?dist}
License:        GPLv2
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Kernel
URL:            https://www.kernel.org/pub/linux/kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.18.15.tar.gz
Source1:        config
Source3:        sha512hmac-openssl.sh
Source4:        emt-ca-20211013.pem
Source5:        cpupower
Source6:        cpupower.service

# Intel Kernel Patches
# Series file for v6.18.15 linux kernel
# df0dc1b06fb6b Linux 6.18.15
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
# edcac
Patch08001: 0001-EDAC-igen6-Add-two-Intel-Amston-Lake-SoCs-support.edac
Patch08002: 0002-EDAC-igen6-Add-more-Intel-Panther-Lake-H-SoCs-support.edac
Patch08003: 0003-EDAC-igen6-Fix-masks-of-MCHBAR-TOM-TOUUD-registers.edac
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
# lpss
Patch12001: 0001-Added-spi_set_cs-for-more-stable-r-w-operations-in.lpss

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
%setup -q -n linux-6.18.15
%autosetup -p1 -n linux-6.18.15
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
