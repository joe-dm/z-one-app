import os
import datetime
from resources.config import AppConfig, PathConfig, ThemeConfig


class Logger:
    log_file = PathConfig.log_file()
    log_folder = PathConfig.log_folder()
    log_path = os.path.abspath(os.path.join(log_folder, log_file))
    
    gui_console = None
    preloaded_messages = []

    @staticmethod
    def log(message, flag='default'):
        # get date and time, and create the log and console messages
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{now}] {ThemeConfig.console_flags.get(flag, '')}{message}\n"
        console_message = f"{ThemeConfig.console_flags.get(flag, '')}{message}"

        # write to log file
        with open(Logger.log_path, 'a') as log_file:
            log_file.write(log_message)

        # check if debug message and print it if debugging output is enabled
        if flag == 'debug' and not AppConfig.debug():
            pass
        else:            
            if Logger.gui_console:
                Logger.gui_console.append(console_message)           
            else:
                Logger.preloaded_messages.append(console_message)

    @staticmethod
    def setup_logs():
        #os.system('cls' if os.name=='nt' else 'clear')
        Logger.create_log_dir()
        os.environ['QT_LOGGING_RULES'] = "qt.dbus.*=false"
        Logger.log(f'{AppConfig.description()}\n', 'none')
        Logger.log(f'{AppConfig.name()} started at {os.getcwd()}', 'info')
        if AppConfig.debug():
            Logger.log(f'Debugging mode is enabled', 'info')
        else:
            Logger.log(f'Debugging mode is disabled', 'info')

    @staticmethod
    def create_log_dir():
        if not os.path.exists(Logger.log_folder):
            os.makedirs(Logger.log_folder)

    @staticmethod
    def set_gui_console(gui_console): 
        Logger.gui_console = gui_console
        # process preloaded messages
        for message in Logger.preloaded_messages:
            Logger.gui_console.append(message)
        # clear preloaded messages
        Logger.preloaded_messages = []
