# kickstart-flask-app

This is a simple package to kickstart a new Flask app project

## Install

```bash
pip Install kickstart-flask-app
```

## Usage

you could use this package in two ways:

1. The Python interpreter

```bash
python
```

```python

from kickstart_flask_app import KickstartFlaskApp

create_app = KickstartFlaskApp()
create_app.main()

```
The above will propmt you to enter some data, press enter to use defaults. 
This will create a new Flask project in the path you run the python interpreter

2. Command line (recommended)

```bash
kickstart-flask-app
```
once you have installed the package, it also provides a command line command in your terminal: `kickstart-flask-app`
This, just as the Python interpreter will prompt the same. This is much quicker than importing all 
the code yourself.

## Github repository
[kickstart-flask-app](https://github.com/MurphyAdam/kickstart-flask-app)
