# Install Edge Microvisor Toolkit

Edge Microvisor Toolkit can be installed on bare metal, or as a virtual machine. This section
provides details of how to quickly install and try out Edge Microvisor Toolkit on your system.

## Virtual Machine with Hyper-V

When using Hyper-V you can install the ISO to a virtual hard drive that you create, or directly
use the VHD artifact produced by the build pipeline

- From Hyper-V Select Action->New->Virtual Machine
- Provide a name for your VM and press Next >
- Select Generation 1 (VHD) or Generation 2 (VHDX), then press Next >
- Change Memory size if desired, then press Next >
- Select a virtual switch, then press Next >
- Select Create a virtual hard disk and one of two options:
  - select a location for your VHD(X) and set your desired disk size, then press Next >
  - select Install an operating system from a bootable image file and browse to your microvisor ISO.
  - Press Finish.

  or

  - select "Use existing VHD" to proceed with the VHD(X) produced by the build infrastructure,
  - this option does not need the ISO, just press Next and Finish.

[Gen2/VHDX Only] Fix Boot Options

- Right click your virtual machine from Hyper-V Manager. Select Settings...
- Select Security and disable Secure Boot
- Select Firmware and adjust the boot order so DVD is the first and Hard Drive is second.
- Select Apply to apply all changes.

- Right click your VM and select Connect.... Select Start.
- Follow the Installer Prompts to Install your image
- When installation completes, select restart to reboot the machine. The installation ISO will be automatically ejected.
- When prompted sign in to your Edge Microvisor Toolkit using the user name and password provisioned through the Installer.

> **Note:**
  If installing the VHD directly, without the ISO, default username/password is root/root

## Virtual Machine with Oracle Virtual Box

- Start the Oracle VirtualBox Manager
- Create a new VM and chose a name for the virtual machine
- Select the ISO image of Edge Microvisor Toolkit
- Under Operating System, select Linux, sub-type Fedora (64-bit)
- Configure number of CPUs and memory allocated to the virtual machine
- Enable EFI
- Create virtual disk image, if you choose to use a pre-existing disk image file you may want to first convert the VHD or RAW image file to VDI

### Converting Image File to VDI

You can convert the raw image or VHD to the natively supported VDI format for VirtualBox

```bash
# Navigate to the installation location of VirtualBox, e.g. C:\Program Files\Oracle\VirtualBox

# Converting VHD disk image to VDI
VBoxManage clonehd --format VDI <input-vhd-image.vhd> <output-vdi-image.vdi>

# Convertin RAW disk image to VDI
VBoxManage convertfromraw <input-vhd-image.img> <output-vdi-image.vdi> --format VDI
```

## Virtual Machine with KVM

On Linux you can install and use Edge Microvisor Toolkit directly with KVM using the graphical `virt-manager` and `virsh`. You can install the OS using the ISO image, or the image file. On KVM it is preferred to use a `raw` image although it does support multiple image formats.

On Ubuntu, install `virt-manager` or `virsh`:

```bash
sudo apt update
sudo apt install virt-manager
sudo apt install libvirt-clients
sudo apt install libvirt-daemon-system
sudo usermod -a -G libvirt $(whoami)
```

- Start virt-manager.
- Create a New Virtual Machine.
- Select local install media (ISO image) or alternatively "Import existing disk image" and select the raw disk image.
- Unselect automatic OS discovery and select OS type manually to Fedora.
- Configure how many CPUs and memory to allocate for the virtual machine.
- Create the virtual disk image.
- Create a name for the virtual machine and configure network as desired.

| Image | Support |
| ----- | ------- |
| RAW (.img, .raw)| ✅ Best performance, directly supported|
| QCOW2 (.qcow2)  | ✅ KVM's native format, supports snapshots and compression|
| VHD (.vhd, .vpc)| ⚠️ Limited. Can be converted, but direct use is unreliable.|
| VDI (.vdi)      | ❌ No |

## Baremetal with ISO

### Linux

Follow these steps to create a bootable USB device to install Edge Microvisor Toolkit on a system (baremetal) using `dd`

Ensure you have the microvisor ISO file you want to flash saved on your system. Insert the USB drive and identify it.

```bash
lsblk
```

Compare the output before and after inserting your USB to identify its device name (e.g., /dev/sdb). Flash the ISO Image. Use the `dd` command to write the ISO image. Replace `/path/to/your.iso` with the ISO’s location and `/dev/sdb` with your USB device.

```bash
sudo dd if=/path/to/your.iso of=/dev/sdb bs=4M status=progress oflag=sync
# Warning: Double-check the device name. Using a wrong device can overwrite data.
```

Sync and Eject: Once `dd` finishes, run:

```bash
sudo sync
```

Then safely remove the USB drive.

### Windows

On Windows, download and install an ISO writer software such as [Rufus](https://rufus.ie).
Make sure you follow the steps below:

- Plug in the USB device.
- Launch Rufus and select the USB drive from the dropdown.
- Choose the ISO file by clicking "SELECT" under "Boot Selection".
- Select GPT as the partitioning scheme.
- Click "START" to begin writing the ISO to the USB device.
- Eject the USB device when Rufus has completed writing the ISO.

Install the Edge Microvisor Toolkit, using the live installer ISO and follow the on-screen configuration instructions. Optionally, you can enable
the option for Full Disc Encryption (FDE).

## Next

- Learn how to [Enable Secure Boot for Edge Microvisor Toolkit](sb-howto.md).
- Learn how to customize and manually [build microvisor images](building-howto.md).
