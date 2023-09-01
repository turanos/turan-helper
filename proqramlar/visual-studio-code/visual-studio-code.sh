#!/bin/bash
# visual-studio-code

pkexec bash << EOF
apt-get update 
apt install curl gpg
curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
apt-get update
if ! apt-get install code -y;
then
  echo "ERROR"
  exit 1
fi
EOF