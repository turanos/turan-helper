#!/bin/bash
# metasploit

pkexec bash << EOF
apt-get update
if ! gem --version;
then
  pkexec apt-get install rubygems -y
fi
echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" | pkexec tee /etc/apt/sources.list.d/kali.list
apt-key adv --recv-keys --keyserver hkp://keys.gnupg.net 7D8D0BF6
echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list.d/kali-rolling.list
apt-get update
if ! apt-get install metasploit-framework -y;
then
  echo "ERROR"
  exit 1
fi
EOF