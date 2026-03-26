# Create VMs under Edge Microvisor Toolkit Host

Edge Microvisor Toolkit supports SR-IOV (Single Root Input/Output Virtualization),
which allows it to serve as a host OS for virtualization of other operating systems,
running as a guest OS in a virtual machine.

The guide provides instructions on how to perform automated script-based
deployment of guest Ubuntu 22.04 and Windows 11 Enterprise operating systems,
using virtual machines on [Intel IoT platforms](#supported-intel-iot-platforms)
using [libvirt toolkit](https://libvirt.org/) on
[KVM/QEMU](https://libvirt.org/drvqemu.html) hypervisor/emulator.


**Table of contents:**

- [Requirements](#requirements)
  - [Supported Intel IoT Platforms](#supported-intel-iot-platforms)
  - [Host operating system](#host-operating-system)
  - [Supported guest operating systems](#supported-guest-operating-systems)
  - [Device support in guest VMs](#device-support-in-guest-vms)
  - [KVM MultiOS portfolio release repository](#kvm-kernel-based-virtual-machine-multios-portfolio-release-repository)
- [Set up the Ubuntu host](#set-up-the-ubuntu-host)
  - [Install Ubuntu 22.04](#install-ubuntu-2204)
  - [Clone the KVM MultiOS repository](#clone-the-kvm-multios-repository)
  - [Prepare the host](#prepare-the-host)
    - [Prerequisites](#prerequisites)
    - [Setup the KVM Multios Host](#setup-the-kvm-multios-host)
- [Create guest OS images](#create-guest-os-images)
  - [Create Ubuntu VM image](#create-ubuntu-vm-image)
  - [Create Windows 11 Enterprise VM image](#create-windows-11-enterprise-vm-image)

## Requirements

### Supported Intel IoT Platforms

Currently, only RPL-P (Raptor Lake P) platforms are supported.

### Host operating system

**Ubuntu 22.04 LTS 2024 Engineering Release Candidate** - a host operating
system that is used to prepare the guest OS images.

> **Note:** Contact your Intel representative for more details on this resource.

### Supported guest operating systems

| OS | Details |
| --- | --- |
| Ubuntu 22.04 | 6.12 kernel- [lts-v6.12.76-linux-260309T025316Z](https://github.com/intel/linux-intel-lts/releases/tag/lts-v6.12.76-linux-260309T025316Z) |
| Windows 11 | [IoT Enterprise](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-11-enterprise) |

### Device support in guest VMs

| Device | Ubuntu 22.04 | Windows 11 IoT Enterprise |
| --- | --- | --- |
| Storage | Sharing | Sharing |
| iGPU * | SR-IOV | virtio-gpu, SR-IOV |
| Display* | SR-IOV | SR-IOV |
| Audio | emulation | emulation |
| USB inputs (mouse/keyboard) | Passthrough or emulation | Passthrough or emulation |
| LAN | Virtual NAT | Virtual NAT |
| External PCI Ethernet Adapter | Passthrough | Passthrough |
| External USB Ethernet Adapter | Passthrough | Passthrough |
| TSN i225/i226 Ethernet Adapter | Passthrough | Passthrough |
| Wi-fi | Passthrough | Passthrough |
| Bluetooth | Passthrough | Passthrough |
| SATA controller | Passthrough | Passthrough |
| USB Controller | Passthrough | Passthrough |
| Serial Controller | Passthrough** | Passthrough** |
| NPU | Passthrough | Passthrough |
| IPU | Passthrough | Passthrough |
| TPM | Passthrough | SW emulation |

> **Note:**
> When a device is a passthrough to a guest VM, it can be used by that VM only
> and will not be available to any other VM or host.
>
> \*\* Not Validated in this release.

### KVM (Kernel-based Virtual Machine) MultiOS portfolio release repository

The [kvm-multios](https://github.com/intel/kvm-multios) repository contains
configuration and setup scripts required for preparing kernel-based virtual
machines on Intel IoT platforms. This guide uses the
[`v0.19.0`](https://github.com/intel/kvm-multios/tree/v0.19.0) release tag.
For more details, refer to
[the documentation](https://github.com/intel/kvm-multios/blob/v0.19.0/documentation/README.md).

## Set up the Ubuntu host

The Ubuntu host operating system is used to prepare the guest OS images
that will be used in virtual machines on Edge Microvisor Toolkit serving
as hypervisor.

### Install Ubuntu 22.04

1. Configure BIOS settings.

   To check IFWI/ BIOS Version, refer to the [host operating system](#host-operating-system).
   Make sure the following settings are configured:

   | Name | Menu | Setting |
   | --- | --- | --- |
   | Intel Virtualization Technology (VMX) | Intel Advanced Menu -> CPU Configuration -> VMX | Enable |
   | Intel VT for Directed I/O (VT-d) | Intel Advanced Menu -> System Agent (SA) Configuration -> VT-d | Enable |


2. Flash the host device.

   1. Download the Ubuntu 22 host image.

      > **Note:** Use the base OS image provided in [the host resources](#host-operating-system).

   2. Flash the drive.

      Replace `/dev/nvme0n1` with your drive:

      ```sh
      sudo bmaptool copy --nobmap ubuntu-22.04.img.bz2 /dev/nvme0n1
      ```

   3. Reboot into the Ubuntu 22 host.

3. Download and run the `installer.sh` script.

   > **Note:** The script is provided in [the host resources](#host-operating-system).

   ```sh
   chmod +x installer.sh
   sudo ./installer.sh RPL
   sudo reboot
   ```

### Clone the KVM MultiOS repository

Check the [tag version](#kvm-kernel-based-virtual-machine-multios-portfolio-release-repository)
and clone the [kvm-multios](https://github.com/intel/kvm-multios) repository.

```sh
cd ~
git clone -b <tag> https://github.com/intel/kvm-multios.git
```

### Prepare the host

#### Prerequisites

Make sure the host platform meets the following requirements:

- it has sufficiently large disk allocation for `/var` during installation of OS,

  > **Note:** The default storage path for libvirt for all guest domain disk
  > images and other usage is at `/var`.
- it has a physical display monitor connected prior to the installation,
- it is setup as per platform release BSP guide and booted accordingly,
- it has a network connection and Internet access
- proxy variables (http_proxy, https_proxy, no_proxy) are set appropriately in
  `/etc/environment` if required for the network access,
- it is updated by running `sudo apt update`,
- it has a current date/ time set up,
- a user already logged into the UI home screen prior to any operations,
  or a user account set to auto-login, as required for VM support with Intel
  GPU SR-IOV.

For more details, refer to
[the prerequisites](https://github.com/intel/kvm-multios/blob/v0.19.0/documentation/setup_sriov.md#prerequisites).

#### Setup the KVM MultiOS Host

```bash
cd kvm-multios
./host_setup/ubuntu/setup_host.sh -u GUI
```

## Create Guest OS images

Now that the host has been set up, you can prepare
[Ubuntu 22.04](#create-ubuntu-vm-image) and
[Windows 11 Enterprise](#create-windows-11-enterprise-vm-image)
operating systems for your virtual machines.

### Create Ubuntu VM image

Open a terminal window in the host, and run the following command to start
automated creation of the Ubuntu VM image.

```bash
./guest_setup/ubuntu/ubuntu_setup.sh --force --viewer
```

Once the installation has completed, the VM image will be in the shutdown state.
The `ubuntu.qcow2` VM image will be located in the `/var/lib/libvirt/images/`
directory. The image must be copied to an appropriate host machine with
SR-IOV support.

For more details, refer to
[the Ubuntu VM installation guide](https://github.com/intel/kvm-multios/blob/v0.19.0/documentation/ubuntu_vm.md).

## Create Windows 11 Enterprise VM image

1. Download Windows 11 ISO image.

   Download Windows 11 24H2 Enterprise Evaluation at
   <https://www.microsoft.com/en-us/evalcenter/evaluate-windows-11-enterprise>.

2. (Optional) Create a no-prompt Windows installation ISO image.

   For more details, refer to
   [the Windows VM installation guide](https://github.com/intel/kvm-multios/blob/v0.19.0/documentation/windows_vm.md).

   > **Important:**
   >
   > - This step is required only for a fully-automated setup without any human intervention.
   > - This step is optional if you are able to monitor the initial boot during the installation
       and respond when prompted with _"Press Any Key To Boot From..."_.

3. Download the Windows 11 OS patch 26100.7922.

   1. Download the required .msu files:

      - **KB5043080:**

        ```bash
        https://catalog.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/d8b7f92b-bd35-4b4c-96e5-46ce984b31e0/public/windows11.0-kb5043080-x64_953449672073f8fb99badb4cc6d5d7849b9c83e8.msu
        ```

      - **KB5077241:**

        ```bash
        https://catalog.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/66b28d24-251c-4c0a-8a19-82bc599deac3/public/windows11.0-kb5077241-x64_739bca934f7f45038f9752637f632afa52c35f75.msu
        ```

   2. Copy the .msu files to the `unattend_win11` folder:

      ```bash
      cp windows11.0-kb5043080-x64_953449672073f8fb99badb4cc6d5d7849b9c83e8.msu ./guest_setup/ubuntu/unattend_win11/windows-updates_01.msu
      cp windows11.0-kb5077241-x64_739bca934f7f45038f9752637f632afa52c35f75.msu ./guest_setup/ubuntu/unattend_win11/windows-updates_02.msu
      ```

4. Prepare the iGFX driver.

   1. Download the driver .zip package:

      > **Note:** Contact your Intel representative for more details on this resource.

   2. Copy the package to the `unattend_win11` folder:

      ```bash
      cp GFX-prod-hini-releases* ./guest_setup/ubuntu/unattend_win11/Driver-Release-64-bit.zip
      ```

5. Prepare the Intel Graphics SR-IOV ZeroCopy driver.

   1. Download the `ZCBuild_<version>_Installer.zip` package:

      > **Note:** Contact your Intel representative for more details on this resource.

   2. Copy the `ZCBuild_xxxx_Installer.zip` to the `unattend_win11` folder:

     ```bash
     cp ZCBuild_*_Installer.zip ./guest_setup/ubuntu/unattend_win11/ZCBuild_MSFT_Signed_Installer.zip
     ```

6. Create the guest Windows 11 VM image.

   Use the command below to start automated OS image creation.

   ```bash
   ./guest_setup/ubuntu/win11_setup.sh -p client --force --viewer
   ```

   Once the process has finished, the VM image will be in the shutdown state.
   It will be located at: `/var/lib/libvirt/images/window11.qcow2`.
   The image must be copied to an appropriate host machine with SR-IOV support.

> **Note:**
> If you are installing with a standard ISO file, you will be prompted to
> "Press Any Key To Boot From..." during the initial boot.
> If you miss this prompt, press the ESC key until you reach the BIOS setup
> screen, then select “reset” to start over again.
