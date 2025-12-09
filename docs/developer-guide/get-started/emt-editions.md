# Edge Microvisor Toolkit Editions

You can choose from several editions Edge Microvisor Toolkit to deploy
and validate workloads on Intel® platforms for various scenarios.


| Scenario | Description | Primary outcomes | Technology areas |
|---|---|---|---|
| Real-time & deterministic workloads | Run latency-sensitive workloads with guaranteed bounded jitter and repeatable execution timelines across one or more hosts, maintainable under steady-state and failure-recovery conditions | <br> - Bounded end-to-end latency & jitter <br> - Repeatable scheduling windows under load <br> - Cross-host timing consistency for distributed stages <br> - Fast, predictable recovery without violating SLOs | <br> - [PREEMPT_RT kernel](../emt-architecture-overview.md#preempt-rt-kernel) <br> - [Resource Director Technologies](../emt-architecture-overview.md#resource-director-technology) <br> - [Intel GPU RT](../emt-architecture-overview.md#intel-device-plugins-for-kubernetes) <br> - [CPU & Scheduler Isolation](../emt-architecture-overview.md#isolcpuslist) <br> - [Memory Determinism](../emt-architecture-overview.md#preempt-rt-kernel) <br> - Time & Clocks <br> - [Network Determinism (TSN)](../emt-architecture-overview.md#time-sensitive-networking-support) |
| VM-based workloads on Kubernetes with shared GPUs | Run multiple virtual machines on Kubernetes that concurrently share one or more physical GPUs, with predictable fairness, isolation, and policy-driven placement—using a KubeVirt stack extended for GPU sharing |  <br> - Stable, repeatable GPU performance per VM under contention <br> - Hard/soft sharing policies (fair-share, priority tiers, or quotas) <br> - Safe isolation between tenants/VMs (memory, contexts, resets) <br> - Schedulable resources with clear admission signals (no surprise fails) <br> - Operational guardrails: health checks, graceful drain/eviction, rollback | <br> - [SRIOV](./deployment/emt-vm-host.md) <br> - [Intel GPU](../emt-system-requirements.md#discrete-gpu) <br> - [kubevirt](https://github.com/open-edge-platform/edge-microvisor-toolkit-standalone-node/blob/main/standalone-node/docs/user-guide/desktop-virtualization-image-guide.md) <br> - [Host virtualization](./deployment/emt-vm-host.md) <br> - [Intel GPU device plugin](../emt-architecture-overview.md#intel-device-plugins-for-kubernetes) |
| AI & Vision workloads | Enable AI inference and computer-vision workloads on edge nodes using Intel GPU and NPU acceleration, exposing unified hardware-assisted pipelines through standard APIs and user-space libraries |  <br> - Efficient execution of deep-learning and vision inference on-device without cloud dependency <br> - Unified GPU/NPU compute abstraction for developers (OpenVINO backend, media pipelines) <br> - Deterministic frame-rate and latency for multi-stream analytics workloads (e.g., camera ingest) <br> - Seamless integration with containers or pods, including dynamic device discovery and sharing <br> - Stable ABI/API interface across [OS updates](../architecture/emt-updates.md) and driver versions | <br> - [Edge AI packages](https://eci.intel.com/docs/3.3/packages_list.html) <br> - [OpenVino](https://docs.openvino.ai) <br> - [Intel GPU and NPU drivers](https://docs.openvino.ai/2025/openvino-workflow/running-inference/inference-devices-and-modes.html) <br> - [Intel GPU device plugin](../emt-architecture-overview.md#intel-device-plugins-for-kubernetes) |

The diagram
below will help you select the toolkit version that suits your workflow.

```mermaid
flowchart LR

    A([Start]) --> B{"Need full<br>developer toolchain?"}

    B -->|Yes| D[EMT-D Developer]
    B -->|No| C{"Provisioning<br>only?"}

    C -->|Yes| E[EMT Bootkit<br>Provisioning]
    C -->|No| F{"Need RT?"}

    F -->|Yes| G{"RT deploy<br>method?"}
    F -->|No| H{"NRT deploy<br>method?"}

    G -->|EMF| I[RT + EMF]
    G -->|Standalone| J[RT + EMT-S]

    H -->|EMF| K[NRT + EMF]
    H -->|Standalone| L[NRT + EMT-S]
```

The table below summarizes the released versions:

| Edition | Description | Stable Kernel | [Next Kernel](../emt-architecture-overview.md#next-kernel) | Docs |
|--------|-------------|---------------|-------------|------|
| **Standalone (Immutable)** | Minimal runtime; immutable rootfs | ✓ | ✓ | [Standalone Node](https://github.com/open-edge-platform/edge-microvisor-toolkit-standalone-node) |
| **Developer Node (Mutable)** | Full toolchain, optional RT | ✓ | ✓ | [Developer Node](../emt-architecture-overview.md#developer-node-mutable-iso-image) |
| **EMT for EMF** | EMF-integrated orchestrated deployments | ✓ | ✓ | [EMT + EMF](../emt-deployment-edge-orchestrator.md) |
| **Bootkit** | Minimal iPXE provisioning image | ✓ | – | [Bootkit](../emt-bootkit.md) |

The Edge Microvisor Toolkit has undergone extensive validation across all Intel
platforms such as  Xeon®, Intel® Core Ultra™, Intel Core™ and Intel® Atom®. It
provides robust support for integrated NPU, as well as a
[selection of discrete GPU cards](../emt-system-requirements.md#hardware-requirements).

You can either build the Edge Microvisor Toolkit by following step-by-step
instructions or download it directly. Both the Build system and the Edge Microvisor
Toolkit are available as Open-Source.



## Next

- Learn how to [Install Edge Microvisor Toolkit](./emt-installation-howto.md).
- Learn how to customize and manually [build microvisor images](./emt-building-howto.md).
