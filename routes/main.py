from flask import Blueprint, jsonify
from flask import current_app as app
from station import I2C_Station
import os
import json


main_ = Blueprint("main", __name__, template_folder='template', static_folder='static')
CURRENT_DIR = app.config["CURRENT_DIR"]
LOGS_PATH = app.config["LOGS_PATH"]
ENABLE_POWERGAUGE = app.config["ENABLE_POWERGAUGE"]

WeatherStation = I2C_Station()


@main_.route("/api/station_data")
def station_data():
    uptime = str(os.popen("uptime | awk '{ print $3 }'").read())
    uptime = uptime.replace(",", "")
    uptime = uptime.strip()

    data = {}

    if ENABLE_POWERGAUGE:
        power, voltage = WeatherStation.get_power_stats()

        data["Battery_Voltage"] = voltage
        data["Battery_Level"] = power

    data["Uptime"] = uptime

    return jsonify(data)


@main_.route("/api/weather")
def weather():
    humidity, temperature = WeatherStation.read_weather_data()

    response_data = {
        "temperature": temperature,
        "humidity": humidity
    }

    return jsonify(response_data)


@main_.route("/api/get_logged_days")
def get_logged_days():
    logs_path = os.path.join(CURRENT_DIR, LOGS_PATH)
    logs = list(map(lambda log: log.split(".")[0], os.listdir(logs_path)))

    return jsonify(logs)


@main_.route("/api/get_weather_data/<date>")
def get_weather_data(date):
    log_name = f"{date}.json"
    log_path = os.path.join(CURRENT_DIR, os.path.join(LOGS_PATH, log_name))

    if os.path.exists(log_path):
        with open(log_path, "r") as log_file:
            log_data = json.loads(log_file.read())
    else:
        log_data = {}
        log_data["error"] = "Log file not found"

    return jsonify(log_data)
