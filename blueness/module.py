import os


def name(
    filename: str,
    module_name: str,
) -> str:
    relative_path = filename.split(f"{module_name}{os.sep}", 1)[1]

    if relative_path.endswith(".py"):
        relative_path = relative_path[:-3]

    hierarchy = [item for item in relative_path.split(os.sep)]

    return ".".join([module_name] + hierarchy)
