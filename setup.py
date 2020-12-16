# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="kickstart_flask_app",
    version="1.1.3",
    description="Generate a new Flask app project.",
    license="MIT",
    author="Majdi Mahfoud",
    author_email="elm.majidi@gmail.com",
    url="https://github.com/MurphyAdam/kickstart-flask-app",
    keywords=['Flask', 'template', 'generate'],
    py_modules=["kickstart_flask_app"],
    packages=find_packages(),
    install_requires=[],
    long_description='Please refer to README for docs',
    zip_safe = False,
    entry_points={
        'console_scripts': [
            'kickstart-flask-app = kickstart_flask_app:console'
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires='>=3.6',
)
