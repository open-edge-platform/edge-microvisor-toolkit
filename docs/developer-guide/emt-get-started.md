# Get Started

Edge Microvisor Toolkit is a lightweight, container-first Linux distribution,
optimized for Intel® architecture. It provides a secure and high-performing
environment for deploying edge workloads across multiple deployment models.

[Hardware and Software Requirements](./emt-system-requirements.md)

## Usage Scenarios

This section outlines the key usage models intended for the initial release of
Edge Microvisor Toolkit.

It can be used for standalone edge node deployments, or with Edge Manageability
Framework - a complete integrated system providing full lifecycle management for
your edge devices, including remote deployment and management of Kubernetes
applications.

[Choose pre-configured Edge Microvisor Toolkit Image](./emt-architecture-overview.md#edge-microvisor-toolkit-image-versions)

[Build Your Own Edge Microvisor Toolkit](./get-started/emt-building-howto.md)

## Install Edge Microvisor Toolkit

[Bare Metal Installation](./get-started/deployment/emt-bare-metal.md)

[Virtual Machine Installation](./get-started/deployment/emt-vm-guest.md)

## Host Guest VMs under Edge Microvisor Toolkit

[Deploying Other OS as Guest Virtual Machines under EMT Host](./get-started/deployment/emt-vm-host.md)

[Go to the Edge Microvisor Toolkit Standalone Node repository](https://github.com/open-edge-platform/edge-microvisor-toolkit-standalone-node).

### Edge Microvisor Toolkit with Edge Manageability Framework

Edge Microvisor Toolkit supports deployment of its two versions with Edge
Manageability Framework:

- Microvisor Immutable Image
- Microvisor Immutable Image with Real Time

For details on deploying Microvisor with Edge Manageability Framework, refer to
the [Edge Manageability Framework deployment guide](./emt-deployment-edge-orchestrator.md).

## Image Support

The toolkit comes pre-configured to produce different images, the table below
outlines the key differences between those.

|  Feature         | Edge Microvisor Toolkit Developer Node | Edge Microvisor Toolkit Standalone Node & Orchestrated                                   |
| -----------------| -------------------- | ------------------------------------------------- |
| Capabilities | <ul><li>Easy to install, bootable ISO image with precompiled packages for developer evaluation.</li> <li> Includes installable rpms with TDNF for extending baseline functionality.</li> <li>Complete with toolkit to build image with an opt-in data integrity and security features.</li></ul> | <ul><li>Designed for Open Edge Platforms and can be used to onboard and provision edge nodes at scale.</li><li>Can be used independently on bare-metal and as guest OS.</li><li>Fast atomic updates & rollback support with small image footprint and short boot time.|
| Image Type       | Mutable ISO          | Immutable RAW + VHD                               |
| Update Mechanism | RPM package updates with TDNF | Image based A/B updates + Rollback       |
| Linux Kernel     | Intel® Kernel 6.12   | Intel® Kernel 6.12                                |
| Real time        | Available for opt-in | Two images provided: one with RT kernel and one without |
| Add-on packages  | Available for opt-in: Docker + K3s | Built into image: Docker + K3s |
| OS Bootloader    | GRUB                 | systemd-boot                                      |
| Secure Boot      | Available for opt-in | Enabled                                           |
| Full Disc Encryption | Available for opt-in | Enabled                                       |
| dm-verity        | Available for opt-in | Enabled                                           |
| SELinux          | Permissive           | Permissive                                        |

## Next Steps

- [System Requirements](./emt-system-requirements.md)
- [Production Deployment with Edge Manageability Framework](./emt-deployment-edge-orchestrator.md)

:::{toctree}
./get-started/emt-building-howto.md
./get-started/emt-installation-howto.md
./get-started/emt-sb-howto.md
:::
