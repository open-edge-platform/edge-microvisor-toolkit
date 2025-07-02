# Release Policy

Edge Microvisor Toolkit receives a major release in the cadence of three to four months.
Major releases, versioned as 3.x to remain aligned with Azure Linux, offer both functional
and technical improvements.

<!-- how do we treat minor updates? Minor releases, versioned as ???????, offer ????? -->

The updates may come in different publishing cadence and scope:

<!-- is this cadence correct? How do we explain these differences? -->

**up to 2 weeks (hotfix):**
- Critical Vulnerability updates.

**Every 6 weeks (minor relase):**

- RPM updates including new RPMs or patches to existing RPMs.
- Exception releases to address critical bugs/CVEs.

**Every 12 weeks:**

- ISO image + RPM release.

**Every quarter:**

- RAW/VHD (+RPMs delta) image release.


No long-term support version is currently maintained, nor planned. This means that
the most recent major version is considered the recommended stable release.

If you find a bug or would like to propose or contribute a new feature, for a future release,
check out the [contribution guide](./CONTRIBUTION.md).



