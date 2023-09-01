#!/bin/bash
# nmap

pkexec bash << EOF
apt-get update
if ! apt-get install nmap -y;
then
  echo "ERROR"
  exit 1
fi
EOF