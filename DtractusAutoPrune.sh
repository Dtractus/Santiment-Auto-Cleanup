#!/bin/bash

# Kullanıcıdan girdilerin alınması
read -p "Enter the disk name (e.g., /dev/sda1): " DISK_NAME
read -p "Enter the maximum disk usage percent (e.g., 90): " MAX_DISK_USAGE_PERCENT

# Gereksinimlerin Kurulumu
sudo apt-get update
sudo apt-get install -y python3 python3-pip git curl

# Python script'inin indirilmesi ve ilgili dizine taşınması
git clone https://github.com/Dtractus/Santiment-Auto-Cleanup.git /$HOME/DtractusAutoPrune
cd /$HOME/DtractusAutoPrune

# Kullanıcının verdiği değerlere göre Python dosyasının güncellenmesi
sed -i "s|DISK_NAME = \"/dev/sda1\"|DISK_NAME = \"${DISK_NAME}\"|g" sanr-cleanup.py
sed -i "s/MAX_DISK_USAGE_PERCENT = 90/MAX_DISK_USAGE_PERCENT = ${MAX_DISK_USAGE_PERCENT}/g" sanr-cleanup.py

# Cron job'ın eklenmesi
(crontab -l 2>/dev/null; echo "0 */6 * * * /$HOME/DtractusAutoPrune/sanr-cleanup.py >> /$HOME/DtractusAutoPrune/DtractusSanrLog.log 2>&1") | crontab -

