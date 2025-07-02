# Deploying Edge Microvisor Toolkit on Virtual Machines as Guest OS

Below you will find all methods of deployment on Virtual Machines (VMs) supported by Edge Microvisor Toolkit.

## Hyper-V

When using Hyper-V, you can install the ISO to a virtual hard drive that you create, or
you can attach an existing VHD artifact produced by the build pipeline. See the steps below:

1. From Hyper-V select *Action-> New-> Virtual Machine*.
2. Provide a name for your VM and press *Next*.
3. Select *Generation 1 (VHD)* or *Generation 2 (VHDX)*, then press *Next*.
4. Set the desired amount of memory to allocate, then press *Next*.
5. Select a virtual network switch, then press *Next*.
6. Select *Create a virtual hard disk* and one of two options:
   - either:
     1. Select a location for your VHD(X) and set your desired disk size, then press *Next*.
     2. Select *Install an operating system from a bootable image file* and browse to your
      microvisor ISO.
     3. Press *Finish*.
   - or:
     1. Select *Use existing VHD* to proceed with the VHD(X) produced by the build infrastructure.
     2. This option does not need the ISO, just press *Next* and *Finish*.

[Gen2/VHDX Only] Fix Boot Options

1. Right click your virtual machine from Hyper-V Manager. Select *Settings...*
2. Select *Security* and disable *Secure Boot*.
3. Select *Firmware* and adjust the boot order so DVD is the first and Hard Drive is second.
4. Select *Apply* to apply all changes.
5. Right click your VM and select *Connect...*. Select *Start*.
6. Follow the installer prompts to install your image.
7. When installation completes, select *Restart* to reboot the machine. The installation ISO
   will be automatically ejected.
8. When prompted, sign in to your Edge Microvisor Toolkit using the username and password
   provisioned through the installer.

> **Note:**
  When using an existing VHD, the default username/password is root/root.

## Oracle Virtual Box

1. Start Oracle VM VirtualBox Manager.
2. Create a new VM and chose a name for the virtual machine.
3. Select the ISO image of Edge Microvisor Toolkit.
4. Under *Operating System*, select *Linux*, sub-type *Fedora (64-bit)*.
5. Configure the number of CPUs and the amount of memory to allocate to the virtual machine.
6. Enable EFI.
7. Create the virtual disk image. If you use a pre-existing disk image (VHD or RAW), convert
  it to VDI first.

### Converting Image File to VDI

You can convert a VHD or RAW image to the VDI format, which is natively supported by
VirtualBox. Simply navigate to the installation folder of VirtualBox, e.g.
`C:\Program Files\Oracle\VirtualBox` and run the commands below in a terminal to convert:

a VHD disk image:

```bash
VBoxManage clonehd --format VDI <input-vhd-image.vhd> <output-vdi-image.vdi>
```

a RAW disk image:

```bash
VBoxManage convertfromraw <input-vhd-image.img> <output-vdi-image.vdi> --format VDI
```

## KVM

On Linux you can install and use Edge Microvisor Toolkit directly with KVM using the
graphical `virt-manager` and `virsh`. You can install the OS using the ISO image, or the
image file. On KVM it is preferred to use a RAW image, although it does support multiple
image formats.

On Ubuntu, install `virt-manager` or `virsh`:

```bash
sudo apt update
sudo apt install virt-manager
sudo apt install libvirt-clients
sudo apt install libvirt-daemon-system
sudo usermod -a -G libvirt $(whoami)
```

1. Start `virt-manager`.
2. Create a *New Virtual Machine*.
3. Select *Local installation media* (ISO image) or alternatively *Import existing disk
   image* and select the RAW disk image.
4. Deselect *Automatically detect from the installation /source* and choose the *Fedora* OS
   type manually.
5. Configure the number of CPUs and the amount of memory to allocate to the virtual machine.
6. Create the virtual disk image.
7. Create a name for the virtual machine and configure network as desired.

| Image              | Support                                                              |
| ------------------ | -------------------------------------------------------------------- |
| RAW (.img, .raw)   | ✅ Best performance, directly supported                              |
| QCOW2 (.qcow2)     | ✅ KVM's native format, supports snapshots and compression           |
| VHD (.vhd, .vpc)   | ⚠️ Limited. Direct use is unreliable, conversion is recommended.     |
| VDI (.vdi)         | ❌ No                                                                |

## QEMU and UEFI

Instead of using `virt-manager` you can also use `qemu` commands directly:

1. Create a virtual disk image, specifying a disk size appropriate for your usage and available storage:

```bash
qemu-img create -f qcow2 emt_rootfs.img 10G
```

2. Start the virtual machine

Launch and install the Edge Microvisor Toolkit in a Virtual Machine with UEFI virtual machine firmware ([OVMF](https://github.com/tianocore/tianocore.github.io/wiki/OVMF)):

```bash
qemu-system-x86_64 \
   -nodefaults -M accel=kvm -cpu host \
   -device virtio-rng-pci \
   -machine q35 -smp 2 -m 2048M \
   -vga std \
   -nic user \
   -drive if=pflash,format=raw,readonly=on,file=/usr/share/ovmf/OVMF.fd \
   -drive id=disk,file=/path/to/emt_rootfs.img,if=none,format=qcow2 \
   -device virtio-blk-pci,drive=disk,bootindex=1 \
   -drive id=cdrom,file=/path/to/EdgeMicrovisorToolkit-3.0.iso,if=none,media=cdrom \
   -device ide-cd,drive=cdrom,bootindex=2
```

Use the appropriate acceleration based on your platform, such as `accel=kvm` for Linux or `accel=hvf` for macOS on Intel based Mac systems.  The path to the virtual machine firmware may vary depending on your operating system and qemu package.