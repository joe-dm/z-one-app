import os
from gui.app_gui import AppGUI
from utils.logger import Logger
from resources.config import AppConfig

class App():
    def __init__(self):        
        self.start()
        self.app_gui = AppGUI()

    def start(self):  
        # clear console  
        os.system('cls' if os.name=='nt' else 'clear')
        # set up logs
        Logger.setup_logs()        
        # show app and developer info
        Logger.log(f'{AppConfig.description()}\n', 'none')     
        # show app starting directory
        Logger.log(f'{AppConfig.name()} started at {os.getcwd()}')  
        # show debug mode
        if AppConfig.debug() == True: 
            Logger.log(f'Debugging mode is enabled', 'info')
        else:
            Logger.log(f'Debugging mode is disabled', 'info')

    def exit(self):        
        self.app_gui.exit()
        Logger.log(f'Exiting {AppConfig.name()}...')

if __name__ == '__main__':    
    app = App()
    app.exit()