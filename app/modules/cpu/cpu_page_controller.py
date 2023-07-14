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

        # track cpu usage
        self.last_usage_value = 0
        self.ms_since_usage_updated = 0
        # track cpu frequency
        self.last_frequency_value = 0
        self.ms_since_frequency_updated = 0

        # connect signals
        self.model.signals.updated_usage.connect(self.update_usage)
        self.model.signals.updated_frequency.connect(self.update_frequency)

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