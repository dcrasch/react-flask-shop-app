# -*- coding: utf-8 -*-
import sys
import os

from flask.ext.script import Manager

from rfs.app import create_app

app = create_app(config=os.environ.get('APP_CONFIG', 'rfs.config.DevelopmentConfig'))
manager = Manager(app)

@manager.command
def run():
    """
    Run the application.  If the environment variable `APP_CONFIG` is not set,
    then the default development config `flaskplate.config.DevelopmentConfig`
    will be used.
    To set the path to a different development config:
        export APP_CONFIG=python.path.to.my.ConfigClass
        python manage.py run
    """
    app.run()

if __name__ == "__main__":
    manager.run()
