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
    
    
class CPUStats(CardGroup):
    def __init__(self):
        super().__init__()

        self.usage_card = Card('Usage')
        self.frequency_card = Card('Frequency', 'GHz')

        self.insert_cards([self.usage_card, self.frequency_card])
        