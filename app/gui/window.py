import PySide6.QtWidgets as QtWidgets
from resources.config import AppConfig
from utils.logger import Logger

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        # initialize QMainWindow
        Logger.log('Initializing QMainWindow', 'debug')
        super(Window, self).__init__()        
        # setup the ui
        self.setup_ui()
                
    def setup_ui(self):
        Logger.log('Settig up QMainWindow UI', 'debug')
        # window title
        self.setWindowTitle(f'{AppConfig.name()}')

        # create a central widget
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        # create a vertical layout
        vbox = QtWidgets.QVBoxLayout(central_widget)

        # create buttons
        button1 = QtWidgets.QPushButton('Button 1', self)
        button1.setFixedWidth(150)
        button1.setMaximumHeight(50)

        button2 = QtWidgets.QPushButton('Button 2', self)
        button2.setFixedWidth(150)
        button2.setMaximumHeight(50)

        button3 = QtWidgets.QPushButton('Button 3', self)
        button3.setFixedWidth(150)
        button3.setMaximumHeight(50)

        # add buttons to the layout
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)

        # add stretch to push buttons to top of sidebar
        vbox.addStretch(1)

        # show the window
        self.show()


