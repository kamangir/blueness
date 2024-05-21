import os
from blueness import pypi


def test_get_long_description():
    assert pypi.get_long_description(__file__)


def test_get_requirements():
    assert pypi.get_requirements(__file__)


def test_get_repo_name():
    filename = pypi.find_file(os.path.dirname(__file__), "README.md")

    assert pypi.get_repo_name(filename) == "blueness"
