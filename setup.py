#!/usr/bin/env python

"""
The setup file.
"""

import os

from setuptools import setup

setup(
    name="python_starter_template",
    version="0.0.1",
    description="A starter template for python projects",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__))), "README.md"
    ).read(),
    long_description_content_type="text/markdown",
    author="Bakare Taofiq",
    packages="python_template",
    install_requires=[
        "setuptools",
    ],
)
