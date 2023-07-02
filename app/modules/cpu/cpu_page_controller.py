from modules.cpu.cpu_model import CPUModel
from modules.cpu.cpu_page_view import CPUPageView
from utils.helpers.convert import Convert

class CPUPageController:
    def __init__(self, model: CPUModel, view: CPUPageView):
        self.view = view 
        self.model = model               
        
        # set table data        
        l1_size, l1_unit = Convert.bytes_to_unit(self.model.get_l1_total_size())        
        l2_size, l2_unit = Convert.bytes_to_unit(self.model.get_l2_total_size())   
        l3_size, l3_unit = Convert.bytes_to_unit(self.model.get_l3_cache_size())   
        table_data = [
            ('Name', self.model.get_name()),
            ('Architecture', f"{self.model.get_architecture()}-Bit"),
            ('Cores', self.model.get_cores_physical()),
            ('Threads', self.model.get_cores_logical()),
            ('Base Clock', f"{self.model.get_frequency_max()} GHz"),
            ('L1 Cache', f"{l1_size} {l1_unit}"),
            ('L2 Cache', f"{l2_size} {l2_unit}"),
            ('L3 Cache', f"{l3_size} {l3_unit}")]       
        self.view.info_table.set_data(table_data)

        # connect signals
        self.model.signals.updated_usage.connect(self.view.update_usage)
        self.model.signals.updated_frequency.connect(self.view.update_frequency)

        
        