#!/usr/bin/sh

set -eu

if [ -n "$CADDY_APT_PROXY_URL" ]; then
    # this tmpfile is needed because of read-only root filesystem, except for
    # intel_manageability.conf is a bind mount
    tmpfile=$(mktemp /tmp/tempfile.XXXXXX)
    sed "s|https://EMT_FQDN\.example\.com/|https://$CADDY_APT_PROXY_URL|g" /etc/intel_manageability.conf > "$tmpfile"
    cp "$tmpfile" /etc/intel_manageability.conf    
fi
