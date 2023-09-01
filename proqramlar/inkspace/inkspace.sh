#!/bin/bash
# inkspace

pkexec bash << EOF
apt-get update 
if ! apt-get install inkspace -y;
then
  echo "ERROR"
  exit 1
fi
EOF