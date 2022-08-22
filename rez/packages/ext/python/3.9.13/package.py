# -*- coding: utf-8 -*-

name = 'python'

version = '3.9.13'

tools = ['python']

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7.9.2009'],
    ['platform-osx', 'arch-x86_64', 'os-osx-12.4'],
    ['platform-windows', 'arch-AMD64', 'os-windows-10.0.19041.SP0']
]

def commands():
    env.PATH.append('{this.root}/bin')

def post_commands():
    # these are the builtin modules for this python executable. If we don't
    # include these, some python behavior can be incorrect.
    import os
    import os.path
    
    path = os.path.join(this.root, "python")  # noqa
    for dirname in os.listdir(path):
        path_ = os.path.join(path, dirname)
        env.PYTHONPATH.append(path_)

timestamp = 1657065011

format_version = 2
