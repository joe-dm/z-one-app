from modules.cpu.cpu_model import CPUModel
from modules.cpu.cpu_view import CPUPageView

class CPUPageController:
    def __init__(self, model: CPUModel, view: CPUPageView):
        self.model = model
        self.view = view

        self.model.signals.updated_usage.connect(self.view.update_usage)
        self.model.signals.updated_frequency.connect(self.view.update_frequency)

    