from PySide6 import QtWidgets, QtCore

from config.theme import ThemeColor
from gui.common.elements import LabelWidgetTitle
from tools.system_info import CPUInfo, NetworkInfo

class StatsViewer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()       
        
        self.title_label = LabelWidgetTitle('Live Stats')

        self.card_container = QtWidgets.QWidget()
        self.container_layout = QtWidgets.QHBoxLayout(self.card_container)
        self.container_layout.setContentsMargins(0,0,0,0)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.title_label)
        layout.addWidget(self.card_container)  
    
    
    def insert_cards(self, card_list):
        for card in card_list:
            self.container_layout.addWidget(card)
        self.container_layout.addStretch()

class StatCard(QtWidgets.QFrame):
    def __init__(self, title, get_value_func, timer_ms=1000, unit=''):
        super().__init__(objectName='StatCard') 

        # value to be updated/tracked
        self.get_value_func = get_value_func
        self.unit = unit
        
        # setup labels
        self.title_label = QtWidgets.QLabel(title, objectName='StatCardTitleLabel')
        self.title_label.setAlignment(QtCore.Qt.AlignCenter) 
        self.stat_label = QtWidgets.QLabel(objectName='StatCardTextLabel')
        self.stat_label.setAlignment(QtCore.Qt.AlignCenter) 
        self.unit_label = QtWidgets.QLabel(objectName='StatCardUnitLabel')
        self.unit_label.setText(unit)
        self.unit_label.setAlignment(QtCore.Qt.AlignCenter) 

        # setup layout
        layout = QtWidgets.QVBoxLayout(self)   
        layout.setContentsMargins(5, 1, 5, 1)   
        layout.setSpacing(1) 
        layout.setAlignment(QtCore.Qt.AlignCenter)        
        layout.addWidget(self.title_label)    
        layout.addSpacing(5)
        layout.addWidget(self.stat_label)
        layout.addWidget(self.unit_label)

        # setup timer
        self.stat_timer = QtCore.QTimer()
        self.stat_timer.timeout.connect(self.update_stat)
        self.stat_timer.start(timer_ms)        

    def update_stat(self):
        value = self.get_value_func()                 
        self.stat_label.setText(f'{value}')

class InternetStatCard(StatCard):
    def __init__(self, title, get_value_func, timer_ms=1000, unit=''):
        super().__init__(title, get_value_func, timer_ms, unit)
    
    def update_stat(self):
        value = self.get_value_func()
        self.stat_label.setText(f'{value}')
        if value == 'UP':
            self.stat_label.setStyleSheet(f'color: {ThemeColor.green};')
        elif value == 'DOWN':
            self.stat_label.setStyleSheet(f'color: {ThemeColor.red};')
        else:
            self.stat_label.setStyleSheet(f'color: {ThemeColor.white};')

class CPUStats(StatsViewer):
    def __init__(self):
        super().__init__()
        
        self.utilization = StatCard(
            title='Utilization', 
            get_value_func=lambda: CPUInfo.get_usage_current(include_unit=True))
        
        self.frequency = StatCard(
            title='Frequency', 
            get_value_func=CPUInfo.get_frequency_current, 
            unit=' GHz')
        
        #self.temperature = StatCard('Temperature')
        #self.processes = StatCard('Processes')
        #self.threads = StatCard('Threads')
        #self.up_time = StatCard('Up Time')

        card_list = [self.utilization, self.frequency]

        self.insert_cards(card_list)

class NetworkStats(StatsViewer):
    def __init__(self):
        super().__init__()

        self.internet_status = InternetStatCard(
            title='Internet Status', 
            get_value_func=NetworkInfo.get_internet_available)
        
        self.download_speed = StatCard(
            title='Download Speed',
            get_value_func=NetworkInfo.get_speed_download,
            unit='Mbps')
        self.upload_speed = StatCard(
            title='Upload Speed',
            get_value_func=NetworkInfo.get_speed_upload,
            unit='Mbps')
        
        self.bytes_sent = StatCard(
            title='Bytes Sent', 
            get_value_func=NetworkInfo.get_bytes_sent,
            unit='Mbps')        
        self.bytes_received = StatCard(
            title='Bytes Received', 
            get_value_func=NetworkInfo.get_bytes_received,
            unit='Mbps')
        
        
        cards = [
            self.internet_status, self.download_speed, self.upload_speed,
            self.bytes_received, self.bytes_sent]        

        self.insert_cards(cards)
        
        