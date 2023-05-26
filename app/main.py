from gui.window import QApp
from utils.thread import ThreadManager
from tools.network import NetworkMonitor, SheepCounter

class App:
    def __init__(self):
        self.qapp = QApp()

        self.net_mon = NetworkMonitor()
        self.sheep = SheepCounter()

        # setup window close event
        self.qapp.main_window.closeEvent = self.exit

    def exit(self, event):
        ThreadManager.clean_up()
    

if __name__ == '__main__':
    app = App()
    app.qapp.exec()
