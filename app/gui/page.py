from PySide6 import QtWidgets

from resources.theme import ThemeStylesheet

class PageStack(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()       

        self.stacked_layout = QtWidgets.QStackedLayout(self)
        self.page_dashboard = PageDashboard()
        self.page_processor = PageProcessor()
        self.page_gpu = PageGPU()
        self.page_memory = PageMemory()
        self.page_disk = PageDisk()
        self.page_network = PageNetwork()
        self.page_apps = PageApps()
        self.page_settings = PageSettings()
        self.page_logs = PageLogs()
        
        self.setup_ui()        
    
    def setup_ui(self):
        self.stacked_layout.addWidget(self.page_dashboard)
        self.stacked_layout.addWidget(self.page_processor)
        self.stacked_layout.addWidget(self.page_gpu)
        self.stacked_layout.addWidget(self.page_memory)
        self.stacked_layout.addWidget(self.page_disk)
        self.stacked_layout.addWidget(self.page_network)
        self.stacked_layout.addWidget(self.page_apps)
        self.stacked_layout.addWidget(self.page_settings)
        self.stacked_layout.addWidget(self.page_logs)
    
    def switch_page(self, page):
        self.stacked_layout.setCurrentWidget(page)
        


class Page(QtWidgets.QScrollArea):
    def __init__(self, title):
        super().__init__()
        
        self.label_title = QtWidgets.QLabel(title)   
        self.separator = QtWidgets.QFrame()

        self.page_layout = QtWidgets.QVBoxLayout()        
        self.page_container = QtWidgets.QWidget()

        self.setup_page_ui()        
     
    def setup_page_ui(self):
        # scroll area properties
        self.setWidget(self.page_container)    
        self.setWidgetResizable(True)    
        self.setStyleSheet(ThemeStylesheet.page)

        # title properties
        self.label_title.setStyleSheet(ThemeStylesheet.page_title)

        # separator properties
        self.separator.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator.setFrameShadow(QtWidgets.QFrame.Sunken)    
        self.separator.setStyleSheet(ThemeStylesheet.line_horizontal_1)

        # set the container layout
        self.page_container.setLayout(self.page_layout)

        # add common widgets to layout
        self.page_layout.addWidget(self.label_title)
        self.page_layout.addWidget(self.separator)
        self.page_layout.addSpacing(5)



class PageDashboard(Page):
    def __init__(self):
        super().__init__('Dashboard')        
        self.description = QtWidgets.QLabel(f'This is the Dashboard page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        self.page_layout.addStretch()


class PageProcessor(Page):
    def __init__(self):
        super().__init__('Processor')        
        self.description = QtWidgets.QLabel('This is the Processor page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)  
        self.page_layout.addStretch()


class PageGPU(Page):
    def __init__(self):
        super().__init__('GPU')        
        self.description = QtWidgets.QLabel('This is the GPU page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        self.page_layout.addStretch()


class PageMemory(Page):
    def __init__(self):
        super().__init__('Memory')        
        self.description = QtWidgets.QLabel('This is the Memory page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        self.page_layout.addStretch()


class PageDisk(Page):
    def __init__(self):
        super().__init__('Disk')        
        self.description = QtWidgets.QLabel('This is the Disk page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        self.page_layout.addStretch()


class PageNetwork(Page):
    def __init__(self):
        super().__init__('Network')        
        self.description = QtWidgets.QLabel('This is the Network page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        self.page_layout.addStretch()


class PageApps(Page):
    def __init__(self):
        super().__init__('Apps')        
        self.description = QtWidgets.QLabel('This is the Apps page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        self.page_layout.addStretch()


class PageSettings(Page):
    def __init__(self):
        super().__init__('Settings')        
        self.description = QtWidgets.QLabel('This is the Settings page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        self.page_layout.addStretch()


class PageLogs(Page):
    def __init__(self):
        super().__init__('Logs')        
        self.description = QtWidgets.QLabel('This is the Logs page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        self.page_layout.addStretch()

        