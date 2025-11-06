# Get Started

Edge Microvisor Toolkit is a reference Linux operating system that demonstrates the full
capabilities of Intel platforms for Edge AI workloads. It incorporates Intel-developed Linux
patches that have not yet been upstreamed. These patches optimize performance and enhance other
capabilities for Intel silicon, streamlining integration for operating system vendors and
technology partners.


[Hardware and Software Requirements](./emt-system-requirements.md)

## Usage Scenarios

To validate workloads on Intel silicon, you can deploy Edge Microvisor Toolkit as a
[standalone edge node](./get-started/emt-build-and-deploy.md) or with Edge Manageability
Framework, a complete integrated system for edge devices with full lifecycle management,
including remote deployment and management of applications orchestrated by Kubernetes.

[Choose a pre-configured Edge Microvisor Toolkit Image](./emt-architecture-overview.md#edge-microvisor-toolkit-image-versions)

[Build Your Own Edge Microvisor Toolkit](./get-started/emt-building-howto.md)

## Install Edge Microvisor Toolkit

[Bare Metal Installation](./get-started/deployment/emt-bare-metal.md)

[Virtual Machine Installation](./get-started/deployment/emt-vm-guest.md)

## Host Guest VMs under Edge Microvisor Toolkit

[Deploying Other OS as Guest Virtual Machines under EMT Host](./get-started/deployment/emt-vm-host.md)

<!--hide_directive
:::{toctree}
./get-started/emt-building-howto.md
./get-started/emt-build-and-deploy.md
./get-started/emt-installation-howto.md
:::
hide_directive-->