from gevent import monkey
monkey.patch_all()

from pillbox import create_app

if __name__ == '__main__':
    app=create_app()
    app.run()