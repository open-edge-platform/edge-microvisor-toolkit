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
    "cloud-provider-kubevirt"
    "dcos-cli"
    "fwctl"
    "fwctl-hwe"
    "iser"
    "iser-hwe"
    "isert"
    "isert-hwe"
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
    "srp"
    "srp-hwe"
    "vitess"
    "xpmem"
    "xpmem-hwe"
    "xpmem-lib"
)

if [ -d "${REPO_ROOT}/azurelinux" ]; then
    cd ${REPO_ROOT}/azurelinux
    git clean -xfd &> /dev/null
    git reset --hard &> /dev/null
    git submodule update --init &> /dev/null
    cd ${REPO_ROOT}
    skip_list=("cloud-provider-kubevirt" "perl-DBIx-Simple" "dcos-cli" "vitess" "fwctl" "mlx-bootctl" "kernel-mshv" "srp" "mft_kernel" "knem" "xpmem" "xpmem-lib" "iser" "isert" "mlnx-ethtool" "mlnx-iproute2" "mlnx-nfsrdma" "mlnx-ofa_kernel" "mlnx-tools" "azurelinux-release" "azurelinux-repos" "azurelinux-rpm-macros")
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
fi
