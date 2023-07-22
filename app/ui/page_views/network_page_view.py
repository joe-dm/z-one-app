from config.theme import ThemeColor

from models.network_model import NetworkModel

from ui.common.card import Card, CardGroup
from ui.common.page import Page
from ui.common.table import TableForm

from utils.log import Log


class NetworkPageView(Page):
    def __init__(self):
        super().__init__('Network')

        self.stats_cards = NetworkStatsCards()
        self.speed_cards = NetworkSpeedCards()
        self.ip_isp_table = TableForm(title='Connection')
        self.interface_tables = []

        self.insert_widget(self.stats_cards)    
        self.insert_widget(self.speed_cards)  
        self.insert_widget(self.ip_isp_table)

        self._controller = NetworkPageController(self)
        Log.debug_init(self)

    def clear_interface_tables(self):
        for table in self.interface_tables:
            self.remove_widget(table)        
        self.interface_tables = []
    def add_interface_table(self, data, title):        
        table = TableForm(title)
        table.set_data(data)
        self.insert_widget(table)
        self.interface_tables.append(table)
    

class NetworkSpeedCards(CardGroup):
    def __init__(self):
        super().__init__(title='Speed Test')

        self.download_card = Card('Download', 'Mbps')
        self.upload_card = Card('Upload', 'Mbps')
        self.latency_card = Card('Latency', 'ms')
        self.quality_card = Card('Quality')
        self.insert_cards([self.download_card, self.upload_card, self.latency_card, self.quality_card])       

class NetworkStatsCards(CardGroup):
    def __init__(self):
        super().__init__()

        self.internet_card = Card('Internet')
        self.sent_card = Card('Sent', 'Mbps')
        self.received_card = Card('Received', 'Mbps')
    
        self.insert_cards([self.internet_card, self.sent_card, self.received_card])


class NetworkPageController:
    def __init__(self, view: NetworkPageView):
        self.view = view
        self.model = NetworkModel()
        
        self.update_interface_tables(self.model.get_interfaces())
        self.view.ip_isp_table.set_data([('IP', '-'), ('ISP', '-')])

        self.model.signals.updated_interfaces.connect(self.update_interface_tables)
        self.model.signals.updated_internet_available.connect(self.update_internet_available)
        self.model.signals.updated_speed_download.connect(self.update_speed_download)
        self.model.signals.updated_speed_upload.connect(self.update_speed_upload)
        self.model.signals.updated_latency.connect(self.update_latency)
        self.model.signals.updated_quality.connect(self.update_quality)
        self.model.signals.updated_ip_isp.connect(self.update_ip_isp)
        self.model.signals.updated_bytes_sent.connect(self.update_bytes_sent)
        self.model.signals.updated_bytes_received.connect(self.update_bytes_received)
        
        Log.debug_init(self)

    def update_internet_available(self, internet_available):
        if internet_available:
            self.view.stats_cards.internet_card.update_stat('UP')
            self.view.stats_cards.internet_card.label_stat.setStyleSheet(f'color: {ThemeColor.green}')
        else:
            self.view.stats_cards.internet_card.update_stat('DOWN')
            self.view.stats_cards.internet_card.label_stat.setStyleSheet(f'color: {ThemeColor.red}')
            self.view.speed_cards.upload_card.label_stat.setText('-')
            self.view.speed_cards.download_card.label_stat.setText('-')
            self.view.speed_cards.quality_card.label_stat.setText('-')            

    def update_bytes_sent(self, sent):
        if sent: self.view.stats_cards.sent_card.update_stat(f"{sent:.1f}")
        else: self.view.stats_cards.sent_card.update_stat('-')
    def update_bytes_received(self, received):
        if received: self.view.stats_cards.received_card.update_stat(f"{received:.1f}")
        else: self.view.stats_cards.received_card.update_stat('-')

    def update_latency(self, latency):
        if latency: self.view.speed_cards.latency_card.update_stat(round(latency))
        else: self.view.speed_cards.latency_card.update_stat('-')            
    def update_quality(self, quality):
        if quality: self.view.speed_cards.quality_card.update_stat(quality)   
        else: self.view.speed_cards.quality_card.update_stat('-')

    def update_ip_isp(self):
        if self.model.get_ip_address() and self.model.get_isp():
            table_data = [('IP', self.model.get_ip_address()), ('ISP', self.model.get_isp())]        
            self.view.ip_isp_table.clear_data()           
            self.view.ip_isp_table.update_data(table_data)
        else:
            self.view.ip_isp_table.clear_data()

    def update_speed_download(self, speed):
        if speed: self.view.speed_cards.download_card.update_stat(f"{speed:.1f}")
        else: self.view.speed_cards.download_card.update_stat('-')
    def update_speed_upload(self, speed):
        if speed: self.view.speed_cards.upload_card.update_stat(f"{speed:.1f}")
        else: self.view.speed_cards.upload_card.update_stat('-')    

    def update_interface_tables(self, data):
        self.view.clear_interface_tables()       
        loopback_interface = None

        for interface in data:  
            table_data = []          
            for address, netmask in interface['addresses']:
                table_data.append(('IPv4', address))
                table_data.append(('Netmask', netmask))
            for address, netmask in interface['ipv6_addresses']:
                table_data.append(('IPv6', f"{address} {netmask}"))
            table_data.append(('MAC', interface['mac_address']))
            table_data.append(('MTU', interface['mtu']))            
            table_data.append(('Flags', str(interface['flags']).replace(',', ', ')))
            if 'loopback' in interface['flags']:
                loopback_interface = table_data
            else:
                self.view.add_interface_table(data=table_data, title=f"Interface: {interface['interface']}")
        self.view.add_interface_table(data=loopback_interface, title=f"Loopback Interface")
            