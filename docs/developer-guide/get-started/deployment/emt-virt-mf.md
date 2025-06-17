# Deploying Edge Microvisor Toolkit using EMT VIRT Guest Virtual Machines

## Android

### Setup Android VM

#### Prerequisites

**Build Prerequisites**

- A 64-bit development workstation running Ubuntu* 22.04 (Jammy Jellyfish) operating system.
- Python supported version is 3.6+. This is mainly to be aligned with the latest 
repo command released by Google
- Around 350GB of free disk space on your workstation is required to checkout
the source code and to store the build artifacts.

**Celadon Development Environment Setup**

1.  Create a local bin/ directory, download the repo tool to that directory, and make 
the binary executable with the following commands:

```bash
 mkdir -p ~/bin
$ curl https://storage.googleapis.com/git-repo-downloads/repo > 
~/bin/repo
$ chmod a+x ~/bin/repo
$ export PATH=~/bin:$PATH
```

2. Install the following required packages on your 64-bit Ubuntu 22.04 LTS 
development workstation prior to the compilation

```bash
 sudo apt-get update
$ sudo apt-get install -y wget openjdk-8-jdk git ccache \
 automake lzop bison gperf build-essential zip curl \
 zlib1g-dev g++-multilib python3-networkx \
 libxml2-utils bzip2 libbz2-dev libbz2-1.0 \
 libghc-bzlib-dev squashfs-tools pngcrush \
 schedtool dpkg-dev liblz4-tool make optipng maven \
 libssl-dev bc bsdmainutils gettext python3-mako \
 libelf-dev sbsigntool dosfstools mtools efitools \
 python3-pystache git-lfs python-is-python3 flex clang \
 libncurses5 fakeroot ncurses-dev xz-utils cryptsetup-bin \
 apt-transport-https ca-certificates curl lsb-release \
 rsync vim python-six kmod glslang-tools \
 software-properties-common cpio python3-pip ninja-build \
 cutils cmake pkg-config xorriso mtools libjson-c-dev file
$ sudo pip3 install meson==0.60.0 mako==1.1.0 dataclasses 
pycryptodome ply==3.11
```

3. Setup git config which is required for ‘repo init’ on build server.

```bash
# Setup git config with your name and email ID. Add proxy 
settings if behind a firewall
$ cd /home/$USER
$ vi /home/$USER/.gitconfig
# Append below lines to .gitconfig file
[user]
email = <your email>
name = <your name>
[http]
proxy = <http_proxy>
[https] 
proxy = <https_proxy>
```

**Celadon Source Requirements**

`Vertical_RPL_SRIOV_CIV_WW2445_EXT.xml` from release package [RPL-S_RPL-SR_KVM_MultiOS.zip](https://www.intel.com/content/www/us/en/secure/design/confidential/software-kits/kit-details.html?kitId=839117)

**Build Celadon from Source**

1. Initialize the repository and sync Celadon source workspace:

```bash
# Init with the default manifest
$ repo init -u https://github.com/projectceladon/manifest.git
# Copy RPL CIV manifest and use it
$ cp <source path>/Vertical_RPL_SRIOV_CIV_WW2445_EXT.xml 
.repo/manifests/
$ repo init -m Vertical_RPL_SRIOV_CIV_WW2445_EXT.xml
# Sync the code and setup
$ repo sync -c -j16
$ repo forall -c git lfs pull
```

> **Note:** Depending on network conditions, the sync time may take several hours.

2. Build Android CIV release:

```bash
# Perform the environment setup from directory where repo is 
initialized
$ source build/envsetup.sh
# Select userdebug variant
$ lunch caas-userdebug
# Start the build
$ make flashfiles BASE_LTS2020_YOCTO_KERNEL=true -j16
```
3. Find the required output files for use in setup.

```bash
# Get location of CIV build output
$ find pub -name caas-releasefiles*.tar.gz
pub/caas/userdebug/caas-releasefiles-userdebug.tar.gz
```

4. Copy the packaged caas-releasefiles-userdebug.tar.gz file to the host. 

#### Host setup

**Host OS Hardening**

Users of Celadon-in-VM (CIV) release must ensure that Celadon platform host OS 
hardening measures are in place to ensure that the host OS could be treated as part 
of the secure computing base. This is essential to ensuring CIV security could be 
trusted in CIV operations.
For Celadon Host OS hardening recommendations see [this document](https://projectceladon.github.io/celadon-documentation/getting-started/host-os￾hardening.html)

**Add Celadon Guest VM Support to RPL Host OS**

1. Copy caas-releasefiles-userdebug.tar.gz to the host

```bash
# Copy the artifact
$ cp caas-releasefiles-userdebug.tar.gz /home/$USER
```

2. Extract the package. 

```bash
# Extract files
$ cd /home/$USER
$ tar xzvf caas-releasefiles-userdebug.tar.gz
```

3. Run the host setup. 

```bash
# Update the host
$ sudo -E ./scripts/setup_host.sh
```

4. After the setup has completed, reboot the host. 

```bash
$ sudo reboot
```

#### Creating Android VM Image

Create Android CIV image for running as VM on the Raptor Lake target.

```bash
# Change directory
$ cd /home/$USER
# Generate CIV disk image from caas-flashfiles.
# The script and flashfiles have already been extracted from 
caas-releasefiles-userdebug.tar.gz
# Wait for "Flashing is completed" msg from script.
$ sudo -E ./scripts/start_flash_usb.sh caas-flashfiles￾xxxxx.zip --display-off
```

### Running Android VM

## Yocto

### Setup Yocto VM 

#### Prerequisites

**Build Yocto Project Image**

Refer to “Yocto Project*-based Board Support Package for 13th Gen Intel® Core™ 
Processors and Intel® Core™ Processors (14th Gen) for Edge Platforms Get Started 
Guide” document #788647 for prerequisites to build Yocto Project* - based BSP for 
RPL platform

**Copy Yocto Project Image**

After the Yocto build has completed,rename the output image to yocto.wic and 
copy it to the target RPL platform.

```bash
$ cd ./build/tmp-x86-glibc/deploy/images/intel-corei7-64/
$ sudo mv core-image-sato-sdk-intel-xxxx.wic 
/home/$USER/yocto.wic
```

**Make Separate Copy of OVMF**

Create a separate copy of OVMF for Yocto Project* VM use.

```bash
# Make a copy of OVMF for Yocto guest
$ ln -sf ovmf/OVMF_CODE.fd OVMF_CODE.fd
$ cp ovmf/OVMF_VARS.fd OVMF_VARS_yocto.fd
```

### Running Yocto VM

## Windows 10

### Setup Windows 10 VM 

#### Prerequisites

**Windows Installation Image Required**

Download the Windows 10 IOT Enterprise version 21H2 iso image, save it as windows.iso and copy it to the host

**Installation Script Required**

Use the script `ubuntu_kvm_multios_scripts.zip` 
from the release package [RPL-S_RPL-SR_KVM_MultiOS.zip](https://www.intel.com/content/www/us/en/secure/design/confidential/software￾kits/kit-details.html?kitId=839117)

#### Creating Windows VM Image

**Create Windows VM Image from ISO**

1. Create an empty Windows Guest VM image file along with the Windows OVMF 
files. 

```bash
$ cd /home/$USER/
$ qemu-img create -f qcow2 win.qcow2 80G
$ ln -sf ovmf/OVMF_CODE.fd OVMF_CODE.fd
$ cp ovmf/OVMF_VARS.fd OVMF_VARS_windows.fd
```

2. Run install_windows.sh to start Windows guest installation. 

```bash
# Start guest VM to install Windows
$ cd /home/$USER/
$ sudo ./install_windows.sh 
```

> **Note:** f you miss the “Press Any Key” message, press ESC key until you reach the EFI shell prompt, then type “reset” to start over again.

3. Follow the Windows installation steps until you see the Windows Setup screen. 
Select “Windows 10 IoT Enterprise LTSC” option.

4. Select "Custom: Install Windows only (advanced)".

5. Select "Drive 0 Unallocated Space” and click Next.

6. Follow the Windows installation steps as usual, and Windows will be installed to 
win.qcow2.

7. Once the installation is done, disable the automatic updates temporarily with the 
following steps:

  a. Open Settings.
  b. Click on Update & Security.
  c. Click on Windows Update. 
  d. Click the Pause updates for 7 days button.

8. Shut down the Windows guest

> **Note:** Remember to shut down the Windows Guest properly. 

#### Prepare Windows* Guest VM for SR-IOV Zero Copy

**Launch Windows Guest VM and Install Drivers**

1. From Ubuntu GUI, launch Windows guest VM with start_windows.sh. 

```bash
# Start guest VM to install Windows drivers
$ cd /home/$USER/ 
$ sudo ./start_windows.sh
```
**Install Windows 10 Cumulative Update**

1. Download ‘2024-05 Cumulative Update for Windows 10 Version 21H2 for x64-
based Systems [KB5037768](https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2024/05/windows10.0-kb5037768-x64_a627ecbec3d8dad1754d541b7f89d534a6bdec69.msu)

2. Double-click the msu file to install.

3. Reboot the Windows Guest VM after successful installation. 

4. Open a command prompt in administrator mode and enter “winver” to check the 
version. It should show 21H2 OS Builds 19044.4412.

**Install Graphics GFX Driver**

1. Download Intel® Graphics Driver Production Driver Version 101.5972 for IOTG 
Raptor Lake Virtualization Designs Only [GFX-prod-hini-releases_24ww30-ci-master-17071-osnext-pr-1015972-ms-attestation-sign-832-RPL-Rx64_v1.zip](https://www.intel.com/content/www/us/en/secure/design/confidential/software-kits/kit-details.html?kitId=837935)

2. Use File Explorer to extract the zip file

3. Navigate into the install folder and double click on installer.exe to launch the 
installer. 

4. Click the Begin installation button.

5. After the installation has completed, rebootthe Windows guest VM.

6. Launch the Device Managerto check the installation.

7. Expand the Display adapters item in the device list as shown in Figure 2.

8. Right-click on the graphics device and select Properties. Click Drivertab. Check 
that the Intel® Graphics version is 32.0.101.5972 shown in Figure 3.

> **Note:** If you see the yellow triangle with exclamation, please install the driver manually by selecting the 32.0.101.5972 version. (Right-click to update the driver and select the 
option to point to the main installation directory.)

**Prepare SR-IOV Zero Copy Driver**

1. Download Windows Zero Copy Drivers Release 1716 [DVServer, DVServerKMD] [ ZCBuild_1716_MSFT_Signed_Installer.zip](https://www.intel.com/content/www/us/en/download/837886/display-virtualization-drivers-for-display-virtualization-drivers-for-alder-lake-s-beta-raptor-lake-ps-mr1-raptor-lake-sr-mr3-raptor-lake-s-mr5-raptor-lake-p-mr3-alder-lake-n-mr6-alder-lake-ps-mr7.html)

Please make sure the correct ZCBuild version is chosen from the drop-down. By
default, the latest ZCBuild version will be the first one.

2. Use File Explorer to extract the zip file.

**Install SR-IOV Zero Copy Driver Using GUI Installer**

The SR-IOV Zero Copy Driver can be installed either with the GUI installer or through 
the command line. This section describes the steps for the GUI installer.

1. Go to the directory containing ZeroCopyInstaller.

2. Double-click to run ZeroCopyInstaller.

3. Click on the Install button when prompted.

4. Once the installation has completed, click on the Finish button to restart 
Windows.

**Install SR-IOV Zero Copy Driver Using Command Line**

The SR-IOV Zero Copy Driver can be installed either with the GUI installer or through
the command line. This section describes the steps to install it using command line.

1. Open Powershell in administrator mode.

2. Go to the directory containing ZeroCopyInstaller.

3. Enter the following to perform the installation.

```shell
C:\> .\ZeroCopyInstaller.exe /VERYSILENT /SUPPRESSMSGBOXES
```

> **Note:** Option usage details:
    - `/VERYSILENT` Runs silently without displaying windows
    - `/SUPPRESSMSGBOXES` Suppresses message boxes from displaying
    - `/NORESTART` Avoids restarting the system after installation.

4. Wait forthe Windows guest to automatically restart.

**Check SR-IOV Zero Copy Driver Installation**

1. Launch the Device Managerto check the installation.

2. Expand the Display adapters item in the device list as shown in Figure 4.

3. Right-click on the DVServerUMD device and select Properties. Switch to the
Drivertab. Check that the DVServerUMD Device Driver version is 4.0.0.1716 as 
shown in Figure 5.

4. In Device Manager, expand the System devices item in the device list as shown in 
Figure 6.

5. Right-click on the DVServerKMD device and select Properties. Switch to the 
Drivertab. Check that the DVServerKMD Device Driver version is 4.0.0.1716 as 
shown in Figure 7.

6. Start Task Manager and check that the GPU status is active as shown in Figure 8. 

### Running Windows 10 VM

## Ubuntu

### Setup Ubuntu VM 

### Running Ubruntu VM