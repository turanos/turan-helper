#!/bin/bash
# tuxmath

pkexec bash << EOF
apt-get update 
if ! apt-get install tuxmath -y;
then
  echo "ERROR"
  exit 1
fi
EOF