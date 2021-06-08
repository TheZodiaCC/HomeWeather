from flask import Blueprint, jsonify
from station import I2C_Station
from response_data import ResponseData
import os


main_ = Blueprint("main", __name__, template_folder='template', static_folder='static')

WeatherStation = I2C_Station()


@main_.route("/api/station_data")
def station_data():
    uptime = str(os.popen("uptime | awk '{ print $3 }'").read())
    uptime = uptime.replace(",", "")
    uptime = uptime.strip()

    data = {}

    power, voltage = WeatherStation.get_power_stats()

    data["Battery_Voltage"] = voltage
    data["Battery_Level"] = power
    data["Uptime"] = uptime

    return jsonify(data)


@main_.route("/api/weather")
def weather():
    humidity, temperature = WeatherStation.read_weather_data()
    values = [temperature, humidity]

    response_data = ResponseData(WeatherStation.get_weather_sensor_keys(), values)

    return response_data.create_response()
