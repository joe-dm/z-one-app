from gui.window import QApp
from tools.network import NetworkMonitor, SheepCounter
from utils.thread import ThreadManager

class App:
    def __init__(self):
        self.qapp = QApp()   
        self.network_monitor = NetworkMonitor()        
        self.sheep = SheepCounter()
        
        # connect main window close event to thread cleanup
        self.qapp.main_window.closeEvent = self.cleanup_threads


    def cleanup_threads(self, event):
        ThreadManager.clean_up()
        #event.accept()

    def quit(self): 
        self.qapp.quit()
        



if __name__ == '__main__':
    app = App()
    app.quit()
    