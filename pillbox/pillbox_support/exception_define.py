import json


class PillboxException(Exception):
    def __int__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message if message else 'Unknown'
        self.code = status_code
        self.payload = payload

    def __str__(self):
        payload_str = 'Payload:' + json.dumps(self.payload) if self.payload else ''
        return '[${code}] ${message} ${payload}'.format(code=self.code, message=self.message, payload=payload_str)
