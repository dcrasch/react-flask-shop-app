from flask import Flask
import connexion
from connexion.options import SwaggerUIOptions

from .config import DefaultConfig
from .extensions import db
from .commands import initdb

DEFAULT_BLUEPRINTS = (
    # products,
    # orders
)


def create_app(config=None, app_name=None, blueprints=None):
    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    ## TODO: swagger naming conflict
    ## options = SwaggerUIOptions()

    application = connexion.FlaskApp("rfs", specification_dir="spec/")
    application.add_api(
        "swagger.yaml", base_path="/api"
    )  ## TODO: ,  swagger_ui_options=options)

    app = application.app

    configure_app(app, config)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_error_handlers(app)

    configure_command(app)

    return application  # or app??


def configure_app(app, config=None):
    # Different ways of configurations i.e local or production

    app.config.from_object(DefaultConfig)

    app.config.from_pyfile("production.cfg", silent=True)

    if config:
        app.config.from_object(config)


def configure_extensions(app):
    # flask-sqlalchemy
    db.init_app(app)


def configure_blueprints(app, blueprints):
    # Configure blueprints in views

    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_command(app):
    app.cli.add_command(initdb)


def configure_error_handlers(app):
    @app.errorhandler(403)
    def forbidden_page(error):
        return "Oops! You don't have permission to access this page.", 403

    @app.errorhandler(404)
    def page_not_found(error):
        return "Oops! Page not found.", 404

    @app.errorhandler(500)
    def server_error_page(error):
        return "Oops! Internal server error. Please try after sometime.", 500
