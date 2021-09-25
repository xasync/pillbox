from flask import Flask
import os
import pillbox_support


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = os.urandom(24)

    app.before_request_funcs.setdefault(None, []).append(pillbox_support.login_check_interceptor)

    import auth
    import index

    app.register_blueprint(auth.bp)
    app.register_blueprint(index.bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5200, debug=True)
