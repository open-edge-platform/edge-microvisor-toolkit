#!/bin/bash

echo "ALL ALL=(ALL) NOPASSWD: /usr/bin/X,/opt/idv/init/setup_sriov_vfs.sh,/opt/idv/init/setup_display.sh,/opt/idv/init/setup_file_permissions.sh,/opt/idv/launcher/start_vm.sh,/opt/idv/launcher/start_all_vms.sh,/opt/idv/launcher/stop_vm.sh,/opt/idv/launcher/stop_all_vms.sh" | sudo tee -a /etc/sudoers.d/idv_services_scripts > /dev/null

sed -i '/# End/i \
systemctl --user enable idv-init.service \n\
systemctl --user start idv-init.service \n\
systemctl --user enable idv-launcher.service \n\
systemctl --user start idv-launcher.service' /etc/profile

# Setup display

extensions_file="/usr/share/X11/xorg.conf.d/10-extensions.conf"
serverflags_file="/usr/share/X11/xorg.conf.d/10-serverflags.conf"

# Disable DPMS
if [ ! -f "$extensions_file" ]; then
    sudo touch "$extensions_file"

    sudo bash -c 'cat << EOF > '${extensions_file}'
Section "Extensions"
    Option "DPMS" "false"
EndSection
EOF'
else
  if ! grep -q "DPMS" "${extensions_file}"; then
    sudo sed -i '$a\
    Section "Extensions"\
        Option "DPMS" "false"\
    EndSection' "$extensions_file"
  fi
fi

# Disable screen blanking and timeouts
if [ ! -f "$serverflags_file" ]; then
    sudo touch "$serverflags_file"

    sudo bash -c 'cat << EOF > '${serverflags_file}'
Section "ServerFlags"
    Option "StandbyTime" "0"
    Option "SuspendTime" "0"
    Option "OffTime"     "0"
    Option "BlankTime"   "0"
EndSection
EOF'
else
  if ! grep -q "StandbyTime" "${serverflags_file}"; then
    sudo sed -i '$a\
    Section "ServerFlags"\
      Option "StandbyTime" "0"\
      Option "SuspendTime" "0"\
      Option "OffTime"     "0"\
      Option "BlankTime"   "0"\
    EndSection' "$serverflags_file"
  fi
fi


