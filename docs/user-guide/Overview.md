---
orphan: true
---
# Overview

The Edge Microvisor Toolkit Developer is a package that contains mutable Edge Microvisor Toolkit in an `ISO` installer format. Edge Microvisor Toolkit is a streamlined container operating system that showcases the Intel silicon optimizations. Built on Azure Linux, it features a Linux Kernel maintained by
Intel, incorporating all the latest kernel and user patches.

The Edge Microvisor Toolkit Developer has undergone extensive validation across
all Intel platforms such as Xeon®, Intel® Core Ultra™, Intel Core™ and Intel®
Atom®. The Edge Microvisor Toolkit Developer Node allows users to quickly deploy
and run their solutions for multiple scenarios like benchmarking and validation
of Edge AI computing workloads. The Edge Microvisor Toolkit Developer is
available to download from the Open-source repository.

The Edge Microvisor Toolkit Developer supports Native applications and VM based applications out of the box. Users can customize their Edge Node using the
provided `dnf` package manager to install container runtimes and Docker tools.
This allows users to run Docker containers.

The Edge Microvisor Toolkit Developer is Fully open-Source and royalty free.

## Get started

### System requirements

Edge Microvisor Toolkit Developer is designed to support all Intel® platforms
with the latest Intel® kernel to ensure all features are exposed and available
for application and workloads. The microvisor has been validated on the
following platforms.

|      Atom             |               Core            |      Xeon      |
| ----------------------| ----------------------------- | -------------- |
| Intel® Atom® X Series | 12th Gen Intel® Core™         | 4th Gen Intel® Xeon® SP |
|                       | 13th Gen Intel® Core™         | 3rd Gen Intel® Xeon® SP |
|                       | Intel® Core™ Ultra (Series 1) |                |

The following outlines the recommended hardware configuration to run Edge
Microvisor Toolkit Developer.

| Component    | Standalone Installation    |
|--------------|----------------------------|
| CPU          | Intel® Atom, Core, or Xeon |
| RAM          | 2GB minimum                |
| Storage      | 32GB SSD/NVMe or eMMC      |
| Networking   | 1GbE Ethernet or Wi-Fi     |

### Installation Instructions

You can download the Edge Microvisor Toolkit Developer from [Intel Edge Catalog](https://edgesoftwarecatalog.intel.com/)

> TODO: Add step by step guide to download the ISO image from ESC with screenshots

## Secure by Design

- Package based updates with 'dnf'.
- Support for Secure Boot (optional) and TPM support for hardware-verified integrity.
- Support for Full Disc Encryption (optional)

## Optimized for Intel® Architecture

- Pre-tuned drivers and acceleration libraries for Intel® CPUs and GPUs.
- Enables Intel® silicon ahead of Operating System vendors (OSVs), unlocking
features that may not be accepted upstream.
- Intel® Linux* Kernel 6.12 with optimized security settings

## Flexible and Modular Deployment

- Supports bare metal, VM-based, and containerized deployments.
- Supports Kubernetes*, Docker*, and OCI-compliant runtimes.

## Open Source and Extensible

- Fully open-source and royalty-free.
- Actively integrates OxM platform features and third-party vendor hardware.

## Getting help

If you encounter bugs, have feature requests, or need assistance, file a GitHub Issue. Before submitting a new report, check the existing issues to see if a
similar one has not been filed already. If no matching issue is found, feel free
to file the issue as described in the contribution guide.

## License Information

Edge Microvisor Toolkit Developer is based on [Azure Linux](https://github.com/microsoft/azurelinux), sharing its permissive open-source license:
[MIT](https://github.com/microsoft/azurelinux/blob/3.0/LICENSE).
