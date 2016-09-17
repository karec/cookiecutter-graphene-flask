import logging.config


from flask import Flask

from main_api import blueprints
from main_api.extensions import db

DEFAULT_BLUEPRINTS = (
    blueprints.graphql_bp,
)


__all__ = ['create_app']


def create_app(blueprints=None, testing=False):
    """Create flask app and return it"""
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(
        'main_api',
        instance_path='/tmp',
        instance_relative_config=True
    )

    configure_app(app, testing=testing)
    configure_db(app)
    configure_blueprints(app, blueprints)
    configure_logging(app)

    return app


def configure_app(app, testing):
    """Initialize configuration"""
    app.config.from_object('main_api.config')

    if testing is True:
        app.config.from_object('main_api.test_config')
    else:
        app.config.from_pyfile('config.cfg', silent=True)


def configure_db(app):
    """Initialize database"""
    db.init_app(app)


def configure_blueprints(app, blueprints):
    """Configure blueprints in views"""
    for blueprint in blueprints:
        if isinstance(blueprint, str):
            blueprint = getattr(blueprints, blueprint)
        app.register_blueprint(blueprint)


def configure_logging(app):
    """Configure logging"""
    logging.config.dictConfig(app.config['LOGGING_CONFIG'])
