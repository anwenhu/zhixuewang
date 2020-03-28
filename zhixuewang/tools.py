import datetime

def int2datetime(i: int) -> datetime.datetime:
    return datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=i)