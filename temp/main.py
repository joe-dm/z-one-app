import os
import time

from PySide6 import QtCore, QtWidgets

from gui.window import MainWindow
from resources.config import AppConfig, PathConfig
from tools.info_gatherer import BasicInfo
from utils.log import Logger
from utils.thread import Thread


class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.setup()
        self.window = MainWindow()
        self.gather_info()

    def setup(self):
        # setup log folder and file
        Logger.check_log_dir()

        # show app info
        Logger.log(f'{AppConfig.description}', 'none')
        Logger.log(f'\n', 'none')
        Logger.log(f'{AppConfig.name} started at {os.getcwd()}', 'info')

        # show debugging mode
        debug_mode = "enabled" if AppConfig.debug else "disabled"
        Logger.log(f'Debugging mode is {debug_mode}', 'info')

        Logger.log('Setting up GUI', 'operation')

        # setup stylesheet
        #stylesheet_path = PathConfig.stylesheet
        #try:
        #    Logger.log('Setting stylesheet', 'debug')
        #    with open(stylesheet_path, "r") as f:
        #        stylesheet_content = f.read()
        #        self.setStyleSheet(stylesheet_content)
        #except FileNotFoundError:
        #    Logger.log(f"Stylesheet file not found: {stylesheet_path}", 'warning')
        #    Logger.log("Default system style will be used", 'child')
        #except Exception as e:
        #    Logger.log(f"Failed to load stylesheet: {str(e)}", 'error')

    def gather_info(self):
        Logger.log('Gathering system info', 'operation')
        self.basic_info = BasicInfo()
        Thread.start(self.count)        
        


    def count(self, n=10):
        n = 10
        Logger.log(f'Testing...')
        for i in range(0, n):
            Logger.log(f'{i}...', 'child')
            time.sleep(1)
    
    def exit(self):
        self.exec_()

    


if __name__ == '__main__':
    app = App()
    app.exit()
