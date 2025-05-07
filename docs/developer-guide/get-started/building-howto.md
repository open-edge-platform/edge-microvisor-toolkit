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
[**install pre-requisites (Ubuntu)**](/toolkit/docs/building/prerequisites-ubuntu.md).

The toolkit can use prebuilt packages for building the OS images. This is the recommended
approach, as building the *entire toolchain* may take a lot of time. Adding the
`REBUILD_TOOLCHAIN=y` parameter to the `make` command rebuilds the entire toolchain.

```bash
# Clone the repository
git clone <Microvisor git repo>
cd <Microvisor repo>

# Checkout stable branch of Microvisor
git checkout <latest stable>

# Build the tools
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

To add packages to the default image, you can define your own `packagelist.json`  file,
pointing to `rpms` that should be included in the image. The `edge-image.json` file points to
multiple `packagelist` files, located under `imageconfigs/packagelists`. The same `rpms` may
be included in an `imageconfig` file through the `packagelist` files. The resulting image
will include the set of all `rpms` specified within the array of `packagelist` files from the
`imageconfig`.

### Example: Adding an existing RPM (Nano)

The following example shows how to add `nano` as an alternative text editor to the image.
You can add the packages for which `.spec` files already exist. Simply include them in an
existing `packagelist` file, or create a new one and add it to the `imageconfig`.

```bash
# Create a new packagelist called utilities.json
cat <<EOF > ./imageconfigs/packagelists/utilities.json
{
    "packages": [
        "nano"
    ]
}
EOF

# Edit the edge-image.json file to add custom packagelist and default login account for testing.
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

Then, rebuild the image:

```bash
sudo make image -j8 REBUILD_TOOLS=y REBUILD_PACKAGES=n CONFIG_FILE=./imageconfigs/edge-image.json
```
### Add a new package

To add a new package you need to generate a `SPEC` file for the package which
contains all required information for the build infrastructure to generate the
`SRPM` and `RPM` for the package. There are a few steps involved in creating
a new package for Edge Microvisor Toolkit.

1. Create a folder, define the SPEC file and add it into the `/SPECS` directory.
2. Create the source archive and generate the sha256sum for the package.
3. Update the `cgmanifest.json` file.
4. Build an image with the package included and test locally.
5. Upload the tar.gz package to the source package repository after is has been tested locally.

You need to first install the required build tools for `rpm`. On Fedora you
can simply install the required packages with:

```bash
sudo dnf install rpm-build rpmdevtools
rpmdev-setuptree
```

`rpmdev-setuptree` creates the necessary directories, which you may need to
manually create on an Ubuntu distribution.

```bash
sudo apt-get install rpm
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
```

**Defining the SPEC file**
Define the SPEC file and test that it works as expected and generates locally the required artifacts.
the required artifacts. This example builds a simple hello world `rpm` package
which contains a bash scripts that prints hello world.

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
A very basic "Hello World" script packaged as an RPM.

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

**Create the archive**: Create your source archive, add the simple script and
make it executable.

```bash
# 1. Make your source tree and tarball
mkdir -p ~/helloworld-1.0
cat > ~/helloworld-1.0/helloworld.sh <<'EOF'
#!/bin/bash
echo "Hello, world!"
EOF
chmod +x ~/helloworld-1.0/helloworld.sh

tar -czf helloworld-1.0.tar.gz helloworld-1.0/

# 2. Compute its SHA-256
sum=$(sha256sum helloworld-1.0.tar.gz | awk '{print $1}')

# 3. Write the JSON signature for the tarball
cat > helloworld-1.0.tar.gz.signature.json <<EOF
{
  "file": "helloworld-1.0.tar.gz",
  "sha256": "$sum"
}
EOF

```

Copy and build the `rpm` package to the rpm building directory.

```bash
cp helloworld-1.0.tar.gz ~/rpmbuild/SOURCES/
cp helloworld.spec ~/rpmbuild/SPECS/
rpmbuild -ba ~/rpmbuild/SPECS/helloworld.spec
```

**Adding the SPEC**: Add the `helloworld.spec` and the 'helloworld.spec.signature`
file to the `/SPECS` directory. Finally update the `cgmanifest` by using the
provided `python` script.

```bash
    python3 -m pip install -r ./toolkit/scripts/requirements.txt
    python3 ./toolkit/scripts/update_cgmanifest.py first cgmanifest.json ./SPECS/helloworld.spec
```

**Local Build and Testing**:  If testing is complete and you are ready to contribute this package,
please raise a PR and work with a code owner to upload the source tarball to package source mirror.

```bash
make build-packages # to rebuild the packages
```
Follow the steps under [Customizing an image](./building-howto.md#Customizing-an-Image) to create
an image with your new package.

**Uploading the archive**: Intel will upload the tar.gz archive to the mirror.

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

- Learn how to [Enable Secure Boot for Edge Microvisor Toolkit](sb-howto.md).
- See the detailed description of how to [create a full build and customize it](/toolkit/docs/building/add-package.md).
