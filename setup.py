#!/usr/bin/env python3
from setuptools import setup

setup(
    name="tap-contentful",
    version="0.1.1",
    description="Singer.io tap for extracting data",
    author="Simon Data",
    url="http://simondata.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_contentful"],
    python_requires=">=3.9",
    install_requires=[
        "singer-python>=6,<7",
        "requests>=2.31,<3",
        "pendulum>=3,<4",
        "tap-kit @ git+https://github.com/Radico/tap-kit.git@main",
    ],
    entry_points="""
    [console_scripts]
    tap-contentful=tap_contentful:main
    """,
    packages=["tap_contentful"],
    include_package_data=True,
)
