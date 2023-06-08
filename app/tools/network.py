import subprocess

from PySide6 import QtCore

from utils.thread import Thread

class NetworkMonitor(Thread):
    def __init__(self, address='8.8.8.8'):
        super().__init__()
        self.address = address
    
    def execute(self):
        while True:
            result = subprocess.run(["ping", "-c", "1", self.address], capture_output=True, text=True)
            if result.returncode == 0:
                self.signals.log_debug.emit(f"Network is up. Ping to {self.address} successful")                
            else:
                self.signals.log_warning.emit(f"Network is down. Ping to {self.address} failed")
            QtCore.QThread.msleep(2000)


class SheepCounter(Thread):
    def __init__(self, herd=4):
        super().__init__()
        self.herd = herd        
    
    def execute(self):        
        for sheep in range(self.herd):
            self.signals.log_info.emit(f'Sheep #{sheep}')
            QtCore.QThread.msleep(1000)