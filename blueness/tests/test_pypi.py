from blueness.pypi import get_long_description, get_requirements


def test_get_long_description():
    assert get_long_description(__file__)


def test_get_requirements():
    assert get_requirements(__file__)
