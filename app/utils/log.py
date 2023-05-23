import os
import datetime
from resources.config import AppConfig, PathConfig, ThemeConfig


class Logger:
    log_file = PathConfig.log_file
    log_folder = PathConfig.log_folder
    log_path = os.path.abspath(os.path.join(log_folder, log_file))
    
    gui_console = None
    preloaded_messages = []

    @staticmethod
    def log(message, flag='default'):
        # edit message 
        if flag == 'operation':
            message = f"{message}..."
        elif flag == 'error':
            message = f"ERROR! {message}"
        elif flag == 'warning':
            message = f"WARNING! {message}"

        # get date and time, and create the log and console messages
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{now}] {ThemeConfig.console_flags.get(flag, '')}{message}\n"

        # write to log file
        with open(Logger.log_path, 'a') as log_file:
            log_file.write(log_message)

        # print to gui console
        if Logger.gui_console:                
            Logger.gui_console.append(message, flag)   
        # preload if gui console is unavailable        
        else:                
            Logger.preloaded_messages.append((message, flag))
    
    @staticmethod
    def log_init(obj, show_props=False):
        Logger.log(f"Initialized '{obj.__class__.__name__}'", 'debug')

        if show_props:
            for prop, value in obj.__dict__.items():
                Logger.log(f"{prop}: {value}", 'debug child')

    @staticmethod
    def setup_logs():       
        
        Logger.log(f'{AppConfig.description}', 'none')
        Logger.log(f'\n', 'none')
        Logger.log(f'{AppConfig.name} started at {os.getcwd()}', 'info')
        if AppConfig.debug:
            Logger.log(f'Debugging mode is enabled', 'info')
            Logger.log(f'This is what a warning message looks like', 'warning')
            Logger.log(f'This is what an error message looks like', 'error')
        else:
            Logger.log(f'Debugging mode is disabled', 'info')

    @staticmethod
    def check_log_dir():
        if not os.path.exists(Logger.log_folder):
            os.makedirs(Logger.log_folder)

    @staticmethod
    def set_gui_console(gui_console): 
        Logger.gui_console = gui_console
        # process preloaded messages
        for message, flag in Logger.preloaded_messages:
            Logger.gui_console.append(message, flag)
        # clear preloaded messages
        Logger.preloaded_messages = []
