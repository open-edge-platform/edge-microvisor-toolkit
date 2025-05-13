#!/bin/bash

while true
do
	if [ -e /run/platform-observability-agent/platform-observability-agent.sock ]; then
		echo "Starting Platform Observability Metrics Service"
		break
	else
		sleep 10
	fi
done

exec "$@"
