#!/bin/bash

echo "ALL ALL=(ALL) NOPASSWD: /usr/bin/X,/opt/idv/init/setup_sriov_vfs.sh,/opt/idv/init/setup_display.sh,/opt/idv/init/setup_file_permissions.sh,/opt/idv/launcher/start_vm.sh,/opt/idv/launcher/start_all_vms.sh,/opt/idv/launcher/stop_vm.sh,/opt/idv/launcher/stop_all_vms.sh" | sudo tee -a /etc/sudoers.d/idv_services_scripts > /dev/null

