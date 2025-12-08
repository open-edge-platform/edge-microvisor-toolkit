# System Requirements

<!--
Content Requirements:
1. Provide minimum and recommended hardware specs.
2. List supported software environments or dependencies.
3. Ensure clarity for different installation environments (e.g., virtual machines, embedded systems).
-->

The hardware and software requirements outlined here apply to Edge Microvisor Toolkit itself.
Specific requirements will mostly depend on the type of deployment (container, VM,
K8s workload) and the type and number of workloads deployed on a node. When choosing the
hardware device, microvisor image, and the workload packaging method, consider the
requirements & KPIs of the intended applications/workloads, to ensure that sufficient
residual compute capability is available.

## Hardware Requirements

Edge Microvisor Toolkit is designed to support all Intel® platforms with the latest
Intel® kernel to provide all available features for applications
and workloads. It has been validated on the following platforms:

**CPU**

|      Atom             |               Core™           |      Xeon®              |
| ----------------------| ----------------------------- | ----------------------- |
| Intel® Atom® X Series | 12th Gen Intel® Core™         | 5th Gen Intel® Xeon® SP |
|                       | 13th Gen Intel® Core™         | 4th Gen Intel® Xeon® SP |
|                       | Intel® Core™ Ultra (Series 1) | 3rd Gen Intel® Xeon® SP |

**Discrete GPU**

|        Intel®         |           NVIDIA®             |
|-----------------------|-------------------------------|
| Intel® Arc™ B580      | NVIDIA® Tesla® P100           |
|                       | GeForce RTX™ 3090             |

## Recommended Hardware Configuration

### Edge Microvisor Toolkit Developer Node

| Component                  | Intel® Atom™ | Core™/Core™ Ultra | Xeon®   |
|----------------------------|--------------|-------------------|---------|
| RAM                        | 2 GB         | 2 GB              | 2 GB    |
| Storage (SSD/NVMe or eMMC) | 32 GB        | 32 GB             | 32 GB   |
| Networking (Ethernet)      | 1 GbE        | 1 GbE             | 1 GbE   |

### Edge Microvisor Toolkit (Edge Manageability Framework or Standalone Node)

| Component                  | Intel® Atom™    | Core™/Core™ Ultra | Xeon®           |
|----------------------------|-----------------|-------------------|-----------------|
| RAM                        | 16 GB           | 64 GB             | 128 GB          |
| Storage (SSD/NVMe or eMMC) | 64 GB           | 512 GB            | 1 TB            |
| Networking (Ethernet)      | 1 GbE or higher | 1 GbE or higher   | 1 GbE or higher |

## Software Requirements

| Component        | Edge Microvisor Toolkit Developer Node | Edge Microvisor Toolkit (Edge Manageability Framework or Standalone Node) |
|------------------|-------------------------|-------------------------|
| Kernel Version   | Intel® Kernel 6.12      | Intel® Kernel 6.12      |
| Bootloader       | GRUB                    | Systemd-boot            |
| Update Mechanism | RPM-based with TDNF     | Image-based A/B updates |

## Minimum Hardware Configuration for Building OS Image

| CPU | RAM | Storage |
|---|---|---|
| 13th, 14th Generation Intel® Core™ (Raptor Lake), <br> 4 cores | 32 GB <br> (25 GB free) | 200 GB |