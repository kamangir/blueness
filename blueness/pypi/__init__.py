import os
from setuptools import setup as setup_real


def get_long_description(filename: str) -> str:
    repo_path = os.path.dirname(filename)
    repo_name = os.path.basename(repo_path)

    with open(os.path.join(repo_path, "README.md")) as f:
        return f.read().replace(
            "./",
            f"https://github.com/kamangir/{repo_name}/raw/main/",
        )


def get_requirements(filename: str) -> list:
    with open(os.path.join(os.path.dirname(filename), "requirements.txt")) as f:
        return f.read().strip().split("\n")


def setup(
    filename: str,
    **kwargs,
):
    repo_path = os.path.dirname(filename)
    repo_name = os.path.basename(repo_path)

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
        long_description=get_long_description(filename),
        long_description_content_type="text/markdown",
        url=f"https://github.com/kamangir/{repo_name}",
        **kwargs,
    )
