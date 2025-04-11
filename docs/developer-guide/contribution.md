# Contribute to Edge Microvisor Toolkit

Edge Microvisor Toolkit is open source and always welcomes an active
community to support adding new features, optimizing, and improving security.

There are many areas in which you can contribute, such as:

1. The build infrastructure pipeline.
2. New features and functionality in new or existing microvisor image definitions.
3. Support for new edge platforms.

## New Features

New feature requests should always be made by opening an Architecture Decision Record (ADR) GitHub issue, regardless of whether you want to contribute directly or just file a request. To do so, use this template and provide as much information as possible, as it
helps maintainers and stakeholders to review, better understand, and prioritize the request.

**TODO**: Add link to Andrea's suggested ADR template

## Contribution Flow

The following diagram outlines the general workflow when pull requests are made
to the Edge Microvisor Toolkit repository.

![Contribution Flow](assets/contribution-flow.drawio.svg)

General contribution guidelines to Open Edge platform can be found [TODO]
(/provide/link/to/umbrella contribution guidelines).

### Update of Edge Node Agents

1. If a new package has to be released, follow below steps to ensure the package is available in the artifactory.

    a. Checkout the tag for your agent which has to be released.
    b. cd into your agent's directory.
    c. Invoke `make tarball`.
    d. Upload tarball from `build/artifacts` to the tarball repository.

2. Update the respective .SPEC file in SPECS/<agent-name> directory. Example : `SPECS/node-agent`.

3. Bump the release number declared in the top section of the .SPEC file if on the same version. Else, update the release version and set the number to 1.

4. Update `env_wrapper.sh` and the .SPEC file if there are new configurations to be added or installation changes.

5. Update the changelog to ensure the version and release number are mentioned correctly as well.
Example :

    ```bash
    * Tue Mar 25 2025 Andrea Campanella <andrea.campanella@intel.com> - 1.5.11-2
    - Move from RSTYPE to RS_TYPE in wrapper for node-agent
    ```

6. Generate sha256sum of all files that have been updated.
Example : `sha256sum ./SPECS/node-agent/env_wrapper.sh`

7. Update the signature file name `<agent-name>.signatures.json`. Example : `node-agent.signatures.json`.

8. Update `cgmanifest.json`. You can use a script to do it, if you have an rpm environment. Else, update the version and download the URL manually. Example commands to update using a manifest:

    ```bash
    python3 -m pip install -r ./toolkit/scripts/requirements.txt
    python3 ./toolkit/scripts/update_cgmanifest.py first cgmanifest.json ./SPECS/node-agent/node-agent.spec
    ```
> **Note:** This guide applies to `rpm` package addition in general for Edge Microvisor.

## Release Cadence

Edge Microvisor Toolkit has a steady and predictable release cadence. Issues
and feature requests, raised as issues, are evaluated and prioritized to meet one of the
planned releases.

Edge Microvisor Toolkit releases every 6 weeks. Here are the details:

**every 6 weeks:**
- RPM updates including new RPMs or patches to existing RPMs.
- Exception releases to address critical bugs/CVEs.

**every 12 weeks:**
- ISO image + RPM release.

**every quarter:**
- RAW/VHD (+RPMs delta) image release.

## Contribution license

Since Edge Microvisor Toolkit is open source, by contributing to the project, you agree that
your contributions will be licensed under the terms stated in the
[LICENSE](../../LICENSE) file.
