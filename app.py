from __init__ import create_app
import os
from WeatherLogger import WeatherLogger

app = create_app()

APP_PORT = app.config["APP_PORT"]
WeatherLogger = WeatherLogger(app.config["LOGS_PATH"], app.config["LOGGING_SCHEDULE"])

if __name__ == "__main__":
    WeatherLogger.start()

    app.secret_key = os.urandom(25)
    app.run(debug=True, host='0.0.0.0', port=APP_PORT, threaded=True)
