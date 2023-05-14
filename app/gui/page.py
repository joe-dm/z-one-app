import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets

from resources.config import ThemeConfig
from gui.widgets import SeparatorHLine, LabelTitle

class PageStack(QtWidgets.QScrollArea):
    def __init__(self):
        super().__init__()     
        # initialise widgets
        self.page_stack_layout = QtWidgets.QStackedLayout()
        self.page_dashboard = PageDashboard()
        self.page_cpu = PageCPU()
        self.setup_ui()

    def setup_ui(self):
        # add page widgets to layout
        self.page_stack_layout.addWidget(self.page_dashboard)
        self.page_stack_layout.addWidget(self.page_cpu)

        # create container to hold stacked layout
        container = QtWidgets.QWidget()
        container.setLayout(self.page_stack_layout)

        # scroll area properties
        self.setWidgetResizable(True)
        self.setWidget(container)
        self.setStyleSheet(f"background-color: {ThemeConfig.color_black()};")


class Page(QtWidgets.QWidget):
    def __init__(self, title):
        super().__init__()        
        # initialise widgets
        self.label_title = LabelTitle(title)
        self.separator = SeparatorHLine()
        self.page_layout = QtWidgets.QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):         
        # add widgets to layout
        self.page_layout.addWidget(self.label_title)
        self.page_layout.addWidget(self.separator)

    def add_bottom_widgets(self):
        self.page_layout.addStretch()


class PageDashboard(Page):
    def __init__(self):
        super().__init__('Dashboard')
        # initialise widgets
        self.description = QtWidgets.QLabel('This is the dashboard page!')
        self.setup_widgets()

    def setup_widgets(self):               
        self.page_layout.addWidget(self.description)
        super().add_bottom_widgets()


class PageCPU(Page):
    def __init__(self):
        super().__init__('CPU')
        # initialise widgets
        self.description = QtWidgets.QLabel('This is the CPU page!')
        self.setup_widgets()

    def setup_widgets(self):               
        self.page_layout.addWidget(self.description)
        super().add_bottom_widgets()

