import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets

from gui.widgets import ButtonWithIcon
from resources.config import ThemeConfig

class Sidebar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()   
        # create buttons
        self.button_dashboard = ButtonWithIcon('Dashboard', ThemeConfig.icon_default())
        self.button_cpu = ButtonWithIcon('CPU', ThemeConfig.icon_default())     
        self.setup_ui()

    def setup_ui(self):
        # set sidebar properties
        self.setFixedWidth(150) 

        
        # create layout and add widgets
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.button_dashboard)
        layout.addWidget(self.button_cpu)
        layout.addStretch()