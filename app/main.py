import sys, os

import PySide6.QtWidgets as QtWidgets

from gui.window import MainWindow
from resources.config import AppConfig, PathConfig
from util.logger import Logger

class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__()                        
        self.start()
        self.window = MainWindow() 
    
    def start(self):        
        # setup log folder and file
        Logger.check_log_dir()

        # show app info
        Logger.log(f'{AppConfig.description}', 'none')
        Logger.log(f'\n', 'none')
        Logger.log(f'{AppConfig.name} started at {os.getcwd()}', 'info')

        # show debugging mode 
        if AppConfig.debug: Logger.log(f'Debugging mode is enabled', 'info')            
        else: Logger.log(f'Debugging mode is disabled', 'info')

        Logger.log(f'Setting up GUI', 'operation')

        # setup stylesheet        
        stylesheet_path = PathConfig.stylesheet
        try:
            Logger.log('Setting stylesheet', 'debug')
            with open(stylesheet_path, "r") as f:
                stylesheet_content = f.read()
                self.setStyleSheet(stylesheet_content)
        except FileNotFoundError:
            Logger.log(f"Stylesheet file not found: {stylesheet_path}", 'warning')
            Logger.log(f"Default system style will be used", 'child')
        except Exception as e:
            Logger.log(f"Failed to load stylesheet: {str(e)}", 'error')
      
    
    def exit(self):
        sys.exit(self.exec())


if __name__ == '__main__':
    app = App()
    app.exit()