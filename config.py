import os


class Config:
    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

    #Logging hours
    LOGGING_SCHEDULE = [x for x in range(24)]
    LOGS_PATH = "logs"
    CHECK_INTERVAL = 300
