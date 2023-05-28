import os

from gui.popup import PopupExit
from gui.window import QApp
from resources.config import AppConfig
from tools.network import NetworkMonitor, ImportantCounter
from utils.thread import ThreadManager
from utils.log import Log


class App:
    def __init__(self):
        self.start()

        self.qapp = QApp()        
        self.qapp.main_window.closeEvent = self.exit

        self.net_mon = NetworkMonitor()
        self.counter = ImportantCounter()
        

    def start(self):  
        # clear console      
        os.system('cls' if os.name == 'nt' else 'clear')        

        # setup log folder
        Log.check_dir()

        # show app info
        Log.no_flag(f"{AppConfig.Info.description}")
        Log.no_flag("")
        Log.info(f"{AppConfig.Info.name} started at {os.getcwd()}")

        # show debug mode
        debug_mode = "enabled" if AppConfig.debug else "disabled"
        Log.info(f'Debugging mode is {debug_mode}')
        
    
    def exit(self, event):
        Log.info('Exiting app...')
        ThreadManager.clean_up()  
        
        # open popup
        popup = PopupExit(self.qapp.main_window, 'Cleaning up and exiting...\nPlease wait.')
        
        # wait for all threads to finish
        while ThreadManager.active_threads:
            self.qapp.processEvents()
        
        # close popup
        popup.close()

        # accept close event
        event.accept()    
        
        

if __name__ == '__main__':
    app = App()
    app.qapp.exec()
