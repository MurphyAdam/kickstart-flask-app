from setuptools import setup, find_packages

setup(
    name="kickstart_flask_app",
    version="1.1.5",
    description="Generate a new Flask app project.",
    license="MIT",
    author="Majdi Mahfoud",
    author_email="elm.majidi@gmail.com",
    url="https://github.com/MurphyAdam/kickstart-flask-app",
    keywords=['Flask', 'template', 'generate'],
    packages=find_packages(),
    install_requires=[
        'flask',
    ],
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
