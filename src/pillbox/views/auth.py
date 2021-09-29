from flask import render_template, Blueprint, request, redirect, url_for, flash
from pillbox.pillbox_support import read_vcode_ctl, write_vcode_ctl, VcodeCtl, PillboxException
from pillbox.pillbox_support import validator

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/index')
def index():
    cxt = {
        'html_title': 'pillbox|Log In'
    }
    return render_template('auth/index.html', **cxt)


@bp.route('/verify')
def verify():
    ctl = read_vcode_ctl()
    if not ctl.available():
        raise PillboxException('Invalid Access!')
    return render_template('auth/verify.html',
                           email=ctl.email)


@bp.route('/sendcode', methods=['POST'])
def send_code():
    email = str(request.form.get('email')).strip()
    if validator.email(email) is not True:
        flash('Invalid email! Please input your registered email again!')
        return redirect(url_for('auth.index'))
    ctl = VcodeCtl(email, 888888)
    write_vcode_ctl(ctl)
    return redirect(url_for('auth.verify'))


@bp.route('/login', methods=['POST'])
def login():
    ctl = read_vcode_ctl()
    if not ctl.available():
        raise PillboxException('Invalid Access!')
    # form fields
    email = str(request.form.get('email')).strip()
    vcode = int(request.form.get('vcode'))
    if validator.email(email) is not True:
        flash('Invalid email! Please input your registered email again!')
        return redirect(url_for('auth.index'))
    if vcode <= 0 or len(str(vcode)) != 6:
        flash('Invalid the verification code! Please input your receiving verification code again!')
        return redirect(url_for('auth.verify'))

    if ctl.do_login(email, vcode):
        return redirect(url_for('index.index'))
    else:
        flash('Your verification code is not correct! Please entry it again after checking!')
        return redirect(url_for('auth.verify'))
