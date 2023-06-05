from PySide6 import QtCore, QtWidgets, QtGui

from resources.config import PathConfig
from resources.theme import ThemeSize, ThemeStylesheet

class Sidebar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button_dashboard = SidebarButton('Dashboard', PathConfig.icon_dashboard)
        self.button_processor = SidebarButton('Processor', PathConfig.icon_processor)
        self.button_gpu = SidebarButton('GPU', PathConfig.icon_gpu)
        self.button_memory = SidebarButton('Memory', PathConfig.icon_memory)
        self.button_disk = SidebarButton('Disk', PathConfig.icon_disk)
        self.button_network = SidebarButton('Network', PathConfig.icon_network)
        self.button_apps = SidebarButton('Apps', PathConfig.icon_apps)
        self.button_settings = SidebarButton('Settings', PathConfig.icon_settings)
        self.button_logs = SidebarButton('Logs', PathConfig.icon_logs)

        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(ThemeSize.widget_spacing)
        layout.addWidget(self.button_dashboard)
        layout.addWidget(self.button_processor)
        layout.addWidget(self.button_gpu)
        layout.addWidget(self.button_memory)
        layout.addWidget(self.button_disk)
        layout.addWidget(self.button_network)
        layout.addWidget(self.button_apps)
        layout.addStretch(1)
        layout.addWidget(self.button_settings)
        layout.addWidget(self.button_logs)
        
        layout.addStretch()
        

class SidebarButton(QtWidgets.QWidget):
    def __init__(self, text, icon_path):
        super().__init__()        
        self.icon_path = icon_path
        self.text = text       

        self.button_icon = QtWidgets.QPushButton()
        self.button_text = QtWidgets.QPushButton()        

        self.setup_ui()


    def setup_ui(self):
        # icon button properties        
        self.button_icon.setIcon(QtGui.QIcon(self.icon_path))
        self.button_icon.setIconSize(QtCore.QSize(ThemeSize.sidebar_icon, ThemeSize.sidebar_icon))
        self.button_icon.setFixedWidth(ThemeSize.sidebar_button)
        self.button_icon.setFixedHeight(ThemeSize.sidebar_button)

        # button text properties
        self.button_text.setText(self.text)
        self.button_text.setFixedHeight(ThemeSize.sidebar_button)
        self.button_text.setStyleSheet(ThemeStylesheet.sidebar_button)

        # setup layout
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(ThemeSize.widget_spacing)
        layout.addWidget(self.button_icon)
        layout.addWidget(self.button_text)