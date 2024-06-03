import os
from setuptools import setup as setup_real
from typing import Tuple


def find_file(path: str, filename: str) -> str:
    safety_counter = 0
    while True:
        full_filename = os.path.join(path, filename)
        if os.path.exists(full_filename):
            return full_filename

        path = os.path.dirname(path)

        safety_counter += 1

        if path == "/" or safety_counter > 20:
            raise FileNotFoundError(filename)


def get_long_description(
    filename: str,
    repo_name: str,
) -> str:
    filename = find_file(os.path.dirname(filename), "README.md")

    with open(filename) as f:
        return f.read().replace(
            "./",
            "https://raw.githubusercontent.com/kamangir/{}/{}/".format(
                repo_name,
                "current" if repo_name == "awesome-bash-cli" else "main",
            ),
        )


def get_requirements(filename: str) -> list:
    filename = find_file(os.path.dirname(filename), "requirements.txt")

    with open(filename) as f:
        requirements = f.read().strip().split("\n")

    return [item for item in requirements if "git+https:" not in item]


def setup(
    filename: str,
    repo_name: str,
    **kwargs,
):
    setup_real(
        author="Arash Abadpour (Kamangir)",
        author_email="arash@kamangir.net",
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Unix Shell",
            "License :: Public Domain",
            "Operating System :: OS Independent",
        ],
        install_requires=get_requirements(filename),
        license="Public Domain",
        long_description=get_long_description(filename, repo_name),
        long_description_content_type="text/markdown",
        url=f"https://github.com/kamangir/{repo_name}",
        **kwargs,
    )
