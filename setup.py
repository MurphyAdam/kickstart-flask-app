# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except IOError:
    long_description = ""

setup(
    name="create-flask-app",
    version="1.0.0",
    description="Generate a new Flask app project.",
    license="MIT",
    author="Majdi Mahfoud",
    author_email="elm.majidi@gmail.com",
    keywords=['Flask', 'template', 'generate'],
    requires=['Flask', 'gunicorn'],
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires='>=3.6',
)
