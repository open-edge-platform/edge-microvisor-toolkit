Edge Microvisor Toolkit Documentation
=============================================================================================

.. Content Requirements:
   1. Clearly define the OS purpose and its target users.
   2. Highlight key features that differentiate this OS.
   3. Include any unique design principles or philosophies.

Edge Microvisor Toolkit is an open-source, lightweight operating system based on Azure Linux,
and optimized for Intel® architecture. As a container-first, immutable OS, it is a perfect
foundation for high-performance edge computing workloads that benefit from scalability and
ease of management. It supports various deployment models, from standalone evaluation to
large production-grade systems (large-scale rollouts are possible with Open Edge Platform's
Edge Manageability Framework integration).

Edge Microvisor Toolkit is designed to enable the full potential of Intel® platform
portfolio by integrating the Intel® kernel and offering the most recent features as soon as
possible. It will unlock new functionalities before mainstream Linux distributions, while
also including the existing functionality not downstreamed in the existing distributions.

Currently published default versions are:

- Immutable Edge Microvisor Toolkit for Intel® Core™ and Xeon®.
- Immutable Edge Microvisor Toolkit with real time extensions for Intel® Core™ and Xeon®.
- ISO Edge Microvisor Toolkit installer for standalone edge nodes Intel® Core™ and Xeon®
  platforms.
- ISO Edge Microvisor Toolkit installer for developers for Intel® Core™ and Xeon® platforms.

If you need more than that, the build infrastructure of Edge Microvisor Toolkit enables you
to create your own, custom images.


Why Use Edge Microvisor Toolkit
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

| **Flexible**
|      Build, customize and optimize the Microvisor to suit your specific requirements with a
       powerful build toolkit and validated images tailored to meet most demands.
| **Secure**
|      Security opt-in methodology, enabling you to pick and choose what security features to
       enable, from Secure Boot, dm-verity for integrity protection or Full Disc Encryption
       for security-at-rest.
| **Small Footprint**
|      Microvisor has a small footprint (350MB compressed, 750MB uncompressed), allowing for
       short deployment times and reduced attack vectors.
| **Flexible Deployments**
|      Edge Microvisor supports deployment as containers, virtual machines and as Kubernetes
       workloads, ensuring support for modern cloud-edge native, as well as legacy
       applications.
| **Atomic Updates**
|      Immutable images support A/B updates with short boot-up and update times ensuring
       integrity, eliminating configuration drift and minimizing downtime of workloads.
| **Automatic Rollback**
|      Automatic rollback support provides operational assurance and recovery in case of
       failed updates.
| **Fully managed OS lifecycle**
|      Integration with Edge Manageability Framework enables automated
       deployments, updates, and rollbacks without manual intervention.
| **Immutable design for security**
|      Read-only system partitions prevent tampering, ensuring system integrity.
| **Optimized for Intel® hardware**
|      Delivers performance enhancements tailored to Intel® silicon, ensuring maximum
       efficiency.
| **Scalability for large fleets**
|      Centralized control through Edge Manageability Framework simplifies 
       management across thousands of edge nodes.


Customers Highlights
---------------------------------------------------------------------------------------------

- Edge Microvisor Toolkit as the edge OS with and without real time support.
- Built-in support for Intel® platform features, Ethernet and GPU support.
- Immutable OS with support for atomic (A/B) updates with Open Edge Platform.
- Secure the edge platform with an opt-in security model supporting Secure Boot,
  Full Disc Encryption, dm-verity with TPM 2.0.
- Can be deployed with Edge Manageability Framework or as a standalone OS.

Developers Highlights
---------------------------------------------------------------------------------------------

- Flexible build infrastructure for creating custom images from a large set
  of pre-provisioned packages via .spec files.
- Support for multiple image formats for use on bare-metal systems, virtual machines and
  containers (ISO, VHD, VHDX, RAW).
- Supporting UKI (Unified Kernel Image) format with or without second stage bootloaders
  (GRUB, systemd-boot).
- Supporting mutable developer ISO builds.

Key Performance Indicators
---------------------------------------------------------------------------------------------

- Boot time of less than 8 seconds on entry level Intel® Core™ platforms.
- Fast A/B image updates (<30s) with automatic rollback support on Edge Microvisor Toolkit.
- Small footprint with less than 750MB of disk space required for the OS and under 350MB
  compressed RAW image size.




License Information
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Content Requirements:
   1. Clearly state the license type and link to the LICENSE file.
   2. Mention any third-party open-source licenses if applicable.
   3. Provide guidance on how contributions are licensed.


Edge Microvisor Toolkit is open source and licensed under the MIT License.
See the [LICENSE](../LICENSE) file for more details.

Next Steps
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:doc:`Architecture Overview <./architecture-overview>`





.. toctree::
    get-started
    architecture-overview
    deployment-edge-orchestrator
    security
    contribution
    troubleshooting
    system-requirements
