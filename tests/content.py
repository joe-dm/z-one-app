import PySide6.QtWidgets as QtWidgets

from gui.page import PageDashboard, PageSystemInfo
from gui.widgets import ButtonSidebar
from gui.widgets import HLineSeparator

class MainView(QtWidgets.QWidget):
    def __init__(self):
        super(MainView, self).__init__() 
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("background-color: green;")
        
        # create pages
        self.page_dashboard = PageDashboard()
        self.page_system_info = PageSystemInfo()
        # create stacked layout and add pages
        self.page_stack = QtWidgets.QStackedLayout()
        self.page_stack.addWidget(self.page_dashboard)
        self.page_stack.addWidget(self.page_system_info)      
        
        # create sidebar
        self.sidebar = QtWidgets.QWidget()
        self.sidebar.setMaximumWidth(150)
        self.sidebar.setMinimumWidth(150)        
        # create sidebar buttons 
        self.btn_dashboard = ButtonSidebar('Dashboard')
        self.btn_system_info  = ButtonSidebar('System Info')
        # create sidebar layout and add buttons
        vbox = QtWidgets.QVBoxLayout(self.sidebar)
        vbox.addWidget(self.btn_dashboard)
        vbox.addWidget(self.btn_system_info)
        vbox.addStretch(1)

        # create main view layout
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.sidebar)
        hbox.addLayout(self.page_stack)