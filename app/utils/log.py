import os
import datetime
import inspect

from resources.config import AppConfig

class LogFlag:
    info     = '•| '
    warning  = '!| '
    error    = '×| '
    critical = '✖| '
    task     = '»| '
    debug    = '#| '  
    none     = ''   
    
    def show_samples():
        Log.info('This is an info message')
        Log.warning('This is a warning message')
        Log.error('This is an error message')
        Log.critical('This is a critical error message')
        Log.task('This is a task message')
        Log.debug('This is a debug message')

class LogFile:
    directory = os.path.join('logs')

    app = os.path.join(directory, 'z-one.log')
    network = os.path.join(directory, 'network.log')

    def check_directory():
        if not os.path.exists(LogFile.directory): 
            os.makedirs(LogFile.directory) 

class Log:
    # main writers
    def info(message):
        LogHandler.handle(message, LogFlag.info)
    def warning(message):
        LogHandler.handle(f"WARNING! {message}", LogFlag.warning)
    def error(message):
        LogHandler.handle(f"ERROR! {message}", LogFlag.error)
    def critical(message):
        LogHandler.handle(f"CRITICAL ERROR! {message}", LogFlag.critical)
    def task(message):
        LogHandler.handle(f"{message}...", LogFlag.task)
    def no_flag(message):
        LogHandler.handle(message, LogFlag.none)
    def debug(message):
        LogHandler.handle(message, LogFlag.debug)
    def debug_init(obj, show_attributes=False):        
        message = f"Initialized {obj.__class__.__name__}"
        indent = ' ' * len(LogFlag.debug)
        if show_attributes:
            message += " with attributes:\n"
            for attr, value in obj.__dict__.items():
                message += f"{indent}{attr}: {value}\n"
        Log.debug(message)

class LogHandler:
    gui_console = None
    preloaded_messages = []

    def handle(message, flag):
        LogFile.check_directory()
        LogHandler.write_to_file(message, flag)
        LogHandler.write_to_gui_console(message, flag)
        print(f"{flag}{message}")    

    def write_to_file(message, flag, log_file=LogFile.app):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, 'a') as file:
            file.write(f"[{now}] {flag}{message}\n")
        
    def write_to_gui_console(message, flag):
        if not AppConfig.debug and flag == LogFlag.debug:
            pass
        else:
            if LogHandler.gui_console:
                LogHandler.gui_console.append(message, flag)
            else:
                LogHandler.preloaded_messages.append((message, flag))
    
    def set_gui_console(gui_console):
        LogHandler.gui_console = gui_console        
        for message, flag in LogHandler.preloaded_messages:
            LogHandler.write_to_gui_console(message, flag)
        LogHandler.preloaded_messages = []

    
    
