import os
import sys

from PySide6 import QtWidgets, QtCore

from config.config import AppConfig, PathConfig
from config.theme import Style

from gui.common.dialog import ExitDialog
from gui.window import MainWindow

from utils.log import Log, LogFile
from utils.thread import ThreadManager
from tools.gatherer import Gatherer
from tools.assistant import Assistant


class App:
    is_closing = False

    def __init__(self):       
        self.app = QtWidgets.QApplication([])        
        self.start()     
        
        self.gatherer = Gatherer()  
        self.assistant = Assistant()

        self.main_window = MainWindow()
        self.main_window.closeEvent = self.prep_to_exit        
        
    
    def start(self):
        # show app info
        Log.no_flag(f"{AppConfig.description}")
        Log.no_flag("")
        Log.info(f"App started at {os.getcwd()}")        

        # show debugging mode
        if AppConfig.debug:
            Log.info(f"Debugging output is enabled")
            #LogFlag.show_samples()
        else:
            Log.info(f"Debugging output is disabled")        

        # check resources
        Log.info(f"Checking resources")
        for attr, resource_path in PathConfig.__dict__.items():
            if not callable(resource_path) and not attr.startswith("__"):
                if os.path.exists(resource_path):
                    Log.debug(f"Found resource: {resource_path}")         
                else:
                    Log.critical(f"Resource not found: {resource_path}")
             
        # set app stylesheet 
        Log.info(f"Setting stylesheet")
        with open(PathConfig.stylesheet, "r") as file:
            stylesheet_content = file.read()
        self.app.setStyleSheet(stylesheet_content + Style.custom_style())

        # clear system info file
        LogFile.clear_system_info_file()            
    
    def prep_to_exit(self, event):
        if self.is_closing:
            event.ignore()
        elif ThreadManager.active_threads:
            Log.info('Preparing to exit app')

            self.is_closing = True
            event.ignore()

            self.main_window.prevent_resizing()
            self.main_window.console.scroll_to_bottom()

            exit_dialog = ExitDialog(self.main_window)
            exit_dialog.show()            

            cleanup_timer = QtCore.QTimer(self.app)
            cleanup_timer.timeout.connect(self.exit)
            cleanup_timer.start(100) 

            ThreadManager.clean_up()
        else:
            self.exit()
    
    def exit(self):        
        if not ThreadManager.active_threads: 
            Log.info('App exiting')                    
            sys.exit(0)
        

if __name__ == '__main__':
    z_one = App()
    z_one.app.exec()