import os
import sys
import datetime
from resources.config import AppConfig

class Logger:
    log_file = 'log.log'
    log_dir = 'logs'
    log_path = os.path.join(log_dir, log_file)
    log_flags = {
            'info':    '[i]: ',
            'error':   '[E]: ',
            'warning': '[!]: ',
            'loading': '[~]: ',
            'debug':   '[#]: ',
            'default': '[ ]: ',
            'none':    ''}    

    def log(message, log_type='default'):        
        # get current date and time
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # create message string to be written to the log file 
        log_message = f"[{now}] {Logger.log_flags.get(log_type, '')}{message}\n"
        # write message to the log file
        with open(Logger.log_path, 'a') as log_file: log_file.write(log_message)
        # print message to the console
        if log_type == 'debug' and AppConfig.debug() == False:
            pass
        else:
            print(f"{Logger.log_flags.get(log_type, '')}{message}")     

    def setup_logs():
        #clear console
        os.system('cls' if os.name=='nt' else 'clear')
        # create directory for logs if it doesn't exist
        Logger.create_log_dir()
        # set environment variable to disable qt.dbus.integration message
        os.environ['QT_LOGGING_RULES'] = "qt.dbus.*=false"

    def create_log_dir():
        if not os.path.exists(Logger.log_dir):
            os.makedirs(Logger.log_dir)
