#!/bin/bash

set -eu

update_otelcol_config() {
	local EDGE_NODE_UUID
	local UPDATED_COLLECTOR_UUID

	EDGE_NODE_UUID="$(sudo dmidecode -s system-uuid)"
	UPDATED_COLLECTOR_UUID=$(sed "s#EDGE_NODE_UUID#${EDGE_NODE_UUID}#" /etc/otelcol/otelcol.yaml)
	echo -E "${UPDATED_COLLECTOR_UUID}" > /etc/otelcol/otelcol.yaml

	if [ -n "$OBSERVABILITY_LOGGING_URL" ]; then
		local UPDATED_COLLECTOR_LOGGING_URL
		UPDATED_COLLECTOR_LOGGING_URL=$(sed "s/OBSERVABILITY_HOST/$OBSERVABILITY_LOGGING_URL/g" /etc/otelcol/otelcol.yaml)
		echo -E "${UPDATED_COLLECTOR_LOGGING_URL}" > /etc/otelcol/otelcol.yaml
	fi

	if [ -n "$OBSERVABILITY_LOGGING_PORT" ]; then
		local UPDATED_COLLECTOR_LOGGING_PORT
		UPDATED_COLLECTOR_LOGGING_PORT=$(sed "s/OBSERVABILITY_PORT/$OBSERVABILITY_LOGGING_PORT/g" /etc/otelcol/otelcol.yaml)
		echo -E "${UPDATED_COLLECTOR_LOGGING_PORT}" > /etc/otelcol/otelcol.yaml
	fi

	if [ -n "$OBSERVABILITY_METRICS_URL" ]; then
		local UPDATED_COLLECTOR_METRICS_URL
		UPDATED_COLLECTOR_METRICS_URL=$(sed "s/OBSERVABILITY_METRICS_HOST/$OBSERVABILITY_METRICS_URL/g" /etc/otelcol/otelcol.yaml)
		echo -E "${UPDATED_COLLECTOR_METRICS_URL}" > /etc/otelcol/otelcol.yaml
	fi

	if [ -n "$OBSERVABILITY_METRICS_PORT" ]; then
		local UPDATED_COLLECTOR_METRICS_PORT
		UPDATED_COLLECTOR_METRICS_PORT=$(sed "s/OBSERVABILITY_METRICS_PORT/$OBSERVABILITY_METRICS_PORT/g" /etc/otelcol/otelcol.yaml)
		echo -E "${UPDATED_COLLECTOR_METRICS_PORT}" > /etc/otelcol/otelcol.yaml
	fi
}

update_otelcol_config

while true
do
	if [ -f /etc/intel_edge_node/tokens/platform-observability-agent/access_token ]; then
		echo "Starting Platform Observability Collector Service"
		break
	else
		sleep 10
	fi
done

exec "$@"
