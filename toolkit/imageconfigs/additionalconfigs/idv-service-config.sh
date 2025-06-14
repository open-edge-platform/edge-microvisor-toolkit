echo "guest ALL=(ALL) NOPASSWD: /usr/bin/X,/opt/idv/init/setup_sriov_vfs.sh,/opt/idv/init/setup_display.sh,/opt/idv/init/setup_file_permissions.sh,/opt/idv/launcher/start_vm.sh,/opt/idv/launcher/start_all_vms.sh,/opt/idv/launcher/stop_vm.sh,/opt/idv/launcher/stop_all_vms.sh" | sudo tee -a /etc/sudoers.d/guest > /dev/null

sed -i '/# End/i \
systemctl --user enable idv-init.service \n\
systemctl --user start idv-init.service \n\
systemctl --user enable idv-launcher.service \n\
systemctl --user start idv-launcher.service' /etc/profile

