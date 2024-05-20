from setuptools import setup
import os

from blueness import NAME, VERSION, DESCRIPTION
from blueness.pypi import get_long_description, get_requirements


setup(
    name=NAME,
    author="arash@kamangir.net",
    author_email="arash@kamangir.net",
    version=VERSION,
    description=DESCRIPTION,
    long_description=get_long_description(__file__),
    long_description_content_type="text/markdown",
    url="https://github.com/kamangir/blue-plugin",
    packages=[NAME],
    package_data={
        NAME: ["config.env"],
    },
    install_requires=get_requirements(__file__),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Unix Shell",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    license="Public Domain",
)
