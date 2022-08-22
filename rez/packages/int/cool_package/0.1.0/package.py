# -*- coding: utf-8 -*-

name = 'cool_package'

version = '0.1.0'

authors = ['Cool Person']

description = "Does cool things"

requires = [
    'python-3',
    'PySide2',
]

build_system = 'default'

@late()
def cachable():
    import os
    return os.path.join('rez', 'packages', 'test') not in this.base.lower()

def commands():
    env.PYTHONPATH.append("{root}")

format_version = 2
