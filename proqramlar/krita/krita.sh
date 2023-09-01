#!/bin/bash
# krita

pkexec bash << EOF
apt-get update 
if ! apt-get install krita -y;
then
  echo "ERROR"
  exit 1
fi
EOF