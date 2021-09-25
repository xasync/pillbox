from access_control import *
from flask import jsonify
import validator


class PillboxException(Exception):
    def __int__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message if message else 'Unknown'
        self.code = status_code
        self.payload = payload

    def __str__(self):
        payload_str = 'Payload:' + jsonify(self.payload) if self.payload else ''
        return '[${code}] ${message} ${payload}'.format(code=self.code, message=self.message, payload=payload_str)
