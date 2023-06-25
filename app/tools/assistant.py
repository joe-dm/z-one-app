from PySide6 import QtCore

from config.config import PathConfig
from tools.system_info import NetworkInfo, CPUInfo
from utils.thread import Thread
from utils.log import LogFile


class Assistant(Thread):
    def __init__(self):
        super().__init__()        
    
    def execute(self):
        self.connection_down = None        

        while self.is_running:
            self.check_network_internet_connection()
            QtCore.QThread.msleep(100)
        

    def check_network_internet_connection(self):
        if NetworkInfo.internet_available:
            if self.connection_down == None:
                self.signals.log_info.emit(f"Internet connection available", LogFile.network)
            elif self.connection_down == True:
                self.signals.log_info.emit(f"Internet connection restored", LogFile.network)
                self.signals.play_alert.emit(PathConfig.alert_internet_restored)
            self.connection_down = False
        elif NetworkInfo.internet_available == None:
            pass
        else:
            if self.connection_down == None or self.connection_down == False:
                self.signals.log_warning.emit(f"Internet connection not available", LogFile.network)
                self.signals.play_alert.emit(PathConfig.alert_internet_down)
            self.connection_down = True
