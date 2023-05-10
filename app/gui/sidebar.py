import PySide6.QtWidgets as QtWidgets
from gui.widgets import ButtonWithIcon
from resources.config import ThemeConfig
from utils.logger import Logger

class Sidebar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()          
        self.setup_ui()

    def setup_ui(self):
        # set properties
        self.setMaximumWidth(150)
        self.setMinimumWidth(150)
        # create buttons
        self.btn_dashboard = ButtonWithIcon('Dashboard', ThemeConfig.get_icon_path('default'))
        self.btn_system_info = ButtonWithIcon('System Info', ThemeConfig.get_icon_path('default'))
        self.btn_settings = ButtonWithIcon('Settings', ThemeConfig.get_icon_path('default'))
        # create sidebar layout and add buttons
        sidebar_layout = QtWidgets.QVBoxLayout(self)
        sidebar_layout.addWidget(self.btn_dashboard)
        sidebar_layout.addWidget(self.btn_system_info)
        sidebar_layout.addWidget(self.btn_settings)
        sidebar_layout.addStretch()

    def connect_btn_signals(self, page_stack):
        # connect dashboard page
        self.btn_dashboard.btn_icon.clicked.connect(lambda: page_stack.show_page(page_stack.page_dashboard))
        self.btn_dashboard.btn_text.clicked.connect(lambda: page_stack.show_page(page_stack.page_dashboard))
                
        # connect system info page
        self.btn_system_info.btn_icon.clicked.connect(lambda: page_stack.show_page(page_stack.page_system_info))
        self.btn_system_info.btn_text.clicked.connect(lambda: page_stack.show_page(page_stack.page_system_info))