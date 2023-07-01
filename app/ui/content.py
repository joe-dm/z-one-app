import functools

from PySide6 import QtWidgets, QtCore

from ui.console import Console
from ui.page_stack import PageStack
from ui.sidebar import Sidebar
from utils.log import Log


class Content(QtWidgets.QSplitter):
    def __init__(self):
        super().__init__(QtCore.Qt.Vertical)        
        # initialize main widgets
        self.sidebar = Sidebar()
        self.page_stack = PageStack()
        self.console = Console()

        # setup sidebar/page widget
        self.sidebar_page = QtWidgets.QWidget()
        sidebar_page_layout = QtWidgets.QHBoxLayout(self.sidebar_page)
        sidebar_page_layout.setContentsMargins(0,0,0,0)        
        sidebar_page_layout.setSpacing(0)
        sidebar_page_layout.addWidget(self.sidebar)
        sidebar_page_layout.addWidget(self.page_stack)

        # setup sidebar/page connections
        for button, page in zip(self.sidebar.buttons, self.page_stack.pages):
            # connect each pair of buttons to their corresponding page
            button.button_icon.clicked.connect(functools.partial(self.page_stack.switch_page, page=page))
            button.button_text.clicked.connect(functools.partial(self.page_stack.switch_page, page=page))
            # connect each pair of buttons to set_active function
            button.button_icon.clicked.connect(functools.partial(self.sidebar.set_active_button, button=button))
            button.button_text.clicked.connect(functools.partial(self.sidebar.set_active_button, button=button))        


        # splitter properties
        self.addWidget(self.sidebar_page)
        self.addWidget(self.console)
        self.setHandleWidth(3)        

        Log.debug_init(self)