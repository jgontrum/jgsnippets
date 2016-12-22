import datetime


def now():
    return datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")