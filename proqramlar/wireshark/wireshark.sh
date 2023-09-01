#!/bin/bash
# wireshark

pkexec bash << EOF
apt-get update
if ! apt-get install wireshark -y;
then
  echo "ERROR"
  exit 1
fi
EOF