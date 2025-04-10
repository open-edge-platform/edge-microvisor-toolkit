# Get Started

Edge Microvisor Toolkit is a lightweight, container-first Linux distribution
optimized for Intel® architecture. It provides a secure and high-performing environment for
deploying edge workloads across multiple deployment models.

This section provides its overview in terms of both the Operating System and the build pipeline.
See what usage scenarios you can choose, in the description below, and move on to:

* [Build an Edge Microvisor Toolkit Image](./get-started/building-howto.md)
* [Install Edge Microvisor Toolkit](./get-started/installation-howto.md)



## Usage Scenarios

Edge Microvisor Toolkit can be used for standalone edge node deployments or with Edge
Orchestrator, a complete integrated system providing full lifecycle management for your edge
devices, including remote deployment and management of Kubernetes applications.

This section outlines the key usage models intended for the initial release of
Edge Microvisor Toolkit.

### Standalone Developer Edge Node

To create a custom developer build of Edge Microvisor Toolkit, follow the steps below:

- Install the mutable OS via ISO image that includes only essential pre-installed packages, providing a ready-to-use base environment.
- Install additional RPM packages, using DNF to tailor the OS to your specific needs.
- Update installed RPMs regularly to stay up-to-date in the OS, for package updates, kernel updates, security vulnerability fixes and bug fixes
- Build a custom OS image, using the OS toolkit and available packages, which enables you to:
  - Configure the system for specialized workloads or environments.
  - Experiment with simplified or enhanced configurations tailored for your specific workloads.
  - Explore, using in-built monitoring tools to track system performance, resource
    usage, and log data for deeper insights into operational behavior.

| Item | Details |
| -------------| ------- |
| Packages     | ~400 approximately    |
| Core system tools | bash, coreutils, util-linux, tar, gzip|
| Networking | curl, wget, iproute2, iptables, openssh |
| Package Management | tdnf, rpm |
| Development | gcc, make, python3, perl, cmake, git |
| Security | openssl, gnupg, selinux, cryptsetup, tpm2-tools |
| Filesystem | e2fsprogs, mount |
| Included in kernel | iGPU, dGPU (Intel® Arc), SRIOV, WiFi, Ethernet, Bluetooth, GPIO, UART, I2C, CAN, USB, PCIe, PWM, SATA, NVMe, MMC/SD, TPM, Manageability Engine, Power Management, Watchdog, RAS |

The supported package repository offers additional `rpm` for tailoring the image to specific needs of container runtime, virtualization, orchestration software, monitoring tools, standard cloud-edge (CNCF) software, and more.

### Standalone Edge Node

The standalone edge node uses the standard immutable build and provides an ISO image that can be flashed to a USB device and installed on edge nodes. The installer installs the microvisor and Kubernetes to the edge node with just essential functionality to run a single node cluster. The edge node will serve as both control- and worker node. Additional worker nodes can be added to the cluster through Kubernetes. Future releases will allow standalone edge nodes to join an existing Edge Orchestrator Toolkit backend deployed on-prem or in the cloud to support scale out and management of larger infrastructures. The Standalone Edge Node enables you to quickly get an edge node up and running without deploying backend services, ready to deploy Kubernetes applications through `kubectl`, `helm`, or Kubernetes web dashboard.

```{admonition} The standalone edge node does not support the real-time version currently.
:class: note

The immutable OS image does not include the Kubernetes software and
extensions. After the OS is installed, they are deployed on a writable section of the
filesystem. Image and orchestration system updates are not enabled natively, at the moment.
```

The ISO installer for the standalone Edge Node is available for download at
[Intel® Edge Software Hub](TODO/add/link/to/download).

### Edge Node with Edge Orchestrator

Edge Microvisor Toolkit supports deployment of its two versions with Edge Orchestrator:

- Microvisor Immutable Image
- Microvisor Immutable Image with Real Time

For details on deploying Microvisor with Edge Orchestrator, refer to the
[Edge Orchestrator deployment guide](../user-guide/deployment-edge-orchestrator.md)

## Image Support

The toolkit comes pre-configured to produce different images, the table below outlines the key
differences between those.

|  Use Case        | Standalone Image     | Immutable Image                                   |
| -----------------| -------------------- | ------------------------------------------------- |
| What can you do? | <ul><li>Easy to install, bootable ISO image with precompiled packages for developer evaluation</li> <li> Includes installable rpms with TDNF for extending baseline functionality.</li> <li>Complete with toolkit to build image with an opt-in data integrity and security features </li></ul> | <ul><li>Designed for Open Edge Platforms and can be used to onboard and provision edge nodes at scale</li><li>Can be used independently on baremetal and as guest OS</li><li>Fast atomic updates & rollback support with small image footprint and short boot time|
| Image Type       | Mutable ISO          | Immutable RAW + VHD                               |
| Update Mechanism | RPM package updates with TDNF | Image based A/B updates + Rollback       |
| Linux Kernel     | Intel® Kernel 6.12   | Intel® Kernel 6.12                                |
| Real time        | No                   | Two images provided one RT kernel and one without |
| OS Bootloader    | GRUB                 | systemd-boot                                      |
| Secure Boot      | Available for opt-in | Enabled                                           |
| Full Disc Encryption | Available for opt-in | Enabled                                       |
| dm-verity        | Available for opt-in | Enabled                                           |
| SELinux          | Permissive           | Permissive                                        |

## Next Steps

- [System Requirements](./introduction)
- [Production Deployment with Edge Orchestrator](./deployment-edge-orchestrator.md)


```{toctree}
./get-started/building-howto.md
./get-started/installation-howto.md
./get-started/sb-howto.md
```
