from flask import Flask
import os


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.secret_key = os.urandom(25)

    with app.app_context():
        from routes import main

        app.register_blueprint(main.main_)

        return app
