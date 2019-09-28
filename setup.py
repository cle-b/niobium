# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    desc = fh.read()
    title_index = desc.find("# Niobium")
    long_description = desc[title_index:]  # remove bagde

setuptools.setup(
    name="niobium",
    version="0.3.1",
    author="cle-b",
    author_email="cle@tictac.pm",
    description="Niobium extends the Python Selenium client with nice features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cle-b/niobium",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=["selenium", "opencv-python", "pillow"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
)
