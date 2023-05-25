import subprocess
import time

from PySide6 import QtCore

from utils.thread import ThreadManager


class NetworkMonitor(QtCore.QRunnable):
    def __init__(self, address='8.8.8.8'):
        super().__init__()

        self.address = address   
        self.is_running = True      
        
        ThreadManager.start_thread(self)

    @QtCore.Slot()
    def run(self):
        while self.is_running:
            result = subprocess.run(["ping", "-c", "1", self.address], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Ping to {self.address} successful")
            else:
                print(f"Ping to {self.address} failed")
            time.sleep(1)    

    def finish(self):
        self.is_running = False        
        ThreadManager.finish_thread(self)
            


class SheepCounter(QtCore.QRunnable):
    def __init__(self):
        super().__init__()

        self.is_running = True        

        ThreadManager.start_thread(self)    

    @QtCore.Slot()
    def run(self):        
        for sheep in range(1, 3):            
            print(f"Sheep {sheep}")
            time.sleep(1)

        if self.is_running:
            self.finish()

    def finish(self):
        self.is_running = False
        ThreadManager.finish_thread(self)
