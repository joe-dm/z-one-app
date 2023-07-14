import os
import datetime

from config.config import AppConfig


class LogFlag:
    info     = 'i| '
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
    directory   = os.path.join('logs')    
    full_log    = os.path.join(directory, 'z-one.log')
    network     = os.path.join(directory, 'network.log')

    system_info = os.path.join(directory, '_system_info.txt')

    def check_directory():
        if not os.path.exists(LogFile.directory): 
            os.makedirs(LogFile.directory) 

    def clear_system_info_file():
        if os.path.exists(LogFile.system_info):
            os.remove(LogFile.system_info)

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

    def debug(message, file=None, show_timestamp=True):
        LogHandler.handle(message, LogFlag.debug, file, show_timestamp=show_timestamp)

    def debug_init(obj, show_attributes=False, file=None, obj_name=None, show_timestamp=True):
        message = f"Initialized {obj.__class__.__name__}"
        if obj_name: message = f"{message} '{obj_name}'"

        indent = ' ' * len(LogFlag.debug)
        if show_attributes:
            message += " with attributes:"
            for attr, value in obj.__dict__.items():
                message += f"\n{indent}{attr}: {value}"
        Log.debug(message, file, show_timestamp=show_timestamp)
    
    def debug_static(cls, file=None, cls_name=None, show_timestamp=True):
        message = f"{cls.__name__}:"
        #if cls_name:
        #    message += f"'{cls_name}' "    

        indent = ' ' * len(LogFlag.debug)
        for var_name, var_value in cls.__dict__.items():
            if not callable(var_value) and not var_name.startswith("__"):
                message += f"\n{indent}{var_name}: {var_value}"
        Log.debug(message, file, show_timestamp=show_timestamp)


class LogHandler:
    gui_console = None
    preloaded_messages = []

    def handle(message, flag, file, show_timestamp=True):
        LogFile.check_directory()
        LogHandler.write_to_file(message, flag, file, show_timestamp=show_timestamp)
        LogHandler.write_to_gui_console(message, flag)
        print(f"{flag}{message}")    

    def write_to_file(message, flag, log_file, show_timestamp=True):        
        now = f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] '        

        # write to main log file
        with open(LogFile.full_log, 'a') as file:
                file.write(f"{now}{flag}{message}\n")

        # write to second log file 
        if log_file:
            if not show_timestamp:
                now = ''
            with open(log_file, 'a') as file:
                file.write(f"{now}{flag}{message}\n")        

        
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

    
    
