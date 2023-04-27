import sys

import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from gui.content import MainView
from resources.config import AppConfig, ThemeConfig


class AppGUI(QtWidgets.QApplication):
    def __init__(self):
        super(AppGUI, self).__init__(sys.argv)         
        self.setup_ui()       

    def setup_ui(self):    
        self.window = Window()

        # load and set stylesheet
        stylesheet = QtCore.QFile(ThemeConfig.path_to_stylesheet())
        stylesheet.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        stream = QtCore.QTextStream(stylesheet)
        self.setStyleSheet(stream.readAll())
        
    def exit(self):        
        self.exec()


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  
        self.setup_ui()
                
    def setup_ui(self):
        self.setWindowTitle(f'{AppConfig.name()}')
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)

        # central widget
        central_widget = WindowCentralWidget() 
        self.setCentralWidget(central_widget)

        # show the window
        self.show()


class WindowCentralWidget(QtWidgets.QWidget):
    def __init__(self):
        super(WindowCentralWidget, self).__init__()   
        self.setup_ui()

    def setup_ui(self):
        hbox = QtWidgets.QHBoxLayout()        
        self.setLayout(hbox)
        
        main_view = MainView()        
        hbox.addWidget(main_view) 