from . import auth
from . import index

def init_app(app):
    app.register_blueprint(auth.bp)
    app.register_blueprint(index.bp)


