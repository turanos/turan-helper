#!/bin/bash
# qt creator

pkexec bash << EOF
apt-get update 
if ! apt-get install qtcreator -y;
then
  echo "ERROR"
  exit 1
fi
EOF