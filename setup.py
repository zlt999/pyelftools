#-------------------------------------------------------------------------------
# pyelftools: setup.py
#
# Setup/installation script.
#
# Eli Bendersky (eliben@gmail.com)
# This code is in the public domain
#-------------------------------------------------------------------------------
import os, sys
from setuptools import setup


try:
    with open('README', 'rt') as readme:
        description = '\n' + readme.read()
except IOError:
    # maybe running setup.py from some other dir
    description = ''


setup(
    # metadata
    name='pyelftools',
    description='Library for analyzing ELF files and DWARF debugging information',
    long_description=description,
    license='Public domain',
    version='0.31.1',
    author='Eli Bendersky',
    maintainer='zlt999',
    author_email='ltzhang999@163.com',
    url='https://github.com/zlt999/pyelftools',
    platforms='Cross Platform',
    classifiers = [
        'Programming Language :: Python :: 3',
        ],

    # All packages and sub-packages must be listed here
    packages=[
        'elftools',
        'elftools.elf',
        'elftools.common',
        'elftools.dwarf',
        'elftools.ehabi',
        'elftools.construct', 'elftools.construct.lib',
        ],

    scripts=['scripts/readelf.py'],
    package_data={'elftools': ['py.typed']}
)
