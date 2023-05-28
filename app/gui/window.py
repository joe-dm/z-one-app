import functools

from PySide6 import QtWidgets, QtCore

from gui.console import Console
from gui.page import PageStack
from gui.sidebar import Sidebar
from resources.config import AppConfig
from utils.log import Log



class QApp(QtWidgets.QApplication):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.main_window = MainWindow()               

    def setup_ui(self):
        # load stylesheet
        try:
            Log.debug('Loading stylesheet')
            with open(AppConfig.Path.stylesheet, "r") as f:
                stylesheet_content = f.read()
                self.setStyleSheet(stylesheet_content)
        except FileNotFoundError:
            Log.warning(f"Stylesheet file not found: {AppConfig.Path.stylesheet}")            
        except Exception as e:
            Log.error(f"Failed to load stylesheet: {str(e)}")

        Log.debug_init(self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.content = Content()
        self.setup_ui()

    def setup_ui(self):        
        # set window properties
        self.setWindowTitle(AppConfig.Info.name)
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)        
        self.resize(800, 600)
        self.setCentralWidget(self.content)
        # show window
        self.show() 

        Log.debug_init(self)    
    
        

class Content(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # initialise main widgets
        self.sidebar = Sidebar()
        self.page_stack = PageStack()
        self.console = Console()

        self.setup_ui()
        self.setup_sidebar_connections()


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

        Log.debug_init(self)

    def setup_sidebar_connections(self):
        Log.debug('Setting up sidebar connections')
        sidebar_buttons = [
            (self.sidebar.button_dashboard, self.page_stack.page_dashboard),
            (self.sidebar.button_cpu, self.page_stack.page_cpu),
            (self.sidebar.button_gpu, self.page_stack.page_gpu),   
            (self.sidebar.button_ram, self.page_stack.page_ram),
            (self.sidebar.button_disk, self.page_stack.page_disk),
            (self.sidebar.button_network, self.page_stack.page_network),
            (self.sidebar.button_apps, self.page_stack.page_apps),
            (self.sidebar.button_settings, self.page_stack.page_settings),
            (self.sidebar.button_logs, self.page_stack.page_logs)
        ] 

        # connect sidebar buttons
        for button, page in sidebar_buttons:
            button.button_icon.clicked.connect(functools.partial(self.switch_page, page=page))
            button.button_text.clicked.connect(functools.partial(self.switch_page, page=page))
        
        # connect header toggle
        self.sidebar.header.button_toggle.clicked.connect(functools.partial(self.sidebar.toggle))

    
    def switch_page(self, page):
        Log.debug(f'Switching to page "{page.label_title.text()}"')
        self.page_stack.page_stack_layout.setCurrentWidget(page)
        