from PySide6 import QtWidgets, QtCore

from gui.common.elements import LabelWidgetTitle
from tools.info_gatherer import CPUInfo

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

        # setup layout
        layout = QtWidgets.QVBoxLayout(self)       
        layout.setAlignment(QtCore.Qt.AlignCenter)        
        layout.addWidget(self.title_label)        
        layout.addWidget(self.stat_label)

        # setup timer
        self.stat_timer = QtCore.QTimer()
        self.stat_timer.timeout.connect(self.update_stat)
        self.stat_timer.start(timer_ms)        

    def update_stat(self):
        try:
            value = self.get_value_func(format_output=True)
        except TypeError:
            value = self.get_value_func()

        if value:             
            self.stat_label.setText(f'{value}')


class CPUStats(StatsViewer):
    def __init__(self):
        super().__init__()
        
        self.utilization = StatCard(
            title='Utilization', get_value_func=CPUInfo.check_current_usage, unit='%')
        self.frequency = StatCard(
            title='Frequency', get_value_func=CPUInfo.check_current_frequency, unit=' GHz')
        #self.temperature = StatCard('Temperature')
        #self.processes = StatCard('Processes')
        #self.threads = StatCard('Threads')
        #self.up_time = StatCard('Up Time')

        card_list = [
            self.utilization, self.frequency]

        self.insert_cards(card_list)
        
        