# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    desc = fh.read()
    title_index = desc.find("# niobium")
    long_description = desc[title_index:]  # remove bagde

setuptools.setup(
    name="niobium",
    version="0.0.1",
    author="cle-b",
    author_email="cle@tictac.pm",
    description="Niobium extends Selenium for simplify web automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cle-b/niobium",
    packages=setuptools.find_packages(),
    python_requires=">=3.4",
    install_requires=["selenium"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
