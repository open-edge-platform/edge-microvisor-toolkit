#!/bin/bash

# Copyright (c) Intel Corporation.
# Licensed under the MIT License.

# Failure can be ignored.
set -e
set -x

# regen initramfs for tink
echo "Tink: final regen initramfs"

ramfs=$(find /boot -type f -name initramfs*img -printf '%f\n')
# unzip initramfs
mkdir /tmp/initramfs
cd /tmp/initramfs
echo "Tink: inside $(pwd)"
echo "Tink: unziping initial initramfs for repack"
gunzip -c -k /boot/$ramfs | cpio -idmv --no-absolute-filenames
echo "Tink: free space $(df -h)"

mkdir /tmp/rootfs
cd /tmp/rootfs
echo "Tink: inside $(pwd)"
echo "Tink: free space $(df -h)"
mkdir -p boot dev etc home mnt media proc sys run tmp usr usr/bin usr/sbin usr/lib usr/libexec var
chown root:root boot dev etc home mnt media proc sys run tmp usr usr/bin usr/sbin usr/lib usr/libexec var
chmod 0700 boot
chmod 0755 dev etc home mnt media proc sys run tmp usr usr/bin usr/sbin usr/lib usr/libexec var
echo "Tink: copy initial initramfs for rootfs"
cp -a /tmp/initramfs/dev/* dev/
ln -s usr/bin bin
ln -s usr/sbin sbin
ln -s usr/lib lib
ln -s usr/lib lib64
chown root:root bin sbin lib lib64
chmod 0777 bin sbin lib lib64
echo "Tink: after initramfs copy $(ls -l .)"
echo "Tink: after initramfs copy $(du -h /tmp/rootfs)"
echo "Tink: copying rootfs files"
cp -R -p /usr/sbin/* usr/sbin/
cp -R -p /usr/bin/* usr/bin/
cp -R -p /usr/lib/* usr/lib/
cp -R -p /usr/libexec/* usr/libexec/
cp -R -p /var/lib var/
cp -R -p /etc/* etc/
# override boot device command line
echo "Tink: fstab contents $(cat etc/fstab)"
echo 'Tink: tmpfs   /   tmpfs   defaults,size=1G   0   0' > etc/fstab
#echo "" > etc/fstab
echo "Tink: fstab contents after edit $(cat etc/fstab)"
# simple setup for console
#echo 'LANG=en_US.UTF-8' > etc/locale.conf
#echo 'KEYMAP=us' > etc/vconsole.conf
#echo 'FONT=lat9w-16' >> etc/vconsole.conf
echo "Tink: console setup $(cat etc/locale.conf etc/vconsole.conf)"
mkdir -p usr/share/terminfo/v
cp -R -p /usr/share/terminfo/v/vt100 usr/share/terminfo/v/
cp -R -p /usr/share/terminfo/v/vt220 usr/share/terminfo/v/
mkdir -p usr/share/keymaps
cp -R -p /usr/share/keymaps/include usr/share/keymaps/
mkdir -p usr/share/keymaps/i386/include
cp -R -p /usr/share/keymaps/i386/include/* usr/share/keymaps/i386/include/
mkdir -p usr/share/keymaps/i386/qwerty
cp -R -p /usr/share/keymaps/i386/qwerty/us.map.gz usr/share/keymaps/i386/qwerty/
mkdir -p usr/share/consolefonts
cp -R -p /usr/share/consolefonts/lat9w-16* usr/share/consolefonts/
mkdir -p usr/share/dbus-1
cp -R -p /usr/share/dbus-1/system.conf usr/share/dbus-1/
echo "Tink: after copy $(du -h /tmp/rootfs)"
echo "Tink: free space $(df -h)"
tar cf - -C . . | gzip -9 > /rootfs.tar.gz
cd -
echo "Tink: rootfs size: $(ls -l /rootfs.tar.gz)"
rm -rf /tmp/rootfs

cd /tmp/initramfs
echo "Tink: inside $(pwd)"
echo "Tink: after copy $(du -h /tmp/initramfs)"
echo "Tink: check cmdline.d $(ls etc/cmdline.d)"
echo "Tink: check cmdline.d contents $(cat etc/cmdline.d/95root-dev.conf)"
#echo 'root=tmpfs rootfstype=tmpfs'  > etc/cmdline.d/95root-dev.conf
#echo 'root= rootfstype=auto'  > etc/cmdline.d/95root-dev.conf
echo 'root=tmpfs rootflags=size=1G,mode=0755' > etc/cmdline.d/95root-dev.conf
echo "Tink: check cmdline.d contents after edit $(cat etc/cmdline.d/95root-dev.conf)"
echo "Tink: before rm devexist* $(ls -al var/lib/dracut/hooks/initqueue/finished/)"
rm -f var/lib/dracut/hooks/initqueue/finished/devexists*
echo "Tink: after rm devexist* $(ls -al var/lib/dracut/hooks/initqueue/finished/)"
echo "Tink: before rm wants $(ls -al etc/systemd/system/initrd.target.wants/)"
rm -rf etc/systemd/system/initrd.target.wants/dev-disk-b*
echo "Tink: after rm wants $(ls etc/systemd/system/initrd.target.wants/)"
echo "Tink: before rm disk service $(ls -al etc/systemd/system/dev-disk-b*)"
rm -rf etc/systemd/system/dev-disk-b*
echo "Tink: after rm disk service $(ls -al etc/systemd/system/)"
echo "$(find . -iname dev-disk*)"
# copy tar required for uncompressing rootfs archive
echo "Tink: before copy tar $(find . -iname tar)"
cp /usr/bin/tar usr/bin
echo "Tink: after copy tar $(find . -iname tar)"
mv /rootfs.tar.gz /tmp/initramfs/
find . | cpio -o -H newc | gzip > /boot/$ramfs
cd -

echo "Tink: $(ls -l /boot/$ramfs)"
rm -rf /tmp/initramfs
