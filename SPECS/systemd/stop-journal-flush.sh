#!/bin/bash
if [ -x /usr/bin/systemctl ]; then
    /usr/bin/systemctl stop systemd-journal-flush.service >/dev/null 2>&1 || :
fi
