"""
GEOS 697 web app
"""

from flask import Flask
from config import config


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .model import model as model_blueprint
    app.register_blueprint(model_blueprint, url_prefix='/model')

    return app
