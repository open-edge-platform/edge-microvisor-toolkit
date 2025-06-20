#!/bin/bash

echo "ALL ALL=(ALL) NOPASSWD: /usr/bin/X,/usr/local/bin/idv/init/setup_sriov_vfs.sh,/usr/local/bin/idv/init/setup_display.sh,/usr/local/bin/idv/launcher/start_vm.sh,/usr/local/bin/idv/launcher/start_all_vms.sh,/usr/local/bin/idv/launcher/stop_vm.sh,/usr/local/bin/idv/launcher/stop_all_vms.sh" | sudo tee -a /etc/sudoers.d/guest > /dev/null

