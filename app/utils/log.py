import os
import datetime

from resources.config import AppConfig

class LogFlag:
    info     = '•| '
    warning  = '!| '
    error    = '×| '
    critical = '✖| '
    task     = '»| '
    debug    = '#| '  
    no_flag  = ''   
    
    def show_samples():
        Log.info('This is an info message')
        Log.warning('This is a warning message')
        Log.error('This is an error message')
        Log.critical('This is a critical error message')
        Log.task('This is a task message')
        Log.debug('This is a debug message')

class LogFile:
    directory = os.path.join('logs')
    full_log  = os.path.join(directory, 'z-one.log')

    network   = os.path.join(directory, 'network.log')

    def check_directory():
        if not os.path.exists(LogFile.directory): 
            os.makedirs(LogFile.directory) 

class Log:
    # main writers
    def info(message, file=None):
        LogHandler.handle(message, LogFlag.info, file)

    def warning(message, file=None):
        LogHandler.handle(f"WARNING! {message}", LogFlag.warning, file)

    def error(message, file=None):
        LogHandler.handle(f"ERROR! {message}", LogFlag.error, file)

    def critical(message, file=None):
        LogHandler.handle(f"CRITICAL ERROR! {message}", LogFlag.critical, file)

    def task(message, file=None):
        LogHandler.handle(f"{message}...", LogFlag.task, file)

    def no_flag(message, file=None):
        LogHandler.handle(message, LogFlag.no_flag, file)

    def debug(message, file=None):
        LogHandler.handle(message, LogFlag.debug, file)

    def debug_init(obj, obj_name=None, show_attributes=False, file=None):        
        message = f"Initialized {obj.__class__.__name__}"
        if obj_name: message = f"{message} '{obj_name}'"

        indent = ' ' * len(LogFlag.debug)
        if show_attributes:
            message += " with attributes:\n"
            for attr, value in obj.__dict__.items():
                message += f"{indent}{attr}: {value}\n"
        Log.debug(message, file)

class LogHandler:
    gui_console = None
    preloaded_messages = []

    def handle(message, flag, file):
        LogFile.check_directory()
        LogHandler.write_to_file(message, flag, file)
        LogHandler.write_to_gui_console(message, flag)
        print(f"{flag}{message}")    

    def write_to_file(message, flag, log_file):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # write to main log file
        with open(LogFile.full_log, 'a') as file:
                file.write(f"[{now}] {flag}{message}\n")

        # write to second log file 
        if log_file:
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

    
    
