# Flash Edge Microvisor Toolkit RAW Image to Storage Medium

## Installation

1. **Download the image**

You can download the image from artefactory under [this link](https://af01p-png.devtools.intel.com/artifactory/)

2. **Copy and paste the .raw.xz image onto the SUT image**

Run one of the following:

```
unxz core-2.0.20240726.0106.raw.xz
```
OR
```
tar -xvf core-2.0.20240726.0106.raw.xz
```
OR
```
gzip -d core-2.0.20240726.0106.raw.gz
chmod -Rf 777 core-2.0.20240726.0106.raw
```

3. **Flash the RAW image to a different, available storage device using the 'dd' command**

Run:
```
sudo dd if=core-2.0.20240726.0106.raw of=/dev/sdc status=progress
```

> **Note:** Successful flashing of the image should produce partitions such as /dev/sdb and /dev/sdc

![Result of flashing with `dd`](../assets/emt_flashing_raw_flashedpartitions_image-2024-8-1_13-2-43-1.png)

4. **Configure the server to reboot with required disk/OS/partition**

Using the CLI method, run `sudo efibootmgr` and then `sudo efibootmgr -o 0012` and `sudo reboot`:

```
$ sudo efibootmgr
[sudo] password for abjyoti:
BootCurrent: 0002
BootOrder: 0002,0012,0014,0015
Boot0002* ubuntu
Boot0012  EFI Fixed Disk Boot Device 2
Boot0014  Cruzer Blade
Boot0015  NIC in Slot 2 Port 2 Partition 1
MirroredPercentageAbove4G: 0.00
MirrorMemoryBelow4GB: false



$sudo efibootmgr -o 0012

$sudo reboot
```

You can also use the UI method, by rebooting the machine and going to boot manager to select partition flashed with image:

![Partition selection UI](../assets/emt_flashing_raw_partitionrebootui_image-2024-8-1_13-3-1-1.png)

## Post-installation steps

1. **Check date**

Run:

`sudo date080509312024`

The string of numbers after `date` is the date in time in the following format: Month:08 Date:05 Hour:09 Minute:31 Year: 2024

2. **Install openssh-server package**

Run:

`tdnf install openssh-server`

3. **Install vim package**

Run:

`tdnf install vim`

4. **Configure and enable ssh**

Run:

```
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```
5. **Restart sshd service to apply changes**

Run:

`sudo systemctl restart sshd`


> **Note**: If you want to use the bootable storage medium for other purposes, you can [allocate the remaining storage space to one of the partitions](./emt-flashing-raw-partition-resize.md)

## Troubleshooting (Best Known Methods)

- **BIOS Security Settings**

Disable the Secure Boot option in BIOS Settings if it was enabled.

- **Network is not working in XR12 (with x710 NIC)**

1. Install the drivers manually:

```
$ modprobe i40e
```

2. Install vim tool to edit the ssh config file:

```
$ tdnf install vim
```

3. Install and Configure the SSH server

```
$ tdnf install openssh-server
```

4. Update the ssh configuration to ssh with the following information:

```
$ vi /etc/ssh/sshd_config


PermitRootLogin yes

PasswordAuthentication yes
```

5. Restart sshd service

```
$ systemctl restart sshd
```

To debug, run only

```
journalctl -u sshd -f
```

- **Switching between multiple OS disks**

1. Install and configure efibootmgr
```
$ tdnf install efibootmgr

]# efibootmgr
BootCurrent: 0000
BootOrder: 0000,0005,0006,0002
Boot0000* EFI Fixed Disk Boot Device 2
Boot0002* ubuntu
Boot0005* Cruzer Blade
Boot0006* NIC in Slot 2 Port 2 Partition 1
MirroredPercentageAbove4G: 0.00
MirrorMemoryBelow4GB: false
```

2. Select the required disk to boot

```
$ efibootmgr -o 0002
```

3. Reboot to change the OS to boot

```
$reboot
```

