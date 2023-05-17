import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets

from resources.config import ThemeConfig

class Sidebar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()   
        # create logo widget
        self.logo = SidebarLogo()
        # create button widgets
        self.button_dashboard = SidebarButton('Dashboard', ThemeConfig.Icon.dashboard)
        self.button_cpu = SidebarButton('CPU', ThemeConfig.Icon.cpu)
        self.button_gpu = SidebarButton('GPU', ThemeConfig.Icon.gpu)
        self.button_ram = SidebarButton('RAM', ThemeConfig.Icon.ram)
        self.button_disk = SidebarButton('Disk', ThemeConfig.Icon.disk)
        self.button_network = SidebarButton('Network', ThemeConfig.Icon.network)
        self.button_apps = SidebarButton('Apps', ThemeConfig.Icon.apps)
        self.button_settings = SidebarButton('Settings', ThemeConfig.Icon.settings)
        self.button_logs = SidebarButton('Logs', ThemeConfig.Icon.logs)
        
        self.setup_ui()

    def setup_ui(self):        
        # create layout and add widgets
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.logo)
        layout.addWidget(self.button_dashboard)
        layout.addWidget(self.button_cpu)
        layout.addWidget(self.button_gpu)
        layout.addWidget(self.button_ram)
        layout.addWidget(self.button_disk)
        layout.addWidget(self.button_network)
        layout.addWidget(self.button_apps)
        layout.addStretch()
        layout.addWidget(self.button_settings)
        layout.addWidget(self.button_logs)

class SidebarButton(QtWidgets.QWidget):
    def __init__(self, text, icon_path):
        super().__init__()

        self.text = text
        self.icon_path = icon_path

        self.button_icon = QtWidgets.QPushButton()
        self.button_text = QtWidgets.QPushButton()

        self.setup_ui()

    def setup_ui(self):        
        # button icon properties
        self.button_icon.setFixedWidth(30)
        self.button_icon.setIcon(QtGui.QIcon(self.icon_path))

        # button text properties
        self.button_text.setText(self.text)
        self.button_text.setStyleSheet("text-align: left;")
        self.button_text.setMinimumWidth(100)         

        # setup layout and add widgets to it
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(1)
        layout.addWidget(self.button_icon)
        layout.addWidget(self.button_text)

        # setup enter/leave events
        self.button_icon.enterEvent = self.on_enter_event
        self.button_icon.leaveEvent = self.on_leave_event
        self.button_text.enterEvent = self.on_enter_event
        self.button_text.leaveEvent = self.on_leave_event
        
    
    def on_enter_event(self, event):
        self.setStyleSheet(f"border: 1px solid {ThemeConfig.Color.primary};")
    def on_leave_event(self, event):
        self.setStyleSheet("")

class SidebarLogo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()  

        self.logo = QtWidgets.QLabel()
        self.logo_text = QtWidgets.QLabel('𝕫-𝕠𝕟𝕖') 

        self.setup_ui()
        
    def setup_ui(self):
        # setup logo widget        
        logo_pixmap = QtGui.QPixmap(ThemeConfig.Icon.logo)
        logo_pixmap = logo_pixmap.scaled(30, 30, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.logo.setPixmap(logo_pixmap)

        # setup application name label       
        logo_font = QtGui.QFont(ThemeConfig.Font.monospace, ThemeConfig.Font.size_logo)     
        logo_font.setWeight(QtGui.QFont.Bold)                     
        self.logo_text.setFont(logo_font)           

        # setup layout and add widgets
        layout = QtWidgets.QHBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignLeft)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(1)
        layout.addWidget(self.logo)
        layout.addWidget(self.logo_text)

class SidebarToggle(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()  
        self.setup_ui()
        
    def setup_ui(self):
        

        # setup layout and add widgets
        layout = QtWidgets.QHBoxLayout(self)

        
