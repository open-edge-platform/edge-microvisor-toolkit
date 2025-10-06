# Edge Microvisor Toolkit

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

Edge Microvisor Toolkit is a reference Linux operating system that demonstrates 
the full capabilities of Intel processors for Edge AI workloads through 
Linux patches from Intel that are yet to be upstreamed. Built on Azure Linux, 
it incorporates all the latest kernel and user patches from a Linux 
Kernel maintained by Intel.

Edge Microvisor Toolkit is published in several versions, both immutable and mutable, for quickly deploying, validating, and benchmarking edge AI workloads, including those requiring real-time processing. You can also use the toolkit's flexible build infrastructure to create custom images from a large set of pre-provisioned packages.

Here are the published versions:

* [Edge Microvisor Toolkit Standalone Node (immutable)](https://github.com/open-edge-platform/edge-microvisor-toolkit-standalone-node)
* [Edge Microvisor Toolkit Developer Node with or without real-time extensions (mutable)](./docs/developer-guide/emt-architecture-overview.md#developer-node-mutable-iso-image)
* [Edge Microvisor Toolkit (mutuable or immutable) for use with Edge Manageability Framework](./docs/developer-guide/emt-deployment-edge-orchestrator.md)
* [Edge Microvisor Bootkit](./docs/developer-guide/emt-bootkit.md)

Edge Microvisor Toolkit has undergone extensive validation across the Intel Xeon®, Intel® Core Ultra™, Intel Core™, and Intel® Atom® processor families. It provides robust support for integrated NPU as well as a
[selection of discrete GPU cards](./docs/developer-guide/emt-system-requirements.md#hardware-requirements).

You can either build Edge Microvisor Toolkit by following step-by-step
instructions or download it directly. Both the build system and Edge Microvisor
Toolkit are available as open source.

## Get Started

To find out how to deploy and work with Edge Microvisor Toolkit, see [Get Started](./docs/developer-guide/emt-get-started.md), check out the video demonstrations on [YouTube](https://www.youtube.com/playlist?list=PLg-UKERBljNxIMUUPWHpA8ZJ_YUU5tPP9), or [view the documentation website](https://docs.openedgeplatform.intel.com/2025.1/edge-microvisor-toolkit/index.html).

## Get Help or Contribute  

Vendors, developers, and technology partners can take part in the GitHub
community for Edge Microvisor Toolkit in various ways: contributing code, proposing
a design, downloading and trying out a release, opening an issue,
benchmarking application performance, and participating in [Discussions](https://github.com/open-edge-platform/edge-microvisor-toolkit/discussions). To get help with Edge Microvisor Toolkit, contribute to its
development, or learn more, see the following resources:

- [Open an issue](https://github.com/open-edge-platform/edge-microvisor-toolkit/issues)
- [Submit a pull request](https://github.com/open-edge-platform/edge-microvisor-toolkit/pulls)
- [Read the Contribution Guide](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/docs/developer-guide/emt-contribution.md)
- [View the Azure Linux documentation](toolkit/docs/), a copy of which is included in the Edge Microvisor Toolkit repository for ease of access.
- [Report a security vulnerability](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/SECURITY.md)
- [Read and respond to blog posts](https://medium.com/open-edge-platform/subpage/5f0ac5579c60)
- [Download the latest weekly release](https://github.com/open-edge-platform/edge-microvisor-toolkit/discussions/categories/announcements?discussions_q=is%3Aopen+category%3AAnnouncements)
- [Participate in discussions](https://github.com/open-edge-platform/edge-microvisor-toolkit/discussions)

## License Information

Based on [Azure Linux](https://github.com/microsoft/azurelinux), Edge Microvisor Toolkit shares its permissive open-source license: [MIT](https://github.com/microsoft/azurelinux/blob/3.0/LICENSE). For more information, see the [LICENSE](./LICENSE) document.

### Attribution

We acknowledge Microsoft's contributions to the open-source community and thank
them for providing a secure and efficient Linux distribution.
