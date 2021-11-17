# coding=utf-8
from flask import request, session, redirect, url_for
import json
from . import xtime


def login_check_interceptor():
    # 后端服务接口请求且非登录模块都需要做登录检查
    if request.endpoint and not str(request.endpoint).startswith('auth.'):
        login_user = session.get('login_user')
        if login_user is None:
            return redirect(url_for('auth.index'))
        print(login_user)
        # check if expired
        user = json.loads(login_user)
        now_millis = xtime.now_millis()
        if now_millis >= user.get('expire_millis'):
            return redirect(url_for('auth.index'))
        session['cur_user_name'] = user.get('user_name')


class VcodeCtl:
    def __init__(self, email, vcode=None):
        self.email = email
        self.vcode = vcode

    def available(self):
        return self.email is not None and self.vcode is not None

    def do_login(self, email, vcode):
        success = self.email == email and self.vcode == vcode
        if success:
            session['login_user'] = json.dumps({
                'user_name': self.email,
                'expire_millis': xtime.now_millis_with_delta(3 * 3600 * 1000)
            })
            del session['vcode_ctl']
        return success


def read_vcode_ctl():
    try:
        vcode_ctl = session.get('vcode_ctl')
        ctl_json = json.loads(vcode_ctl)
        vc = VcodeCtl(None)
        vc.__dict__ = ctl_json
        return vc
    except:
        return VcodeCtl(None)


def write_vcode_ctl(ctl):
    if ctl is not None:
        session['vcode_ctl'] = json.dumps(ctl.__dict__)
