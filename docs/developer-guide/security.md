# Edge Microvisor Toolkit Security Overview

Edge Microvisor Toolkit is designed with the security-first mindset, so that its users can
enjoy the best of Intel® platforms, deploying them in a secure environment with security
assurance for workloads and data. This article describes the most important security features
of the Edge Microvisor Toolkit and how Intel® addresses security vulnerabilities in the field.

The toolkit is built around an opt-in security model where the customer ultimately decides
what security features to enable for their specific deployment, what trade-offs are made
between accepted risk and overhead that may come with some security features enabled.

## Secure Boot and Trusted Boot

Secure Boot - more specifically, Trusted Boot ensures integrity of the operating system.
Trusted Boot halts the boot process if any component in the chain fails verification.
It works by validating each subsequent element in the boot chain, beginning with the Initial
Boot Block (IBB). The IBB itself is verified by a hardware root of trust, typically
implemented through platform fuses or other dedicated technologies. Each component is
authenticated before the next stage loads. If any link cannot be verified, the boot process
stops immediately to prevent potential tampering.

![System Partition](assets/security-partitions.drawio.svg)

> **Note:**
  Measured Boot is a related mechanism that records cryptographic hashes (measurements) of
  each boot stage into TPM (Trusted Platform Module) PCR registers. These measurements
  provide an auditable log of the boot process. However, in the current Secure Boot
  implementation, measured boot is not used as the enforcement mechanism. It is for recording
  and attestation only.

On Intel® platforms, hardware-based root of trust is often provided by technologies such as
Intel® Boot Guard, TPM 2.0, and Intel® TXT. For example, Intel® Boot Guard uses hardware
fuses to ensure that only authenticated firmware is executed, thereby supporting the verified
boot process.

### Platform Keys and Image Integrity

The immutable production image of Edge Microvisor Toolkit uses custom platform keys
(PK, KEK, db) that must be configured in the BIOS for the system to boot successfully.
The Unified Kernel Image (UKI) is signed with the platform keys, ensuring integrity of both
the kernel and the kernel command line. As noted in a previous section, any direct
modification of the kernel command line will invalidate the UKI’s signature, preventing the
system from booting with an unverified configuration.

Additionally, a separate signature is applied to the entire RAW image. This RAW signature is
verified before provisioning or updating an edge node. It protects the complete image,
including all internal partitions and the root filesystem, ensuring that the entire software
stack is authenticated and tamper-resistant.

## Immutability

Edge Microvisor Toolkit ensures that the software image remains immutable both at rest and
during runtime. Once installed on an edge device, the image cannot be modified — whether on
disk or while the system is running. Upgrades can only occur via a controlled, official
upgrade process (detailed in [architecture overview](./architecture-overview.md)),
resulting in a secure and tamper-resistant operating system.
Additionally, runtime modifications are actively prevented by built-in protection of the
microvisor kernel.

### Runtime Immutability

Immutability at runtime is ensured by mounting the root microvisor partition, containing all
software components and configuration data, as Read-Only (RO). It means that no software
running on the device can write to the partition, thereby safeguarding the core operating
system from runtime corruption or infection.

### Protection of the Root Partition at Rest

When the system is powered off, the root microvisor partition is further protected by a Linux
kernel feature called `dm-verity`. The tool verifies that the content of the partition matches
a pre-computed cryptographic hash, the "known good" value, stored separately on disk. In
addition, secure boot, as described in the previous section, ensures that only genuine
versions of Edge Microvisor Toolkit can be booted, and that the image remains intact at both
runtime and rest.

### Application Deployment and Data Persistence

Applications are deployed dynamically via the terminal or the Open Edge Platform.
All necessary software, tools, and packages are contained within the immutable image.
To meet persistence requirements, application data is stored on a dedicated partition that
handles both static and dynamic storage needs.

### Mitigating Offline Storage Attacks - dm-verity

Although the microvisor is immutable and the root partition is mounted as read-only during
operation, an attacker might attempt an offline attack by physically removing the disk,
modifying the partition to insert malicious software, and reinstalling it. Such offline
storage attacks are mitigated by `dm-verity`, a Linux kernel security feature. It continuously
measures the root partition and compares its content against a cryptographic hash: a known
good value of the root partition stored in a separate disk location using full disk encryption.

Since the root partition is immutable, its contents are only expected to change during a
secure upgrade process, when a new hash value is computed and encrypted. This ensures that
the system maintains its integrity at all time. Since an attacker cannot modify the root
partition and the hash value together, any discrepancy detected is an indicator of tampering.

In such a case, system operation halts immediately and the only solution is to wipe and
re-provision the device, preventing any malicious software from persisting on the system.
Although this may disrupt system operation, it does prevent system corruption / malware
injection from an offline storage attack.

## Full Disc Encryption (FDE)

Edge Microvisor Toolkit secures data at rest through full disk encryption (FDE).
While secure boot and immutability ensure integrity of the installed system, they do not
protect the confidentiality of application software or data. FDE addresses this gap by
preventing unauthorized access to sensitive business logic, proprietary AI/ML models, and
confidential data, such as medical records, financial transactions, and operational records.

### How FDE is Implemented

All storage on edge nodes is encrypted using the Linux Unified Key Setup (LUKS), specifically
using the LUKS-2 standard. The encryption is enabled during the provisioning process of the
device by Open Edge Platform, before any sensitive applications or data are deployed. Once
configured, data written to storage is automatically encrypted, and it is seamlessly decrypted
when read by applications. This transparent process extends to the Linux swap partition,
ensuring that cached data remains protected.

![Enabling Full Disc Encryption](./assets/luks-setup.drawio.svg)

### Key Management and Boot Process

Since full disk encryption requires a persistent key, the microvisor setup process generates
an encryption key and securely stores it within the hardware Trusted Platform Module (TPM).
At each boot, the microvisor retrieves the key and initializes the LUKS subsystem. Crucially,
the TPM is locked immediately after the key is obtained, ensuring that only the microvisor
has access to the decryption key, being the first component to run at boot time. This
prevents any subsequent software from accessing the key and potentially decrypting disk data.

### Protection Against Physical Attacks

By storing the encryption key in the TPM rather than on disk, the system mitigates risks
associated with physical theft. If a disk is removed and connected to another system, the
attacker will be unable to access the encrypted data since the decryption key remains locked
in the TPM of the original edge device.

## SELinux

SELinux (Security-Enhanced Linux) is a security module integrated into the Linux kernel that
implements mandatory access control (MAC) policies. Edge Microvisor Toolkit enables SELinux
in all of its images along with the associated policies.

SELinux assigns security labels to processes, files, and other system objects, thereby
enforcing strict access rules. This means that even if a process is compromised, SELinux
restricts it from accessing sensitive parts of the system, limiting potential damage. By
providing a fine-grained security mechanism, SELinux helps ensure that every operation
performed on the system is authorized according to its defined policy.

SELinux can operate in two primary modes: permissive and enforcing. In permissive mode,
SELinux does not block actions that violate its security policies; instead, it logs these
violations as warnings. This mode is particularly useful during the policy development or
debugging phases, allowing administrators to monitor and adjust the policy without impacting
system functionality. It acts as a "test mode" where potential issues are identified and
resolved based on detailed audit logs. Edge Microvisor Toolkit enables SELinux in the
**permissive** mode only. Switching the mode to *enforcing* has not been fully validated.

In contrast, the enforcing mode is where SELinux actively prevents any operations
that do not comply with its policies. In this mode, unauthorized actions are
blocked in real-time, which significantly increases the security posture of the
system. The enforcing mode is crucial in production environments where maintaining
strict security boundaries is essential to protect critical data and system
integrity. Together, these modes enable administrators to balance security and
usability, transitioning from permissive to enforcing mode once the policies have been
thoroughly tested and validated.

The SELinux policies are defined per component in their respective SPECS files, and configured
when the `rpm` is installed to the image. Not every executable component in the microvisor has
an SELinux policy associated with it. Primarily, systemd-services such as the Bare Metal
Agents, reverse-proxy, and the telemetry pipeline have them defined.
