import functools

from PySide6 import QtWidgets, QtCore

from gui.sidebar import Sidebar
from gui.page import PageStack
from gui.console import Console

from utils.config import AppConfig
from utils.theme import ThemeSize
from utils.log import Log

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Log.task(f"Loading interface")

        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.content = QtWidgets.QWidget()
        self.sidebar = Sidebar()
        self.page_stack = PageStack()
        self.console = Console()          

        self.setup_ui()
        self.setup_connections()
    
    def setup_ui(self):    
        # setup content layout
        content_layout = QtWidgets.QHBoxLayout(self.content)
        content_layout.setContentsMargins(0,0,0,0)        
        content_layout.setSpacing(0)
        content_layout.addWidget(self.sidebar)
        content_layout.addWidget(self.page_stack)

        # setup splitter
        self.splitter.addWidget(self.content)
        self.splitter.addWidget(self.console)
        self.splitter.setHandleWidth(ThemeSize.widget_spacing)

        # window properties
        self.setWindowTitle(AppConfig.name)
        self.setMinimumWidth(750)
        self.setMinimumHeight(400)
        self.resize(800, 600)
        self.setCentralWidget(self.splitter)
        self.show()

        Log.debug_init(self)

    def setup_connections(self):
        Log.debug('Setting up main window connections')
        # create a list of sidebar-button/page pairs
        button_page_pairs = [
            (self.sidebar.button_dashboard, self.page_stack.page_dashboard),
            (self.sidebar.button_cpu, self.page_stack.page_cpu),
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

    def prevent_resizing(self):
        self.setFixedSize(self.size())