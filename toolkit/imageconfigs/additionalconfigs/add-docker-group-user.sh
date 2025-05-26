#!/bin/bash
set -e

# Create docker group if it doesn't exist
if ! getent group docker > /dev/null; then
    groupadd docker
fi

# Add guest to docker group
usermod -aG docker guest