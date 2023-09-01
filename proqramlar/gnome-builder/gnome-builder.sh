#!/bin/bash
# arduino

pkexec bash << EOF
apt-get update 
if ! apt-get install gnome-builder -y;
then
  echo "ERROR"
  exit 1
fi
EOF