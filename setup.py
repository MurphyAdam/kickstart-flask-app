# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except IOError:
    long_description = ""

setup(
    name="kickstart_flask_app",
    version="0.0.8",
    description="Generate a new Flask app project.",
    license="MIT",
    author="Majdi Mahfoud",
    author_email="elm.majidi@gmail.com",
    url="https://github.com/MurphyAdam/kickstart-flask-app",
    keywords=['Flask', 'template', 'generate'],
    py_modules=["kickstart_flask_app"],
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    zip_safe = False,
    entry_points={
        'console_scripts': [
            'kickstart-flask-app = kickstart_flask_app.KickstartFlaskApp:main'
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires='>=3.6',
)
