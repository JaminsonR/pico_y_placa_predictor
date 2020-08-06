from flask import Flask, render_template, request
from flask_cors import CORS
from models import LicensePlate, Restriction, Weekdays
from datetime import datetime


# initialize instance of WSGI application
# act as a central registry for the view functions, URL rules, template configs
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.debug = True

# creating initial pico y placa restrictions
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


class Controller:
    def can_circulate(self):

        query_params = request.args
        license_plate = LicensePlate(query_params.get("license_plate"))

        date = query_params.get("date")
        time = query_params.get("time")
        weekday = datetime.strptime(str(query_params.get("date")), "%Y-%m-%d").weekday()
        applicable_restrictions = [
            restriction
            for restriction in pico_y_placa_restrictions
            if restriction.does_restriction_apply(date, time, license_plate.last_digit)
        ]

        response = {
            "is_restricted": True if len(applicable_restrictions) > 0 else False,
            "day": Weekdays(weekday).name,
            "date": date,
            "time": time,
            "digit": license_plate.last_digit,
        }

        return response


controller = Controller()


app.add_url_rule(
    "/circulate", "circulate", lambda: controller.can_circulate(), methods=["GET"]
)


if __name__ == "__main__":
    app.run()
