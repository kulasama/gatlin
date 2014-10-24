from flask import Flask, request
from gatlin.user.views import user
import os
from gatlin.extensions import db
import logging
import logging.handlers  

def create_app(config=None):
    """
    Creates the app.
    """
    # Initialize the app
    app = Flask("gatlin")

    # config
    app.config.from_envvar("GATLIN_SETTINGS")

    configure_extensions(app)
    configure_blueprints(app)
    configure_logging(app)

    return app


def configure_extensions(app):
    """
    Configures the extensions
    """

    # Flask-SQLAlchemy
    db.init_app(app)


def configure_blueprints(app):
    app.register_blueprint(user, url_prefix=app.config["USER_URL_PREFIX"])



def configure_logging(app):
    """
    Configures logging.
    """

    logs_folder = os.path.join(app.root_path, os.pardir, "logs")
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')

    info_log = os.path.join(logs_folder, app.config['INFO_LOG'])


    info_file_handler = logging.handlers.RotatingFileHandler(
        info_log,
        maxBytes=100000,
        backupCount=10
    )

    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(formatter)
    app.logger.addHandler(info_file_handler)

    error_log = os.path.join(logs_folder, app.config['ERROR_LOG'])


    error_file_handler = logging.handlers.RotatingFileHandler(
        error_log,
        maxBytes=100000,
        backupCount=10
    )

    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)
