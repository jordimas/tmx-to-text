import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="tmx-to-text",
    version="0.1.5",
    description="Converts TMX files to text files",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jordimas/tmx-to-text",
    author="Jordi Mas",
    author_email="jmas@softcatala.org",
    license="GPLv2+",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["src/tmx_to_text"],
    include_package_data=True,
    install_requires=["lxml"],
    entry_points={
        "console_scripts": [
            "tmx-to-text=src.tmx_to_text.tmx_to_text:main",
        ]
    },
)

