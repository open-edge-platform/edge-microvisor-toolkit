# Edge Microvisor Toolkit

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE) ![go-test-coverage](https://github.com/open-edge-platform/edge-microvisor-toolkit/actions/workflows/go-test-coverage.yml/badge.svg?branch=3.0) ![lint](https://github.com/open-edge-platform/edge-microvisor-toolkit/actions/workflows/lint.yml/badge.svg?branch=3.0)

The Edge Microvisor Toolkit is a streamlined container host that
showcases the Intel silicon optimizations. Built on Azure Linux, it features a
Linux Kernel maintained by Intel, incorporating all the latest kernel and user
patches.

It is published in several versions, both immutable and mutable. Use them to
quickly deploy and run your solutions for multiple scenarios, like benchmarking
and validation of edge AI computing workloads, or build your own system, using
the existing infrastructure.

The currently published versions are:

* Edge Microvisor Toolkit (immutable)
* Edge Microvisor Toolkit with real time extensions (immutable)
* Edge Microvisor Toolkit Standalone (immutable)
* Edge Microvisor Toolkit Developer (mutable)
  
The Edge Microvisor Toolkit has undergone extensive validation across all Intel
platforms such as  Xeon®, Intel® Core Ultra™, Intel Core™ and Intel® Atom®. It
provides robust support for integrated and Intel discrete GPU cards, as well as
integrated NPU.

You can either build the Edge Microvisor Toolkit by following step-by-step
instructions or download it directly. Both the Build system and the Edge Microvisor
Toolkit are available as Open-Source.

## Get Started

Check out these articles to quickly learn how to work with Edge Microvisor Toolkit:

* [System requirements](./docs/developer-guide/system-requirements.md)
  for the hardware and software requirements.
* [Install on bare metal edge node](./docs/developer-guide/get-started/installation-howto.md#baremetal-with-iso) or
  [Install on a Virtual Machine](./docs/developer-guide/get-started/installation-howto.md#virtual-machine-with-hyper-v)
  to learn how to install Edge Microvisor Toolkit.
* [Install the developer ISO image](./docs/developer-guide/get-started.md#standalone-developer-edge-node)
  for a mutable container host providing only minimum functionality.
* [Install the production RAW image]( ./docs/developer-guide/get-started.md#standalone-edge-node)
  for an immutable container host with essential functionality.
* [Build or customize the Edge Microvisor](./docs/developer-guide/get-started/building-howto.md)
  for maximum control over the system you want to deploy.
* [Edge Orchestrator integration](./docs/developer-guide/deployment-edge-orchestrator.md)
  for scalable, secure, reliable, and automated management of edge infrastructure.
* [Understand the security features of the Edge Microvisor](./docs/developer-guide/security.md)
  to ensure security for workloads and data.
* [Troubleshooting](./docs/developer-guide/troubleshooting.md) provides you answers to commonly asked questions.

## Getting Help

If you encounter bugs, have feature requests, or need assistance,
[file a GitHub Issue](https://github.com/open-edge-platform/edge-microvisor-toolkit/issues).

Before submitting a new report, check the existing issues to see if a similar one has not
been filed already. If no matching issue is found, feel free to file the issue as described
in the [contribution guide](./docs/developer-guide/contribution.md).

For security-related concerns, please refer to [SECURITY.md](./SECURITY.md).

[Azure Linux Documentation](toolkit/docs/), may also be useful, if you encounter
problems when using Edge Microvisor Toolkit. Its copy is part of the Edge
Microvisor Toolkit repository, for easier access.

## Contributing

As an open-source project, Edge Microvisor Toolkit always looks for community-driven
improvements. If you are interested in making the product even better, see how you can
help in the [contribution guide](./docs/developer-guide/contribution.md).

## License Information

Edge Microvisor Toolkit is based on [Azure Linux](https://github.com/microsoft/azurelinux),
sharing its permissive open-source license:
[MIT](https://github.com/microsoft/azurelinux/blob/3.0/LICENSE).

For more details, see the [LICENSE](./LICENSE) document.

### Attribution

We acknowledge Microsoft's contributions to the open-source community and thank
them for providing the secure and efficient Linux distribution.
