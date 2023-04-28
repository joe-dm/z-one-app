import random

import PySide6.QtWidgets as QtWidgets
import PySide6.QtCore as QtCore

from gui.widgets import PageTitle, SeparatorHLine, TableWithTitle
from resources.config import TestData

class Page(QtWidgets.QWidget):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.setup_ui()

    def setup_ui(self):
        # create common page widgets
        self.label_title = PageTitle(self.title)

        # create layout and add common widgets
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label_title)
        self.layout.addWidget(SeparatorHLine())

    def add_bottom_widgets(self):   
        self.layout.addStretch(1)
        pass

class PageDashboard(Page):
    def __init__(self):
        super().__init__('Dashboard')
        self.setup_widgets()

    def setup_widgets(self):
        # add widgets specific to this page
        self.description = QtWidgets.QLabel('This is the dashboard page!')
        self.layout.addWidget(self.description)

        # add some random widgets for testing scrolling
        for i in range(20):
            widget = QtWidgets.QLabel(f'This is widget {i}')
            widget.setStyleSheet('background-color: #1d2022; color: #e5e5e5;')
            self.layout.addWidget(widget)

        super().add_bottom_widgets()


class PageSystemInfo(Page):
    def __init__(self):
        super().__init__('System Info')
        self.setup_widgets()

    def setup_widgets(self):        

        
        self.table1 = TableWithTitle('Hardware', TestData.hardware())
        self.table2 = TableWithTitle('Operating System', TestData.operating_system())


        self.layout.addWidget(self.table1)
        self.layout.addWidget(self.table2)

        super().add_bottom_widgets()