import subprocess

from PySide6 import QtCore

from utils.thread import ThreadManager
from utils.log import Log


# thread that never ends
class NetworkMonitor(QtCore.QRunnable):
    def __init__(self, address='8.8.8.8'):
        super().__init__()

        self.address = address        
        self.is_running = True
        
        ThreadManager.start_thread(self)

    @QtCore.Slot()
    def run(self):
        Log.task('Started monitoring network')
        while self.is_running:
            result = subprocess.run(["ping", "-c", "1", self.address], capture_output=True, text=True)
            if result.returncode == 0:                
                Log.debug(f"Ping to {self.address} successful")
            else:
                Log.debug(f"Ping to {self.address} failed")
            #QtCore.QThread.msleep(100)  

    def finish(self):
        self.is_running = False        
        ThreadManager.report_finished(self)

# thread that ends and can be ended early by ThreadManager
class TestThread(QtCore.QRunnable):
    def __init__(self):
        super().__init__()

        self.is_running = True      
        
        ThreadManager.start_thread(self)

    @QtCore.Slot()
    def run(self, maximum=100000):
        Log.task('Started test thread')
        for n in range(1, maximum):
            if not self.is_running:
                break
            
            Log.debug(f"Test #{n}")  

            if n == 3:
                Log.warning('This is a warning message.')
            elif n == 5:
                Log.error('This is an error message.')
                
            #QtCore.QThread.msleep(100)
        
        if self.is_running:
            self.finish()

    def finish(self):
        self.is_running = False        
        ThreadManager.report_finished(self)


# thread that ends on its own and cannot be ended early by ThreadManager
class ImportantCounter(QtCore.QRunnable):    

    def __init__(self):
        super().__init__()
        self.is_running = True
        ThreadManager.start_thread(self)

    @QtCore.Slot()
    def run(self, count=15):
        Log.task('Started counting important things')
        for n in range(1, count):
            Log.debug(f"Counting important thing #{n}")
            QtCore.QThread.msleep(1000)
        
        self.is_running = False
        ThreadManager.report_finished(self)

    def finish(self):
        ThreadManager.report_waiting(self)