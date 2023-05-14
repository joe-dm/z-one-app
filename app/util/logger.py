import os
import datetime
import logging
from resources.config import AppConfig, ConsoleConfig, PathConfig

class Logger:
    log_file = PathConfig.log_file()
    log_folder = PathConfig.log_folder()
    #log_path = os.path.join(log_folder, log_file)
    log_path = os.path.abspath(os.path.join(log_folder, log_file))


    def log(message, flag='default'):
        # get current date and time
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # create message string to be written to the log file 
        log_message = f"[{now}] {ConsoleConfig.flags.get(flag, '')}{message}\n"
        # write message to the log file
        with open(Logger.log_path, 'a') as log_file: log_file.write(log_message)
        # print message to system console
        if flag == 'debug' and AppConfig.debug() == False:
            pass
        else:
            print(f"{ConsoleConfig.flags.get(flag, '')}{message}")

    def setup_logs():
        #clear console
        os.system('cls' if os.name=='nt' else 'clear')
        # create directory for logs if it doesn't exist
        Logger.create_log_dir()
        # set environment variable to disable qt.dbus.integration message
        os.environ['QT_LOGGING_RULES'] = "qt.dbus.*=false"
        # show app and developer info
        Logger.log(f'{AppConfig.description()}\n', 'none')     
        # show app starting directory
        Logger.log(f'{AppConfig.name()} started at {os.getcwd()}', 'info')  
        # show debug mode
        if AppConfig.debug() == True: 
            Logger.log(f'Debugging mode is enabled', 'info')
        else:
            Logger.log(f'Debugging mode is disabled', 'info')

    def create_log_dir():
        if not os.path.exists(Logger.log_folder):
            os.makedirs(Logger.log_folder)