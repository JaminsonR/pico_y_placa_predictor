import pytest

from api import app
from datetime import datetime

TEST_ROUTE = "/circulate"


def get_query_string(license_plate, date, time):
    return {"license_plate": license_plate, "date": date, "time": time}


@pytest.fixture(scope="module")
def test_client():
    yield app.test_client()


def test_is_restricted(test_client):
    """Verify if license_plate is restricted on datetime"""

    license_plate = "GRT0948"
    date = "2020-05-14"
    time = "9:29"

    response = test_client.get(
        TEST_ROUTE, query_string=(get_query_string(license_plate, date, time))
    )
    json_response = response.get_json()

    assert response.status_code == 200
    assert json_response["is_restricted"] == True
    assert json_response["day"] == "JUEVES"
    assert json_response["digit"] == 8
    assert json_response["date"] == "2020-05-14"
    assert json_response["time"] == "9:29"


def test_is_not_restricted_between_times(test_client):
    """Verify if license_plate is not restricted at time between restricted times"""

    license_plate = "GRT0949"
    date = "2020-05-15"
    time = "10:00"

    response = test_client.get(
        TEST_ROUTE, query_string=(get_query_string(license_plate, date, time))
    )
    json_response = response.get_json()

    assert response.status_code == 200
    assert json_response["is_restricted"] == False
    assert json_response["day"] == "VIERNES"
    assert json_response["digit"] == 9
    assert json_response["date"] == "2020-05-15"
    assert json_response["time"] == "10:00"


def test_is_not_restricted_on_datetime(test_client):
    """Verify if license_plate is not restricted on datetime"""

    license_plate = "GRT0946"
    date = "2020-05-14"
    time = "9:15"

    response = test_client.get(
        TEST_ROUTE, query_string=(get_query_string(license_plate, date, time))
    )
    json_response = response.get_json()

    assert response.status_code == 200
    assert json_response["is_restricted"] == False
    assert json_response["day"] == "JUEVES"
    assert json_response["digit"] == 6
    assert json_response["date"] == "2020-05-14"
    assert json_response["time"] == "9:15"

