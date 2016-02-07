import os
import datetime
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment, Bundle
from flask.ext.restless import APIManager
from flask_admin import Admin

from rfs.config import DefaultConfig

db = SQLAlchemy()
assets = Environment()

from rfs.products.views import products
from rfs.orders.views import orders

DEFAULT_BLUEPRINTS = (
    products, orders
)

from rfs.products.models import Product, ProductVariant
from rfs.orders.models import Order

DEFAULT_API_MODELS = (
    Product,
    ProductVariant,
    Order
)


from rfs.products.admin import ProductAdmin

DEFAULT_ADMIN_MODELS = (
    ProductAdmin,
)
    

def create_app(config=None, app_name=None, blueprints=None,api_models=None,admin_models=None):
    """
    Create and configure the Flask app
    """
    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS
    if api_models is None:
        api_models = DEFAULT_API_MODELS
    if admin_models is None:
        admin_models = DEFAULT_ADMIN_MODELS
    app = Flask(app_name,
                static_url_path='/static',
                instance_relative_config=True
               )

    configure_app(app, config)
    configure_template_processors(app)
    configure_blueprints(app, blueprints)
    configure_logging(app)
    configure_error_handlers(app)
    configure_database(app)
    configure_assets(app)
    configure_api(app,api_models)
    configure_admin(app,admin_models)

    return app

def configure_app(app, config=None):
    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(DefaultConfig)

    if config is not None:
        app.config.from_object(config)

def configure_logging(app):

    if app.debug or app.testing:
        app.logger.setLevel(logging.DEBUG)
        # Skip debug and test mode. Just check standard output.
        return

    app.logger.setLevel(logging.INFO)

    info_log = os.path.join(app.config['LOG_FOLDER'], 'shop.log')
    info_file_handler = RotatingFileHandler(info_log, maxBytes=100000, backupCount=10)
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(info_file_handler)


def configure_template_processors(app):
    @app.context_processor
    def my_processors():
        def now(format="%d-%m-%d %H:%M:%S"):
            return datetime.datetime.now().strftime(format)

        return dict(now=now)

def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def configure_error_handlers(app):

    @app.errorhandler(403)
    @app.errorhandler(401)
    def forbidden_page(error):
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/500.html"), 500

def configure_database(app):
    db.init_app(app)

def configure_assets(app):
    assets.init_app(app)
    js = Bundle("libs/react/react.js",
                "libs/jquery/dist/jquery.js",
                "libs/fluxxor/build/fluxxor.js",
                filters="jsmin", output="libs/bundle.js")
    assets.register("js_all",js)

    import rfs.webassets_filters
    jsx = Bundle(
        "products/jsx/product.js",
        "orders/jsx/cart.js",
        "jsx/app.js",
        filters="jsx", output="js/app.js")
    assets.register("jsx_all",jsx)
    
    css = Bundle("css/app.css",
                 filters="cssmin",
                 output="libs/bundle.css")
    assets.register("css_all",css)

def configure_api(app, api_models):
    api_manager=APIManager(app,flask_sqlalchemy_db=db)
    for api in api_models: 
        api_manager.create_api(api)


def configure_admin(app,admin_models):
    admin = Admin(app,name="Store backend")
    for admin_view in admin_models:
        admin.add_view(admin_view(Product,db.session))
