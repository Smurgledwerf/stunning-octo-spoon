# -*- coding: utf-8 -*-

name = 'blender'

version = '3.1.0'

variants = [
    ['platform-linux', 'arch-x86_64'],
    ['platform-osx', 'arch-x86_64'],
    ['platform-windows', 'AMD64']
]

cachable = False

def commands():
    import sys
    if sys.platform == 'win32':
        # TODO: figure out how to get aliases to work with rez on windows
        # alias('blender', r"C:\Program Files\Blender Foundation\Blender 3.1\blender.exe")
        env.PATH.append(r"C:\Program Files\Blender Foundation\Blender 3.1")
    elif sys.platform == 'darwin':
        alias('blender', 'open -n -a Blender.app --args')
    elif sys.platform == 'linux2':
        alias('blender', '/software/blender/blender-3.1-linux64/blender')

timestamp = 1639194877

format_version = 2
