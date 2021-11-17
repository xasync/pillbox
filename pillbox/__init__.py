from flask import Flask
import os
import sys
from . import pillbox_support
from . import views


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = os.urandom(24)

    app.before_request_funcs.setdefault(None, []).append(pillbox_support.login_check_interceptor)

    app.register_blueprint(views.auth.bp)
    app.register_blueprint(views.index.bp)

    return app
