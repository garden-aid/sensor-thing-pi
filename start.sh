#!/bin/bash
set -e

udevd &
modprobe i2c-bcm2708
modprobe i2c-dev

. /usr/src/generate-cert.sh

python app.py