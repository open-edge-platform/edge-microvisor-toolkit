#!/bin/bash
# Copyright (c) Intel Corporation.
# Licensed under the MIT License.

info "mount tmpfs for root"
mount -t tmpfs -o size=1G tmpfs $NEWROOT

cd $NEWROOT

if [[ -f /rootfs.tar.gz ]]; then
  info "extract rootfs.tar.gz to $NEWROOT"
  tar -xvf /rootfs.tar.gz -C $NEWROOT
else
  warn "no rootfs.tar.gz found"
  die
fi

info "rootfs on tmpfs complete"
