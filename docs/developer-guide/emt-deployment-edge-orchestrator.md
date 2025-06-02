# Production Deployment with Edge Orchestrator

Edge Microvisor Toolkit integrates with Edge Manageability Framework for
scalable, secure, reliable, and automated management of edge infrastructure. It
provides centralized control for OS provisioning, automated updates, and
lifecycle management across distributed edge environments.

| **Benefit** | **Edge Microvisor Toolkit** | **Edge Manageability Framework** | **Outcome** |
|-------------|-----------------------------|-----------------------|-------------|
| **Security-First OS Management**  | Enforces read-only system partitions and signed OS updates to prevent unauthorized changes. | Automates OS deployment with policy-based enforcement and zero-trust security models. | System integrity, reduced attack vectors or unauthorized modifications. |
| **Automated & Fail-Safe Updates** | Uses A/B partitioning for seamless updates with rollback capabilities. | Manages update policies, schedules maintenance windows, and provides status tracking for fleet-wide OS updates. | Minimized downtime and safe updates, preventing failures in production environments. |
| **Scalability Across Edge Fleets** | Lightweight OS with a small image size (<750MB) and fast boot time (<10s). | Centralized OS Resource Manager enables fleet-wide updates without manual intervention. | Large-scale deployments with minimal operational overhead. |
| **Optimized for Performance & Reliability** | Tailored for Intel® hardware with low-latency kernel optimizations. | Orchestrates deployments to match workload requirements across distributed infrastructure. | High-performance workloads with predictable system behavior. |
| **Enables Silicon Innovations Faster** | Provides early access to next-generation Intel® platform features ahead of commercial OS vendors. | Automates rollout of new OS profiles to compatible hardware platforms. | The latest Intel® optimizations are deployed quickly, accelerating innovation. |

## OS Deployment and Update Workflow

Edge Manageability Framework provides centralized control over OS installation,
updates, and rollback management. The key components involved in the update
process include:

- **OS Resource Manager**: Detects and manages available OS versions.
- **Maintenance Manager**: Schedules updates during maintenance windows.
- **Platform Update Agent**: Executes OS updates on edge nodes.
- **A/B Partitioning System**: Ensures fail-safe updates by switching between partitions.

### Update Process

1. A new image of Edge Microvisor Toolkit is published to the Release Service.
2. The OS Resource Manager automatically detects the new image.
3. A scheduled maintenance window triggers an update via the Maintenance Manager.
4. The Platform Update Agent applies the update by installing the new image in an alternate
   partition.
5. On reboot, the system switches to the updated OS image, ensuring rollback is available
   if needed.

## Learn More

- [Edge Microvisor Toolkit Architecture](emt-architecture-overview.md)
- [Edge Manageability Framework](https://github.com/open-edge-platform/edge-manageability-framework)
