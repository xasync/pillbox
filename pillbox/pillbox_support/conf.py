from __future__ import print_function

import configparser
import os

from . import env

CONF_DEFAULT_DATA = '''
[app]
# set the administer email for signing in system.
;admin_emails=admin1@example.com,admin2@example.com
'''


class Configure:
    def __init__(self):
        self.file_path = env.get_app_conf_path(env.app_conf_file)
        self.sp = '.'
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as fd:
                fd.write(CONF_DEFAULT_DATA)
        cp = configparser.ConfigParser()
        cp.read(self.file_path, encoding='utf-8')
        self._cp = cp

    def app(self):
        admin_emails = []
        if self._cp.has_option('app', 'admin_emails'):
            ae = str(self._cp.get('app', 'admin_emails'))
            admin_emails = ae.split(',')
        return {
            'admin_emails': admin_emails
        }

    def show(self):
        with open(self.file_path, 'r') as fd:
            while True:
                line = fd.readline()
                if not line:
                    break
                print(line)

    def get(self, name, default_value=None):
        n = str(name).strip()
        if len(n) <= 0:
            return default_value
        pos = n.rfind(self.sp)
        if pos > 0:
            section = n[0:pos]
            option = n[pos + len(self.sp):] if pos + len(self.sp) < len(n) else ''
        else:
            section = 'app'
            option = n
        if self._cp.has_option(section, option):
            return self._cp.get(section, option)
        else:
            return default_value

    def set(self, name, data):
        n = str(name).strip()
        if len(n) <= 0:
            print('the name is empty.')
            return False
        pos = n.rfind('.')
        if pos > 0:
            section = n[0:pos]
            option = n[pos + len(self.sp):] if pos + len(self.sp) < len(n) else ''
        else:
            section = 'app'
            option = n
        if not self._cp.has_section(section):
            self._cp.add_section(section)
        self._cp.set(section, option, data)
        self._cp.write(open(self.file_path, 'w+'))

    def erase(self, name):
        n = str(name).strip()
        if len(n) <= 0:
            print('the name is empty.')
            return False
        pos = n.rfind('.')
        if pos > 0:
            section = n[0:pos]
            option = n[pos + len(self.sp):] if pos + len(self.sp) < len(n) else ''
        else:
            section = 'app'
            option = n
        if not self._cp.has_section(section):
            self._cp.add_section(section)
        self._cp.remove_option(section, option)
        self._cp.write(open(self.file_path, 'w+'))
