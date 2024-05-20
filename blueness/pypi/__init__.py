import os


def get_long_description(filename: str) -> str:
    with open(os.path.join(os.path.dirname(filename), "README.md")) as f:
        return f.read().replace(
            "./",
            "https://github.com/kamangir/giza/raw/main/",
        )


def get_requirements(filename: str) -> list:
    with open(os.path.join(os.path.dirname(filename), "requirements.txt")) as f:
        return f.read().strip().split("\n")
