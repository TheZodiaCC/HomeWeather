from flask import Blueprint, jsonify
from Station import Station


main_ = Blueprint("main", __name__, template_folder='template', static_folder='static')

weather_station = Station()


@main_.route("/api/station_data")
def station_data():
    data = {}
    data["Battery_Level"] = 5

    return jsonify(data)


@main_.route("/api/weather")
def weather():
    temperature, humidity = weather_station.read()

    data = {}
    data["temperature"] = temperature
    data["humidity"] = humidity

    return jsonify(data)
