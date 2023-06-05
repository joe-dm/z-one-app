import os

from PySide6 import QtWidgets, QtCore

from gui.sidebar import Sidebar
from gui.console import Console
from resources.config import AppConfig, PathConfig
from resources.theme import ThemeSize
from utils.log import Log, LogHandler, LogFlag


class App:
    def __init__(self):
        self.start()

        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.content = QtWidgets.QWidget()
        self.sidebar = Sidebar()
        self.page_stack = QtWidgets.QTextEdit()
        self.console = Console()

        self.setup_ui()        
    
    def start(self):
        # setup log folder/file
        if not os.path.exists(LogHandler.log_dir): 
            os.makedirs(LogHandler.log_dir)        
        if not os.path.exists(LogHandler.log_file): 
            with open(LogHandler.log_file, "w"): pass

        # show app info
        Log.no_flag(f"{AppConfig.description}")
        Log.no_flag("")
        Log.info(f"App started at {os.getcwd()}")        

        # show debugging mode
        if AppConfig.debug:
            Log.info(f"Debugging output is enabled")
            LogFlag.show_flag_samples()
        else:
            Log.info(f"Debugging output is disabled")

        # check resources
        Log.task(f"Checking resources")
        for attr, resource_path in PathConfig.__dict__.items():
            if not callable(resource_path) and not attr.startswith("__"):
                if os.path.exists(resource_path):
                    Log.debug(f"Found resource: {resource_path}")         
                else:
                    Log.critical(f"Resource not found: {resource_path}")
        

    def setup_ui(self):      
        # set stylesheet        
        with open(PathConfig.stylesheet, "r") as file:
            stylesheet_content = file.read()
        self.app.setStyleSheet(stylesheet_content)
        
        # setup content (sidebar/page stack)
        content_layout = QtWidgets.QHBoxLayout(self.content)
        content_layout.setContentsMargins(0,0,0,0)
        content_layout.setSpacing(ThemeSize.widget_spacing)
        content_layout.addWidget(self.sidebar)
        content_layout.addWidget(self.page_stack)

        # setup splitter
        self.splitter.addWidget(self.content)
        self.splitter.addWidget(self.console)
        self.splitter.setHandleWidth(ThemeSize.widget_spacing)
        self.splitter.setHandleWidth(0)

        # setup main window
        self.window.setWindowTitle(AppConfig.name)
        self.window.setMinimumWidth(600)
        self.window.setMinimumHeight(400)
        self.window.resize(800, 600)
        self.window.setCentralWidget(self.splitter)
        self.window.show()

    

if __name__ == '__main__':
    z_one = App()
    z_one.app.exec()