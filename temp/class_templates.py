from PySide6 import QtCore
from app.utils.thread import ThreadManager

class ThreadEndless(QtCore.QRunnable):
    def __init__(self):
        super().__init__()
               
        self.is_running = True 
        
        ThreadManager.start_thread(self)

    @QtCore.Slot()
    def run(self):
        while self.is_running:
            # code goes here
            pass

    

    def finish(self):
        self.is_running = False        
        ThreadManager.finish_thread(self)