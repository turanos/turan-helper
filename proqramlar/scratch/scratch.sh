#!/bin/bash
# scratch

pkexec bash << EOF
apt-get update
if ! apt-get install scratch -y;
then
  echo "ERROR"
  exit 1
fi
EOF