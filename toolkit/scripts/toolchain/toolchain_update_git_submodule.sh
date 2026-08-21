#!/bin/bash
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# This script clean up any change to the Azure Linux git submodule directory.

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"

skip_list=(
    "apparmor"
    "azurelinux-release"
    "azurelinux-repos"
    "azurelinux-rpm-macros"
    "azure-vm-utils"
    "bootengine"
    "cloud-provider-kubevirt"
    "coreos-cloudinit"
    "coreos-init"
    "ceph"
    "coredns"
    "dcos-cli"
    "fwctl"
    "fwctl-hwe"
    "ignition-flatcar"
    "iser"
    "iser-hwe"
    "isert"
    "isert-hwe"
    "kernel-hwe"
    "kernel-hwe-headers"
    "kernel-mshv"
    "knem"
    "knem-hwe"
    "mft_kernel"
    "mft_kernel-hwe"
    "mlnx-ethtool"
    "mlnx-iproute2"
    "mlnx-nfsrdma"
    "mlnx-nfsrdma-hwe"
    "mlnx-ofa_kernel"
    "mlnx-ofa_kernel-hwe"
    "mlnx-tools"
    "mlx-bootctl"
    "mlx-steering-dump"
    "nodejs24"
    "patterns-ceph-containers"
    "perl-DBIx-Simple"
    "rust-afterburn"
    "srp"
    "srp-hwe"
    "trident"
    "ucx"
    "update-ssh-keys"
    "vitess"
    "xpmem"
    "xpmem-hwe"
    "xpmem-lib"
)

extended_list=(
    "bolt"
    "libogg"
    "libtheora"
    "libutempter"
    "libvorbis"
    "lksctp-tools"
    "pyserial"
    "python-dmidecode"
    "xterm"
)


if [ -d "${REPO_ROOT}/azurelinux" ]; then
    cd ${REPO_ROOT}/azurelinux
    git clean -xfd &> /dev/null
    git reset --hard &> /dev/null
    git submodule update --init &> /dev/null
    cd ${REPO_ROOT}
    for folder in azurelinux/SPECS/*; do
        fbasename=$(basename "$folder")
        skip=false
        for skip_item in "${skip_list[@]}"; do
            if [ "$fbasename" == "$skip_item" ]; then
                skip=true
                break
            fi
        done
        if $skip; then
            # echo "Skipping $fbasename"
            continue
        fi
        [ -d "$folder" ] && [ ! -d "SPECS/$fbasename" ] && cp -r "$folder" SPECS/
    done
    # Copy specific folders from azurelinux/SPECS-EXTENDED/
    for extended_spec in "${extended_list[@]}"; do
        extended_folder="$REPO_ROOT/azurelinux/SPECS-EXTENDED/$extended_spec"
        if [ -d "$extended_folder" ]; then
            cp -r "$extended_folder" SPECS/
        else
            echo "Error: Extended package $extended_spec not found in azurelinux/SPECS-EXTENDED/"
            exit 1
	fi
    done
fi
