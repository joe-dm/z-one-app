from PySide6 import QtWidgets

from gui.widgets import PageTitle, Separator, TableWithTitle
from resources.config import ThemeConfig, SampleData
from utils.log import Log

class PageStack(QtWidgets.QScrollArea):
    def __init__(self):
        super().__init__()     
        # initialise widgets
        self.page_stack_layout = QtWidgets.QStackedLayout()
        self.page_dashboard = PageDashboard()
        self.page_cpu = PageCPU()
        self.page_gpu = PageGPU()
        self.page_ram = PageRAM()
        self.page_disk = PageDisk()
        self.page_network = PageNetwork()
        self.page_apps = PageApps()
        self.page_settings = PageSettings()
        self.page_logs = PageLogs()
        self.setup_ui()

    def setup_ui(self):
        # add page widgets to layout
        self.page_stack_layout.addWidget(self.page_dashboard)
        self.page_stack_layout.addWidget(self.page_cpu)
        self.page_stack_layout.addWidget(self.page_gpu)
        self.page_stack_layout.addWidget(self.page_ram)
        self.page_stack_layout.addWidget(self.page_disk)
        self.page_stack_layout.addWidget(self.page_network)
        self.page_stack_layout.addWidget(self.page_apps)
        self.page_stack_layout.addWidget(self.page_settings)
        self.page_stack_layout.addWidget(self.page_logs)

        # create container to hold stacked layout
        container = QtWidgets.QWidget()
        container.setLayout(self.page_stack_layout)

        # scroll area properties
        self.setWidgetResizable(True)
        self.setWidget(container)
        self.setStyleSheet(f"background-color: {ThemeConfig.Color.black};")
        
        Log.debug_init(self)

class Page(QtWidgets.QWidget):
    def __init__(self, title):
        super().__init__()        
        # initialise widgets
        self.label_title = PageTitle(title)
        self.separator = Separator()
        self.page_layout = QtWidgets.QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):         
        # add widgets to layout
        self.page_layout.addWidget(self.label_title)
        self.page_layout.addWidget(self.separator)
        
        Log.debug_init(self)

    def add_bottom_widgets(self):
        self.page_layout.addStretch()


class PageDashboard(Page):
    def __init__(self):
        super().__init__('Dashboard')
        # initialise widgets        
        self.cpu = TableWithTitle('CPU', SampleData.cpu_info)
        self.gpu = TableWithTitle('GPU', SampleData.gpu_info)
        self.disk = TableWithTitle('Disk', SampleData.disk_info)
        self.os = TableWithTitle('Operating System', SampleData.os_info)
        self.setup_widgets()

    def setup_widgets(self):               
        self.page_layout.addWidget(self.cpu)
        self.page_layout.addWidget(self.gpu)
        self.page_layout.addWidget(self.disk)
        self.page_layout.addWidget(self.os)
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


class PageGPU(Page):
    def __init__(self):
        super().__init__('GPU')
        # initialise widgets
        self.description = QtWidgets.QLabel('This is the GPU page!')
        self.setup_widgets()

    def setup_widgets(self):               
        self.page_layout.addWidget(self.description)
        super().add_bottom_widgets()


class PageRAM(Page):
    def __init__(self):
        super().__init__('RAM')
        # initialise widgets
        self.description = QtWidgets.QLabel('This is the RAM page!')
        self.setup_widgets()

    def setup_widgets(self):               
        self.page_layout.addWidget(self.description)
        super().add_bottom_widgets()


class PageDisk(Page):
    def __init__(self):
        super().__init__('Disk')
        # initialise widgets
        self.description = QtWidgets.QLabel('This is the Disk page!')
        self.setup_widgets()

    def setup_widgets(self):               
        self.page_layout.addWidget(self.description)
        super().add_bottom_widgets()


class PageNetwork(Page):
    def __init__(self):
        super().__init__('Network')
        # initialise widgets
        self.description = QtWidgets.QLabel('This is the Network page!')
        self.setup_widgets()

    def setup_widgets(self):               
        #self.page_layout.addWidget(self.description)
        super().add_bottom_widgets()


class PageApps(Page):
    def __init__(self):
        super().__init__('Apps')
        # initialise widgets
        self.description = QtWidgets.QLabel('This is the Apps page!')
        self.setup_widgets()

    def setup_widgets(self):               
        self.page_layout.addWidget(self.description)
        super().add_bottom_widgets()


class PageSettings(Page):
    def __init__(self):
        super().__init__('Settings')
        # initialise widgets
        self.description = QtWidgets.QLabel('This is the Settings page!')
        self.setup_widgets()

    def setup_widgets(self):               
        self.page_layout.addWidget(self.description)
        super().add_bottom_widgets()


class PageLogs(Page):
    def __init__(self):
        super().__init__('Logs')
        # initialise widgets
        self.description = QtWidgets.QLabel('This is the Logs page!')
        self.setup_widgets()

    def setup_widgets(self):               
        self.page_layout.addWidget(self.description)
        super().add_bottom_widgets()