from datetime import datetime
from enum import Enum


class LicensePlate:
    def __init__(self, number_str):
        self.number_str = number_str
        self.last_digit = int(number_str[-1])


class Restriction:
    def __init__(self, start_time_str, end_time_str, weekday, digits):
        self.start_time = datetime.strptime(start_time_str, "%H:%M").time()
        self.end_time = datetime.strptime(end_time_str, "%H:%M").time()
        self.weekday = Weekdays(weekday)
        self.digits = digits

    def __str__(self):
        return "Day: {}, Start time: {}, End time: {}, Digits: {}".format(
            self.weekday, self.start_time, self.end_time, str(self.digits)
        )

    # TODO remove
    __repr__ = __str__

    def does_restriction_apply(self, date_str, time_str, digit):
        inquired_time = datetime.strptime(time_str, "%H:%M").time()
        inquired_weekday = datetime.strptime(date_str, "%Y-%m-%d").weekday()

        if (
            Weekdays(inquired_weekday) == self.weekday
            and self.start_time <= inquired_time <= self.end_time
        ):
            if digit in self.digits:
                return True
        return False


class Weekdays(Enum):
    LUNES = 0
    MARTES = 1
    MIERCOLES = 2
    JUEVES = 3
    VIERNES = 4
    SABADO = 5
    DOMINGO = 6

