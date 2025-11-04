# Bare Metal Agents

The Bare Metal Agents (BMAs) are included in all immutable builds and are required for
deployment with
[Edge Manageability Framework](https://github.com/open-edge-platform/edge-manageability-framework).
The BMAs are running on the system as systemd-services.
In the standalone ISO version of the immutable edge node version, the BMAs are included in
the image but not started by default, as the installation is designed to work autonomously
without requiring a backend.

Each Bare Metal Agent is developed in `golang` and has a corresponding resource manager it
communicates with (dial-out). Below is a brief summary of the Bare Metal Agents included in
the build and their purpose. For additional information on each agent, visit the
[Edge Node Agents](https://github.com/open-edge-platform/edge-node-agents) repository.

## Hardware Discovery Agent

[The hardware discovery agent](https://github.com/open-edge-platform/edge-node-agents/tree/main/hardware-discovery-agent)
is responsible for initial discovery and introspection of the
platform to ensure that it is provisioned and configured correctly.

## Platform Update Agent

[The platform update agent (PUA)](https://github.com/open-edge-platform/edge-node-agents/tree/main/platform-update-agent)
is responsible for updating the edge node, particularly
performing updates during scheduled maintenance windows. For Edge Microvisor Toolkit, this
involves:

- Downloading a new OS image when available in the remote registry service.
- Verifying its integrity.
- Writing the image to the inactive user partition.
- Reconfiguring the bootloader to make the inactive partition active and reboot the system.

If a failure occurs during the boot process to the image, the bootloader will revert back to
the last image. Update flows are discussed in more detail in the following sections.

## Node Agent

[The node agent](https://github.com/open-edge-platform/edge-node-agents/tree/main/node-agent)
is responsible for configuration aspects related to platform functions on the
edge node. It also assists the onboarding process by providing JWT (JSON Web Tokens) to the
other Bare Metal Agents.

## Cluster Agent

[The cluster agents](https://github.com/open-edge-platform/edge-node-agents/tree/main/cluster-agent)
are responsible for installation and formation of the Kubernetes cluster,
which may involve one or more edge nodes. The Kubernetes software, and associated extensions
(scheduler extensions, device plugins, network extensions, etc.) are **not** included in the
microvisor image itself, but installed on a writable portion of the filesystem.

## Telemetry Agent

[The telemetry agent](https://github.com/open-edge-platform/edge-node-agents/tree/main/platform-telemetry-agent)
provides the configuration plane for telemetry collected from the edge
node, including metrics and logs. It enables collection of various telemetry data, as well as
configuration of scraping intervals and caching policies.

## Observability Agent

[The observability agent](https://github.com/open-edge-platform/edge-node-agents/tree/main/platform-observability-agent)
provides the data plane portion of telemetry data. It uses
configuration provided by the telemetry agent and uses  `Fluent Bit`, `Telegraf`,
`OpenTelemetry`, and other standard Cloud Native Computing Foundation (CNCF) projects to
collect, process, and transmit telemetry data to the backend for further processing and
visualization purposes.

## Reporting Agent

[The reporting agent](https://github.com/open-edge-platform/edge-node-agents/tree/main/reporting-agent)
collects system information and metrics from
[Edge Manageability Framework](https://github.com/open-edge-platform/edge-manageability-framework)
installations. It gathers data from a variety of sources, including `lscpu`, `lsblk`,
`lshw`, `dmidecode`, and `kubectl`, to provide a comprehensive insight into hardware, software,
and runtime environment.