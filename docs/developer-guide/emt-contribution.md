# Contribute to Edge Microvisor Toolkit

Edge Microvisor Toolkit is open source and always welcomes an active
community to support adding new features, optimizing, and improving security.

There are many areas in which you can contribute, such as:

1. The build infrastructure pipeline.
2. New features and functionality in new or existing microvisor image definitions.
3. Support for new edge platforms.

## New Features

New feature requests should always be made by opening an Architecture Decision Record (ADR)
GitHub issue, regardless of whether you want to contribute directly or just file a request.
To do so, use the [Design Proposal](/design-proposals/design-propsal-template.md) template
and provide as much information as possible. This helps maintainers and stakeholders to
review, better understand, and prioritize the request.

## Contribution Flow

The following diagram outlines the general workflow for pull requests made
to the Edge Microvisor Toolkit repository:

![Contribution Flow](assets/emt-contribution-flow.drawio.svg)

## Release Cadence

Edge Microvisor Toolkit has a steady and predictable release cadence. Both issues and
feature requests, which are also raised as issues, are evaluated and prioritized to meet one
of the planned releases.

Edge Microvisor Toolkit releases every 6 weeks. Here are the details:

**Every 6 weeks:**

- RPM updates including new RPMs or patches to existing RPMs.
- Exception releases to address critical bugs/CVEs.

**Every 12 weeks:**

- ISO image + RPM release.

**Every quarter:**

- RAW/VHD (+RPMs delta) image release.

## Contribution license

Since Edge Microvisor Toolkit is open source, by contributing to the project, you agree that
your contributions will be licensed under the terms stated in the
[LICENSE](../../LICENSE) file.
