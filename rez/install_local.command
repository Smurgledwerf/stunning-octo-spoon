#!/usr/bin/env bash

python39=/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# check for python 3.9
if [ ! -f $python39 ]; then
    read -s -p "Missing python 3.9 at ${python39}"
    exit
fi

# check if rez is already installed
if [ -f ~/Applications/rez/bin/rez/.rez_production_install ]; then
    read -s -p "Rez is already installed!"
    exit
fi

install_script="/Volumes/path/to/rez/config/rez_src-2.111.2/install.py"
echo 'Installing rez locally, this can take a while...'
$python39 $install_script -v "~/Applications/rez"

# double check if rez installed correctly
if [ ! -f ~/Applications/rez/bin/rez/.rez_production_install ]; then
    read -s -p "Error occurred installing rez, check the error message above."
    exit
fi

read -s -p "Rez successfully installed!"

