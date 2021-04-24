import json
import time
import threading
import datetime
import os
from Station import I2C_Station


class WeatherLogger:
    def __init__(self, logs_path, logging_schedule):
        self.logs_path = logs_path
        self.logging_schedule = logging_schedule
        self.logger_thread = threading.Thread(target=self.log)
        self.is_running = False
        self.weather_station = I2C_Station()

    def create_dict(self, name):
        d = {}

        for hour in self.logging_schedule:
            d[hour] = None

        with open(os.path.join(self.logs_path, name), "w") as file:
            file.write(json.dumps(d, indent=4))

    def log(self):
        while self.is_running:
            date = datetime.datetime.now().date()
            hour = datetime.datetime.now().hour
            log_file_name = f"{date}.json"

            if not os.path.exists(os.path.join(self.logs_path, log_file_name)):
                self.create_dict(log_file_name)

            else:
                with open(os.path.join(self.logs_path, log_file_name), "r") as file_to_read:
                    log_content = json.loads(file_to_read.read())

                    if log_content[str(hour)] is None:
                        temperature, humidity = self.weather_station.read_weather_data()

                        log_content[str(hour)] = [temperature, humidity]

                        with open(os.path.join(self.logs_path, log_file_name), "w") as file_to_write:
                            file_to_write.write(json.dumps(log_content))

            time.sleep(60)

    def start(self):
        self.is_running = True
        self.logger_thread.start()

    def stop(self):
        self.is_running = False
        self.logger_thread.join()
