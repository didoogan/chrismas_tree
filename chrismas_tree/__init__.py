from flask import Flask

from chrismas_tree.views import blueprint


def create_app(config=None):
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    return app
