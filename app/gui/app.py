import sys

import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from gui.page import PageDashboard, PageSystemInfo
from gui.widgets import ButtonSidebar
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
        # window central widget
        main_view = ContentView()      
        self.window.setCentralWidget(main_view)
        # show the window
        self.window.show()

    def exit(self):        
        self.exec()


class ContentView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__() 
        self.setup_ui()

    def setup_ui(self):        
        # create pages
        self.page_dashboard = PageDashboard()
        self.page_system_info = PageSystemInfo()
        # create stacked layout and add pages
        self.page_stack = QtWidgets.QStackedLayout()
        self.page_stack.addWidget(self.page_dashboard)
        self.page_stack.addWidget(self.page_system_info)   
        # create widget to hold the stacked layout
        self.page_widget = QtWidgets.QWidget()
        self.page_widget.setLayout(self.page_stack)         
        # wrap page_widget in a scroll area
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.page_widget)
        scroll_area.setStyleSheet("background-color: #1d2022;")
        
        # create sidebar
        self.sidebar = QtWidgets.QWidget()
        self.sidebar.setMaximumWidth(150)
        self.sidebar.setMinimumWidth(150)        
        # create sidebar buttons 
        self.btn_dashboard = ButtonSidebar('Dashboard')
        self.btn_system_info  = ButtonSidebar('System Info')
        # connect sidebar button signals to switch pages
        self.btn_dashboard.clicked.connect(lambda: self.set_current_page(self.page_dashboard))
        self.btn_system_info.clicked.connect(lambda: self.set_current_page(self.page_system_info))
        # create sidebar layout and add buttons
        vbox = QtWidgets.QVBoxLayout(self.sidebar)
        vbox.addWidget(self.btn_dashboard)
        vbox.addWidget(self.btn_system_info)
        vbox.addStretch(1)        

        # create main view layout
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.sidebar)
        hbox.addWidget(scroll_area)

    def set_current_page(self, page):
        self.page_stack.setCurrentWidget(page)
