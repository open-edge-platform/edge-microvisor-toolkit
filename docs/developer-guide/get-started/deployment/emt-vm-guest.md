# Deploying Edge Microvisor Toolkit on Virtual Machines as Guest OS

Below you will find all methods of deployment on Virtual Machines (VMs) supported by Edge
Microvisor Toolkit.

The methods presented below assume the use of **"dev"** versions of Edge Microvisor Toolkit,
published as RAW and VHD images. If you want to start virtual machines using
**"non-dev"** images, built with
[edge-image-json](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/toolkit/imageconfigs/edge-image.json)
or [edge-image-rt.json](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/toolkit/imageconfigs/edge-image-rt.json)
, you need to unseal disk encryption key with TPM, or
[rebuild them](../emt-building-howto.md#building-the-default-microvisor-image)
with the `"EMTEncryptionEnabled": false` parameter in the corresponding JSON config file.

## Hyper-V

When using Hyper-V, you can install the ISO to a virtual hard drive that you create.
See the steps below:

1. From Hyper-V select *Action-> New-> Virtual Machine*.
2. Provide a name for your VM and press *Next*.
3. Select *Generation 1 (VHD)* or *Generation 2 (VHDX)*, then press *Next*.
4. Set the desired amount of memory to allocate, then press *Next*.
5. Select a virtual network switch, then press *Next*.
6. Select *Create a virtual hard disk* and one of two options:

     1. Select a location for your VHD(X) and set your desired disk size, then press *Next*.
     2. Select *Install an operating system from a bootable image file* and browse to your
      microvisor ISO.
     3. Press *Finish*.

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

> **NOTE:**
  When using an existing VHD, the default username/password is root/root.

## Oracle Virtual Box

1. Start Oracle VM VirtualBox Manager.
2. Create a new VM and chose a name for the virtual machine.
3. Select the ISO image of Edge Microvisor Toolkit.
4. Under *Operating System*, select *Linux*, sub-type *Ubuntu (64-bit)*.
5. Configure the number of CPUs and the amount of memory to allocate to the virtual machine.
6. Enable EFI.
7. Create the virtual disk image. If you use a pre-existing disk image (VHD or RAW), convert
  it to VDI first.

### Converting Image File to VDI

You can convert a VHD or RAW image to the VDI format, which is natively supported by
VirtualBox. Simply navigate to the installation folder of VirtualBox, e.g.
`C:\Program Files\Oracle\VirtualBox` and run the commands below in a terminal to convert:

- a VHD disk image:

  ```bash
  VBoxManage clonehd --format VDI <input-vhd-image.vhd> <output-vdi-image.vdi>
  ```

- a RAW disk image:

  ```bash
  VBoxManage convertfromraw <input-vhd-image.img> <output-vdi-image.vdi> --format VDI
  ```

## KVM

On Linux you can install and use Edge Microvisor Toolkit directly with KVM using the
graphical `virt-manager` and `virsh`. Install the OS using the ISO image, or by
importing an existing disk image in a [supported format](#support-for-disk-image-formats).

On Ubuntu, install `virt-manager` or `virsh`:

```bash
sudo apt update
sudo apt install virt-manager
sudo apt install libvirt-clients
sudo apt install libvirt-daemon-system
sudo usermod -a -G libvirt $(whoami)
```

Start `virt-manager` and create a *New Virtual Machine*. Choose the preferred installation
method:

- *Local install media* (ISO image)

  1. Click *Browse* to open the *Locate ISO media volume* window.
  2. Click *Browse local* and navigate to the folder with the ISO image. Select the image
     file and click *Open*.
  3. You may be prompted with the *"The emulator may not have search permissions for the
     specified path. Do you want to correct this now?"* Click *Yes*.
  4. Deselect *Automatically detect from the installation /source* and choose the *Fedora* OS
     type manually and click *Forward*.
  5. Configure the number of CPUs and the amount of memory to allocate to the virtual machine.
  6. Check *Enable storage for this virtual machine* and choose
     *Create a disk image for the virtual machine*. Then, specify the size of the disk image.
  7. Create a name for the virtual machine, configure network as desired, check the
     *Customize configuration before install* option and click *Finish*.
  8. In *Overview* tab, go to *Hypervisor Details* and change *Firmware* to
     `UEFI x86_64: /usr/share/OVMF/OVMF_CODE_4M.fd`.
  9. Click *Begin Installation*. The virtual machine will boot and run the installation of
     Edge Microvisor Toolkit.
  10. Select the desired installer when prompted and proceed.
  11. Choose an *Installation Type*.
  12. Select the *Virtual Disk* for installation and click *Next* if you want to use the
      default partitioning method. Otherwise, select *Custom Partition* to set it up
      manually.
  13. Skip disk encryption (optional).
  14. Use the default *Hostname* and select *Next* to set up the user account.
  15. Select *Yes* to *Start Installation*.
  16. Upon successful installation, you need to press ENTER to restart.

- *Import existing disk image* (RAW, QCOW2)

  1. Click *Browse* to open the *Locate or create storage volume* window.
  2. Click *Browse local* and navigate to the folder with the disk image. Select the image
     file and click *Open*.
  2. Choose the *Fedora* OS type manually and click *Forward*.
  3. Configure CPU and memory settings.
  4. Specify the name for the virtual machine and check the
     *Customize configuration before install* option and click *Finish*.
  5. In *Overview* tab, go to *Hypervisor Details* and change *Firmware* to
     `UEFI x86_64: /usr/share/OVMF/OVMF_CODE_4M.fd`.
  6. Click *Begin Installation* to boot and run Edge Microvisor Toolkit.

**You are now ready to use Edge Microvisor Toolkit!**

### Support for Disk Image Formats

| Image              | Support                                                              |
| ------------------ | -------------------------------------------------------------------- |
| RAW (.img, .raw)   | ✅ Best performance, directly supported                              |
| QCOW2 (.qcow2)     | ✅ KVM's native format, supports snapshots and compression           |
| VHD (.vhd, .vpc)   | ⚠️ Limited. Direct use is unreliable, conversion is recommended.     |
| VDI (.vdi)         | ❌ No                                                                |

### Converting Image File to QCOW2

You can convert a RAW or VHD image to the QCOW2 format, which is natively supported by
KVM. Start a terminal and use `qemu-img` to convert:

- a RAW disk image:

  ```bash
  qemu-img convert -f raw -O qcow2 <input-image.img> <output-image.qcow2>
  ```

- a VHD disk image:

  ```bash
  qemu-img convert -f vpc -O qcow2 <input-image.vhd> <output-image.qcow2>
  ```

> **NOTE**: You can also run `qemu-img` without the `-f` parameter to let it detect the input
format:
>
> ```bash
> qemu-img convert -O qcow2 <input-image.vhd> <output-image.qcow2>
> ```

## QEMU and UEFI

You can launch Edge Microvisor Toolkit in a virtual machine using `qemu-img` and the
([OVMF firmware](https://github.com/tianocore/tianocore.github.io/wiki/OVMF)), which provides
UEFI support. See the examples below to learn how to install Edge Microvisor Toolkit from
the ISO image, or launch the toolkit from existing RAW/ VHD disk images.

Use an appropriate acceleration type based on your platform, such as `accel=kvm` for Linux
or `accel=hvf` for macOS on Intel-based Macs. Specify the path to the virtual machine
firmware (OVMF). The path may vary depending on your OS and the version of Qemu.


### Create Virtual Machine using ISO

1. Create a virtual disk image, specifying a disk size appropriate for your usage and
   available storage:

   ```bash
   qemu-img create -f qcow2 emt_rootfs.img 10G
   ```

2. Start the virtual machine and install Edge Microvisor Toolkit.

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

### Create Virtual Machine using RAW or VHD

- RAW

  ```bash
  qemu-system-x86_64 \
     -nodefaults -M accel=kvm -cpu host \
     -device virtio-rng-pci \
     -machine q35 -smp 2 -m 2048M \
     -vga std \
     -nic user \
     -drive if=pflash,format=raw,readonly=on,file=/usr/share/ovmf/OVMF.fd \
     -drive id=disk1,file=/path/to/EdgeMicrovisorToolkit-3.0.raw,if=none,format=raw,cache=none \
     -device virtio-blk-pci,drive=disk1,bootindex=1
  ```

- VHD

  ```bash
  qemu-system-x86_64 \
     -nodefaults -M accel=kvm -cpu host \
     -device virtio-rng-pci \
     -machine q35 -smp 2 -m 2048M \
     -vga std \
     -nic user \
     -drive if=pflash,format=raw,readonly=on,file=/usr/share/ovmf/OVMF.fd \
     -drive id=disk1,file=/path/to/EdgeMicrovisorToolkit-3.0.vhd,if=none,format=vpc,cache=none \
     -device virtio-blk-pci,drive=disk1,bootindex=1
  ```
