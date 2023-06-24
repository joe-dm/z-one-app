import subprocess

from PySide6 import QtCore

from config.config import PathConfig
from utils.log import LogFile
from utils.thread import Thread
from utils.log import Log

class NetworkMonitor(Thread):
    def __init__(self, address='8.8.8.8'):
        super().__init__()
        
        self.address = address
        self.is_down = None        

        self.signals.log_task.emit(f"Monitoring network", LogFile.network)
    
    def execute(self):
        
        while self.is_running:                 
            result = subprocess.run(["ping", "-c", "1", self.address], capture_output=True, text=True)
            if result.returncode == 0:
                #self.signals.log_debug.emit(f"Ping to {self.address} successful", None)                
                if self.is_down == None:
                    self.signals.log_info.emit(f"Internet connection available", LogFile.network)                    
                elif self.is_down == True:
                    self.signals.log_info.emit(f"Internet connection restored", LogFile.network)
                    self.signals.play_alert.emit(PathConfig.sound_internet_restored)
                self.is_down = False
            else:
                #self.signals.log_debug.emit(f"Ping to {self.address} failed", None) 
                if self.is_down == None or self.is_down == False:                 
                    self.signals.log_warning.emit(f"Internet connection not available. Ping to {self.address} failed", LogFile.network)
                    self.signals.play_alert.emit(PathConfig.sound_internet_down)
                self.is_down = True
            QtCore.QThread.msleep(2500)

    def finish(self):
        self.is_running = False


class SheepCounter(Thread):
    def __init__(self, herd=10000):
        super().__init__()
        self.herd = herd        
    
    def execute(self):        
        for sheep in range(self.herd):
            if not self.is_running:
                break
            self.signals.log_info.emit(f'Sheep #{sheep}', None)
            QtCore.QThread.msleep(1000)
    
    def finish(self):
        self.is_running = False


class ImportantCounter(Thread):
    def __init__(self, number=5):
        super().__init__()
        self.number = number
    
    def execute(self):        
        for n in range(self.number):            
            self.signals.log_info.emit(f'Important thread #{n}', None)
            QtCore.QThread.msleep(1000)
    
    def finish(self):
        self.signals.waiting.emit(self)