#!/usr/bin/env python
# -*- coding: utf-8 -*

# This file should not be needed!
# It's just a temporary workaround to get readthedocs running.
# Sphinx-Scale uses Poetry for packing!

import os
from setuptools import setup, find_packages


setup(
    name='sphinx-scale',
    # If you raise, think about versions in conf.py and needs.py!!!
    version='0.6.0',
    url='http://github.com/useblocks/sphinx-scale',
    download_url='http://pypi.python.org/pypi/sphinx-scale',
    license='MIT',
    author='team useblocks',
    author_email='info@useblocks.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
)
