#!/bin/bash
# Copyright (c) Intel Corporation.
# Licensed under the MIT License.

check() {
    require_binaries tar || return 1
    return 0
}

depends() {
    return 0
}

install() {
    inst_hook mount 90 "$moddir/tmpfsroot-mount.sh"
}
