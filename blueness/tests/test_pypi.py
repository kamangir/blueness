import os
from blueness import pypi


def test_get_long_description():
    assert pypi.get_long_description(__file__, repo_name="blueness")


def test_get_requirements():
    assert pypi.get_requirements(__file__)
