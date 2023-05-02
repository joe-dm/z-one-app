import sys

import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from gui.widgets import Sidebar
from gui.page import PageStack
from resources.config import AppConfig, ThemeConfig


class AppGUI(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)         
        self.setup_ui()     

    def setup_ui(self):    
        # load and set stylesheet
        stylesheet = QtCore.QFile(ThemeConfig.path_to_stylesheet())
        stylesheet.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        stream = QtCore.QTextStream(stylesheet)
        self.setStyleSheet(stream.readAll())

        # setup main window
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle(f'{AppConfig.name()}')
        self.window.setMinimumWidth(600)
        self.window.setMinimumHeight(400)

        # initialize main widgets
        self.sidebar = Sidebar()
        self.page_stack = PageStack()

        # connect sidebar button signals to switch pages        
        self.sidebar.btn_dashboard.clicked.connect(
            lambda: self.page_stack.show_page(self.page_stack.page_dashboard))
        self.sidebar.btn_system_info.clicked.connect(
            lambda: self.page_stack.show_page(self.page_stack.page_system_info))

        # setup window central widget
        central_widget = QtWidgets.QWidget()      
        self.window.setCentralWidget(central_widget)

        # setup app layout
        app_layout = QtWidgets.QHBoxLayout(central_widget)
        app_layout.addWidget(self.sidebar)
        app_layout.addWidget(self.page_stack)

        # show the window
        self.window.show()

    def exit(self):        
        self.exec()
