from PySide6 import QtWidgets, QtCore

from gui.common.elements import Heading, HLine
from gui.common.widgets import Chart, Table

from tools.info_gatherer import InfoGatherer, CPUInfo
from config.theme import ThemeStylesheet
from utils.log import Log

class PageStack(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()     
        self.setObjectName('PageStack')  

        self.stacked_layout = QtWidgets.QStackedLayout(self)
        self.page_dashboard = PageDashboard()
        self.page_cpu = PageCPU()
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
        self.stacked_layout.addWidget(self.page_cpu)
        self.stacked_layout.addWidget(self.page_gpu)
        self.stacked_layout.addWidget(self.page_memory)
        self.stacked_layout.addWidget(self.page_disk)
        self.stacked_layout.addWidget(self.page_network)
        self.stacked_layout.addWidget(self.page_apps)
        self.stacked_layout.addWidget(self.page_settings)
        self.stacked_layout.addWidget(self.page_logs)
        self.setStyleSheet(ThemeStylesheet.page_stack)

        Log.debug_init(self)
    
    def switch_page(self, page):
        Log.debug(f"Switching to page '{page.title}'")
        self.stacked_layout.setCurrentWidget(page)
        

class Page(QtWidgets.QScrollArea):
    def __init__(self, title):
        super().__init__()        
        self.title = title

        # main widgets
        self.label_title = QtWidgets.QLabel(self.title, objectName='PageTitle')   
        self.separator = HLine()             
        
        # container properties
        self.page_container = QtWidgets.QWidget() 
        self.page_container.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
               
        # setup layout
        self.page_layout = QtWidgets.QVBoxLayout(self.page_container)              
        self.page_layout.addWidget(self.label_title) 
        self.page_layout.addWidget(self.separator) 
        
        # page properties
        self.setStyleSheet(ThemeStylesheet.page)        
        self.setWidget(self.page_container)    
        self.setWidgetResizable(True)  

        Log.debug_init(self)
    
    def set_static_values(self): pass    

    def insert_widget(self, widget):
        self.page_layout.addSpacing(10)
        self.page_layout.addWidget(widget)



class PageCPU(Page):
    def __init__(self):
        super().__init__('CPU')
        self.setup_ui()        

    def setup_ui(self):     
        self.name_heading = Heading(CPUInfo.get_name())
        
        self.usage_chart = Chart(get_value_func=CPUInfo.check_current_usage, title='Usage', y_axis_max=100, unit='%')        
        self.info_table = Table(InfoGatherer.get_list(CPUInfo))

        # add widgets to layout
        self.insert_widget(self.name_heading)        
        self.insert_widget(self.usage_chart) 
        self.insert_widget(self.info_table)     


class PageDashboard(Page):
    def __init__(self):
        super().__init__('Dashboard')        
        self.description = QtWidgets.QLabel(f'This is the Dashboard page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)

class PageGPU(Page):
    def __init__(self):
        super().__init__('GPU')        
        self.description = QtWidgets.QLabel('This is the GPU page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()


class PageMemory(Page):
    def __init__(self):
        super().__init__('Memory')        
        self.description = QtWidgets.QLabel('This is the Memory page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()


class PageDisk(Page):
    def __init__(self):
        super().__init__('Disk')        
        self.description = QtWidgets.QLabel('This is the Disk page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()


class PageNetwork(Page):
    def __init__(self):
        super().__init__('Network')        
        self.description = QtWidgets.QLabel('This is the Network page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()


class PageApps(Page):
    def __init__(self):
        super().__init__('Apps')        
        self.description = QtWidgets.QLabel('This is the Apps page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()


class PageSettings(Page):
    def __init__(self):
        super().__init__('Settings')        
        self.description = QtWidgets.QLabel('This is the Settings page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()


class PageLogs(Page):
    def __init__(self):
        super().__init__('Logs')        
        self.description = QtWidgets.QLabel('This is the Logs page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()

        