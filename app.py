from __init__ import create_app
from weather_logger import WeatherLogger


app = create_app()

APP_PORT = app.config["APP_PORT"]
WeatherLogger = WeatherLogger(app.config["LOGS_PATH"], app.config["LOGGING_SCHEDULE"])
WeatherLogger.start()

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=APP_PORT, threaded=True)
