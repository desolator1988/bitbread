# coding: utf-8

from flask import Flask
from config import load_config


def create_app():
    app = Flask(__name__)

    # import blueprint
    from controller.index import index_blueprint

    # reg blueprint
    app.register_blueprint(index_blueprint)

    config = load_config()
    app.config.from_object(config)

    from flask.ext.mako import MakoTemplates
    MakoTemplates(app)

    return app

app = create_app()


@app.before_request
def before_request():
    pass


@app.after_request
def after_request(response=None):
    return response

if __name__ == '__main__':
    app.run(host='localhost', port=8848)
