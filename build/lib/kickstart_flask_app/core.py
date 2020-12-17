#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import version_info
from getpass import getuser
import os

from .templates import (wsgi_template,
    procfile_template,
    tests_template,
    app_init_template,
    main_bp_routes_template,
    main_bp_init_template,
    requirements_template, 
    config_template,
    runtime_template)

class KickstartFlaskApp():

    def __init__(self):
        self.project_name: str = 'Hello-Flask'
        self.root_app_name: str = 'server'
        self.app_version: float = 1.0
        self.description: str = ''
        self.author: str = getuser()
        self.main_bp_name: str = 'main_bp'
        self.setup_heroku_deployment_files: str = 'yes'
        self.fields_names = [f'Project name. Default ({self.project_name})', 
            f'Root app name. Default ({self.root_app_name})', 
            f'App version. Default ({self.app_version})', 
            f'Description. Default ({self.description})', 
            f'Author. Default ({self.author})', 
            f'Main Blueprint name. Default ({self.main_bp_name})', 
            f'Setup Heroku deployment files. Default ({self.setup_heroku_deployment_files})']
        self.runtime: str = ".".join(map(str, version_info[:3]))
        self.flask_files = ['wsgi.py', 
            '__init__.py', 
            'routes.py', 
            '__init__.py', 
            'config.py', 
            'tests.py', 
            'requirement.txt'
        ]
        self.flask_files_paths = []
        self.flask_files_templates = []

        self.heroku_files = ['runtime.txt', 'Procfile']
        self.heroku_files_paths = []
        self.heroku_files_templates = []

    def get_input(self, input_msg, default=None):
        if version_info >= (3, 0):
            input_value = input(f'{input_msg}: ')
        else:
            input_value = raw_input(input_msg.encode('utf8')).decode('utf8')

        if input_value == '':
            return default
        return input_value


    def write_content(self, file, content, path) -> None:
        with open(f'{path}/{file}', 'w') as file:
            if version_info >= (3, 0):
                file.write(content)
            else:
                file.write(content.encode('utf8'))

    def create_project_structure(self) -> None:
        path = f'{self.project_name}/{self.root_app_name}/{self.main_bp_name}'
        os.makedirs(path, exist_ok=True)

    def populate_project_files(self) -> None:
        for flask_file, flask_file_path, flask_file_template in zip(self.flask_files, 
            self.flask_files_paths,
            self.flask_files_templates):
            self.write_content(flask_file, flask_file_template, flask_file_path)

    def setup_heroku_files(self) -> None:
        for heroku_file, heroku_file_path, heroku_file_template in zip(self.heroku_files, 
            self.heroku_files_paths,
            self.heroku_files_templates):
            self.write_content(heroku_file, heroku_file_template, heroku_file_path)

    def main(self):

        self.project_name = self.get_input(f'Project name. Default ({self.project_name})', 
            default=self.project_name)
        self.root_app_name = self.get_input(f'Root app name. Default ({self.root_app_name})', 
            default=self.root_app_name)
        self.app_version = self.get_input(f'App version. Default ({self.app_version})', 
            default=self.app_version)
        self.description = self.get_input(f'Description. Default ({self.description})', 
            default=self.description)
        self.author = self.get_input(f'Author. Default ({self.author})', 
            default=self.author)
        self.main_bp_name = self.get_input(f'Main Blueprint name. Default ({self.main_bp_name})', 
            default=self.main_bp_name)
        self.setup_heroku_deployment_files = self.get_input(f'Setup Heroku deployment files (yes/no). Default ({self.setup_heroku_deployment_files})', 
            default=self.setup_heroku_deployment_files)
        
        self.flask_files_paths = [f'{self.project_name}', 
            f'{self.project_name}/{self.root_app_name}', 
            f'{self.project_name}/{self.root_app_name}/{self.main_bp_name}', 
            f'{self.project_name}/{self.root_app_name}/{self.main_bp_name}', 
            f'{self.project_name}', 
            f'{self.project_name}', 
            f'{self.project_name}'
        ]

        self.flask_files_templates = [wsgi_template.substitute(app_name=self.root_app_name), 
            app_init_template.substitute(app_name=self.root_app_name, main_bp_name=self.main_bp_name) , 
            main_bp_routes_template.substitute(app_name=self.root_app_name, main_bp_name=self.main_bp_name), 
            main_bp_init_template.substitute(app_name=self.root_app_name, main_bp_name=self.main_bp_name), 
            config_template.substitute(app_name=self.root_app_name, project_name=self.project_name, runtime=self.runtime), 
            tests_template.substitute(), 
            requirements_template.substitute()
        ]

        self.create_project_structure()
        self.populate_project_files()

        if 'y'.lower() in self.setup_heroku_deployment_files:
            self.heroku_files_paths = [f'{self.project_name}'] * len(self.heroku_files)
            self.heroku_files_templates = [runtime_template.substitute(runtime=self.runtime), 
                procfile_template.substitute()
            ]
            self.setup_heroku_files()

def console() -> None:
    kickstart_flask_app = KickstartFlaskApp()
    kickstart_flask_app.main()

if __name__ == '__main__':
    kickstart_flask_app = KickstartFlaskApp()
    kickstart_flask_app.main()
