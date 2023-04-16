import sys

import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from gui.window import Window
from utils.logger import Logger
from resources.config import ThemeConfig

class AppGUI(QtWidgets.QApplication):
    def __init__(self):
        # initialize QApplication
        Logger.log('Initializing QApplication', 'debug')
        super(AppGUI, self).__init__(sys.argv)                
        # setup the ui
        self.setup_ui()
        # create main window
        self._window = Window()

    def setup_ui(self):
        Logger.log('Settig up QApplication UI', 'debug')
        # load and set stylesheet
        stylesheet = QtCore.QFile(ThemeConfig.path_to_stylesheet())
        stylesheet.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        stream = QtCore.QTextStream(stylesheet)
        self.setStyleSheet(stream.readAll())
        
    def exit(self):         
        # exit the application
        self.exec()
        Logger.log('Closing QApplication', 'debug')
