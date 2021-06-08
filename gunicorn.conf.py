import multiprocessing
from config import Config


APP_HOST = Config.APP_HOST
APP_PORT = Config.APP_PORT

bind = f"{APP_HOST}:{APP_PORT}"
workers = multiprocessing.cpu_count() * 2 + 1
