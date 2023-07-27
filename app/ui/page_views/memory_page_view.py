from models.memory_model import MemoryModel

from ui.common.chart import Chart
from ui.common.table import TableForm
from ui.common.page import Page
from utils.log import Log

class MemoryPageView(Page):
    def __init__(self):
        super().__init__('Memory')

        self.ram_usage_chart = Chart(title='RAM Usage', y_axis_max=100)
        
        self.insert_widget(self.ram_usage_chart)

        self._controller = MemoryPageController(self)
        self.check_missing_info()
        Log.debug_init(self)

    def add_device_table(self, data, title):
        table = TableForm(title)
        table.set_data(data)
        self.insert_widget(table)        


class MemoryPageController:
    def __init__(self, view: MemoryPageView):
        self.view = view
        self.model = MemoryModel()

        self.set_device_tables()

        # connect signals
        self.model.signals.updated_ram_usage.connect(self.update_ram_usage)
    
    def set_device_tables(self):         
        ram_devices = self.model.get_ram_devices()

        if ram_devices:
            for device_dict in ram_devices:
                table_data = [
                    ('Manufacturer', device_dict['Manufacturer']),
                    ('Type', device_dict['Type']),
                    ('Serial Num', device_dict['Serial Number']),
                    ('Part Num', device_dict['Part Number']),
                    ('Size', device_dict['Size']),
                    ('Data Width', device_dict['Data Width']),
                    ('Total Width', device_dict['Total Width']),
                    ('Speed', device_dict['Speed']),                
                    ('Config Speed', device_dict['Configured Memory Speed']),  
                    ('Min Voltage', device_dict['Minimum Voltage']),                
                    ('Max Voltage', device_dict['Maximum Voltage']),   
                    ('Config Voltage', device_dict['Configured Voltage']),   
                ]
                self.view.add_device_table(data=table_data, title=device_dict['Bank Locator'])
        else:
            self.view.missing_info = True
        

    def update_ram_usage(self, value):
        self.view.ram_usage_chart.update_chart(value)
