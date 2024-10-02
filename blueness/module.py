import os


def name(
    filename: str,
    module_name: str,
) -> str:
    assert (
        module_name in filename
    ), f'is NAME imported correctly? module name "{module_name}" is not in the filename "{filename}"!'

    relative_path = filename.split(f"{module_name}{os.sep}", 1)[1]

    if relative_path.endswith(".py"):
        relative_path = relative_path[:-3]

    hierarchy = [item for item in relative_path.split(os.sep)]

    hierarchy = [item for item in hierarchy if item not in ["__main__"]]

    return ".".join([module_name] + hierarchy)
