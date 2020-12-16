#!/usr/bin/python
# -*- coding: utf-8 -*-
from string import Template
from textwrap import dedent

wsgi_template = Template(dedent("""\
    # -*- coding: utf-8 -*-
    from ${app_name} import create_app

    app = create_app()

    """))

procfile_template = Template(dedent("""\
    web: gunicorn wsgi:app

    """))

tests_template = Template(dedent("""\
    import unittest

    # write your tests here
    """))


app_init_template = Template(dedent("""\
    import logging, os
    from logging.handlers import SMTPHandler, RotatingFileHandler
    from flask import Flask
    from config import Config, Development

    def config_class():
        env = os.environ.get('APP_ENV') or os.environ.get('FLASK_ENV')
        if env == 'development':
            return Development
        elif env == 'production':
            return Config
        else:
            raise EnvironmentError("No APP_ENV or FLASK_ENV is not set! Please set one.")


    def create_app(config_class=config_class()):
        # Construct the core application.
        app = Flask(__name__, instance_relative_config=False)
        # Application Configuration
        app.config.from_object(config_class)
        with app.app_context():
            # Reginter API BP
            from ${app_name}.${main_bp_name} import ${main_bp_name}
            app.register_blueprint(${main_bp_name}, url_prefix='/')
            # Configute Debugging
            if app.debug or app.testing:
                if app.config['LOG_TO_STDOUT']:
                    stream_handler = logging.StreamHandler()
                    stream_handler.setLevel(logging.INFO)
                    app.logger.addHandler(stream_handler)
                else:
                    if not os.path.exists('logs'):
                        os.mkdir('logs')
                    file_handler = RotatingFileHandler(f'logs/{app.config["APP_NAME"]}.log',
                                                       maxBytes=20480, backupCount=20)
                    file_handler.setFormatter(logging.Formatter(
                        '%(asctime)s %(levelname)s: %(message)s '
                        '[in %(pathname)s:%(lineno)d]'))
                    file_handler.setLevel(logging.INFO)
                    app.logger.addHandler(file_handler)
                app.logger.setLevel(logging.INFO)
                app.logger.info(f'{app.config["APP_NAME"]} startup')
            return app

    """))

main_bp_routes_template = Template(dedent("""\
    from ${app_name}.${main_bp_name} import ${main_bp_name}

    @${main_bp_name}.route('/')
    def Hello():
        return 'Hello world!', 200

    """))

main_bp_init_template = Template(dedent("""\
    from flask import Blueprint
    ${main_bp_name} = Blueprint('${main_bp_name}', __name__)
    from ${app_name}.${main_bp_name} import routes

    """))

requirements_template = Template(dedent("""\
    flask
    gunicorn

    """))

config_template = Template(dedent("""\
    import os

    '''
        Flask config classes.
        All config classes inherit from the base class
        Config.

    '''

    basedir = os.path.abspath(os.path.dirname(__file__))

    class Config(object):
        #Set Flask configuration vars.

        '''
        App name and runtime
        '''
        PROJECT_NAME = '${project_name}'
        APP_NAME = '${app_name}'
        APP_RUNTIME = '${runtime}'

        '''
        Environment variabbles
        '''

        APP_ENV = os.environ.get('APP_ENV') or 'production'
        FLASK_ENV = os.environ.get('APP_ENV') or 'production'
        TESTING = os.environ.get('TESTING') or False
        DEBUG = os.environ.get('DEBUG') or False


        LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT') or False
        SECRET_KEY = os.environ.get('SECRET_KEY') or b'your_secrete_key'

    class Development(Config):

        '''
        Environment variabbles
        '''
        
        APP_ENV = os.environ.get('APP_ENV') or 'development'
        FLASK_ENV = os.environ.get('APP_ENV') or 'development'
        TESTING = os.environ.get('TESTING') or False
        DEBUG = os.environ.get('DEBUG') or True

        LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT') or True
        SECRET_KEY = os.environ.get('SECRET_KEY') or b'your_secrete_key'

    """))

runtime_template = Template(dedent("""\
    python-${runtime}

    """))

bashrc_template = Template(dedent("""\
    EXPORT FLASK_ENV='development'
    EXPORT FLASK_APP='development'

    """))