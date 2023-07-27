from models.cpu_model import CPUModel

from ui.common.page import Page
from ui.common.chart import Chart
from ui.common.card import Card, CardGroup
from ui.common.table import TableForm

from utils.convert import Convert
from utils.log import Log


class CPUPageView(Page):
    def __init__(self):
        super().__init__('CPU')         

        self.usage_chart = Chart(title='Overall Usage', y_axis_max=100)
        self.stats_cards = CPUStatsCards()
        self.specs_table = TableForm(title='Specifications')

        self.insert_widget(self.usage_chart)
        self.insert_widget(self.stats_cards)
        self.insert_widget(self.specs_table) 
        
        self._controller = CPUPageController(self)  
        
        self.check_missing_info()
        Log.debug_init(self)      
    
    
class CPUStatsCards(CardGroup):
    def __init__(self):
        super().__init__()

        self.usage_card = Card('Usage')
        self.frequency_card = Card('Frequency', 'GHz')

        self.insert_cards([self.usage_card, self.frequency_card])


class CPUPageController:
    def __init__(self, view: CPUPageView):
        self.view = view
        self.model = CPUModel()          

        # set the data for the specs table
        self.set_specs_table_data() 

        # used to track cpu usage
        self.last_usage_value = 0
        self.ms_since_usage_updated = 0
        # used to track cpu frequency
        self.last_frequency_value = 0
        self.ms_since_frequency_updated = 0

        # connect signals
        self.model.signals.updated_usage.connect(self.update_usage)
        self.model.signals.updated_frequency.connect(self.update_frequency)
        

    def set_specs_table_data(self):      
        l1_size, l1_unit = Convert.bytes_to_unit(self.model.get_l1_total_size())        
        l2_size, l2_unit = Convert.bytes_to_unit(self.model.get_l2_total_size())   
        l3_size, l3_unit = Convert.bytes_to_unit(self.model.get_l3_cache_size())   
        
        table_data = [
            ('Name', self.model.get_name()),
            ('Signature', self.model.get_signature()),
            ('Manufacturer', self.model.get_manufacturer()),
            ('Architecture', f"{self.model.get_architecture()}-Bit"),
            ('Cores', self.model.get_cores_physical()),
            ('Threads', self.model.get_cores_logical()),            
            ('Max Speed', f"{self.model.get_frequency_max()} GHz"),
            ('Voltage', self.model.get_voltage()),
            ('Socket', self.model.get_socket()),
            ('L1 Cache', f"{l1_size} {l1_unit}"),
            ('L2 Cache', f"{l2_size} {l2_unit}"),
            ('L3 Cache', f"{l3_size} {l3_unit}"),
            ('ID', self.model.get_id())]        
        
        # check if data is missing
        for item in table_data:
            if item[1] == None:
                self.view.missing_info = True

        self.view.specs_table.set_data(table_data)

    def update_usage(self, value):
        # update the chart
        self.view.usage_chart.update_chart(value)

        # update the card
        if self.ms_since_usage_updated > 300:
            if abs(self.last_usage_value - value) > 15:
                self.view.stats_cards.usage_card.update_stat(f"{value}%")
                self.ms_since_usage_updated = 0
            elif self.ms_since_usage_updated > 1000:
                self.view.stats_cards.usage_card.update_stat(f"{value}%")
                self.ms_since_usage_updated = 0
            else:
                self.ms_since_usage_updated += 100
        else:
            self.ms_since_usage_updated += 100
        
        # set the last value for next iteration
        self.last_usage_value = value
    
    def update_frequency(self, value):
        # update the card
        if self.ms_since_frequency_updated > 300:
            if abs(self.last_frequency_value - value) > 0.2:
                self.view.stats_cards.frequency_card.update_stat(value)
                self.ms_since_frequency_updated = 0
            elif self.ms_since_frequency_updated > 1000:
                self.view.stats_cards.frequency_card.update_stat(value)
                self.ms_since_frequency_updated = 0
            else:
                self.ms_since_frequency_updated += 100
        else:
            self.ms_since_frequency_updated += 100
        # set the last value for next iteration
        self.last_frequency_value = value  