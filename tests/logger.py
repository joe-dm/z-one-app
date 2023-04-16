import os
import datetime

class Logger:
    log_file = 'log.log'
    log_dir = 'logs'
    log_path = os.path.join(log_dir, log_file)

    @staticmethod
    def create_log_dir():
        if not os.path.exists(Logger.log_dir):
            os.makedirs(Logger.log_dir)

    @staticmethod
    def log(message):
        Logger.create_log_dir()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{now}] {message}\n"
        with open(Logger.log_path, 'a') as log_file:
            log_file.write(log_message)
        print(message)

