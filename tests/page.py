import PySide6.QtWidgets as QtWidgets

from gui.widgets import HLineSeparator, PageTitle

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
        self.layout.addWidget(HLineSeparator())

        
    def add_bottom_widgets(self):
        # create a spacer to push widgets to the bottom of the page
        self.spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout.addItem(self.spacer)
        self.layout.addWidget(HLineSeparator())


class PageDashboard(Page):
    def __init__(self):
        super().__init__('Dashboard')
        self.setup_widgets()
    
    def setup_widgets(self):        
        # add widgets specific to this page
        self.description = QtWidgets.QLabel('This is the dashboard page!')
        self.layout.addWidget(self.description)

        super().add_bottom_widgets()


class PageSystemInfo(Page):
    def __init__(self):
        super().__init__('System Info')
        self.setup_widgets()
    
    def setup_widgets(self):        
        # add widgets specific to this page
        self.description = QtWidgets.QLabel('This is the system info page!')
        self.layout.addWidget(self.description)

        super().add_bottom_widgets() 
