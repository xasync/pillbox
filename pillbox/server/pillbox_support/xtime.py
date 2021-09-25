import time


def now_unix():
    return int(time.time())


def now_millis():
    return int(round(time.time() * 1000))


def now_millis_with_delta(millis):
    return now_millis() + millis
