from weather_logger import WeatherLogger
from config import Config


def run_weather_logger():
    logger = WeatherLogger(Config.LOGS_PATH, Config.LOGGING_SCHEDULE, Config.CHECK_INTERVAL)
    logger.start()


def init():
    run_weather_logger()
