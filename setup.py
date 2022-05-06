from setuptools import setup, find_packages

import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

requirements = ["ipython>=6", "colorama>=0.4.4", "matplotlib>=3.5.2", "numpy>=1.22.3", "openpyxl>=3.0.9", "pandas>=1.4.2",
                "scipy>=1.8.0", "statsmodels>=0.13.2", "tabulate>=0.8.9"
]

setup(
    name="pycafee",
    version="0.1",
    author="Anderson Marcos Dias Canteli",
    author_email="andersonmdcanteli@gmail.com",
    description="A package to make life easy",
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
    keywords="statistics, data analisys, sample",  # Optional
)
