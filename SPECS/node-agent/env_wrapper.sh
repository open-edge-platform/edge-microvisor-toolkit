#!/bin/bash

set -eu

update_uuid() {
	local EDGE_NODE_UUID
	local UPDATED_NODE_AGENT_UUID

	EDGE_NODE_UUID="$(sudo dmidecode -s system-uuid)"
	UPDATED_NODE_AGENT_UUID=$(sed "s/^GUID: '.*'/GUID: '${EDGE_NODE_UUID}'/" /etc/edge-node/node/confs/node-agent.yaml)
	echo -E "${UPDATED_NODE_AGENT_UUID}" > /etc/edge-node/node/confs/node-agent.yaml
}

update_node_urls() {
	if [ -n "$NODE_ONBOARDING_ENABLED" ]; then
		local UPDATED_NODE_AGENT_ONBOARD_ENABLED
		UPDATED_NODE_AGENT_ONBOARD_ENABLED=$(sed -e '/^onboarding:$/{n' -e 's/enabled:.*/enabled: '"$NODE_ONBOARDING_ENABLED"'/' -e '}' /etc/edge-node/node/confs/node-agent.yaml)
		echo -E "${UPDATED_NODE_AGENT_ONBOARD_ENABLED}" > /etc/edge-node/node/confs/node-agent.yaml
	fi

	if [ -n "$NODE_ONBOARDING_URL" ]; then
		local UPDATED_NODE_AGENT_ONBOARD_URL
		UPDATED_NODE_AGENT_ONBOARD_URL=$(sed -e '/^onboarding:$/{n' -e '/.*enabled:/{n' -e 's#serviceURL:.*#serviceURL: '"$NODE_ONBOARDING_URL"'#' -e '}}' /etc/edge-node/node/confs/node-agent.yaml)
		echo -E "${UPDATED_NODE_AGENT_ONBOARD_URL}" > /etc/edge-node/node/confs/node-agent.yaml
	fi

	if [ -n "$NODE_ONBOARDING_HEARTBEAT" ]; then
		local UPDATED_NODE_AGENT_ONBOARD_HEARTBEAT
		UPDATED_NODE_AGENT_ONBOARD_HEARTBEAT=$(sed -e '/^onboarding:$/{n' -e '/.*enabled:/{n' -e '/.*serviceURL:/{n' -e 's/heartbeatInterval:.*/heartbeatInterval: '"$NODE_ONBOARDING_HEARTBEAT"'/' -e '}}}' /etc/edge-node/node/confs/node-agent.yaml)
		echo -E "${UPDATED_NODE_AGENT_ONBOARD_HEARTBEAT}" > /etc/edge-node/node/confs/node-agent.yaml
	fi

	if [ -n "$NODE_ACCESS_URL" ]; then
		local UPDATED_NODE_AGENT_ACCESS_URL
		UPDATED_NODE_AGENT_ACCESS_URL=$(sed -e '/^auth:$/{n' -e 's#accessTokenURL:.*#accessTokenURL: '"$NODE_ACCESS_URL"'#' -e '}' /etc/edge-node/node/confs/node-agent.yaml)
		echo -E "${UPDATED_NODE_AGENT_ACCESS_URL}" > /etc/edge-node/node/confs/node-agent.yaml
	fi

	if [ -n "$NODE_RS_URL" ]; then
		local UPDATED_NODE_AGENT_RS_URL
		UPDATED_NODE_AGENT_RS_URL=$(sed -e '/^auth:$/{n' -e '/.*accessTokenURL:/{n' -e 's#rsTokenURL:.*#rsTokenURL: '"$NODE_RS_URL"'#' -e '}}' /etc/edge-node/node/confs/node-agent.yaml)
		echo -E "${UPDATED_NODE_AGENT_RS_URL}" > /etc/edge-node/node/confs/node-agent.yaml
	fi
}

update_uuid
update_node_urls

exec "$@"
