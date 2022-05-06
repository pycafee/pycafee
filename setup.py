from setuptools import setup, find_packages
import pathlib

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requirements = ["colorama>=0.4.4", "matplotlib>=3.2.2", "numpy>=1.21.6", "openpyxl>=3.0.9", "pandas>=1.3.5",
                "scipy>=1.4.1", "statsmodels>=0.10.2", "tabulate>=0.8.9"
]

setup(
    name="pycafee",
    version="0.0.3",
    author="Anderson Marcos Dias Canteli",
    author_email="andersonmdcanteli@gmail.com",
    description="A package to make scientific researchers easy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pycafee/pycafee",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    include_package_data=True,
    keywords="statistics, sample analisys",  # Optional
)
