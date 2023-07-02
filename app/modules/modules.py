from utils.helpers.decorators import singleton
from modules.cpu.cpu_model import CPUModel
from modules.cpu.cpu_page_view import CPUPageView
from modules.cpu.cpu_page_controller import CPUPageController

@singleton
class Modules:
    def __init__(self):
        self.cpu_model = CPUModel()

        self.cpu_page_view = CPUPageView()
        self.cpu_page_controller = CPUPageController(self.cpu_model, self.cpu_page_view)