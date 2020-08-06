from flask import Flask, render_template, request
from flask_cors import CORS
from models import LicensePlate, Restriction, Weekdays


# initialize instance of WSGI application
# act as a central registry for the view functions, URL rules, template configs
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.debug = True

# initial setup
pico_y_placa_restrictions = Restriction.create_pico_y_placa_restrictions()


class Controller:
    def can_circulate(self):

        query_params = request.args
        license_plate = LicensePlate(query_params.get("license_plate"))

        date = query_params.get("date")
        time = query_params.get("time")
        weekday = Restriction.get_weekday_from_date(date)
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
