from flask import render_template, Blueprint, session

bp = Blueprint('index', __name__, url_prefix='/')


@bp.app_errorhandler
def error(e):
    return render_template('error.html')


@bp.route('/')
def index():
    session['cur_nav'] = 'nav_app'
    return render_template('index/index.html')


@bp.route('/meta')
def meta():
    session['cur_nav'] = 'nav_meta'
    return render_template('index/meta.html')
