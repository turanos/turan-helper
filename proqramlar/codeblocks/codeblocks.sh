#!/bin/bash
# codeblocks

pkexec bash << EOF
apt-get update
if ! apt-get install codeblocks -y;
then
  echo "ERROR"
  exit 1
fi
EOF