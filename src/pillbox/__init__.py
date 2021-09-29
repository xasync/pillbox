from flask import Flask
import os
from pillbox import pillbox_support


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = os.urandom(24)

    app.before_request_funcs.setdefault(None, []).append(pillbox_support.login_check_interceptor)

    from pillbox.views import auth
    from pillbox.views import index

    app.register_blueprint(auth.bp)
    app.register_blueprint(index.bp)

    return app
