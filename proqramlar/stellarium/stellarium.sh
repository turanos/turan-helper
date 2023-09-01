#!/bin/bash
# stellarium

pkexec bash << EOF
apt-get update
if ! apt-get install stellarium -y;
then
  echo "ERROR"
  exit 1
fi
EOF