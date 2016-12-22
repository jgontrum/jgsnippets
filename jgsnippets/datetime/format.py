import datetime


def now():
    return datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")


def format_dt(dt):
    return dt.strftime("%Y%m%dT%H%M%SZ")