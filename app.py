from __init__ import create_app
from weather_logger import WeatherLogger


app = create_app()

WeatherLogger = WeatherLogger(app.config["LOGS_PATH"], app.config["LOGGING_SCHEDULE"], app.config["CHECK_INTERVAL"])
WeatherLogger.start()

if __name__ == "__main__":
    APP_PORT = app.config["APP_PORT"]
    APP_HOST = app.config["APP_HOST"]

    app.run(debug=False, host=APP_HOST, port=APP_PORT, threaded=True)
