# System Requirements

<!--
Content Requirements:
1. Provide minimum and recommended hardware specs.
2. List supported software environments or dependencies.
3. Ensure clarity for different installation environments (e.g., virtual machines, embedded systems).
-->

The hardware and software requirements outlined below are reflective of Edge Microvisor Toolkit itself. Specific requirements will for the most part depend on the deployment (e.g. container, VM, K8s workload), type and number of workloads deployed on a node. Consideration should be given to the requirements & KPIs by the applications/workloads intended to run on the edge devices to ensure sufficient residual compute is available when choosing hardware device, microvisor image and how the workload is packaged.

## Hardware Requirements

Edge Microvisor Toolkit is designed to support all Intel® platforms with the latest
Intel® kernel to provide all available features for application
and workloads. The microvisor has been validated on the following platforms:

|      Atom             |               Core            |      Xeon      |
| ----------------------| ----------------------------- | -------------- |
| Intel® Atom® X Series | 12th Gen Intel® Core™         | 4th Gen Intel® Xeon® SP |
|                       | 13th Gen Intel® Core™         | 3rd Gen Intel® Xeon® SP |
|                       | Intel® Core™ Ultra (Series 1) |                |

## Recommended Hardware Configuration

The following outlines the recommended hardware configuration to run Edge Microvisor Toolkit.

| Component    | Standalone Installation    | Production Deployment (Orchestrator Managed) |
|--------------|----------------------------|----------------------------------------------|
| CPU          | Intel® Atom, Core, or Xeon | Intel® Atom, Core, or Xeon                   |
| RAM          | 2GB minimum                | 8GB minimum                                  |
| Storage      | 32GB SSD/NVMe or eMMC      | 64GB SSD or NVMe                             |
| Networking   | 1GbE Ethernet or Wi-Fi     | 1GbE Ethernet or higher                      |

## Software Requirements

| Component        | Standalone Installation | Production Deployment   |
|------------------|-------------------------|-------------------------|
| Kernel Version   | Intel® Kernel 6.12      | Intel® Kernel 6.12      |
| Bootloader       | GRUB                    | Systemd-boot            |
| Update Mechanism | RPM-based with TDNF     | Image-based A/B updates |