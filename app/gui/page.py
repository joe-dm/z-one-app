from PySide6 import QtWidgets, QtGui

from gui.common.elements import LabelHeading, HLine
from gui.common.chart import Chart
from gui.common.table import Table
from gui.common.stats import CPUStats, NetworkStats

from config.theme import ThemeColor

from tools.system_info import CPUInfo, NetworkInfo
from utils.log import Log

class PageStack(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()       

        self.stacked_layout = QtWidgets.QStackedLayout(self)        
        self.page_dashboard = PageDashboard()
        self.page_cpu = PageCPU()
        self.page_gpu = PageGPU()
        self.page_memory = PageMemory()
        self.page_disk = PageDisk()
        self.page_network = PageNetwork()
        self.page_software = PageSoftware()
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
        self.stacked_layout.addWidget(self.page_software)
        self.stacked_layout.addWidget(self.page_settings)
        self.stacked_layout.addWidget(self.page_logs)

        Log.debug_init(self)
    
    def switch_page(self, page):
        Log.debug(f"Switching to page '{page.title}'")
        self.stacked_layout.setCurrentWidget(page)    
        

class Page(QtWidgets.QScrollArea):
    def __init__(self, title):
        super().__init__(objectName='Page')          
        self.title = title        
        
        # main widgets
        self.label_title = QtWidgets.QLabel(self.title, objectName='PageTitleLabel')   
        self.separator = HLine(color=ThemeColor.primary)             
        
        # container properties
        self.page_container = QtWidgets.QWidget() 
        self.page_container.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
               
        # setup layout
        self.page_layout = QtWidgets.QVBoxLayout(self.page_container)              
        self.page_layout.addWidget(self.label_title) 
        self.page_layout.addWidget(self.separator) 
        
        # page properties       
        self.setWidget(self.page_container)    
        self.setWidgetResizable(True)  

        Log.debug_init(self)     

    def insert_widget(self, widget):
        self.page_layout.addSpacing(10)
        self.page_layout.addWidget(widget)



class PageCPU(Page):
    def __init__(self):
        super().__init__('CPU')
            
        self.name_heading = LabelHeading(f"{CPUInfo.get_name()}")        
        
        self.usage_chart = Chart(
            get_value_func=CPUInfo.get_usage_current, 
            title='Overall Usage', y_axis_max=100)
        self.info_table = Table(CPUInfo.get_tuple_list(), 'Specifications')        
        self.stats_view = CPUStats()

        # add widgets to layout
        self.insert_widget(self.name_heading)        
        self.insert_widget(self.usage_chart)
        self.insert_widget(self.stats_view)
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
        
        self.speed_chart = Chart(
            get_value_func=lambda: NetworkInfo.get_speed_download(format_output=False),
            title='Download Speed')
        self.stats_view = NetworkStats()

        # add widgets to layout
        self.insert_widget(self.speed_chart)
        self.insert_widget(self.stats_view)


class PageSoftware(Page):
    def __init__(self):
        super().__init__('Software')        
        self.description = QtWidgets.QLabel('This is the Software page!')
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

        