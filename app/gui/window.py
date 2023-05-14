import functools

import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets

from gui.sidebar import Sidebar
from gui.console import Console
from gui.page import PageStack
from resources.config import AppConfig, ThemeConfig
from util.logger import Logger

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        self.content = Content()
        self.setup_ui()
    
    def setup_ui(self):
        # set window properties
        self.setWindowTitle(AppConfig.name())
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)        
        self.resize(800, 600)
        self.setCentralWidget(self.content)
        self.show()

        # set icon
        icon = QtGui.QIcon(ThemeConfig.logo())
        self.setWindowIcon(icon)


class Content(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # initialise main widgets
        self.sidebar = Sidebar()
        self.page_stack = PageStack()
        self.console = Console()

        self.setup_ui()
        self.setup_connections()


    def setup_ui(self):
        # create widget to hold sidebar and pages
        main_view = QtWidgets.QWidget()
        # create main view (horizontal) layout, add sidebar and pages to it
        main_view_layout = QtWidgets.QHBoxLayout(main_view)       
        main_view_layout.addWidget(self.sidebar)
        main_view_layout.addWidget(self.page_stack)

        # create vertical splitter
        vertical_splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        vertical_splitter.addWidget(main_view)
        vertical_splitter.addWidget(self.console)        
        vertical_splitter.setSizes([350, 150])        

        # set content layout, add splitter to it
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)        
        self.setLayout(layout)
        self.layout().addWidget(vertical_splitter)

    def setup_connections(self):
        sidebar_buttons = [
            (self.sidebar.button_dashboard, self.page_stack.page_dashboard),
            (self.sidebar.button_cpu, self.page_stack.page_cpu)
        ]
        for button, page in sidebar_buttons:
            button.button_icon.clicked.connect(functools.partial(self.switch_page, page=page))
            button.button_text.clicked.connect(functools.partial(self.switch_page, page=page))

    
    def switch_page(self, page):
        self.page_stack.page_stack_layout.setCurrentWidget(page)
        Logger.log(f'Switched to page "{page.label_title.text()}"', 'debug')