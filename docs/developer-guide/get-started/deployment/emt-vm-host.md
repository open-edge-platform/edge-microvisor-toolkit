# Create Guest OS VMs for Edge Microvisor Toolkit Host

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
  - [KVM MultiOS repository](#kvm-multios-repository)
- [Set up the Ubuntu host](#set-up-the-ubuntu-host)
  - [Configure BIOS settings](#configure-bios-settings)
  - [Install Ubuntu 22.04](#install-ubuntu-2204)
  - [Prepare the host with KVM MultiOS scripts](#prepare-the-host-with-kvm-multios-scripts)
- [Create Guest OS images](#create-guest-os-images)
  - [Ubuntu VM image](#ubuntu-vm-image)
    - [Configure Ubuntu user creation](#configure-ubuntu-user-creation)
    - [Create Ubuntu VM image](#create-ubuntu-vm-image)
      - [Start automated creation of Ubuntu VM](#start-automated-creation-of-ubuntu-vm)
      - [(Optional) Customize disk size for Ubuntu VM](#optional-customize-disk-size-for-ubuntu-vm)
- [Windows 11 Enterprise VM image](#windows-11-enterprise-vm-image)
  - [Configure Windows 11 creation](#configure-windows-11-creation)
    - [1. Download Windows 11 ISO image](#1-download-windows-11-iso-image)
    - [2. Create a no-prompt Windows installation ISO image](#2-create-a-no-prompt-windows-installation-iso-image)
    - [3. Prepare the Windows 11 OS patch 26100.7922](#3-prepare-the-windows-11-os-patch-261007922)
    - [4. Prepare the Intel Graphics driver](#4-prepare-the-intel-graphics-driver)
    - [5. Prepare the Intel Graphics SR-IOV ZeroCopy driver](#5-prepare-the-intel-graphics-sr-iov-zerocopy-driver)
  - [Create the guest Windows 11 VM image](#create-the-guest-windows-11-vm-image)
    - [Start automated OS image creation](#start-automated-creation-of-windows-11-vm)
    - [(Optional) Customize disk size for Windows VM](#optional-customize-disk-size-for-windows-vm)

## Requirements

### Supported Intel IoT Platforms

Currently, only RPL-P (Raptor Lake P) platforms are supported.

### Host operating system

[Ubuntu 22.04.5 (Jammy Jellyfish)](https://releases.ubuntu.com/jammy/) -
the operating system used as a host where [guest VM images are created](#create-guest-os-images).

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

### KVM MultiOS repository

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

### Configure BIOS settings

Make sure the following settings are configured:

| Name | Menu | Setting |
| --- | --- | --- |
| Intel Virtualization Technology (VMX) | Intel Advanced Menu -> CPU Configuration -> VMX | Enable |
| Intel VT for Directed I/O (VT-d) | Intel Advanced Menu -> System Agent (SA) Configuration -> VT-d | Enable |

### Install Ubuntu 22.04

1. Download [Ubuntu 22.04 (Jammy Jellyfish)](https://releases.ubuntu.com/jammy/ubuntu-22.04.5-desktop-amd64.iso).

2. Install the OS:

   ```bash
   # Copy the iso file into a USB drive
   sudo dd if=./ubuntu-22.04.5-desktop-amd64.iso of=/dev/sdX bs=4M && sync

   # Check the boot order number X of the USB drive
   sudo efibootmgr

   # Select the USB drive as the next boot device
   sudo efibootmgr -n X

   # Reboot into the drive to start the installation
   sudo reboot
   ```

> **Note:** If operating behind a corporate firewall, setup proxy settings as required.

3. In the **Software & Updates** GUI, make sure to download from **Main server**, as shown below:

   ![Software and Updates](../../assets/ubuntu-softwareupdates.png)

4. Update the main APT sources configuration file:

   ```bash
   sudo nano /etc/apt/sources.list.d/intel-rpl.list
   ```

   Add the following lines:

   ```bash
   deb https://download.01.org/intel-linux-overlay/ubuntu jammy main non-free multimedia kernels
   deb-src https://download.01.org/intel-linux-overlay/ubuntu jammy main non-free multimedia kernels
   ```
5. Download the GPG key:

   ```bash
   sudo wget https://download.01.org/intel-linux-overlay/ubuntu/E6FA98203588250569758E97D176E3162086EE4C.gpg -O /etc/apt/trusted.gpg.d/rpl.gpg
   ```

6. Set the preferred list for pinning APT packages:

   ```bash
   sudo nano /etc/apt/preferences.d/intel-rpl
   ```

   Add the following lines:

   ```bash
   Package:*
   Pin:release o=intel-iot-linux-overlay
   Pin-Priority:2000
   ```
4. Upgrade the Ubuntu host software to the latest version:

   ```bash
   sudo apt -y update
   sudo apt -y upgrade
   ```

   > **Note:** Generic host kernel installed from Ubuntu may be incompatible
   > with the board. Therefore, after the upgrade, continue to install the
   > host kernel and firmware before rebooting (step 7).

5. Install required APT packages:

   ```bash
   sudo apt install vim ocl-icd-libopencl1 curl openssh-server net-tools \
   gir1.2-gst-plugins-bad-1.0 gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 \
   gir1.2-gst-rtsp-server-1.0 gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 \
   gstreamer1.0-opencv gstreamer1.0-plugins-bad gstreamer1.0-plugins-bad-apps \
   gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps gstreamer1.0-plugins-good \
   gstreamer1.0-plugins-ugly gstreamer1.0-pulseaudio gstreamer1.0-qt5 gstreamer1.0-rtsp \
   gstreamer1.0-tools gstreamer1.0-x intel-media-va-driver-non-free libdrm-amdgpu1 \
   libdrm-common libdrm-dev libdrm-intel1 libdrm-nouveau2 libdrm-radeon1 libdrm-tests \
   libdrm2 libgstrtspserver-1.0-dev libgstrtspserver-1.0-0 libgstreamer-gl1.0-0 \
   libgstreamer-opencv1.0-0 libgstreamer-plugins-bad1.0-0 libgstreamer-plugins-bad1.0-dev \
   libgstreamer-plugins-base1.0-0 libgstreamer-plugins-base1.0-dev \
   libgstreamer-plugins-good1.0-0 libgstreamer-plugins-good1.0-dev libgstreamer1.0-0 \
   libgstreamer1.0-dev libigdgmm-dev libigdgmm12 libmfx-gen1.2 libtpms-dev libtpms0 \
   libva-dev libva-drm2 libva-glx2 libva-wayland2 libva-x11-2 libva2 libwayland-bin \
   libwayland-client0 libwayland-cursor0 libwayland-dev libwayland-doc \
   libwayland-egl-backend-dev libwayland-egl1 libwayland-server0 libxatracker2 \
   linux-firmware mesa-utils libgl1-mesa-dev libglx-mesa0 libgl1-mesa-dri \
   mesa-va-drivers mesa-vdpau-drivers mesa-vulkan-drivers libvpl-dev libvpl-tools \
   libmfx-gen-dev onevpl-tools ovmf ovmf-ia32 va-driver-all vainfo weston \
   xserver-xorg-core libvirt0 libvirt-clients libvirt-daemon \
   libvirt-daemon-config-network libvirt-daemon-config-nwfilter \
   libvirt-daemon-driver-lxc libvirt-daemon-driver-qemu \
   libvirt-daemon-driver-storage-gluster libvirt-daemon-driver-storage-iscsi-direct \
   libvirt-daemon-driver-storage-rbd libvirt-daemon-driver-storage-zfs \
   libvirt-daemon-driver-vbox libvirt-daemon-driver-xen libvirt-daemon-system \
   libvirt-daemon-system-systemd libvirt-dev libvirt-doc libvirt-login-shell \
   libvirt-sanlock libvirt-wireshark libnss-libvirt swtpm swtpm-tools bmap-tools adb \
   autoconf automake libtool cmake g++ gcc git intel-gpu-tools libssl3 libssl-dev make \
   mosquitto mosquitto-clients build-essential apt-transport-https default-jre \
   docker-compose git-lfs gnuplot lbzip2 libglew-dev libglm-dev libsdl2-dev mc openssl \
   pciutils python3-pandas python3-pip python3-seaborn terminator wmctrl \
   wayland-protocols gdbserver ethtool iperf3 msr-tools powertop linuxptp lsscsi \
   tpm2-tools tpm2-abrmd binutils cifs-utils i2c-tools xdotool gnupg lsb-release \
   intel-opencl-icd iproute2 socat
   ```

6. Download and install graphics userspace packages:

   ```bash
   wget https://github.com/intel/intel-graphics-compiler/releases/download/v2.10.8/intel-igc-core-2_2.10.8+18926_amd64.deb
   wget https://github.com/intel/intel-graphics-compiler/releases/download/v2.10.8/intel-igc-opencl-2_2.10.8+18926_amd64.deb
   wget https://github.com/intel/compute-runtime/releases/download/25.13.33276.16/intel-level-zero-gpu_1.6.33276.16_amd64.deb
   wget https://github.com/intel/compute-runtime/releases/download/25.13.33276.16/intel-opencl-icd_25.13.33276.16_amd64.deb
   sudo dpkgi -i *.deb
   ```

7. Install the Linux kernel and reboot:

   - Install Linux headers:

     ```bash
     sudo apt install linux-headers-6.12-intel linux-image-6.12-intel
     ```

   - Update the bootloader:

     ```bash
     sudo sed -i 's/GRUB_CMDLINE_LINUX=.*/GRUB_CMDLINE_LINUX=\"i915.enable_guc=3 i915.max_vfs=7 i915.force_probe=* udmabuf.list_limit=8192 console=tty0 console=ttyS0,115200n8 systemd.unified_cgroup_hierarchy=0 cgroup_enable=memory cgroup_enable=cpuset\"/' /etc/default/grub
     sudo sed -i 's/GRUB_DEFAULT=.*/GRUB_DEFAULT=\"Advanced options for Ubuntu>Ubuntu, with Linux 6.12-intel\"/g' /etc/default/grub
     sudo update-grub
     ```

   - Reboot the system:

     ```bash
     sudo reboot
     ```

### Prepare the host with KVM MultiOS scripts

1. Ensure the host platform meets the following requirements:

   - it has sufficiently large disk allocation for `/var` during installation of OS,

     > **Note:** The default storage path for libvirt for all guest domain disk
     > images and other usage is at `/var`.
   - it has a physical display monitor connected prior to the installation,
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


2. Clone the KVM MultiOS repository:

   Check the [tag version](#kvm-multios-repository)
   and clone the [kvm-multios](https://github.com/intel/kvm-multios) repository.

   ```sh
   cd ~
   git clone -b <tag> https://github.com/intel/kvm-multios.git
   ```

3. Run the host setup script:

   ```bash
   cd kvm-multios
   ./host_setup/ubuntu/setup_host.sh -u GUI
   ```

## Create Guest OS images

Now that the host has been set up, you can prepare
[Ubuntu 22.04](#ubuntu-vm-image) and
[Windows 11 Enterprise](#windows-11-enterprise-vm-image)
operating systems for your virtual machines.

### Ubuntu VM image

### Configure Ubuntu user creation

By default, Ubuntu desktop images prompt for user creation during the first boot
on the welcome screen. To enable automatic user
creation and login, modify the auto-install configuration file.

1. Automated Configuration (Recommended)

   Run the following commands to configure automatic user creation and auto-login.

   > **Note**:  Make sure to replace `YOURUSERNAME` and `YOURPASSWORD` with
   > your proper credentials.

   ```bash
   cd ~/kvm-multios
   # Backup the original file
   cp guest_setup/ubuntu/auto-install-ubuntu-desktop.yaml guest_setup/ubuntu/auto-install-ubuntu-desktop.yaml.backup
   # Apply the user creation configuration
   sed -i "/users: \[''\]/c\    users:\n      - name: 'YOURUSERNAME'\n        plain_text_passwd: 'YOURPASSWORD'\n        shell
   # Add automatic login configuration
   sed -i '/runcmd:/a\      - sed -i '"'"'s/#  AutomaticLoginEnable =/AutomaticLoginEnable =/g'"'"' /etc/gdm3/custom.conf\n
   ```

2. Manual Edit

   If you prefer to manually edit the file, open
   `guest_setup/ubuntu/auto-install-ubuntu-desktop.yaml` in a text editor and
   make the following changes:

   - Find the `user-data:` section and replace:

     ```text
       user-data:
         # This inhibits user creation, which for Desktop images means that
         # gnome-initial-setup will prompt for user creation on first boot.
         users: ['']
     ```

     with the following data:

     ```text
       user-data:
         # This inhibits user creation, which for Desktop images means that
         # gnome-initial-setup will prompt for user creation on first boot.
         users:
           - name: 'YOURUSERNAME'
             plain_text_passwd: 'YOURPASSWORD'
             shell: /bin/bash
             lock_passwd: false
             gecos: 'user'
             sudo:  ALL=(ALL) NOPASSWD:ALL
             groups: [adm, cdrom, sudo, dip, plugdev, lpadmin, lxd, render]
     ```

   - Find the `runcmd:` section and add the following lines:

     ```text
       runcmd:
         - sed -i 's/#  AutomaticLoginEnable =/AutomaticLoginEnable =/g' /etc/gdm3/custom.conf
         - sed -i 's/#  AutomaticLogin = user1/AutomaticLogin = user/g' /etc/gdm3/custom.conf
         - cp /var/log/syslog /tmp/syslog_setup_cont
         # shutdown after install
         - shutdown
     ```

     **Configuration details:**

     - Username: <your-user-name>
     - Password: <your-password>
     - Sudo access: Passwordless sudo enabled
     - Auto-login: Enabled via GDM3 configuration

Verify the changes:

```bash
grep -A 8 "users:" guest_setup/ubuntu/auto-install-ubuntu-desktop.yaml
grep -A 3 "runcmd:" guest_setup/ubuntu/auto-install-ubuntu-desktop.yaml
```

### Create Ubuntu VM image

#### Start automated creation of Ubuntu VM

Open a terminal window in the host, and run the following command to start
automated creation of the Ubuntu VM image.

```bash
./guest_setup/ubuntu/ubuntu_setup.sh --force --viewer
```

#### (Optional) Customize disk size for Ubuntu VM

The default storage size of the ubuntu VM is 60 GiB. To customize the disk size,
add the `--disk-size` option:

```bash
./guest_setup/ubuntu/ubuntu_setup.sh --force --viewer --disk-size 100
```

Replace `100` with your desired disk size in GiB.

Once the installation has completed, the VM image will be in the shutdown state.
The `ubuntu.qcow2` VM image will be located in the `/var/lib/libvirt/images/`
directory. The image must be copied to an appropriate host machine with
SR-IOV support.

For more details, refer to
[the Ubuntu VM installation guide](https://github.com/intel/kvm-multios/blob/v0.19.0/documentation/ubuntu_vm.md).

You can use the virtual machine on [Edge Microvisor Toolkit host](../emt-installation-howto.md).

## Windows 11 Enterprise VM image

### Configure Windows 11 creation

#### 1. Download Windows 11 ISO image

Download Windows 11 24H2 Enterprise Evaluation at
<https://www.microsoft.com/en-us/evalcenter/evaluate-windows-11-enterprise>.


Fill out the required registration form, select your language and download
the 64-bit ISO. Save the ISO file to your host system.

#### 2. Create a no-prompt Windows installation ISO image

> **Important:**
>
> - This step is required only for a fully-automated setup without any human
>   intervention.
> - This step is optional if you are able to monitor the initial boot during
>   the installation and respond when prompted with _"Press Any Key To Boot From..."_.
> - You will need a Windows machine to perform the steps below.


1. Install Windows ADK (Assessment and Deployment Kit)

   Download and install the Windows ADK that matches Windows 11
   Enterprise 24H2 above:

   1. Download both components:

   - [Windows ADK for Windows 11, version 22H2](https://go.microsoft.com/fwlink/?linkid=2196127)
   - [Windows PE add-on for the ADK](https://go.microsoft.com/fwlink/?linkid=2196224)

   2. Install both components:

      - First, run the ADK installer (accept all defaults).
      - Then, run the Windows PE add-on installer.

      The default installation path is `C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit`.

2. Prepare the "NoPrompt ISO Creation" script.

   1. Download the [CreateNoPromptISO.ps1](https://github.com/DeploymentResearch/DRFiles/raw/906151a1cdd55a14bc226196a3f597b0538273dd/Scripts/Create-NoPromptISO.ps1)
      PowerShell script and save it to
      `C:\Users\<YourUsername>\Downloads\CreateNoPromptISO.ps1`.

   2. Configure the script.

      Open `CreateNoPromptISO.ps1` in a text editor (Notepad or PowerShell
      ISE) and modify the following three variables

      ```text
      # Input: Your original Windows 11 ISO file
      $WinPE_InputISOfile = "C:\Users\<YourUsername>\Downloads\26100.1.240331-1435.ge_release_CLIENTENTERPRISE_OEM_x64FRE_en-us.iso
      # Output: The NoPrompt ISO file to create
      $WinPE_OutputISOfile = "C:\Users\<YourUsername>\Downloads\Windows11-NoPrompt.iso"
      # ADK Path: Where you installed Windows ADK (from Step 2.1.1)
      $ADK_Path = "C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit"
      ```

      - `$WinPE_InputISOfile` - the path to the downloaded Windows 11 ISO file.
      - `$WinPE_OutputISOfile` - the path for saving the generated
        NoPrompt ISO. Mmake sure the folder exists.
      - `$ADK_Path` - the installation path for ADK from Step 1.

3. Generate the ISO image.

   1. Start PowerShell as administrator.
   2. Navigate to your Downloads folder:

      ```bash
      cd $env:USERPROFILE\Downloads
      ```

   3. Enable script execution (if needed):

      ```bash
      Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
      ```

   4. When prompted, type Y and press Enter to confirm.

      ```text
      Execution Policy Change
      The execution policy helps protect you from scripts that you do not trust. Changing the execution
      policy might expose you to the security risks described in the about_Execution_Policies help topic at
      https://go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
      [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): Y
      ```

   4. Run the script:

      ```bash
      .\CreateNoPromptISO.ps1
      ```

      The script will create the NoPrompt ISO file at the location specified
      in `$WinPE_OutputISOfile`. The new ISO file is ready for automated
      installation.

   5. Copy the generated ISO image.

      ```bash
      cd kvm-multios
      cp ../Windows11-NoPrompt.iso guest_setup/ubuntu/unattend_win11/windowsNoPrompt.iso
      ```

#### 3. Prepare the Windows 11 OS patch 26100.7922

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
   # Copy KB5043080
   cp windows11.0-kb5043080-x64_953449672073f8fb99badb4cc6d5d7849b9c83e8.msu ./guest_setup/ubuntu/unattend_win11/windows-updates_01.msu
   # Copy KB5077241
   cp windows11.0-kb5077241-x64_739bca934f7f45038f9752637f632afa52c35f75.msu ./guest_setup/ubuntu/unattend_win11/windows-updates_02.msu
   ```

#### 4. Prepare the Intel Graphics driver

1. Download the driver package:

   [win64.zip](https://www.intel.com/content/www/us/en/secure/design/confidential/software-kits/kit-details.html?kitId=915334)

2. Copy the driver package to the `unattend_win11` folder:

   ```bash
   mkdir install
   sudo cp win64.zip install
   cd install/
   unzip win64.zip
   rm win64.zip
   cd ..
   zip -r Driver-Release-64-bit.zip ./install
   cd ~/kvm-multios
   # Copy and rename the graphics driver
   cp ~/Driver-Release-64-bit.zip \
      ./guest_setup/ubuntu/unattend_win11/Driver-Release-64-bit.zip
   ```

#### 5. Prepare the Intel Graphics SR-IOV ZeroCopy driver

1. Download the driver package required for GPU virtualization:

   [ZCBuild_\*_Installer.zip](https://www.intel.com/content/www/us/en/download/861056/display-virtualization-drivers-for-panther-lake-h.html)

2. Copy the driver package to the `unattend_win11` folder:

   ```bash
   cd ~/kvm-multios
   # Copy the ZeroCopy driver
   cp ~/ZCBuild_*_Installer.zip \
   ./guest_setup/ubuntu/unattend_win11/ZCBuild_MSFT_Signed_Installer.zip
   ```

### Create the guest Windows 11 VM image

#### Start automated creation of Windows 11 VM

```bash
# Start Windows 11 VM automated installation
./guest_setup/ubuntu/win11_setup.sh -p client --force --viewer
```

Once the process has finished, the VM image will be located in
`/var/lib/libvirt/images/window11.qcow2`.
The image must be copied to an appropriate host machine with SR-IOV support.

#### (Optional) Customize disk size for Windows VM

The default storage size of the Windows VM is 60 GiB. To customize the disk size,
add the `--disk-size` option. Replace `100` with your desired disk size in GiB:

```bash
# Example: Create Windows VM with 100 GiB disk
./guest_setup/ubuntu/win11_setup.sh -p client --force --viewer --disk-size 100
```

For more details, refer to
[the Windows VM installation guide](https://github.com/intel/kvm-multios/blob/v0.19.0/documentation/windows_vm.md).

You can use the virtual machine on [Edge Microvisor Toolkit host](../emt-installation-howto.md).

