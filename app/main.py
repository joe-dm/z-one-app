import os
import sys

from PySide6 import QtWidgets, QtCore

from config.config import AppConfig, PathConfig
from config.theme import Style
from modules.modules import Modules
from ui.common.dialog import OverlayDialog
from ui.content import Content
from utils.log import Log, LogFile
from utils.thread import ThreadManager


class App:
    is_closing = False

    def __init__(self):       
        self.app = QtWidgets.QApplication([])        
        self.start()     
        self.setup_ui()        

    def setup_ui(self):
        Log.info(f"Setting up UI")

        # initialize window content
        self.content = Content()        

        # setup main window
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.setWindowTitle(AppConfig.name)
        self.main_window.setMinimumWidth(750)
        self.main_window.setMinimumHeight(400)
        self.main_window.resize(800, 600)
        self.main_window.setCentralWidget(self.content)
        self.main_window.show()
        self.main_window.closeEvent = self.prep_to_exit             

    
    def start(self):
        # show app info
        Log.no_flag(f"{AppConfig.full_name}")
        Log.no_flag(f"{AppConfig.copyright_info}")
        Log.no_flag("")
        Log.info(f"App started at {os.getcwd()}")        

        # show debugging mode
        if AppConfig.debug:
            Log.info(f"Debugging output is enabled")            
        else:
            Log.info(f"Debugging output is disabled")        

        # check app resources
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

            # prevent main window from resizing
            self.main_window.setFixedSize(self.main_window.size())
            # scroll console to bottom
            self.content.console.scroll_to_bottom()            
            
            # create exit dialog
            exit_dialog = OverlayDialog(
                parent_widget=self.main_window,
                heading='Exiting',
                message='Waiting for processes to finish')
            exit_dialog.show()            

            # setup timer to wait for threads to finish
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