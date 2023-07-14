from utils.helpers.decorators import singleton

from modules.cpu.cpu_model import CPUModel
from modules.cpu.cpu_page_view import CPUPageView
from modules.cpu.cpu_page_controller import CPUPageController

from modules.network.network_model import NetworkModel
from modules.network.network_page_view import NetworkPageView
from modules.network.network_page_controller import NetworkPageController

from modules.software.software_model import SoftwareModel
from modules.software.software_page_view import SoftwarePageView
from modules.software.software_page_controller import SoftwarePageController

from modules.gpu.gpu_model import GPUModel

@singleton
class Modules:
    def __init__(self):        
        # models
        self.software_model = SoftwareModel()
        self.cpu_model = CPUModel()
        self.network_model = NetworkModel()
        self.gpu_model = GPUModel()       
        
        # software page
        self.software_page_view = SoftwarePageView()
        self.software_page_controller = SoftwarePageController(self.software_model, self.software_page_view)
        # cpu page
        self.cpu_page_view = CPUPageView()
        self.cpu_page_controller = CPUPageController(self.cpu_model, self.cpu_page_view)
        # network page
        self.network_page_view = NetworkPageView()
        self.network_page_controller = NetworkPageController(self.network_model, self.network_page_view)     