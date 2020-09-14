import os

from flask import Flask
import config


# creating an app factory function to register blueprints with it and
# accessing the app in the project through a proxy of created app called
# current_app and this approach help us make the project more scalable
# and maintainable


def create_app(testing=False):
    """Application factory

    Args:
        testing (bool, optional): will load testing config if True. Defaults to False.
    Returns: 
        the flask application object
    """
    app = Flask(__name__)

    # Dynamically load config based on the testing argument or FLASK_ENV evironment variable
    flask_env = os.getenv('FLASK_ENV', None)
    if testing or flask_env == 'testing':
        app.config.from_object(config.TestingConfig)
    elif flask_env == 'development':
        app.config.from_object(config.DevelopmentConfig)
    else:
        app.config.from_object(config.ProductionConfig)

    # setting up extensions to the app

    # Import and register blueprints
    from app.coffee import coffee
    app.register_blueprint(coffee, url_prefix='/coffee')

    return app
