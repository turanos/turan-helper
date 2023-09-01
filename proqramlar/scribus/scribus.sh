#!/bin/bash
# scribus

pkexec bash << EOF
apt-get update
if ! apt-get install scribus -y;
then
  echo "ERROR"
  exit 1
fi
EOF