#!/bin/bash
# pitivi

pkexec bash << EOF
apt-get update 
if ! apt-get install pitivi -y;
then
  echo "ERROR"
  exit 1
fi
EOF