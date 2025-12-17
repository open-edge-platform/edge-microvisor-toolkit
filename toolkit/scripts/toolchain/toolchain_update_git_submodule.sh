#!/bin/bash
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# This script clean up any change to the Azure Linux git submodule directory.

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"

if [ -d "${REPO_ROOT}/azurelinux" ]; then
    cd ${REPO_ROOT}/azurelinux
    git clean -xfd &> /dev/null
    git reset --hard &> /dev/null
    git submodule update --init &> /dev/null
    cd ${REPO_ROOT}
    skip_list=("fwctl" "mlx-bootctl" "kernel-mshv" "srp" "mft_kernel" "knem" "xpmem" "iser" "isert" "mlnx-ethtool" "mlnx-iproute2" "mlnx-nfsrdma" "mlnx-ofa_kernel" "mlnx-tools" "azurelinux-release" "azurelinux-repos" "azurelinux-rpm-macros")
    for folder in azurelinux/SPECS/*; do
        fbasename=$(basename "$folder")
        if [[ " ${skip_list[@]} " == *" ${fbasename} "* ]]; then
            # echo "Skipping $fbasename"
            continue
        fi
        [ -d "$folder" ] && [ ! -d "SPECS/$fbasename" ] && cp -r "$folder" SPECS/
    done
fi
