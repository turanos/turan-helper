#!/bin/bash
# openboard

pkexec bash << EOF
apt-get update
if ! apt-get install openboard -y;
then
  echo "ERROR"
  exit 1
fi
EOF