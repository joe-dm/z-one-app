import sys
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from gui.window import Window
from resources.config import PathConfig
from util.logger import Logger

class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__()        
        Logger.setup_logs()     # setup logging               
        self.setup_stylesheet() # setup stylesheet
        self.window = Window()  # initialise main window

    def setup_stylesheet(self):        
        stylesheet_path = PathConfig.stylesheet()
        try:
            Logger.log('Loading app stylesheet', 'trying')
            with open(stylesheet_path, "r") as f:
                stylesheet_content = f.read()
                self.setStyleSheet(stylesheet_content)
        except FileNotFoundError:
            Logger.log(
                f"WARNING: Stylesheet file not found: {stylesheet_path}", 'warning')            
        except Exception as e:
            Logger.log(f"ERROR: Failed to load stylesheet: {str(e)}", 'error')
      
    
    def exit(self):
        sys.exit(self.exec())


if __name__ == '__main__':
    app = App()
    app.exit()