#!/bin/bash

set -eu

update_fluentbit_config() {
	local EDGE_NODE_UUID
	local UPDATED_FLUENTBIT_UUID
	local HOST_NAME
	local UPDATED_FLUENTBIT_HOSTNAME

	EDGE_NODE_UUID="$(sudo dmidecode -s system-uuid)"
	UPDATED_FLUENTBIT_UUID=$(sed "s#EDGE_NODE_UUID#${EDGE_NODE_UUID}#" /etc/fluent-bit/fluent-bit.conf)
	echo -E "${UPDATED_FLUENTBIT_UUID}" > /etc/fluent-bit/fluent-bit.conf

	HOST_NAME="$(cat /proc/sys/kernel/hostname)"
	UPDATED_FLUENTBIT_HOSTNAME=$(sed "s#HOSTNAME#${HOST_NAME}#" /etc/fluent-bit/fluent-bit.conf)
	echo -E "${UPDATED_FLUENTBIT_HOSTNAME}" > /etc/fluent-bit/fluent-bit.conf
}

update_fluentbit_config

while true
do
	if [ -e /run/platform-observability-agent/agent-logs.sock ]; then
		echo "Starting Platform Observability Logging Service"
		break
	else
		sleep 10
	fi
done

exec "$@"
