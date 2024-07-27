import os


def name(
    filename: str,
    module_name: str,
) -> str:
    return ".".join(
        [module_name]
        + filename.split(
            f"{module_name}{os.sep}",
            1,
        )[1].split(
            os.sep
        )[:-1]
    )
