#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from setuptools import setup

VERSION = '0.1.0-rc1'

setup(
    name='amortization',
    version=VERSION,
    py_modules=['amortization'],
    url='https://github.com/roniemartinez/amortization',
    download_url='https://github.com/roniemartinez/amortization/tarball/{}'.format(VERSION),
    license='MIT',
    author='Ronie Martinez',
    author_email='ronmarti18@gmail.com',
    description='Python library for calculating amortizations and generating amortization schedules',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['tabulate==0.8.3'],
    entry_points={
        'console_scripts': ['amortization=amortization:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
