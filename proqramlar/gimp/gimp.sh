#!/bin/bash
# gimp

pkexec bash << EOF
apt-get update 
if ! apt-get install gimp -y;
then
  echo "ERROR"
  exit 1
fi
EOF