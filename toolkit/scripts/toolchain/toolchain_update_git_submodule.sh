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
    [ ! -d ./SPECS-SIGNED ] && cp -r azurelinux/SPECS-SIGNED ./ 
    [ ! -d ./SPECS-EXTENDED ] && cp -r azurelinux/SPECS-EXTENDED ./
    skip_list=("mlnx-ethtool" "mlnx-iproute2" "mlnx-tools" "azurelinux-image-tools" "azurelinux-release" "azurelinux-repos" "azurelinux-rpm-macros")
    for folder in azurelinux/SPECS/*; do
        fbasename=$(basename "$folder")
        if [[ " ${skip_list[@]} " == *" ${fbasename} "* ]]; then
            # echo "Skipping $fbasename"
            continue
        fi
        [ -d "$folder" ] && [ ! -d "SPECS/$fbasename" ] && cp -r "$folder" SPECS/
        #&& echo "Copied $folder to SPECS/$fbasename"
    done
#else
# echo "Directory ${TIBEROS_DIR}/azurelinux does not exist. Skipping submodule update."
fi
# echo "Submodules updated successfully"
