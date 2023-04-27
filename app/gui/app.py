import sys

import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from gui.content import MainView
from resources.config import AppConfig, ThemeConfig


class AppGUI(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)         
        self.setup_ui()     

    def setup_ui(self):    
        # load and set stylesheet
        stylesheet = QtCore.QFile(ThemeConfig.path_to_stylesheet())
        stylesheet.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        stream = QtCore.QTextStream(stylesheet)
        self.setStyleSheet(stream.readAll())

        # setup main window
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle(f'{AppConfig.name()}')
        self.window.setMinimumWidth(600)
        self.window.setMinimumHeight(400)
        # window central widget
        main_view = MainView()      
        self.window.setCentralWidget(main_view)
        # show the window
        self.window.show()

    def exit(self):        
        self.exec()