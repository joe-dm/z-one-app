from PySide6 import QtWidgets

from modules.modules import Modules

from ui.common.page import Page 
from utils.log import Log


class PageStack(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()       
        # initialize stacked layout
        self.stacked_layout = QtWidgets.QStackedLayout(self)        
        
        # initialize page views
        modules = Modules() 
        self.page_dashboard = Page('Dashboard')            
        self.page_cpu = modules.cpu_page_view
        self.page_gpu = Page('GPU')
        self.page_memory = Page('Memory')
        self.page_disk = Page('Disk')
        self.page_network = modules.network_page_view
        self.page_software = modules.software_page_view
        self.page_settings = Page('Settings')
        self.page_logs = Page('Logs')

        # list of all pages
        self.pages = [
            self.page_dashboard, self.page_cpu,
            self.page_gpu, self.page_memory,
            self.page_disk, self.page_network,
            self.page_software, self.page_settings,
            self.page_logs]
        
        # add pages to layout
        for page in self.pages:
            self.stacked_layout.addWidget(page)    
    
        Log.debug_init(self)
    
    def switch_page(self, page: Page):
        Log.debug(f"Switching to {page.title} page")
        self.stacked_layout.setCurrentWidget(page)    