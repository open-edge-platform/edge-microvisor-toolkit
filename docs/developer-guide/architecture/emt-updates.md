# Atomic Updates

The immutable microvisor uses a read-only file system and avoids traditional differential
package management (like `dnf` or `apt`) in favor of updating the entire system image. This
approach simplifies system management and increases reliability by preventing configuration
drifts.

## A/B Update Paradigm

At the heart of this design is an A/B update mechanism. Two dedicated partitions are reserved
on the system — one holds the active image, while the other remains inactive. This section
outlines the process.

## Active vs. Inactive Partitions

One partition is designated as active and is used during system boot via EFI and systemd-boot.
The other remains inactive until an update is applied.

## Update Process

When a new update is available, the following steps occur:

- The new image is downloaded and then verified for integrity and authenticity.
  Once verified, the new image is written to the inactive partition.

- The bootloader (systemd-boot) is then reconfigured to boot from the updated partition,
  which will become the new active partition upon the next reboot.

- Rollback Capability:

  Systemd-boot has the ability to detect boot failures. If the system fails to boot from the
  new image, the bootloader can automatically rollback to the previous, stable partition,
  ensuring continuous availability of the system.

## Benefits of The Approach

- **Stability and Predictability**

  By updating the entire image and maintaining immutable partitions, the system avoids
  configuration drift, often seen with writable filesystems.

- **Simplified Maintenance**

  The A/B paradigm eliminates the complexities associated with handling partial updates or
  rollbacks in traditional package management systems.

- **Enhanced Security**

  With a read-only filesystem and a verified update process, the risk of unauthorized
  modifications is greatly reduced.

This comprehensive update mechanism ensures that Edge Microvisor Toolkit remains stable,
secure, and easy to maintain, even in environments where reliability is paramount.

## Standalone Updates

The Edge Microvisor Toolkit can be updated as a standalone solution through a manual
update procedure. You can download the
new version of the microvisor and run the update by invoking the `os-update-script` and
providing the path to the downloaded image. Plans for future versions of Edge Microvisor
Toolkit may include implementing automatic image validation, update checks, and releases.
