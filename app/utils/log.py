import os
import datetime
from queue import Queue
from PySide6 import QtCore
from resources.config import AppConfig

class Flag:                  
        info    = '•| '
        warning = '!| '
        error   = '×| '
        debug   = '#| '
        task    = '»| '
        none    = ''   

class Log:    
    lock = QtCore.QMutex()
    gui_console = None 
    preloaded = []

    # log writers    
    def info(message):      Log._log(message, Flag.info)
    def warning(message):   Log._log(f"WARNING! {message}", Flag.warning)
    def error(message):     Log._log(f"ERROR! {message}", Flag.error)
    def task(message):      Log._log(message, Flag.task)  
    def no_flag(message):   Log._log(message, Flag.none)    
    def debug(message):     Log._log(message, Flag.debug) 
    def debug_init(obj, show_props=False):        
        class_name = obj.__class__.__name__
        message = f"Initialized {class_name} "
        indent = ' ' * len(Flag.info)
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
        if gui_console:    
            for message, flag in Log.preloaded:
                Log._log(message, flag)     
            Log.preloaded = [] 
            

    # process log message
    def _log(message, flag):         
        
        file_path = os.path.abspath(AppConfig.Path.log_app)    
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        Log.lock.lock()
        try:
            #if Log.gui_console:
                # write to gui console
            #    Log.gui_console.append(message, flag)
            #else:
            #    Log.preloaded.append((message, flag))

            # write to file
            with open(file_path, 'a') as log_file:
                log_file.write(f"[{now}]{message}")
        finally: 
            Log.lock.unlock()
              