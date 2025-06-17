#!/bin/bash
# Copyright (c) Intel Corporation.
# Licensed under the MIT License.

# This script adds a custom package list to an image configuration JSON file.

# $1 - List of packages to be added into image configuration
# $2 - The path to the image configuration JSON file
# $3 - (Optional) Name of the custom package list file. Defaults to "custom-packages.json"

# Usage: 
#   ./add_custom_packages.sh "<package1 package2 ...>" path/to/image.json [custom-packages.json]

# Example:
#   ./add_custom_packages.sh "nano docker" ../imageconfigs/full.json custom-packages.json

PACKAGE_LISTS="$1"
IMAGE_JSON="$2"
CUSTOM_PACKAGELIST_NAME="${3:-custom-packages.json}"
CUSTOM_PACKAGELIST_PATH="packagelists/${CUSTOM_PACKAGELIST_NAME}"

if ! command -v jq >/dev/null 2>&1; then
    echo "Error: jq is not installed." >&2
    exit 1
fi

JQ_VERSION=$(jq --version | cut -d- -f2)
if [ "$(printf '%s\n' "1.6" "$JQ_VERSION" | sort -V | head -n1)" != "1.6" ]; then
    echo "Error: jq version 1.6 or higher is required. Detected: $JQ_VERSION" >&2
    exit 1
fi

if [[ -z "$PACKAGE_LISTS" || -z "$IMAGE_JSON" ]]; then
    echo "Usage: $0 \"<pkg1 pkg2 ...>\" path/to/image.json [custom-packages.json]" >&2
    exit 1
fi

if [[ ! -f "$IMAGE_JSON" ]]; then
    echo "Error: IMAGE JSON file '$IMAGE_JSON' does not exist." >&2
    exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$SCRIPT_DIR/.."
PACKAGELIST_DIR="$BASE_DIR/imageconfigs/packagelists"
CUSTOM_PACKAGES_JSON="$PACKAGELIST_DIR/$CUSTOM_PACKAGELIST_NAME"

mkdir -p "$PACKAGELIST_DIR"
PKG_ARRAY=$(for pkg in $PACKAGE_LISTS; do printf '"%s", ' "$pkg"; done | sed 's/, $//')
echo "{ \"packages\": [ $PKG_ARRAY ] }" | jq . > "$CUSTOM_PACKAGES_JSON"
echo "Created $CUSTOM_PACKAGES_JSON"

# Check if the custom packagelist is already present
if jq --arg path "$CUSTOM_PACKAGELIST_PATH" '
  [.. | objects | select(has("PackageLists")) | .PackageLists[]?] | index($path)
' "$IMAGE_JSON" | grep -qv null; then
    echo "'$CUSTOM_PACKAGELIST_PATH' is already present in PackageLists in $IMAGE_JSON."
    echo "No changes made."
    exit 0
fi

# Append to all PackageLists arrays
TMP_JSON=$(mktemp)
jq --arg path "$CUSTOM_PACKAGELIST_PATH" '
  walk(
    if type == "object" and has("PackageLists") and (.PackageLists | type == "array")
      then .PackageLists += [$path]
      else .
    end
  )
' "$IMAGE_JSON" | jq . > "$TMP_JSON" && mv "$TMP_JSON" "$IMAGE_JSON"

echo "Appended '$CUSTOM_PACKAGELIST_PATH' to all PackageLists in $IMAGE_JSON"
