# Build an Edge Microvisor Toolkit Image

Edge Microvisor Toolkit is a downstream of Azure Linux. It is composed of multiple modules to
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
   cd ./toolkit
   sudo make toolchain REBUILD_TOOLS=y
   ```

## Building the Default Microvisor Image

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

To build the default microvisor image based on its `imageconfig` file, run the following
command:

```bash
sudo make image -j8 REBUILD_TOOLS=y REBUILD_PACKAGES=n CONFIG_FILE=./imageconfigs/edge-image.json
```

## Customizing an Image

To add packages to the default image, you can define your own `packagelist.json` file,
pointing to `rpms` that should be included in the image. The `edge-image.json` file points to
multiple `packagelist` files, located under `imageconfigs/packagelists`. The same `rpms` may
be included in an `imageconfig` file through the `packagelist` files.

The resulting image will include the set of all `rpms` specified within the array of
`packagelist` files from the `imageconfig`.

### Example 1: Adding an existing RPM (Nano)

Note that you can only add the packages for which SPEC files exist. To add `nano` as an
alternative text editor to the image:

1. Define a new JSON file.

   ```bash
   # Create a new packagelist called utilities.json
   cat <<EOF > ./imageconfigs/packagelists/utilities.json
   {
       "packages": [
           "nano"
       ]
   }
   EOF
   ```

2. Include it in an existing `imageconfig` JSON file, for example `edge-image.json`.
   You can also create a new file and add it to the `imageconfigs` folder.

   ```bash
   # Edit the edge-image.json file. Add the custom packagelist and default login account for testing.
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

To add a new package you need to generate a SPEC file for the package which
contains all required information for the build infrastructure to generate the
`SRPM` and `RPM` for the package. There are a few steps involved in creating
a new package for Edge Microvisor Toolkit.

1. Create a folder, define the SPEC file and add it into the `/SPECS` directory.
2. Create the source archive and generate the sha256sum for the package.
3. Update the `cgmanifest.json` file.
4. Build an image with the package included and test locally.
5. Upload the tar.gz package to the source package repository after is has been tested locally.

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

Then, manually create the necessary directories:

```bash
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
```

**Preparing the files**

1. Navigate to user home directory.

   ```bash
   cd
   ```

2. Define the SPEC file, using the example below.

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

3. Create the simple script and make it executable.

   ```bash
   mkdir -p ./helloworld-1.0
   cat > ./helloworld-1.0/helloworld.sh <<'EOF'
   #!/bin/bash
   echo "Hello, world!"
   EOF
   chmod +x ./helloworld-1.0/helloworld.sh
   ```

4. Compute its SHA-256 and generate the JSON signature for it.

   ```bash
   sum=$(sha256sum ./helloworld-1.0/helloworld.sh | awk '{print $1}')
   cat > ./helloworld-1.0/helloworld.signature.json <<EOF
   {
     "file": "helloworld.sh",
     "sha256": "$sum"
   }
   EOF
   ```

5. Create the tarball archive and generate its JSON signature.

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

4. Copy the RPM package files to the building directories and build it.

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

**Local Build and Testing**

If testing is complete and you are ready to contribute this package,
please raise a PR and work with a code owner to upload the source tarball to package source mirror.

```bash
make build-packages # to rebuild the packages
```

Follow the steps under [Customizing an image](./emt-building-howto.md#Customizing-an-Image) to create
an image with your new package.

**Uploading the archive**

Intel will upload the tar.gz archive to the mirror.

### Update an agent

To add or update an existing BMA (Bare metal agent) from the Edge Management
Framework, follow these steps.

1. If a new package has to be released, follow these steps to ensure the package
   is available in the artifactory:

    a. Checkout the tag for your agent which has to be released.
    b. cd into your agent's directory.
    c. Invoke `make tarball`.
    d. Upload tarball from `build/artifacts` to the tarball repository.

2. Update the respective .spec file in SPECS/`package` directory. Example: `SPECS/node-agent`.

3. Bump the release number declared in the top section of the .spec file if on the same
   version. Otherwise, update the release version and set the number to 1.

4. Update `env_wrapper.sh` and the .spec file if there are installation changes or new
   configurations to be added.

5. Update the changelog to ensure the version and release number are mentioned correctly as
   well. Example:

    ```bash
    * Tue Mar 25 2025 Andrea Campanella <andrea.campanella@intel.com> - 1.5.11-2
    - Move from RSTYPE to RS_TYPE in wrapper for node-agent
    ```

6. Generate sha256sum of all files that have been updated.
Example : `sha256sum ./SPECS/node-agent/env_wrapper.sh`

7. Update the signature file name `<agent-name>.signatures.json`. Example: `node-agent.signatures.json`.

8. Update `cgmanifest.json`. You can use a script to do it, if you have an RPM environment.
   Otherwise, update the version and download the URL manually. Example commands to update
   using a manifest:

    ```bash
    python3 -m pip install -r ./toolkit/scripts/requirements.txt
    python3 ./toolkit/scripts/update_cgmanifest.py first cgmanifest.json ./SPECS/node-agent/node-agent.spec
    ```
## Next

- Learn how to [Enable Secure Boot for Edge Microvisor Toolkit](emt-sb-howto.md).
- See the detailed description of how to [create a full build and customize it](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/toolkit/docs/building/add-package.md).
