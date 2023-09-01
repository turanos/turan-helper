#!/bin/bash
# arduino

pkexec bash << EOF
apt-get update 
if ! apt-get install arduino -y;
then
  echo "ERROR"
  exit 1
fi
EOF