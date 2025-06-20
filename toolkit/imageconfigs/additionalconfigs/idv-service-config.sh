#!/bin/bash

# This script adds specific sudo permissions for user to execute certain scripts that are run as part of idv-init.service and idv-launcher.service

set -e

FILE="/etc/sudoers.d/idv_scripts"
ENTRY=$(cat <<EOF
ALL ALL=(ALL) NOPASSWD: /usr/bin/X, \
/usr/local/bin/idv/init/setup_sriov_vfs.sh, \
/usr/local/bin/idv/init/setup_display.sh, \
/usr/local/bin/idv/launcher/start_vm.sh, \
/usr/local/bin/idv/launcher/start_all_vms.sh, \
/usr/local/bin/idv/launcher/stop_vm.sh, \
/usr/local/bin/idv/launcher/stop_all_vms.sh
EOF
)

# If file does not exist, create one
if [ ! -f "$FILE" ]; then
    sudo touch "$FILE"
fi

# Check if the entry already exists, if not, add it
if ! sudo grep -Fxq "$ENTRY" "$FILE"; then
    echo "$ENTRY" | sudo tee -a "$FILE" > /dev/null
fi
