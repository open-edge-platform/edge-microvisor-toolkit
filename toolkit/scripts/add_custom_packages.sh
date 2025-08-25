#!/bin/bash
# Copyright (c) Intel Corporation.
# Licensed under the MIT License.

# This script adds a custom package list to an image configuration JSON file.

# $1 - List of packages to be added into image configuration
# $2 - The path to the image configuration JSON file
# $3 - (Optional) Name of the custom package list file. Defaults to "custom-packages.json"

# Usage: 
#   ./add_custom_packages.sh "<package1 package2 ...>" path/to/image.json [custom-packages.json]
#   ./add_custom_packages.sh --verify "<package1 package2 ...>" path/to/image.json [custom-packages.json]

# Example:
#   ./add_custom_packages.sh "nano docker" ../imageconfigs/full.json custom-packages.json
#   ./add_custom_packages.sh --verify "nano docker" ../imageconfigs/full.json custom-packages.json

# Options:
#   --verify   Verifies if the specified packages exist in the custom package list
#              and if the custom package list is included in the image configuration file.

# Parse arguments
VERIFY=false
if [[ "$1" == "--verify" ]]; then
    VERIFY=true
    shift
fi

PACKAGE_LISTS="$1"
IMAGE_JSON="$2"
CUSTOM_PACKAGELIST_NAME="${3:-custom-packages.json}"
CUSTOM_PACKAGELIST_PATH="packagelists/${CUSTOM_PACKAGELIST_NAME}"

# Check if jq is installed
if ! command -v jq >/dev/null 2>&1; then
    echo "Error: jq is not installed." >&2
    exit 1
fi

# Check jq version
JQ_VERSION=$(jq --version | cut -d- -f2)
if [ "$(printf '%s\n' "1.6" "$JQ_VERSION" | sort -V | head -n1)" != "1.6" ]; then
    echo "Error: jq version 1.6 or higher is required. Detected: $JQ_VERSION" >&2
    exit 1
fi

# Validate input arguments
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

# Prepare the package array
NEW_PACKAGES=()
for pkg in $PACKAGE_LISTS; do
    NEW_PACKAGES+=("\"$pkg\"")
done

# Verification logic
if $VERIFY; then
    echo "Verification Results:"
    
    # Check the custom package list file
    if [[ -f "$CUSTOM_PACKAGES_JSON" ]]; then
        MISSING_PACKAGES=()
        for pkg in $PACKAGE_LISTS; do
            if ! jq -e --arg pkg "$pkg" '.packages[] | select(. == $pkg)' "$CUSTOM_PACKAGES_JSON" >/dev/null; then
                MISSING_PACKAGES+=("$pkg")
            fi
        done
        if [[ ${#MISSING_PACKAGES[@]} -eq 0 ]]; then
            echo "- $CUSTOM_PACKAGELIST_NAME: All packages found."
        else
            echo "- $CUSTOM_PACKAGELIST_NAME: Missing packages: ${MISSING_PACKAGES[*]}"
        fi
    else
        echo "- $CUSTOM_PACKAGELIST_NAME: File not found."
    fi

    # Check if the custom packagelist is included in the image JSON
    if jq --arg path "$CUSTOM_PACKAGELIST_PATH" '
      [.. | objects | select(has("PackageLists")) | .PackageLists[]?] | index($path)
    ' "$IMAGE_JSON" | grep -qv null; then
        echo "- $IMAGE_JSON: The custom package list '$CUSTOM_PACKAGELIST_NAME' is included."
    else
        echo "- $IMAGE_JSON: The custom package list '$CUSTOM_PACKAGELIST_NAME' is not included."
    fi

    exit 0
fi

# Check if the custom-packages.json file already exists
if [[ -f "$CUSTOM_PACKAGES_JSON" ]]; then
    echo "Appending to custom package list file '$CUSTOM_PACKAGELIST_NAME'..."
    # Get existing packages
    EXISTING_PACKAGES=$(jq -r '.packages[]' "$CUSTOM_PACKAGES_JSON")
    FILTERED_PACKAGES=()

    # Filter out packages that already exist
    for pkg in "${NEW_PACKAGES[@]}"; do
        if ! echo "$EXISTING_PACKAGES" | grep -q -w "${pkg//\"}"; then
            FILTERED_PACKAGES+=("$pkg")
        fi
    done

    if [[ ${#FILTERED_PACKAGES[@]} -eq 0 ]]; then
        echo "No new packages to add. All packages already exist in '$CUSTOM_PACKAGELIST_NAME'."
    else
        # Append new packages to the existing file
        TMP_JSON=$(mktemp)
        jq --argjson newPackages "$(printf '[%s]' "$(IFS=,; echo "${FILTERED_PACKAGES[*]}")")" '
          .packages += $newPackages | .packages |= unique
        ' "$CUSTOM_PACKAGES_JSON" > "$TMP_JSON" && mv "$TMP_JSON" "$CUSTOM_PACKAGES_JSON"

        # Join the filtered packages into a single string
        FORMATTED_PACKAGES=$(printf '%s ' "${FILTERED_PACKAGES[@]//\"/}" | sed 's/ $//')
        echo "Packages \"$FORMATTED_PACKAGES\" added successfully to '$CUSTOM_PACKAGELIST_NAME'."
    fi
else
    # Create a new custom-packages.json file
    echo "{ \"packages\": [ $(printf '%s,' "${NEW_PACKAGES[@]}" | sed 's/,$//') ] }" | jq . > "$CUSTOM_PACKAGES_JSON"
    echo "Created custom package list file '$CUSTOM_PACKAGES_JSON'."
    echo "Packages \"${NEW_PACKAGES[*]//\"}\" added successfully to '$CUSTOM_PACKAGELIST_NAME'."
fi

# Ensure the custom packagelist is present in the image JSON
if jq --arg path "$CUSTOM_PACKAGELIST_PATH" '
  [.. | objects | select(has("PackageLists")) | .PackageLists[]?] | index($path)
' "$IMAGE_JSON" | grep -qv null; then
    echo "The custom package '$CUSTOM_PACKAGELIST_NAME' already exists in the image configuration file '$IMAGE_JSON'."
else
    # Append to PackageLists arrays in the image JSON
    TMP_JSON=$(mktemp)
    jq --arg path "$CUSTOM_PACKAGELIST_PATH" '
      walk(
        if type == "object" and has("PackageLists") and (.PackageLists | type == "array")
          then .PackageLists += [$path]
          else .
        end
      )
    ' "$IMAGE_JSON" > "$TMP_JSON" && mv "$TMP_JSON" "$IMAGE_JSON"

    echo "The custom package '$CUSTOM_PACKAGELIST_PATH' has been added to PackageLists in '$IMAGE_JSON'."
fi