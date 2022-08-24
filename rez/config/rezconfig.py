# Rez config options that override the defaults in rez-src-2.#.#\src\rez\rezconfig.py
# You can further customize by including a .rezconfig file in your home dir.

import sys

# The package search path. Rez uses this to find packages. A package with the
# same name and version in an earlier path takes precedence.
packages_path = [
    "~/packages",           # locally installed pkgs, not yet deployed
    "/path/to/rez/packages/int",  # internally developed pkgs, deployed
    "/path/to/rez/packages/ext",  # external (3rd party) pkgs, such as houdini, boost
    "/path/to/rez/packages/python",  # pip-installable python packages from pypi
]
# Note: don't worry about the syntax, this will be addressed per OS

# The path that Rez will locally install packages to when rez-build is used
local_packages_path = "~/packages"

# The path that Rez will deploy packages to when rez-release is used. For
# production use, you will probably want to change this to a site-wide location.
release_packages_path = "/path/to/rez/packages/int"

# Search path for rez plugins.
plugin_path = ["/path/to/rez/config/plugins/rez-default-build"]

# Whether a package is cachable or not, if it does not explicitly state with
# the 'cachable' attribute in its package definition file. If None, defaults
# to packages' relocatability (ie cachable will == relocatable).
default_cachable = True

def _cache_packages_path():
    if sys.platform == 'win32':
        return r'C:\rez_cache'
    elif sys.platform == 'darwin':
        return '~/rez_cache'
    elif sys.platform == 'linux2':
        return None  # TODO: add the linux cache path here
    return None

# The path where rez locally caches variants. If this is None, then package
# caching is disabled.
cache_packages_path = _cache_packages_path()

