#!/bin/bash
# atom

pkexec bash << EOF
wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/atomeditor-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/atomeditor-keyring.gpg] https://packagecloud.io/AtomEditor/atom/any/ any main" | sudo tee /etc/apt/sources.list.d/atom.list
apt-get update 
if ! apt-get install atom -y;
then
  echo "ERROR"
  exit 1
fi
EOF