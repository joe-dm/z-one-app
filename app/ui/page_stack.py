from PySide6 import QtWidgets

from ui.common.page import Page
from utils.log import Log


class PageStack(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()       
        # initialize stacked layout
        self.stacked_layout = QtWidgets.QStackedLayout(self)        
        
        # initialize pages
        self.page_dashboard = Page('Dashboard')
        self.page_cpu = Page('CPU')
        self.page_gpu = Page('GPU')
        self.page_memory = Page('Memory')
        self.page_disk = Page('Disk')
        self.page_network = Page('Network')
        self.page_software = Page('Software')
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
    
    def switch_page(self, page):
        Log.debug(f"Switching to page '{page.title}'")
        self.stacked_layout.setCurrentWidget(page)    