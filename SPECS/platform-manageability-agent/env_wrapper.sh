#!/bin/bash

set -eu

update_infra_url() {
	if [ -n "$PLATFORM_MANAGEABILITY_URL" ]; then
		local UPDATED_PM_DISCOVERY_INFRA_URL
		UPDATED_PM_DISCOVERY_INFRA_URL=$(sed "s/^  serviceURL: '.*'/  serviceURL: '$PLATFORM_MANAGEABILITY_URL'/" /etc/edge-node/node/confs/platform-manageability-agent.yaml)
		echo -E "${UPDATED_PM_DISCOVERY_INFRA_URL}" > /etc/edge-node/node/confs/platform-manageability-agent.yaml
	fi

	if [ -n "$RPS_ADDRESS" ]; then
		local UPDATED_RPS_DISCOVERY_INFRA_URL
		UPDATED_RPS_DISCOVERY_INFRA_URL=$(sed "s/^rpsAddress: '.*'/rpsAddress: '$RPS_ADDRESS'/" /etc/edge-node/node/confs/platform-manageability-agent.yaml)
		echo -E "${UPDATED_RPS_DISCOVERY_INFRA_URL}" > /etc/edge-node/node/confs/platform-manageability-agent.yaml
	fi
}

update_infra_url

exec "$@"