import random

import PySide6.QtWidgets as QtWidgets
import PySide6.QtCore as QtCore

from gui.widgets import PageTitle, SeparatorHLine, TableWithTitle
from resources.config import TestData, ThemeConfig

class PageStack(QtWidgets.QScrollArea):
    def __init__(self):
        super().__init__()          
        self.setup_ui()

    def setup_ui(self):
        # create pages
        self.page_dashboard = PageDashboard()
        self.page_system_info = PageSystemInfo()
        
        # create stacked layout and add pages
        self.page_stack_layout = QtWidgets.QStackedLayout()
        self.page_stack_layout.addWidget(self.page_dashboard)
        self.page_stack_layout.addWidget(self.page_system_info)

        # create container to hold stacked layout
        self.container = QtWidgets.QWidget()
        self.container.setLayout(self.page_stack_layout)

        # set scroll area properties
        self.setWidgetResizable(True)
        self.setWidget(self.container)
        self.setStyleSheet(f"background-color: {ThemeConfig.get_color('black')};")

    def show_page(self, page):
        self.page_stack_layout.setCurrentWidget(page)

class Page(QtWidgets.QWidget):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.page_layout = QtWidgets.QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        # create common widgets
        self.label_title = PageTitle(self.title)
        # add common widgets        
        self.page_layout.addWidget(self.label_title)
        self.page_layout.addWidget(SeparatorHLine())    

    def add_bottom_widgets(self):   
        self.page_layout.addStretch(1)
        pass

class PageDashboard(Page):
    def __init__(self):
        super().__init__('Dashboard')
        self.setup_widgets()

    def setup_widgets(self):
        # add widgets specific to this page
        self.description = QtWidgets.QLabel('This is the dashboard page!')          
        self.page_layout.addWidget(self.description)
        super().add_bottom_widgets()


class PageSystemInfo(Page):
    def __init__(self):
        super().__init__('System Info')
        self.setup_widgets()

    def setup_widgets(self):        
        self.table1 = TableWithTitle('Hardware', TestData.hardware())
        self.table2 = TableWithTitle('Operating System', TestData.operating_system())

        self.page_layout.addWidget(self.table1)
        self.page_layout.addWidget(self.table2)

        super().add_bottom_widgets()