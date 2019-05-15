#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from setuptools import setup, Extension

try:
    from Cython.Build import cythonize

    ext_modules = cythonize([
        Extension("amortization.amount", ["amortization/amount.py"]),
        Extension("amortization.schedule", ["amortization/schedule.py"]),
        Extension("amortization.amortize", ["amortization/amortize.py"]),
    ])
except ImportError:
    ext_modules = None

setup(
    ext_modules=ext_modules
)
