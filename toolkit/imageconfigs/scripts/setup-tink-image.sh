#!/bin/bash

# Copyright (c) Intel Corporation.
# Licensed under the MIT License.

set -e
set -x

pprefix="Tink"

# services
systemctl disable systemd-homed.service
systemctl enable caddy.service
systemctl enable fluent-bit.service
mkdir -p /etc/fluent-bit
if [ ! -f /etc/fluent-bit/fluent-bit.conf ]; then
  touch /etc/fluent-bit/fluent-bit.conf
fi
echo "$pprefix: fstab contents $(cat /etc/fstab)"
echo 'tmpfs   /   tmpfs   defaults,size=1G   0   0' > /etc/fstab
echo "$pprefix: $(du -h /usr/share)"
find /usr/share -type f \
  ! -path "/usr/share/terminfo/v/vt100" \
  ! -path "/usr/share/terminfo/v/vt220" \
  ! -path "/usr/share/keymaps/include/*" \
  ! -path "/usr/share/keymaps/i386/include/*" \
  ! -path "/usr/share/keymaps/i386/qwerty/us.map.gz" \
  ! -path "/usr/share/consolefonts/lat9w-16*" \
  ! -path "/usr/share/dbus-1/system.conf" \
  ! -path "/usr/share/caddy/*" \
  ! -path "/usr/share/pki/*" \
  -exec rm -f {} +
echo "$pprefix: reduced $(du -h /usr/share)"

ramfs=$(find /boot -type f -name initramfs*img -printf '%f\n')
# unzip initramfs
mkdir /tmp/initramfs
cd /tmp/initramfs
echo "$pprefix: inside $(pwd)"
echo "$pprefix: unziping initial initramfs for repack"
gunzip -c -k /boot/$ramfs | cpio -idmv --no-absolute-filenames
echo "$pprefix: free space $(df -h)"

cd /tmp/initramfs
echo "$pprefix: inside $(pwd)"
echo "$pprefix: after copy $(du -h /tmp/initramfs)"
echo "$pprefix: check cmdline.d $(ls etc/cmdline.d)"
echo "$pprefix: check cmdline.d contents $(cat etc/cmdline.d/95root-dev.conf)"
echo 'root=tmpfs rootflags=size=1G,mode=0755' > etc/cmdline.d/95root-dev.conf
echo "$pprefix: check cmdline.d contents after edit $(cat etc/cmdline.d/95root-dev.conf)"
echo "$pprefix: before rm devexist* $(ls -al var/lib/dracut/hooks/initqueue/finished/)"
rm -f var/lib/dracut/hooks/initqueue/finished/devexists*
echo "$pprefix: after rm devexist* $(ls -al var/lib/dracut/hooks/initqueue/finished/)"
echo "$pprefix: before rm wants $(ls -al etc/systemd/system/initrd.target.wants/)"
rm -rf etc/systemd/system/initrd.target.wants/dev-disk-b*
echo "$pprefix: after rm wants $(ls etc/systemd/system/initrd.target.wants/)"
echo "$pprefix: before rm disk service $(ls -al etc/systemd/system/dev-disk-b*)"
rm -rf etc/systemd/system/dev-disk-b*
echo "$pprefix: after rm disk service $(ls -al etc/systemd/system/)"
echo "$(find . -iname dev-disk*)"
# copy tar required for uncompressing rootfs archive
echo "$pprefix: before copy tar $(find . -iname tar)"
cp /usr/bin/tar usr/bin
echo "$pprefix: after copy tar $(find . -iname tar)"
#mv /rootfs.tar.gz /tmp/initramfs/
find . | cpio -o -H newc | gzip > /boot/$ramfs
cd -

echo "$pprefix: $(ls -l /boot/$ramfs)"
rm -rf /tmp/initramfs
