from setuptools import setup, find_packages
from pathlib import Path

CURRENT_DIR = Path(__file__).parent


def get_long_description() -> str:
    return (
        (CURRENT_DIR / "README.md").read_text(encoding="utf8")
    )

setup(
    name="cmlint",
    use_scm_version={
        "write_to": "cmlint/_cmlint_version.py",
        "write_to_template": 'version = "{version}"\n',
    },
    description="The commit message linter.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Aleix Alcacer",
    author_email="aleixalcacer@gmail.com",
    url="https://github.com/aleixalcacer/cmlint",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "click>=8.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    entry_points={
        "console_scripts": [
            "cmlint=cmlint.command_line:main",
        ]
    },
)
