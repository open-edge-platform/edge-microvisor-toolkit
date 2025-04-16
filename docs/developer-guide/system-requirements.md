# System Requirements

<!--
Content Requirements:
1. Provide minimum and recommended hardware specs.
2. List supported software environments or dependencies.
3. Ensure clarity for different installation environments (e.g., virtual machines, embedded systems).
-->

General hardware and software requirements outlined apply to Edge Microvisor Toolkit itself. Specific requirements will mostly depend on specific deployment (container, VM, K8s workload), as well as type and number of workloads deployed on a node. When choosing the hardware device, microvisor image and the workload packaging method, consider the requirements & KPIs of the intended applications/workloads, to ensure that sufficient local compute capability is available.

## Hardware Requirements

Edge Microvisor Toolkit is designed to support all Intel® platforms with the latest
Intel® kernel to provide all available features for applications
and workloads. Microvisor has been validated on the following platforms:

|      Atom             |               Core            |      Xeon      |
| ----------------------| ----------------------------- | -------------- |
| Intel® Atom® X Series | 12th Gen Intel® Core™         | 4th Gen Intel® Xeon® SP |
|                       | 13th Gen Intel® Core™         | 3rd Gen Intel® Xeon® SP |
|                       | Intel® Core™ Ultra (Series 1) |                |

## Recommended Hardware Configuration

| Component    | Edge Microvisor Toolkit Developer | Edge Microvisor Toolkit (Open Edge Platform or Standalone) |
|--------------|----------------------------|----------------------------------------------|
| CPU          | Intel® Atom, Core, or Xeon | Intel® Atom, Core, or Xeon                   |
| RAM          | 2GB minimum                | 8GB minimum                                  |
| Storage      | 32GB SSD/NVMe or eMMC      | 64GB SSD or NVMe                             |
| Networking   | 1GbE Ethernet              | 1GbE Ethernet or higher                      |

## Software Requirements

| Component        | Edge Microvisor Toolkit Developer | Edge Microvisor Toolkit (Open Edge Platform or Standalone) |
|------------------|-------------------------|-------------------------|
| Kernel Version   | Intel® Kernel 6.12      | Intel® Kernel 6.12      |
| Bootloader       | GRUB                    | Systemd-boot            |
| Update Mechanism | RPM-based with TDNF     | Image-based A/B updates |
