#!/bin/bash
# thonny


pkexec bash << EOF
mkdir -p /tmp/.pacperro-recommender_thonny
cd /tmp/.pacperro-recommender_thonny
if ! wget https://github.com/thonny/thonny/releases/download/v4.0.2/thonny-4.0.2-x86_64.tar.gz -y;
then
  echo "ERROR"
  exit 1
fi
tar -xf thonny-$thonny_version-x86_64.tar.gz
cd thonny
python3 install.py
cd ..
cd ..
rm -r .pacperro-recommender_thonny
exit
EOF