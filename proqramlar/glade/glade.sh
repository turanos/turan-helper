#!/bin/bash
# glade 

pkexec bash << EOF
apt-get update 
if ! apt-get install glade -y;
then
  echo "ERROR"
  exit 1
fi
EOF