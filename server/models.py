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
        inquired_weekday = self.get_weekday_from_date(date_str)

        if (
            Weekdays(inquired_weekday) == self.weekday
            and self.start_time <= inquired_time <= self.end_time
        ):
            if digit in self.digits:
                return True
        return False

    @staticmethod
    def get_weekday_from_date(date_str):
        return datetime.strptime(date_str, "%Y-%m-%d").weekday()

    @staticmethod
    def create_pico_y_placa_restrictions():
        pico_y_placa_restrictions = []
        offset = 0
        for i in range(0, 7):

            first_digit = i + offset + 1
            second_digit = i + 2 + offset

            pico_y_placa_restrictions.append(
                Restriction(
                    "07:00",
                    "09:30",
                    Weekdays(i),
                    (first_digit, second_digit if second_digit is not 10 else 0),
                )
            )

            pico_y_placa_restrictions.append(
                Restriction(
                    "16:00",
                    "19:30",
                    Weekdays(i),
                    (first_digit, second_digit if second_digit is not 10 else 0),
                )
            )
            offset += 1
        return pico_y_placa_restrictions


class Weekdays(Enum):
    LUNES = 0
    MARTES = 1
    MIERCOLES = 2
    JUEVES = 3
    VIERNES = 4
    SABADO = 5
    DOMINGO = 6

