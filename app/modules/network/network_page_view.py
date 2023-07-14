from PySide6 import QtWidgets
from ui.common.card import Card, CardGroup
from ui.common.page import Page
from ui.common.table import TableForm

class NetworkPageView(Page):
    def __init__(self):
        super().__init__('Network')

        self.stats_cards = NetworkStats()
        self.speed_cards = NetworkSpeed()
        self.ip_isp_table = TableForm(title='Connection')
        self.interface_tables = []

        self.insert_widget(self.stats_cards)    
        self.insert_widget(self.speed_cards)  
        self.insert_widget(self.ip_isp_table)

    def clear_interface_tables(self):
        for table in self.interface_tables:
            self.remove_widget(table)        
        self.interface_tables = []
    def add_interface_table(self, data, title):        
        table = TableForm(title)
        table.set_data(data)
        self.insert_widget(table)
        self.interface_tables.append(table)
    
class NetworkSpeed(CardGroup):
    def __init__(self):
        super().__init__(title='Speed Test')

        self.download_card = Card('Download', 'Mbps')
        self.upload_card = Card('Upload', 'Mbps')
        self.latency_card = Card('Latency', 'ms')
        self.quality_card = Card('Quality')
        self.insert_cards([self.download_card, self.upload_card, self.latency_card, self.quality_card])        

class NetworkStats(CardGroup):
    def __init__(self):
        super().__init__()

        self.internet_card = Card('Internet')
        self.sent_card = Card('Sent', 'Mbps')
        self.received_card = Card('Received', 'Mbps')
    
        self.insert_cards([self.internet_card, self.sent_card, self.received_card])

