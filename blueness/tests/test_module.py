from blueness import module, NAME


def test_module_name():
    assert isinstance(
        module.name(__file__, NAME),
        str,
    )
