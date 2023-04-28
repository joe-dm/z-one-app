import PySide6.QtWidgets as QtWidgets

from gui.page import PageDashboard, PageSystemInfo
from gui.widgets import ButtonSidebar


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
        # connect button signals to switch pages
        self.btn_dashboard.clicked.connect(self.show_dashboard_page)
        self.btn_system_info.clicked.connect(self.show_system_info_page)
        # create sidebar layout and add buttons
        vbox = QtWidgets.QVBoxLayout(self.sidebar)
        vbox.addWidget(self.btn_dashboard)
        vbox.addWidget(self.btn_system_info)
        vbox.addStretch(1)        

        # create main view layout
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.sidebar)
        hbox.addWidget(scroll_area)

    def show_dashboard_page(self):
        self.page_stack.setCurrentWidget(self.page_dashboard)

    def show_system_info_page(self):
        self.page_stack.setCurrentWidget(self.page_system_info)
