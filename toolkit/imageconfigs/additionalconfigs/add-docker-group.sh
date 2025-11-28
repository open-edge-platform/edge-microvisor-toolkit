#!/bin/bash
set -e

if id "guest" &>/dev/null; then
    usermod -aG docker guest
fi
