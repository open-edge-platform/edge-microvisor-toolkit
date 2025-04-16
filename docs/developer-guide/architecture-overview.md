# Architecture Overview

Edge Microvisor Toolkit is an OS build pipeline based on
Azure Linux (as an RPM-based OS), designed to produce Linux OS images optimized for Intel®
platforms. This article provides an overview of the build infrastructure, as well as
architectural details of the OS itself.

## Edge Microvisor Toolkit

Edge Microvisor Toolkit is produced and maintained in several versions, in both immutable and
mutable images. It enables users to quickly deploy and run their workloads on Intel®
platforms, offering quick solutions to multiple scenarios. Currently, it is deployed as:

- ISO installer with a mutable image using GRUB as the second-stage bootloader.
- ISO installer - mutable image, GRUB as the second-stage bootloader.
- RAW and VHD/X - immutable image, systemd-boot as the second-stage bootloader.
- RAW and VHD/X - immutable image, systemd-boot as the second-stage bootloader, with
  real-time support.

The two immutable image microvisor versions integrate the Intel® kernel and
enable the software and features offered by Intel® Open Edge Platform. Check out the
overview of key software components:

![overview of key software components](./assets/architecture-key-components.drawio.svg)

## Edge Microvisor Toolkit Real Time

To support workloads that have real-time requirements, a dedicated image is generated.
The RT version of Edge Microvisor Toolkit includes several features over the standard release.

### Preempt RT Kernel

The Preempt RT Linux Kernel 6.12 is designed to offer enhanced real-time performance compared
to the standard kernel:

- **Reduced Latency**
The real-time (RT) patch transforms parts of the kernel to be fully preemptible. This means
that high-priority tasks can interrupt lower-priority tasks quickly, leading to significantly
lower worst-case latencies.

- **Deterministic Scheduling**
By threading interrupt handlers and converting spinlocks to preemptible mutexes, the RT
kernel provides more predictable and deterministic behavior. This is crucial for
time-sensitive applications where meeting strict deadlines is mandatory.

- **Improved Interrupt Handling**
In the RT kernel, most interrupts are handled by kernel threads. This allows the scheduler to
manage them more effectively, ensuring that critical real-time tasks are not unduly delayed
by interrupt processing.

- **Better Synchronization Primitives**
The patch refines locking mechanisms, reducing the time when critical sections cannot be
interrupted. This improves the overall responsiveness and guarantees that the system can
handle real-time workloads with minimal jitter.

### perf tool

The Linux `perf` tool is a powerful, integrated performance analysis suite, that taps
directly into the Linux Performance Events subsystem. The tool is mostly known for:

- **Comprehensive Metrics**
`perf` can measure a wide range of performance events, including CPU cycles, instructions,
cache misses, branch mispredictions, and more. This granular data is invaluable for
identifying performance bottlenecks in both kernel and user-space applications.

- **Multiple Modes of Operation**
`perf` provides multiple modes of operation that enable capturing a quick summary of
performance counters over different periods. It provides in-depth reports of overall system
performance, as well as visualization of real-time performance data
(using the `top`command).

### Turbostat

Turbostat is an Intel® tool, invaluable when diagnosing performance issues or optimizing
power consumption on systems with Intel® processors. It leverages hardware performance
counters to display detailed, real-time information for each processor core.
The data includes:

- **Real-Time Monitoring** displays per-core frequency, C-state (idle state) residency,
  and power usage.
- **Detailed Metrics** offer insights into performance states (P-states) and helps identify
  issues with efficiency or power management.
- **Diagnostic Utility** is particularly useful for system tuning and benchmarking. It helps
  understand how modern Intel® CPUs manage power under varying workloads.


### cpupower

`cpupower` is a general tool for controlling CPU power management on Linux, essential
for system administrators looking to optimize CPU behavior according to workload demands.
It is used to query and set up CPU frequency scaling, managing the trade-offs between
performance and power consumption.

- **Frequency Management** enables you to view current CPU frequencies and adjust settings
  using various governors (like performance, powersave, or on demand).
- **Power Saving Adjustments** helps in tuning system’s energy usage by adjusting parameters
  such as frequency limits and enabling/disabling turbo boost.
- **Dynamic Control** provides commands such as `cpupower frequency-info` (to display current
  frequency information) and `cpupower frequency-set` (to adjust CPU frequency settings).


### Kernel Command Line

The kernel command line for the RT kernel can be customized specifically for customer
workloads. Currently, `idle` is the only configured command-line argument that affects
real-time performance.

- **idle=poll**
Forces the CPU to actively poll for work when idle, rather than entering low-power idle
states. In RT systems, this can reduce latency by ensuring the CPU is always ready to
handle high-priority tasks immediately, at the cost of higher power consumption.

> **Note:**
  It is currently not possible to directly modify the kernel command-line parameters once
  a build has been generated, as it is packaged inside the signed UKI. Modifying the kernel
  command line would invalidate the signature. The mechanism to enable customization of the
  kernel command line will be added in future releases.

- **isolcpus=<list>**
Isolates specific CPU cores from the general scheduler, preventing non-RT tasks from
being scheduled on those cores. This ensures that designated cores are available solely
for RT tasks.

- **nohz_full=<list>**
Enables full tickless (nohz) mode on specified cores, reducing periodic timer interrupts
that could introduce latency on cores dedicated to RT workloads.

- **rcu_nocbs=<list>**
Offloads RCU (Read-Copy-Update) callbacks from the specified CPUs, reducing interference
on cores that need to be as responsive as possible.

- **threadirqs**
Forces interrupts to be handled by dedicated threads rather than in interrupt context,
which can improve the predictability and granularity of scheduling RT tasks.

- **nosmt**
Disables simultaneous multi-threading (hyperthreading). This can prevent contention between
sibling threads that share the same physical core, leading to more predictable performance.

- **numa_balancing=0**
Disables automatic NUMA balancing. While NUMA awareness is important, automatic migration
of processes can introduce latency. Disabling it helps maintain predictable memory locality.

- **intel_idle.max_cstate=0**
Limits deep idle states on Intel® CPUs, reducing wake-up latencies that can adversely
affect RT performance.

## Build Artifacts

Each build of Edge Microvisor Toolkit produces several build artifacts based on
the used image configuration. The artifacts come with associated `sha256` files.

- Unique build ID.
- Manifest containing version, kernel version, size, release details and CVE manifest.
- Software BOM package manifests (included packages, dependencies, and patches).
- Signed Image in `raw.gz` format.
- Image in VHD format.
- Signing key.


## Packaging

The image is compressed and packaged as a RAW image file that consists of
the bootloader, kernel, and root filesystem, ready to be flashed to a
drive directly. The image consists of three partitions:

|Device  |Start  |End  |Sectors  |Size |Type  |
|-------|-------|-----|---------|-----|------|
|...raw1  |2048  |614399 |612352 |299M |EFI System|
|...raw2  |614400|3145727|2531328|1.2G  |Linux filesystem|
|...raw3  |3145728|4192255|1046528|511M|Linux filesystem|

- The first partition is the EFI boot partition.
- The second partition contains the read-only `rootfs` filesystem.
- The third partition contains the persistent filesystem.

UKI (Unified Kernel Image) is an EFI executable that bundles several components, reducing
the number of artifacts and simplifying management of operating system updates.

```bash
.
├── BOOT
│   ├── BOOTX64.EFI
│   └── grubx64.efi
└── Linux
└── linux-6.6.71-1.tmv3.efi
```

The `linux-6.6.71-1.tmv3.efi` holds the UKI, with key components:

- .osrel – contains /etc/os-release data or references.
- .cmdline – embedded kernel command line parameters.
- .initrd – initramfs, used at early boot.
- .linux – the actual kernel binary.

## Unified Kernel Image

The microvisor uses a Unified Kernel Image (UKI), which is a single EFI binary that packages
together the Intel® kernel, initramfs, and associated kernel command-line parameters. This
design simplifies the boot process on UEFI systems and enhances security, especially when
combined with Secure Boot.

- Unified Packaging:
Instead of managing separate files for the kernel, initramfs, and boot configuration,
a UKI bundles them all into one EFI binary. This simplifies updates and maintenance.

- Embedded Kernel Command Line:
The UKI embeds the kernel command-line options directly within its structure. These
options — such as specifying the root device, setting boot verbosity (e.g., quiet), or
defining custom parameters — are stored in a dedicated section. This means the kernel
receives its parameters immediately upon boot, without needing separate configuration files.

On UEFI systems with Secure Boot enabled, the firmware will only boot images that have been
cryptographically signed. The build infrastructure signs the UKI to ensure that the image is
trusted and has not been tampered with. Since the kernel command-line options are embedded
inside the UKI, signing the image secures not only the kernel and initramfs but also the
command-line parameters. This means all boot-time configuration is verified by the firmware.

## Hostfile system and Persistent Partition

The `rootfs` is read-only in the immutable images of Edge Microvisor Toolkit to prevent any
changes. The partitioning layout above also shows a persistent `ext4` partition that is
mounted under `/opt` and is read-writable.

A `dracut` module mounts the persistent partition, and creates overlays for `tmpfs` and
persistent bind mount paths for the directories that must be writable for different OS
components.

The `layout.env` defines the `tmpfs` and persistent bind mounts for the image. Below is
a snapshot of the key directories for `tmpfs` and bind mounts:

### **tmpfs**

```bash
  /var
  /etc/lp
  /etc/node-agent
  /etc/cluster-agent
  /etc/fluent-bit
  /etc/health-check
  /etc/telegraf
  /etc/caddy
  /etc/otelcol
```

- The `/var` directory requires to be writable as its content changes during normal operation
  (logs, cache, OS runtime data, persistent application data and temporary files).
- The `/etc/lp` holds assets and configuration for the system's printing subsystem.
- The `/etc/node-agent`, `/etc/cluster-agent` and `/etc/health-check` are required for the
  Open Edge Platform's bare-metal agents for configuration data.
- The `/etc/telegraf` and `/etc/otelcol` are used for telemetry data and configuration for
  the `telemetry-agent` and `observability-agent`, required by the Open Edge Platform.
- `/etc/caddy` is the ephemeral data required by the reverse-proxy required by the Open Edge
  Platform to communicate with the backend service(s).

### **Persistent-Bind Paths**

```bash
PERSISTENT_BIND_PATHS="
  /etc/fstab
  /etc/environment
  /etc/hosts
  /etc/intel_edge_node
  /etc/machine-id
  /etc/pki
  /etc/ssh
  /etc/systemd
  /etc/udev
  /etc/cloud
  /etc/sysconfig
  /etc/rancher
  /etc/netplan
  /etc/cni
  /etc/kubernetes
  /etc/lvm/archive
  /etc/lvm/backup
  /var/lib/rancher"
```

- Several key directories required for the OS to be writable for normal system operations are
  kept as persistent bind paths, such as `/etc/fstab`, `/etc/environemnt`, `/etc/hosts`,
  `/etc/pki`, `/etc/ssh`, `/etc/systemd`, `/etc/udev`, `/etc/sysconfig`, `/etc/netplan`.
- The Kubernetes distribution used for Open Edge platform uses Rancher's RKE2 and requires
  additional bind mounts such as `/etc/rancher`, `/etc/cni`, `/etc/kubernetes`,
  `/var/lib/rancher`.

## Bare Metal Agents

The Bare Metal Agents (BMAs) are included in all immutable builds and are required for
deployment with Open Edge Platform. The BMAs are running on the system as systemd-services.
In the standalone ISO version of the immutable edge node version, the BMAs are included in
the image but not started by default, as the installation is designed to work autonomously
without requiring a backend.

Each Bare Metal Agent is developed in `golang` and has a corresponding resource manager it
communicates with (dial-out). Below is a brief summary of the Bare Metal Agents included in
the build and their purpose.

### Hardware Discovery Agent

The hardware discovery agent is responsible for initial discovery and introspection of the
platform to ensure that it is provisioned and configured correctly.

### Platform Update Agent

The platform update agent (PUA) is responsible for updating the edge node, particularly
performing updates during scheduled maintenance windows. For Edge Microvisor Toolkit, this
involves:

- Downloading a new OS image when available in the remote registry service.
- Verifying its integrity.
- Writing the image to the inactive user partition.
- Reconfiguring the bootloader to make the inactive partition active and reboot the system.

If a failure occurs during the boot process to the image, the bootloader will revert back to
the last image. Update flows are discussed in more detail in the following sections.

### Node Agent

The node agent is responsible for configuration aspects related to platform functions on the
edge node. It also assists the onboarding process by providing JWT (JSON Web Tokens) to the
other Bare Metal Agents.

### Cluster Agent

The cluster agents are responsible for installation and formation of the Kubernetes cluster,
which may involve one or more edge nodes. The Kubernetes software, and associated extensions
(scheduler extensions, device plugins, network extensions, etc.) are **not** included in the
microvisor image itself, but installed on a writable portion of the filesystem.

### Telemetry Agent

The telemetry agent provides the configuration plane for telemetry collected from the edge
node, including metrics and logs. It enables collection of various telemetry data, as well as
configuration of scraping intervals and caching policies.

### Observability Agent

The observability agent provides the data plane portion of telemetry data. It uses
configuration provided by the telemetry agent and uses  `Fluent Bit`, `Telegraf`,
`OpenTelemetry`, and other standard Cloud Native Computing Foundation (CNCF) projects to
collect, process, and transmit telemetry data to the backend for further processing and
visualization purposes.

## Atomic Updates

The immutable microvisor uses a read-only file system and avoids traditional differential
package management (like `dnf` or `apt`) in favor of updating the entire system image. This
approach simplifies system management and increases reliability by preventing configuration
drifts.

### A/B Update Paradigm

At the heart of this design is an A/B update mechanism. Two dedicated partitions are reserved
on the system — one holds the active image, while the other remains inactive. This section
outlines the process.

### Active vs. Inactive Partitions

One partition is designated as active and is used during system boot via EFI and systemd-boot.
The other remains inactive until an update is applied.

### Update Process

When a new update is available, the following steps occur:

- The new image is downloaded and then verified for integrity and authenticity.
  Once verified, the new image is written to the inactive partition.

- The bootloader (systemd-boot) is then reconfigured to boot from the updated partition,
  which will become the new active partition upon the next reboot.

- Rollback Capability:

  Systemd-boot has the ability to detect boot failures. If the system fails to boot from the
  new image, the bootloader can automatically rollback to the previous, stable partition,
  ensuring continuous availability of the system.

### Benefits of The Approach

- **Stability and Predictability**

  By updating the entire image and maintaining immutable partitions, the system avoids
  configuration drift, often seen with writable filesystems.

- **Simplified Maintenance**

  The A/B paradigm eliminates the complexities associated with handling partial updates or
  rollbacks in traditional package management systems.

- **Enhanced Security**

  With a read-only filesystem and a verified update process, the risk of unauthorized
  modifications is greatly reduced.

This comprehensive update mechanism ensures that Edge Microvisor Toolkit remains stable,
secure, and easy to maintain, even in environments where reliability is paramount.

### Updating Open Edge Platform vs. Standalone

Edge Microvisor Toolkit updates are well integrated when using the Open Edge Platform.
The maintenance manager enables the administrator to configure when to run updates to edge
nodes. While the update will only occur during these maintenance windows, new images will be
downloaded in the background as soon as they become available. The diagram below shows the
overall update flow and state transitions.

![update flow and state transitions](./assets/architecture-update-flow.drawio.svg)

The Edge Microvisor Toolkit may also be updated as a standalone solution, through a manual
update procedure, without the automation offered by Open Edge Platform. You can download the
new version of the microvisor and run the update by invoking the `os-update-script` and
providing the path to the downloaded image.

> **Note:**
  Future versions of Edge Microvisor Toolkit will implement automatic image validation,
  update checks, and releases.

