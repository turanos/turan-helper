#!/bin/bash
# kdenlive

pkexec bash << EOF
apt-get update 
if ! apt-get install kdenlive -y;
then
  echo "ERROR"
  exit 1
fi
EOF