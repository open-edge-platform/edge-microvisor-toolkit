#!/bin/bash

set -eu

update_health_check_config() {
	local EDGE_NODE_UUID
	local UPDATED_HEALTH_CHECK_UUID
	local HOST_NAME
	local UPDATED_HEALTH_CHECK_HOSTNAME

	EDGE_NODE_UUID="$(sudo dmidecode -s system-uuid)"
	UPDATED_HEALTH_CHECK_UUID=$(sed "s#EDGE_NODE_UUID#${EDGE_NODE_UUID}#" /etc/health-check/health-check.conf)
	echo -E "${UPDATED_HEALTH_CHECK_UUID}" > /etc/health-check/health-check.conf

	HOST_NAME="$(cat /proc/sys/kernel/hostname)"
	UPDATED_HEALTH_CHECK_HOSTNAME=$(sed "s#HOSTNAME#${HOST_NAME}#" /etc/health-check/health-check.conf)
	echo -E "${UPDATED_HEALTH_CHECK_HOSTNAME}" > /etc/health-check/health-check.conf
}

update_health_check_config

while true
do
	if [ -e /run/platform-observability-agent/agent-logs.sock ]; then
		echo "Starting Platform Observability Health Check Service"
		break
	else
		sleep 10
	fi
done

exec "$@"
