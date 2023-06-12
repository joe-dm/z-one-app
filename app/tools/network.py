import subprocess

from PySide6 import QtCore

from utils.thread import Thread
from utils.log import LogFile

class NetworkMonitor(Thread):
    def __init__(self, address='8.8.8.8'):
        super().__init__()
        self.address = address
        self.is_down = True
    
    def execute(self):
        self.signals.log_task.emit(f"Monitoring network", LogFile.network)
        while self.is_running:
            result = subprocess.run(["ping", "-c", "1", self.address], capture_output=True, text=True)
            if result.returncode == 0:                
                if self.is_down:
                    self.signals.log_info.emit(f"Internet connection available", LogFile.network)
                    self.is_down = False
            else:
                if not self.is_down:
                    self.signals.log_warning.emit(f"Internet connection not available. Ping to {self.address} failed", LogFile.network)
                    self.is_down = True
            QtCore.QThread.msleep(2000)

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
            self.signals.log_info.emit(f'Sheep #{sheep}')
            QtCore.QThread.msleep(1000)
    
    def finish(self):
        self.is_running = False


class ImportantCounter(Thread):
    def __init__(self, number=5):
        super().__init__()
        self.number = number
    
    def execute(self):        
        for n in range(self.number):            
            self.signals.log_info.emit(f'Important thread #{n}')
            QtCore.QThread.msleep(1000)
    
    def finish(self):
        self.signals.waiting.emit(self)