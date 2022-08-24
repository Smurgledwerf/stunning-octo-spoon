
# Rez Directory Structure
This is a recommended directory structure to use with rez on multiple platforms.
Note: for windows and macos, python should be installed locally. It can be done with a "portable" python on the network,
but that's so much slower.

Note for macos with the new m1 chip: there are still many issues with this cpu architecture, so you will likely need to
install rosetta and prefix every rez command with arch -x86_64

# Installing Rez
Rez is actually just a bunch of python scripts in a trench coat, so the first requirement is a python interpreter.
Pick a python version and make sure it's installed locally on every computer (or network-installed for linux), I'll use
python-3.9 as an example.

IMPORTANT: make sure it's a standard install for every user (requires admin), so "C:\Program Files\Python39" on windows
or "/Library/Frameworks/Python.framework/Versions/3.9" for macos, not installed to a user's home directory.

Next, run the install.py script for every platform you plan to use. Example on linux:
/path/to/python39 ./install.py -v /path/to/rez/linux 

Follow the quickstart steps on the rez github page to set up your operating system, CPU architecture, and platform
packages. This needs to be done for every operating system version that you'll use, ex. osx-12.4 is distinct from
osx-12.5. By default they will install to your home directory, so to install them as real packages, do
rez-bind -i /path/to/rez/packages/ext platform . Rez will automatically create the folders and organize them.

# Python as a Rez Package
One of the most important rez packages you will need is python. This can be a bit tricky to set up, especially on
windows and macos. On each operating system, do

rez-bind -i /path/to/rez/packages/ext python --exe /path/to/python39

This will create different variants for every combination of platform, CPU architecture, and operating system version.
This rez package is special because it will create an alias to the python executable that you passed as an argument
and add it to $PATH. That way no matter what platform you're on, the python alias will point to the specific python
version executable that you requested. For windows and macos, it is very important that python is installed locally,
otherwise the python alias will not work.

Note: this needs to be done for every python version you want to use, on every platform you want to use.

# 3rd Party Packages
For python packages that are pip-installable from PyPi, simply do:
1. rez-pip --install <package>
1. this installs it to your ~/packages directory
1. do a quick test to make sure it all works
1. release it to the python packages directory:
`rez-pip --python-version 3.9 --install --release --prefix /path/to/rez/packages/python <package>`

# Releases
To release internal packages, make sure you merge your changes into your upstream repository then do the following:
1. In your clone, checkout the main branch and run `rez-release`. This will
    1. pull the upstream main branch
    1. run a rez-build locally
    1. deploy it to the path defined by the $REZ_RELEASE_PACKAGES_PATH
1. If you run into an error `fatal: no upstream configured for branch 'main'` then you likely need to do:
    1. git push --set-upstream upstream main
1. If you run into a permission error `git@github.com: Permission denied (publickey)` then run these commands:
    1. eval "$(ssh-agent -s)"
    1. ssh-add

