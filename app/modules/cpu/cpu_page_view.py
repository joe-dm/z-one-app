from ui.common.page import Page
from ui.common.chart import Chart
from ui.common.card import Card, CardGroup
from ui.common.table import TableForm


class CPUPageView(Page):
    def __init__(self):
        super().__init__('CPU')         

        self.usage_chart = Chart(title='Overall Usage', y_axis_max=100)
        self.stats_cards = CPUStats()
        self.info_table = TableForm(title='Specifications')

        self.insert_widget(self.usage_chart)
        self.insert_widget(self.stats_cards)
        self.insert_widget(self.info_table)

        self.last_usage_value = 0
        self.ms_since_usage_updated = 0

        self.last_frequency_value = 0
        self.ms_since_frequency_updated = 0               

    def update_usage(self, value):           
        self.usage_chart.update_chart(value)

        if self.ms_since_usage_updated > 300:
            if abs(self.last_usage_value - value) > 15:
                self.stats_cards.update_card(self.stats_cards.usage_card, f"{value}%")            
                self.ms_since_usage_updated = 0
            elif self.ms_since_usage_updated > 1000:
                self.stats_cards.update_card(self.stats_cards.usage_card, f"{value}%")
                self.ms_since_usage_updated = 0
            else:
                self.ms_since_usage_updated += 100
        else:
            self.ms_since_usage_updated += 100
        
        self.last_usage_value = value
    
    def update_frequency(self, value):
        if self.ms_since_frequency_updated > 300:        
            if abs(self.last_frequency_value - value) > 0.2:
                self.stats_cards.update_card(self.stats_cards.frequency_card, value)
                self.ms_since_frequency_updated = 0
            elif self.ms_since_frequency_updated > 1000:
                self.stats_cards.update_card(self.stats_cards.frequency_card, value)
                self.ms_since_frequency_updated = 0
            else:
                self.ms_since_frequency_updated += 100
        else:
            self.ms_since_frequency_updated += 100
        
        self.last_frequency_value = value        


class CPUStats(CardGroup):
    def __init__(self):
        super().__init__()

        self.usage_card = Card('Usage')
        self.frequency_card = Card('Frequency', 'GHz')

        self.insert_cards([self.usage_card, self.frequency_card])
    
    def update_card(self, card: Card, value):
        card.update_stat(value)