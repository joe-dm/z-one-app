import os
from PySide6 import QtCore
from resources.config import AppConfig

class Flag:    
        default = '[ ] '        
        info    = '[i] '
        warning = '[!] '
        error   = '[E] '
        debug   = '[#] '
        task    = '[~] '
        none    = ''   

class Log:    
    file_lock = QtCore.QMutex()
    gui_console = None 
    preloaded_messages = []

    # writers
    def info(message):
        Log._log(message, Flag.info)
    def warning(message):
        Log._log(f"WARNING! {message}", Flag.warning)
    def error(message):
        Log._log(f"ERROR! {message}", Flag.error)
    def task(message):
        Log._log(message, Flag.task)  
    def no_flag(message):
        Log._log(message, Flag.none)    
    def debug(message):
        Log._log(message, Flag.debug)    
    def debug_init(obj, show_props=False):        
        class_name = obj.__class__.__name__
        message = f"Initialized {class_name} "
        indent = ' ' * len(Flag.default)
        if show_props:
            message += f"with properties:\n"
            for prop, value in obj.__dict__.items():
                message += f"{indent}{prop}: {value}\n"        
        Log.debug(message)    

    # check log directory 
    def check_dir():
        if not os.path.exists(AppConfig.Path.log_folder):
            os.makedirs(AppConfig.Path.log_folder)       
    
    # set the front gui console
    def set_gui_console(gui_console):
        Log.gui_console = gui_console
        
        for message, flag in Log.preloaded_messages:
            Log.gui_console.append(message, flag)
        
        Log.preloaded_messages = []
        
    

    # process log message
    def _log(message, flag=Flag.default):   
        # print to gui console
        if Log.gui_console:
            Log.gui_console.append(message, flag)
        # preload messages
        else:
            Log.preloaded_messages.append((message, flag))        
        
        # write to terminal
        print(f"{flag}{message}")
        # write to file
        Log._to_file(f"{flag}{message}\n")
        
    
    # write to log file
    def _to_file(message, file_name=AppConfig.Path.log_app):
        path = os.path.abspath(file_name)    
        Log.file_lock.lock()

        try:
            with open(path, 'a') as log_file:
                log_file.write(message)
        finally:
            Log.file_lock.unlock()        