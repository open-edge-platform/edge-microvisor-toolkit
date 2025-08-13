# Releases and their Support

The releases of Edge Microvisor Toolkit take three forms: major, minor, and weekly.

## Major Releases

A major release of Edge Microvisor Toolkit typically occurs once a year in June. New feature development takes place on the latest major release and its subsequent minor releases. A major release is supported for 18 to 24 months.

During the 18-24 month support window for a major release of Edge Microvisor Toolkit, active support follows open-source practices, including the fixing of bugs found by the community. You can [open an issue](https://github.com/open-edge-platform/edge-microvisor-toolkit/issues) or [submit a design proposal or a pull request](./docs/developer-guide/emt-contribution.md).

A major release introduces significant changes to the operating system and its capabilities. These changes might include base operating system updates and a Linux kernel upgrade, which could affect software compatibility. A major release also typically includes new features, bug fixes, and CVE patches.

Beyond the active support window of 18-24 months, support will be in the form of a community-driven best effort. After the end of the 18-24 month active support window for a major release, it is recommended that you transition your Edge Microvisor Toolkit deployments to the next major release for continued support.


![Release cadence and support.](./docs/developer-guide/assets/emt-releases-and-support.png)



## Minor Releases

A minor release, which delivers incremental updates on top of the current major version, typically occurs three times a year, in March, September, and December. These minor releases are part of the 18-24 month active support window of a major release.
During the active support window, no separate branches other than the branch for the standalone node and the branch for the developer node are supported for every major and minor release.

Minor releases aim to be seamless upgrades or updates that maintain the integrity of applications and data without requiring reimaging. Focused on continuous improvement, these non-disruptive minor releases might include package upgrades, new feature enablement, bug fixes, performance optimizations, and security vulnerability patches.
Minor releases might also include new packages, such as developer tools and user applications, available through the Edge Microvisor Toolkit RPM repository.

## Weekly Releases

Weekly releases typically include bug fixes, performance optimizations, and vulnerability patches for known CVEs. You can find the latest weekly build in [Discussions](https://github.com/open-edge-platform/edge-microvisor-toolkit/discussions/categories/announcements?discussions_q=is%3Aopen+category%3AAnnouncements).


![Release cadence and support.](./docs/developer-guide/assets/emt-weekly-releases.png)



## No Long-Term Support

No long-term support version is maintained, nor planned. The most recent major version is the recommended stable release.

## Version Numbers

Starting with the minor release planned for December 2025, Edge Microvisor Toolkit will adopt a `YEAR-BASED MAJOR.MONTH.PATCH` format.

As a result, the version number of the minor release planned for December 2025 will be `25.06.1`, with the number for `MONTH` denoting the month in which the minor release's major version was released --- in this case, `06` for June.

The minor release planned for March 2026 will be version number `25.06.2`, and the next major release, planned for June 2026, will advance to the following form: `26.06`.


## Get Support or Contribute on GitHub

To get support for Edge Microvisor Toolkit or contribute to its development, see the following resources:

* [Issues](https://github.com/open-edge-platform/edge-microvisor-toolkit/issues)
* [Discussions](https://github.com/open-edge-platform/edge-microvisor-toolkit/discussions)
* [Contribution Guide](./docs/developer-guide/emt-contribution.md)

