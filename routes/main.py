from flask import Blueprint, jsonify
from Station import I2C_Station
from ResponseData import ResponseData


main_ = Blueprint("main", __name__, template_folder='template', static_folder='static')

WeatherStation = I2C_Station()


@main_.route("/api/station_data")
def station_data():
    #Placeholder

    data = {}
    data["Battery_Level"] = 5

    return jsonify(data)


@main_.route("/api/weather")
def weather():
    temperature, humidity = WeatherStation.read_weather_data()
    values = [temperature, humidity]

    response_data = ResponseData(WeatherStation.get_weather_sensor_keys(), values)

    return response_data.create_response()
