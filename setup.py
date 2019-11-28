#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup function for the package."""

from setuptools import setup

setup(
  name='gbj_pythonlib_hws',
  version='1.0.0',
  description='Python libraries for hardware simulation.',
  long_description=(
    'Modules suitable for utilizing Pi microcomputers,'
    'system buses, and sensors in python console applications.'
  ),
  classifiers=[
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    'Topic :: System :: Monitoring',
  ],
  keywords='pi, orangepi, raspberrypi, nanopi',
  url='http://github.com/mrkalePythonLib/gbj_pythonlib_hws',
  author='Libor Gabaj',
  author_email='libor.gabaj@gmail.com',
  license='MIT',
  packages=['gbj_pythonlib_hws'],
  install_requires=[],
  include_package_data=True,
  zip_safe=False
)
