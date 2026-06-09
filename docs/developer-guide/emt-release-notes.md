# Edge Microvisor Toolkit - Release Notes

## Version 26.06

The Open Edge Platform 2026.1 release introduces the 26.06 branch of Edge
Microvisor Toolkit (EMT) — the next evolution following EMT 3.0.
The branch is recommended for continued development and innovation on latest
Intel Edge platforms.

The 26.06 series is built on Linux Kernel 6.18 and adds support for
Intel Wildcat Lake platform, along with ongoing platform enablement and
improvements.

**New**

- Support for libdisplay-info

**Improved**

- Upgraded the Linux kernel to 6.18.23 with support for
  [Intel Wildcat Lake and other platforms](./emt-system-requirements.md).
- Updated the Azure Linux base to 3.0.20260304, sync golang, runc, libseccomp and
  few other packages.
- Removed support for edge-node-agents.
- Removed the `add-sudoer.sh` post-install script from non-development image
  configurations, tightening the default security posture of production images.
- Removed SPECS-EXTENDED and SPECS-SIGNED spec directories, simplifying the
  repository structure.
- Removed support for perl-DBIx-Simple package from the distribution.
- Updated versions of:

  alsa-lib,caddy, device-discovery, elfutils, expat, fluent-bit,\
  gstreamer1, gstreamer1-plugins-base, intel-compute-runtime,\
  intel-gmmlib, intel-idv-services, intel-level-zero, intel-media-driver,\
  intel-npu-driver, intel-npu-firmware, intel-vpl-gpu-rt, intel-xpu-smi,\
  libvirt, libvirt-python, libvpl, linux-firmware, nvidia-data-center-driver,\
  ocl-icd, otelcol-contrib, rpc, tink-worker, xorg-x11-server, yq
