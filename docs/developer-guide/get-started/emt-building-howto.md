# Build Your Own Edge Microvisor Toolkit

Edge Microvisor Toolkit is an operating system derived from Azure Linux. It is composed of multiple modules to
facilitate creating `rpm` based OS images supporting a variety of different image formats.

The toolkit has an `imageconfig` construct in the JSON format that defines the characteristics
of the resulting image, such as:

- Type and size of partitioning table.
- Partitions, their types (such as EFI, rootfs, etc.), settings, file system, and size.
- Reference to `packagelists` which defines what packages (i.e. `rpms`) should be included in
  the image.
- Additional configuration files that should be embedded in the image (e.g. network-, systemd
  configurations).
- Any required post-installation scripts that should be executed once the image has been
  generated.
- Kernel and command line options.
- Final configuration properties that should be applied (e.g. enable full disc encryption,
  immutable image, second stage bootloader provider, purge documentation etc.).

## Build the Toolchain

Before you can build OS images you need to build the toolchain and make sure to
[**install pre-requisites (Ubuntu)**](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/toolkit/docs/building/prerequisites-ubuntu.md).

> **Note:**
  Use the *stable* tag instead of *latest* for building the OS images with prebuilt packages.
  This is the recommended approach, as building the **entire toolchain** may take a lot of
  time. Adding the `REBUILD_TOOLCHAIN=y` parameter to the `make` command rebuilds
  the entire toolchain.


1. Clone the stable branch of the Edge Microvisor Toolkit repository.

   Check the [tags](https://github.com/open-edge-platform/edge-microvisor-toolkit/tags) for
   the `<stable_tag_name>`.

   ```bash
   git clone https://github.com/open-edge-platform/edge-microvisor-toolkit --branch=<stable_tag_name>
   ```

2. Navigate to the `toolkit` subdirectory.

   ```bash
   cd edge-microvisor-toolkit/toolkit
   ```

3. Build the tools.

   ```bash
   sudo make toolchain REBUILD_TOOLS=y
   ```

## Build the Edge Microvisor Toolkit Image

Multiple image configurations are located in the `imageconfigs` folder:

```bash
microvisor/
├── docs/
├── LICENSES-AND-NOTICES/
├── SPECS/
├── SPECS-EXTENDED/
├── SPECS-SIGNED/
└── toolkit/
    ├── docs/
    └── imageconfigs/
      ├── edge-image-dev.json
      ├── edge-image-rt-dev.json
      ├── edge-image-rt.json
      ├── edge-image.json
      ...
      └──
  ...
```

Different image types can be built by using different JSON config files and parameters.
You can find more information about specific parameters [here.](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/toolkit/docs/building/building.md#local-build-variables)

To build an ISO image, run the following command:

```bash
sudo make iso -j8 REBUILD_TOOLS=y REBUILD_PACKAGES=n CONFIG_FILE=./imageconfigs/full.json
```

To build a RAW image without real-time extensions, run the following command:


```bash
sudo make image -j8 REBUILD_TOOLS=y REBUILD_PACKAGES=n CONFIG_FILE=./imageconfigs/edge-image.json
```

To build a RAW image with real-time extensions, use the following command:

```bash
sudo make image -j8 REBUILD_TOOLS=y REBUILD_PACKAGES=n CONFIG_FILE=./imageconfigs/edge-image-rt.json
```

## Customize Your Edge Microvisor Toolkit Image

To add packages to the default image, you can define your own `packagelist.json` file, pointing to RPMs that should be included in the image.
To streamline this process, you can use the `add_custom_packages.sh` script located in `toolkit/scripts`.
This script helps generate a `custom-packages.json` file and updates an existing imageconfig JSON file.
The `edge-image.json` file points to multiple `packagelist` files, located under `imageconfigs/packagelists`.
The same `rpms` may be included in an `imageconfig` file through the `packagelist` files.

The resulting image will include the set of all `rpms` specified within the array of
`packagelist` files from the `imageconfig`.

### Example 1: Adding an existing RPM (Nano)

Note that you can only add the packages for which SPEC files exist. To add `nano` as an
alternative text editor to the image:

1. Use the script to create a custom package list file, for example `utilities.json`, and update an existing `imageconfig` JSON file, for example, `edge-image.json`.

   ```bash
   # Refer to this usage format:
   # Usage: ./add_custom_packages.sh "<pkg1 pkg2 ...>" path/to/image.json [custom-packages.json]

   # Run the script to add nano into the edge-image.json configuration.
   ./add_custom_packages.sh "nano" ../imageconfigs/edge-image.json utilities.json
   ```

   - `"<pkg1 pkg2 ...>"` - List names of packages to include. Keep them separated by spaces.
   - `path/to/image.json` - Specify the path to your `imageconfig` JSON file, for example, `../imageconfigs/edge-image.json`.
   - `[custom-packages.json]` - Optionally, provide a name for the custom package list file. If omitted, the default `custom-packages.json` name will be used.

2. After running the script, your `imageconfig` JSON file (e.g., `edge-image.json`) will include the custom package list you specified. You can also create a new file and add it to the `imageconfigs` folder. Before running `add_custom_packages.sh` to include your custom package list, make sure that the `PackageLists` section exists in the `imageconfig` JSON file.

   ```bash
   # Edit the edge-image.json file. Add the default login account for testing.
   ...
   "PackageLists": [
     "packagelists/core-packages-image-systemd-boot.json",
     "packagelists/ssh-server.json",
     "packagelists/virtualization-host-packages.json",
     "packagelists/agents-packages.json",
     "packagelists/tools-tinker.json",
     "packagelists/persistent-mount-package.json",
     "packagelists/fde-verity-package.json",
     "packagelists/selinux-full.json",
     "packagelists/intel-gpu-base.json",
     "packagelists/os-ab-update.json",
     "packagelists/utilities.json"
   ],
   "Users": [
     {
         "Name": "user",
         "Password": "user"
     }
   ],
   ...
   ```

3. Rebuild the image:

   ```bash
   sudo make image -j8 REBUILD_TOOLS=y REBUILD_PACKAGES=n CONFIG_FILE=./imageconfigs/edge-image.json
   ```

### Example 2: Adding a new RPM package

To add a new package you need to generate for the package a SPEC file containing
all information required for the build infrastructure to generate `SRPM` and `RPM`
for the package. There are a few steps involved in creating a new package for Edge Microvisor Toolkit.

**Prerequisites**

Make sure you have the required build tools for `rpm`.
On Fedora, you can simply install the required packages with:

```bash
sudo dnf install rpm-build rpmdevtools
rpmdev-setuptree
```

where `rpmdev-setuptree` creates the necessary directories.

On Ubuntu, use the following command:

```bash
sudo apt-get install rpm
```

**Preparing the files**

1. Manually create the necessary directories:

   ```bash
   mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
   echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
   ```

2. Navigate to user home directory and create your SPEC file:

   ```bash
   cd
   touch helloworld.spec
   ```

3. Open the spec file using the method of your choice, for example:

   ```bash
   nano helloworld.spec
   ```

   Copy the example below into the file.
   It will create a simple hello world RPM package, which will include a bash script that
   prints *"Hello, world!"*.

   ```bash
   Name:           helloworld
   Version:        1.0
   Release:        1%{?dist}
   Summary:        Simple Hello World script

   License:        MIT
   URL:            https://example.com/helloworld
   Source0:        helloworld-1.0.tar.gz

   BuildArch:      noarch

   %description
   A very basic "Hello, world!" script packaged as an RPM.

   %prep
   %setup -q

   %build
   # Nothing to build for a shell script

   %install
   mkdir -p %{buildroot}/usr/bin
   install -m 0755 helloworld.sh %{buildroot}/usr/bin/helloworld

   mkdir -p %{buildroot}/usr/share/helloworld
   install -m 0644 helloworld.signature.json %{buildroot}/usr/share/helloworld/

   %files
   /usr/bin/helloworld
   /usr/share/helloworld/helloworld.signature.json

   %changelog
   * Wed May 01 2025 Your Name <you@example.com> - 1.0-1
   - Initial package
   ```

4. Create the simple script and make it executable.

   ```bash
   mkdir -p ./helloworld-1.0
   cat > ./helloworld-1.0/helloworld.sh <<'EOF'
   #!/bin/bash
   echo "Hello, world!"
   EOF
   chmod +x ./helloworld-1.0/helloworld.sh
   ```

**Create the source archive and generate the sha256sum for the package.**

1. Compute the SHA-256 and generate the JSON signature for it.

   ```bash
   sum=$(sha256sum ./helloworld-1.0/helloworld.sh | awk '{print $1}')
   cat > ./helloworld-1.0/helloworld.signature.json <<EOF
   {
     "file": "helloworld.sh",
     "sha256": "$sum"
   }
   EOF
   ```

2. Create the tarball archive and generate its JSON signature.

   ```bash
   tar -czf helloworld-1.0.tar.gz ./helloworld-1.0
   sum=$(sha256sum helloworld-1.0.tar.gz | awk '{print $1}')
   cat > helloworld-1.0.tar.gz.signature.json <<EOF
   {
     "file": "helloworld-1.0.tar.gz",
     "sha256": "$sum"
   }
   EOF
   ```

3. Copy the RPM package files to the building directories and build it.

   ```bash
   cp helloworld-1.0.tar.gz ./rpmbuild/SOURCES
   cp helloworld.spec ./rpmbuild/SPECS
   rpmbuild -ba ./rpmbuild/SPECS/helloworld.spec
   ```

**Adding the package**

1. Create the `helloworld` folder in the `edge-microvisor-toolkit/SPECS` directory.

   ```bash
   mkdir ./edge-microvisor-toolkit/SPECS/helloworld
   ```

2. Copy the `helloworld.spec` and `helloworld.signature.json` files to the
   `helloworld` folder.

   ```bash
   cp ./helloworld.spec ./edge-microvisor-toolkit/SPECS/helloworld
   cp ./helloworld-1.0/helloworld.signature.json ./edge-microvisor-toolkit/SPECS/helloworld
   ```

3. Finally, update the `cgmanifest` by using the provided `python` script.

   ```bash
       cd ./edge-microvisor-toolkit/toolkit
       python3 -m pip install -r ./scripts/requirements.txt
       python3 ./scripts/update_cgmanifest.py first ../cgmanifest.json ../SPECS/helloworld.spec
   ```

**Building the package and testing it locally**

1. Build your package by running the following command:

   ```bash
   make build-packages # to rebuild the packages
   ```

2. Build the image containing the package by following the steps outlined in [Building the Edge Microvisor Toolkit Image](#build-the-edge-microvisor-toolkit-image), and pointing to your modified imageconfig file.