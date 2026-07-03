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

Intel Atom® processor:
- Intel Atom® X series processor
- Intel Atom® x7000RE, x7000C, and x7000FE processor series (code-named Amston Lake)

Intel® Core™  processor:
- 12th Gen Intel® Core™ processor
- 13th Gen Intel® Core™ processor
- Intel® Core™ Ultra (Series 1) processor
- Intel® processor N150 and N250, and Intel® Core™ 3 processor N355 (code-named Twin Lake)
- Intel® Core™ Ultra processor series 2 (code-named Arrow Lake-S)
- Intel® Core™ Ultra 200U and 200H series processors (code-named Arrow Lake U/H)
- Intel® Core™ processor 200 series
- Intel® Core™ Ultra processor
- Intel® Core™ Ultra processor for the Edge (PS Series)

Intel® Xeon® processor:
- 5th Gen Intel® Xeon® SP
- 4th Gen Intel® Xeon® SP
- 3rd Gen Intel® Xeon® SP

**Discrete GPU**

Intel® GPU:
- Intel® Arc™ B580 GPU

NVIDIA® GPU:
- NVIDIA® Tesla® P100 GPU
- GeForce RTX™ 3090 GPU

## Recommended Hardware Configuration

### Edge Microvisor Toolkit Developer Node

| Component                  | Intel® Atom™ | Core™/Core™ Ultra | Xeon®   |
|----------------------------|--------------|-------------------|---------|
| RAM                        | 2 GB         | 2 GB              | 2 GB    |
| Storage (SSD/NVMe or eMMC) | 32 GB        | 32 GB             | 32 GB   |
| Networking (Ethernet)      | 1 GbE        | 1 GbE             | 1 GbE   |

### Edge Microvisor Toolkit (Standalone Node)

| Component                  | Intel® Atom™    | Core™/Core™ Ultra | Xeon®           |
|----------------------------|-----------------|-------------------|-----------------|
| RAM                        | 16 GB           | 64 GB             | 128 GB          |
| Storage (SSD/NVMe or eMMC) | 64 GB           | 512 GB            | 1 TB            |
| Networking (Ethernet)      | 1 GbE or higher | 1 GbE or higher   | 1 GbE or higher |


## Software Requirements

| Component        | Edge Microvisor Toolkit Developer Node | Edge Microvisor Toolkit (Standalone Node) |
|------------------|----------------------------------------|---------------------------------------------------------------------------|
| Kernel Version   | Intel® Kernel 6.18                     | Intel® Kernel 6.18                                                        |
| Bootloader       | GRUB                                   | Systemd-boot                                                              |
| Update Mechanism | RPM-based with TDNF                    | Image-based A/B updates                                                   |
