#!/bin/bash

pip install docker

read -p "Enter the disk name (e.g., /dev/sda1): " DISK_NAME
read -p "Enter the maximum disk usage percent (e.g., 90): " MAX_DISK_USAGE_PERCENT

SANR_CLEANUP_PATH="$HOME/DtractusAutoPrune/sanr-cleanup.py"
sed -i "s|DISK_NAME = \".*\"|DISK_NAME = \"$DISK_NAME\"|g" $SANR_CLEANUP_PATH
sed -i "s/MAX_DISK_USAGE_PERCENT = .*/MAX_DISK_USAGE_PERCENT = $MAX_DISK_USAGE_PERCENT/g" $SANR_CLEANUP_PATH


(crontab -l | grep -v 'sanr-cleanup.py'; echo "0 */6 * * * /usr/bin/python3 $SANR_CLEANUP_PATH >> $HOME/DtractusAutoPrune/DtractusSanrLog.log 2>&1") | crontab -

if ! grep -q '#!/usr/bin/python3' $SANR_CLEANUP_PATH; then
    sed -i '1s|^|#!/usr/bin/python3\n|' $SANR_CLEANUP_PATH
fi

chmod +x $SANR_CLEANUP_PATH
