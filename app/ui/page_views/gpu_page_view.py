from models.gpu_model import GPUModel

from ui.common.page import Page
from ui.common.table import TableForm

from utils.log import Log


class GPUPageView(Page):
    def __init__(self):
        super().__init__('GPU')

        self.adapter_table = TableForm(title='Specifications')

        self.insert_widget(self.adapter_table)

        self._controller = GPUPageController(self)
        Log.debug_init(self)

class GPUPageController:
    def __init__(self, view: GPUPageView):
        self.view = view
        self.model = GPUModel()

        adapter_data = [
            (key.split()[0].capitalize() + ' ' + ' '.join(word.capitalize() for word in key.split()[1:]), value)
            for key, value in self.model.get_display_adapter_dict().items()]
        self.view.adapter_table.set_data(adapter_data)

        Log.debug_init(self)

