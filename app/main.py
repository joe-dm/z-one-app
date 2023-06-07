import os
import functools

from PySide6 import QtWidgets, QtCore

from gui.console import Console
from gui.page import PageStack
from gui.sidebar import Sidebar
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
        self.page_stack = PageStack()
        self.console = Console()

        self.setup_ui()
        self.setup_connections()   
    
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
            LogFlag.show_samples()
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
        self.splitter.setHandleWidth(ThemeSize.widget_spacing)

        # setup main window
        self.window.setWindowTitle(AppConfig.name)
        self.window.setMinimumWidth(600)
        self.window.setMinimumHeight(400)
        self.window.resize(800, 600)
        self.window.setCentralWidget(self.splitter)
        self.window.show()


    def setup_connections(self):
        # create a list of sidebar-button/page pairs
        button_page_pairs = [
            (self.sidebar.button_dashboard, self.page_stack.page_dashboard),
            (self.sidebar.button_processor, self.page_stack.page_processor),
            (self.sidebar.button_gpu, self.page_stack.page_gpu),
            (self.sidebar.button_memory, self.page_stack.page_memory),
            (self.sidebar.button_disk, self.page_stack.page_disk),
            (self.sidebar.button_network, self.page_stack.page_network),
            (self.sidebar.button_apps, self.page_stack.page_apps),
            (self.sidebar.button_settings, self.page_stack.page_settings),
            (self.sidebar.button_logs, self.page_stack.page_logs)]
        # connect sidebar buttons to switch pages
        for button, page in button_page_pairs:
            button.button_icon.clicked.connect(functools.partial(self.page_stack.switch_page, page=page))
            button.button_text.clicked.connect(functools.partial(self.page_stack.switch_page, page=page))
            button.button_icon.clicked.connect(functools.partial(self.sidebar.set_active_button, button=button))
            button.button_text.clicked.connect(functools.partial(self.sidebar.set_active_button, button=button))        
        # connect sidebar toggle button
        self.sidebar.header.button_toggle.clicked.connect(functools.partial(self.sidebar.toggle))
        

if __name__ == '__main__':
    z_one = App()
    z_one.app.exec()