from PySide6 import QtWidgets

from ui.common.page import Page 
from ui.page_views.software_page_view import SoftwarePageView
from ui.page_views.cpu_page_view import CPUPageView
from ui.page_views.network_page_view import NetworkPageView
from ui.page_views.gpu_page_view import GPUPageView
from ui.page_views.memory_page_view import MemoryPageView
from ui.page_views.device_page_view import DevicePageView

from utils.log import Log


class PageStack(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()       
        # initialize stacked layout
        self.stacked_layout = QtWidgets.QStackedLayout(self)        
        
        # initialize page views
        self.page_software = SoftwarePageView() # must be initialized first (for os info)
        self.page_network = NetworkPageView()
        self.cpu_page_view = CPUPageView()
        self.page_gpu = GPUPageView()
        self.page_memory = MemoryPageView()
        self.page_device = DevicePageView()

        self.page_dashboard = Page('Dashboard')                
        self.page_disk = Page('Disk')
        self.page_settings = Page('Settings')
        self.page_logs = Page('Logs')

        # list of all pages
        self.pages = [
            self.page_dashboard, self.page_device, self.cpu_page_view, 
            self.page_gpu, self.page_memory, self.page_disk, self.page_network,
            self.page_software, self.page_settings, self.page_logs]
        
        # add pages to layout
        for page in self.pages:
            self.stacked_layout.addWidget(page)    
    
        Log.debug_init(self)
    
    def switch_page(self, page: Page):
        Log.debug(f"Switching to {page.title} page")
        self.stacked_layout.setCurrentWidget(page)    