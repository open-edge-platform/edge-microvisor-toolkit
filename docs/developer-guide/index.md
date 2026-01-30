# Edge Microvisor Toolkit Documentation

<!--hide_directive
<div class="component_card_widget">
  <a class="icon_github" href="https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/README.md">
     GitHub project
  </a>
</div>
hide_directive-->

Edge Microvisor Toolkit is a Linux-based operating system that demonstrates the full potential of Intel hardware for Edge AI workloads with the most recent updates that may not yet be available in other distributions. The Linux patches optimize both performance and capabilities of Intel silicon, streamlining integration for operating system vendors and other technology partners.

Edge Microvisor Toolkit is published in several pre-configured versions to target
various use cases. The toolkit is available as immutable and mutable versions -- including a standalone node prepared for partner evaluation and a real-time developer node designed with the Preempt RT Linux Kernel for predictable performance -- results in a
Linux operating system primed to demonstrate how Intel processors can cost-effectively minimize latency, maximize security, and optimize performance for edge AI workloads.
To learn more, refer to [Edge Microvisor Toolkit Versions](./get-started/emt-versions.md).

## Demonstrating the Capabilities of Intel Technology

Through its optimizations for Intel platforms, Edge Microvisor Toolkit showcases distinctive capabilities for operating system vendors and other partners, who can typically obtain early access to next-generation Intel platform innovations, features, and optimizations. Here are some of the toolkit's capabilities that help highlight the power of Intel technology:

**Support for [multiple scenarios](./get-started/emt-versions.md#how-usage-scenarios-affect-emt-setup):**
Use industry-specific sample applications with benchmarks, as well as edge AI libraries with OpenVINO™ inferencing runtime software development kits, to rapidly build, validate, and optimize edge AI solutions on Intel silicon across scenarios and industries.

**[Built-in security](./emt-security-considerations.md):**
Protect computers, hypervisors, apps, and data with such capabilities as trusted compute, single-root I/O virtualization (SR-IOV), secure boot, full-disk encryption, dm-verity, and Trusted Platform Module (TPM).
The microvisor uses a Unified Kernel Image (UKI), which is a single EFI binary that packages together the Intel® kernel, `initramfs`, and associated kernel command-line parameters, a design that simplifies the boot process on UEFI
systems and improves security, especially when combined with Secure Boot.

**[Flexibility and modularity](./get-started/emt-installation-howto.md) with foundational extensions:**
Rapidly evaluate a diversity of deployments and applications, including cloud native, bare metal, and virtual machines. Image formats include ISO, VHD, VHDX, and RAW. The flexible build infrastructure of Edge Microvisor Toolkit enables you to create custom images from a large set of pre-provisioned packages by using .spec files.

## Showcasing Intel Processors and GPUs with Kernel Optimizations

Edge Microvisor Toolkit has undergone extensive validation across the Intel Xeon®, Intel® Core Ultra™, Intel Core™, and Intel® Atom® processor families. The toolkit provides robust support for integrated and Intel discrete GPU cards as well as an integrated NPU. There are pre-tuned drivers and acceleration libraries for Intel® CPUs and GPUs.

> **Note:** You can learn more about specific kernel patches related to GPU and NPU support
> in the relevant [SPEC file](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/SPECS/kernel/kernel.spec)

The kernel used in the developer node of Edge Microvisor Toolkit, for example, includes the following: iGPU, dGPU (Intel® Arc™), SR-IOV, WiFi, Ethernet, Bluetooth, GPIO, UART, I2C, CAN, USB, PCIe, PWM, SATA, NVMe, MMC/SD, TPM, Manageability Engine, Power Management, Watchdog, and RAS.

Intel® Arc™ B-Series Graphics and other components are discoverable for containerized applications and VMs with pass-through mode to deliver processing power to distributed applications at the edge -- and that processing power can be fine tuned to minimize latency.

## Performance Indicators

- Boot time of less than 8 seconds on entry-level Intel® Core™ platforms.
- Fast A/B image updates (<30s) with automatic rollback support on Edge Microvisor Toolkit.
- Small footprint with less than 750MB of disk space required for the operating system and a compressed RAW image size less than 350MB.

## License Information

Based on [Azure Linux](https://github.com/microsoft/azurelinux), Edge Microvisor Toolkit shares its permissive open-source license:
[MIT](https://github.com/microsoft/azurelinux/blob/3.0/LICENSE).

See the
[LICENSE](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/LICENSE)
document.

## Next Steps

[Architecture Overview](./emt-architecture-overview.md)

<!--hide_directive
:::{toctree}
:hidden:

emt-get-started
emt-architecture-overview
emt-deployment-edge-orchestrator
emt-bootkit
emt-security-considerations
emt-contribution
emt-troubleshooting
emt-system-requirements
emt-tutorials
:::
hide_directive-->
