from gui.app import AppGUI
from utils.logger import Logger
from resources.config import AppConfig

class App():
    def __init__(self):        
        self.app_gui = AppGUI()        
        Logger.setup_logs()         

    def exit(self):        
        self.app_gui.exit()
        Logger.log(f'Exiting {AppConfig.name()}...')

if __name__ == '__main__':    
    app = App()
    app.exit()