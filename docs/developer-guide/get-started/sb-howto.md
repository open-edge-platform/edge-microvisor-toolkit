# Enable Secure Boot for Edge Microvisor Toolkit

In most production scenarios, you should consider using Secure Boot for your system, ensuring
it is protected against advanced attacks. Here are the steps required to do so, using:

- [ISO Image](#iso-image) - manually sign extensible firmware interface (EFI) binaries,
  generating local signing certificates, rebuilding packages, and testing the secure boot
  functionality.
- [RAW or VHD/X](#raw-and-vhd-image) - configure BIOS with signed production keys of
a RAW/VHD Edge Microvisor image.

## RAW and VHD Image

Production images of Edge Microvisor are signed by Intel. Secure Boot prevents
unauthorized bootloaders and operating systems from starting, ensuring that only
code signed with a trusted key is executed. For custom signed OS images, you need
to enroll your certificate into the firmware’s trusted key database.

### Step 1: Verify your Certificate File

Make sure you have the certificate file, for example, `edge-readonly-3.0.20250401.0515-signed.der`,
which contains your public key. Many systems accept DER format, but some firmware might
require PEM.

### Step 2: Convert DER to PEM (if necessary)

Although DER is a common format for many BIOS implementations, some UEFI/BIOS
systems may require PEM format. To convert a DER file to PEM using OpenSSL:

Open a Terminal/Command Prompt. Run the following command:

```bash
openssl x509 -in certificate.der -inform DER -out certificate.pem -outform PEM
```

This converts `certificate.der` into PEM-formatted file `certificate.pem`.

### Step 3: Enroll the Certificate in the UEFI/BIOS

- Restart Your Computer:
  - Enter your UEFI/BIOS setup by pressing F2, Del, or Esc during startup (refer to your
    system's manual if needed).
- Navigate to the *Secure Boot* or *Security* Section:
  - Look for a menu labeled *Secure Boot*, *Security*, or similar.
- Enroll the Custom Key:
  - Find the key/certificate management option such as *Manage Keys*, *Enroll Key*, or
    *Add Certificate*.
  - Choose the file selection option and locate your certificate file (use `certificate.der`
    or `certificate.pem` depending on your firmware requirements).
  - Follow the on-screen instructions to enroll the key.

### Step 4: Enable Secure Boot

- Locate the Secure Boot Setting:
  - Within the UEFI/BIOS menu, find the *Secure Boot* option.
- Enable Secure Boot:
  - Change the setting to *Enabled*.
  - Save your changes and exit the UEFI/BIOS setup.
- Reboot:
  - Your system will now check the OS image signature against the enrolled certificate
    during boot.

## ISO Image

### Prerequisites

**Make sure Secure Boot is disabled.**

**Install Required Tools** for signing and building packages:

```bash
sudo tdnf install dnf-utils pesign nss-tools efivar rpmdevtools openssl kernel-devel keyutils dos2unix vim-extra
```

**Add User to the pesign Group**:

```bash
sudo usermod -a -G pesign $(whoami)
```
```bash
cd ~
```

Log out and log back in for the changes to take effect.

### Step 1: Generate Local Signing Certificates

Complete the following steps to create local self-signed certificates:

**Download the pesign source package**:

```bash
base_url=$(grep -E '^\s*baseurl' /etc/yum.repos.d/*.repo | awk -F= '{print $2}' | sed 's/^[ \t]*//')

package=$(tdnf repoquery --source pesign | tail -1)
wget $base_url/SRPMS/$package.rpm

mkdir pesign-files
rpmdev-extract -C pesign-files pesign-*.src.rpm
cd pesign-files/pesign-*.src
tar xvf pesign-*.tar.bz2
cd pesign-*/src/certs
```

**Create a self-signed CA and a signing certificate**:

```bash
export KEY=KeyInShim

./make-certs $KEY emt@edgemicrovisortoolkit.com all codesign 1.3.6.1.4.1.311.10.3.1

certutil -d /etc/pki/pesign -A -n 'my CA' -t CT,CT,CT -i ca.crt
pk12util -d /etc/pki/pesign -i $KEY.p12
certutil -d /etc/pki/pesign -A -i $KEY.crt -n $KEY -t u
```

Repeat the steps for additional keys, such as `KeyInDB`.

```bash
export KEY=KeyInDB
# Repeat the steps.
```

```bash
cd ~
```
Make sure your rpm %_topdir is ~/rpmbuild; if not you should edit your ~/.rpmmacros to include:

```bash
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
%_topdir %(echo $HOME)/rpmbuild
```
If file ~/.rpmmacros does not exist in home directory, create one:
```bash
vi ~/.rpmmacros
```

### Step 2: Rebuild the shim-unsigned Package

**Extract KeyInShim to a DER file**:

```bash
certutil -d /etc/pki/pesign -L -n KeyInShim -r > ~/key-in-shim.der
```

**Rebuild the shim-unsigned package**:

```bash
base_url=$(grep -E '^\s*baseurl' /etc/yum.repos.d/*.repo | awk -F= '{print $2}' | sed 's/^[ \t]*//')

shim_unsigned_package=$(tdnf repoquery --source shim-unsigned-x64 | tail -1 | sed 's/\.src$//')
wget $base_url/SRPMS/$shim_unsigned_package.src.rpm

rpm -i $shim_unsigned_package.src.rpm
cd ~/rpmbuild
cp ~/key-in-shim.der SOURCES/azurelinux-ca-20230216.der
rpmbuild -bb SPECS/shim-unsigned-x64.spec
sudo tdnf install RPMS/x86_64/$shim_unsigned_package.x86_64.rpm
```
```bash
cd ~
```

### Step 3: Build the shim Package

**Install the shim SRPM**:

```bash
base_url=$(grep -E '^\s*baseurl' /etc/yum.repos.d/*.repo | awk -F= '{print $2}' | sed 's/^[ \t]*//')

shim_package=$(tdnf repoquery --source shim | grep -v "unsigned" | tail -1 | sed 's/\.src$//')
wget $base_url/SRPMS/$shim_package.src.rpm

rpm -i $shim_package.src.rpm
```

**Sign the binaries**:

```bash
cd ~/rpmbuild
pesign -s -i /usr/share/shim/*/x64/mmx64.efi -o SOURCES/mmx64.efi -c KeyInShim --force

pesign -s -i /usr/share/shim/*/x64/fbx64.efi -o SOURCES/fbx64.efi -c KeyInShim --force

pesign -s -i /usr/share/shim/*/x64/shimx64.efi -o SOURCES/shimx64.efi -c KeyInDB --force
rpmbuild -bb SPECS/shim.spec
```

### Step 4: Install the new shim-x64 Package

Install the new package and reboot with secure boot disabled:

```bash
sudo tdnf install RPMS/x86_64/$shim_package.x86_64.rpm
```
Ensure that the `$shim_package.x86_64.rpm` package is installed properly. If you encounter any messages, such as "Nothing to do", you can attempt to reinstall the package.

```bash
sudo tdnf reinstall --allowerasing RPMS/x86_64/$shim_package.x86_64.rpm
```

```bash
cd ~
```


### Step 5: Sign the Boot Loader and Kernel

**Copy the EFI binaries**:

```bash
sudo cp /boot/efi/EFI/BOOT/grubx64.efi .
sudo sh -c 'cp /boot/vmlinuz-* .'
```

**Sign the binaries**:

```bash
sudo pesign -s -i grubx64.efi -o /boot/efi/EFI/BOOT/grubx64.efi -c KeyInShim --force

udo sh -c 'pesign -s -i vmlinuz-* -o /boot/vmlinuz-* -c KeyInShim --force'
```

### Step 6: Enroll KeyInDB into UEFI DB

**Export KeyInDB to a DER file**:

```bash
certutil -d /etc/pki/pesign -L -n KeyInDB -r > key-in-db.der
```

**Copy the certificate to the ESP partition**:

```bash
sudo cp key-in-db.der /boot/efi/EFI/
```

**Add the certificate to the UEFI DB**:

```bash
sudo systemctl reboot --firmware-setup
```

Navigate to:

System Bios Settings → System Security → Secure Boot Configuration → Secure Boot Mode (set to `<Custom Mode>`).

Custom Secure Boot Options → DB Options → Enroll Signature → Enroll Signature Using `key-in-db.der` file into the database.

### Step 7: Enable Secure Boot and Test

Re-enable secure boot in the firmware menu and reboot. Verify that the system boots successfully with secure boot enabled.

