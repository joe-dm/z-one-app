import subprocess
import time

from PySide6 import QtCore

from app.utils.thread import ThreadManager


# infinite thread that is ended by ThreadManager
class ThreadEndless(QtCore.QRunnable):
    def __init__(self):
        super().__init__()              
        self.is_running = True        
        ThreadManager.start_thread(self)

    @QtCore.Slot()
    def run(self):
        while self.is_running:            
            pass # endless tasks go here

    def finish(self):
        self.is_running = False        
        ThreadManager.report_finished(self)


# thread that ends and can be ended early by ThreadManager
class ThreadNotImportant(QtCore.QRunnable):
    def __init__(self):
        super().__init__()
        self.is_running = True        
        ThreadManager.start_thread(self)

    @QtCore.Slot()
    def run(self):
        for i in range(1, 10):
            if not self.is_running:
                break
            # tasks go here
        
        if self.is_running:
            self.finish()

    def finish(self):
        self.is_running = False        
        ThreadManager.report_finished(self)


# thread that ends but cannot be ended early by ThreadManager
class ThreadImportant(QtCore.QRunnable):   

    def __init__(self):
        super().__init__()
        self.is_running = True
        ThreadManager.start_thread(self)

    @QtCore.Slot()
    def run(self):
        for n in range(1, 10):
            pass # tasks go here
        
        self.is_running = False
        ThreadManager.report_finished(self)

    def finish(self):
        ThreadManager.report_waiting(self)