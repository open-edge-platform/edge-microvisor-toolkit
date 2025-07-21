#!/bin/bash
# Copyright (c) Intel Corporation.
# Licensed under the MIT License.

set -e

EFIDIR="BOOT"
KERNEL_VERSION=""

# Image generation is done in a chroot environment, so running `uname -r`
# will return the version of the host running kernel. This function works
# under the assumption that exactly one kernel is installed in the end image.
get_kernel_version() {
    kernel_modules_dir="/usr/lib/modules"
    KERNEL_VERSION="$(ls $kernel_modules_dir)"
}

# Install systemd-bootloader in ESP
mkdir -p /boot/efi/EFI/$EFIDIR
cp /lib/systemd/boot/efi/systemd-bootx64.efi /boot/efi/EFI/$EFIDIR/BOOTX64.EFI

# copy UKI into the ESP
mkdir -p /boot/efi/EFI/Linux
get_kernel_version
echo "Kernel version = $KERNEL_VERSION"
cp /boot/linux.efi /boot/efi/EFI/Linux/linux-$KERNEL_VERSION.efi

# Remove unsed binaries
rm -rf /boot/linux.efi
rm -rf /boot/initramfs-*.img
rm -rf /boot/vmlinuz*

# preload the hwdb.bin
systemd-hwdb update
[ -f /etc/udev/hwdb.bin ] && mv /etc/udev/hwdb.bin /usr/lib/udev/hwdb.bin
