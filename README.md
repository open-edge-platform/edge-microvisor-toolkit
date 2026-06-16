# Edge Microvisor Toolkit

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

Edge Microvisor Toolkit is a reference Linux operating system that demonstrates the full
capabilities of Intel® platforms for Edge AI workloads. Built on Azure Linux, it features an
[Intel®-maintained Linux Kernel](./docs/developer-guide/emt-architecture-overview.md#next-kernel),
incorporating all the latest patches that have not yet been
upstreamed. These patches optimize performance and enhance other capabilities for Intel®
silicon, streamlining integration for operating system vendors and technology partners.

Edge Microvisor Toolkit is [published in several versions](./docs/developer-guide/get-started/emt-versions.md),
both immutable and mutable.
It may be used to quickly deploy, validate, and benchmark edge AI workloads, including those
requiring real-time processing. You can also use the toolkit's flexible build infrastructure
to create custom images from a large set of pre-provisioned packages.

Edge Microvisor Toolkit has undergone extensive validation across the Intel® Xeon®,
Intel® Core Ultra™, Intel Core™, and Intel® Atom® processor families. It provides robust
support for integrated NPU as well as a
[selection of discrete GPU cards](./docs/developer-guide/emt-system-requirements.md#hardware-requirements).

You can either build Edge Microvisor Toolkit by following step-by-step instructions or
download it directly. Both the build system and Edge Microvisor Toolkit are available as open
source.

> Intel strongly recommends you to use the latest version of 3.0 branch [here](https://github.com/open-edge-platform/edge-microvisor-toolkit/releases).\
> Intel will not provide any support for previous versions including but not limited to, maintenance or bug fixes. Previous versions have been identified as having known security issues.

## Get Started

To find out how to deploy and work with Edge Microvisor Toolkit, see the
[Get Started guide](https://docs.openedgeplatform.intel.com/2025.2/edge-microvisor-toolkit/emt-get-started.html).

For a quick start, get the current
[ISO](https://files-rs.edgeorchestration.intel.com/files-edge-orch/microvisor/iso/EdgeMicrovisorToolkit-25.06.2.iso)
\ [SHA256](https://files-rs.edgeorchestration.intel.com/files-edge-orch/microvisor/iso/EdgeMicrovisorToolkit-25.06.2.iso.sha256sum).

If you're interested in most up-to-date versions, check out the
[weekly Immutable Raw Images](https://github.com/open-edge-platform/edge-microvisor-toolkit/discussions/categories/announcements?discussions_q=is%3Aopen+category%3AAnnouncements+weekly+build)
and
[CVE](https://github.com/open-edge-platform/edge-microvisor-toolkit/discussions?discussions_q=is%3Aopen+cve+) releases.

**Demos on YouTube**

* [Standalone Edge Microvisor Toolkit (EMT-S) integration with Edge Microvisor Bootkit](https://www.youtube.com/watch?v=rmgmWYi6OpE):
  USB Device Preparation, Provisioning Process, System Readiness, and Final Boot with the cluster starting successfully.
* [Edge Microvisor Toolkit Standalone Node 3.0](https://www.youtube.com/watch?v=j_4EX_wggSI):
  a brief walkthrough of Edge Microvisor Toolkit Standalone Node for the 3.0 release, covering various use cases.

You can also try out the
[Image Composer Tool](http://github.com/open-edge-platform/image-composer-tool) -
a *new* project in the Open Edge platform family that allows you to compose
custom OS images from popular distributions using pre-built artifacts.

## Get Help or Contribute

If you want to participate in the GitHub community for Edge Microvisor Toolkit, you can
contribute code, propose a design, download and try out a release, open an issue,
benchmark application performance, and participate in
[Discussions](https://github.com/open-edge-platform/edge-microvisor-toolkit/discussions).
To learn more, check out the following resources:

- [Open an issue](https://github.com/open-edge-platform/edge-microvisor-toolkit/issues)
- [Submit a pull request](https://github.com/open-edge-platform/edge-microvisor-toolkit/pulls)
- [Read the Contribution Guide](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/docs/developer-guide/emt-contribution.md)
- [View the Azure Linux documentation](toolkit/docs/), a copy of which is included in the Edge Microvisor Toolkit repository for ease of access.
- [Report a security vulnerability](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/SECURITY.md)
- [Read and respond to blog posts](https://medium.com/open-edge-platform/subpage/5f0ac5579c60)
- [Download the latest weekly release](https://github.com/open-edge-platform/edge-microvisor-toolkit/discussions/categories/announcements?discussions_q=is%3Aopen+category%3AAnnouncements)
- [Participate in discussions](https://github.com/open-edge-platform/edge-microvisor-toolkit/discussions)

Before submitting a new report, check the existing issues to see if a similar one has not
been filed already.


## License Information

Based on [Azure Linux](https://github.com/microsoft/azurelinux),
Edge Microvisor Toolkit shares its permissive open-source license:
[MIT](https://github.com/microsoft/azurelinux/blob/3.0/LICENSE).

### Attribution

We acknowledge Microsoft's contributions to the open-source community and thank
them for providing a secure and efficient Linux distribution.
