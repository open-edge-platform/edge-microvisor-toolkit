#!/bin/bash

set -eu

update_infra_url() {
	if [ -n "$PM_INVENTORY_URL" ]; then
		local UPDATED_PM_DISCOVERY_INFRA_URL
		UPDATED_PM_DISCOVERY_INFRA_URL=$(sed "s/^  serviceURL: '.*'/  serviceURL: '$PM_INVENTORY_URL'/" /etc/edge-node/node/confs/pm-agent.yaml)
		echo -E "${UPDATED_PM_DISCOVERY_INFRA_URL}" > /etc/edge-node/node/confs/pm-agent.yaml
	fi
}

update_infra_url

exec "$@"