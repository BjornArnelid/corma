import datetime


class TimeUnit(object):
    """Representation of a unit of time

    A TimeUnit contains date and hours worked
    """
    def __init__(self, date, hours):
        self.date = date
        self.hours = hours
