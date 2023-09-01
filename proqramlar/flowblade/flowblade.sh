#!/bin/bash
# flowblade

pkexec bash << EOF
apt-get update 
if ! apt-get install flowblade -y;
then
  echo "ERROR"
  exit 1
fi
EOF