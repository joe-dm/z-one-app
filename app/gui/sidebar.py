import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets

from gui.widgets import Separator
from resources.config import ThemeConfig

class Sidebar(QtWidgets.QWidget):
    is_expanded = True

    def __init__(self):
        super().__init__()   
        # create header widget
        self.header = SidebarHeader()
        # separator
        self.separator = Separator()
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
        self.button_list = [            
            self.button_dashboard, self.button_cpu, self.button_gpu,
            self.button_ram, self.button_disk, self.button_network,
            self.button_apps, self.button_settings, self.button_logs]
        
        self.setup_ui()

    def setup_ui(self):        
        self.setMaximumWidth(150)
        # create layout and add widgets
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.header)
        layout.addWidget(self.separator)
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

    def toggle(self):
        if Sidebar.is_expanded:            
            # hide text buttons
            for button in self.button_list:                      
                button.button_text.setVisible(False)
            # hide header
            self.header.set_closed()  

            Sidebar.is_expanded = False
        
        else:
            # show text buttons
            for button in self.button_list:
                button.button_text.setVisible(True)         
            # show header 
            self.header.set_opened()

            Sidebar.is_expanded = True


class SidebarButton(QtWidgets.QWidget):
    def __init__(self, text, icon):
        super().__init__()

        self.text = text
        self.icon = icon

        self.button_icon = QtWidgets.QPushButton()
        self.button_text = QtWidgets.QPushButton()

        self.setup_ui()

    def setup_ui(self):        
        # button icon properties
        self.button_icon.setFixedWidth(30)
        self.button_icon.setIcon(QtGui.QIcon(self.icon))

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


class SidebarHeader(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()  

        self.logo = QtWidgets.QLabel()
        self.logo_text = QtWidgets.QLabel('z-one') # 𝕫-𝕠𝕟𝕖

        self.spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.button_toggle = QtWidgets.QPushButton()
        self.icon_close = QtGui.QIcon(ThemeConfig.Icon.arrow_left)
        self.icon_open = QtGui.QIcon(ThemeConfig.Icon.arrow_right)

        self.header_layout = QtWidgets.QHBoxLayout(self)

        self.setup_ui()
        
    def setup_ui(self):
        # setup logo image        
        logo_pixmap = QtGui.QPixmap(ThemeConfig.Icon.logo)
        logo_pixmap = logo_pixmap.scaled(30, 30, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.logo.setPixmap(logo_pixmap)

        # setup logo text     
        logo_font = QtGui.QFont(ThemeConfig.Font.monospace, ThemeConfig.Font.size_logo)     
        logo_font.setWeight(QtGui.QFont.Bold)                     
        self.logo_text.setFont(logo_font)   

        # setup toggle button   
        self.button_toggle.setIcon(self.icon_close)

        # setup layout and add widgets        
        self.header_layout.setAlignment(QtCore.Qt.AlignLeft)
        self.header_layout.setContentsMargins(0,0,0,0)
        self.header_layout.setSpacing(1)
        self.header_layout.addWidget(self.logo)
        self.header_layout.addWidget(self.logo_text)        
        self.header_layout.addSpacerItem(self.spacer)
        self.header_layout.addWidget(self.button_toggle)

        # setup on enter event
        self.button_toggle.enterEvent = self.on_enter_event
        self.button_toggle.leaveEvent = self.on_leave_event

    def set_closed(self):
        self.header_layout.removeWidget(self.logo)
        self.header_layout.removeWidget(self.logo_text)
        self.header_layout.removeItem(self.spacer)
        self.button_toggle.setIcon(self.icon_open)
    def set_opened(self):
        # remove toggle button
        self.header_layout.removeWidget(self.button_toggle)
        # add all widgets again
        self.header_layout.addWidget(self.logo)
        self.header_layout.addWidget(self.logo_text)
        self.header_layout.addItem(self.spacer)
        self.header_layout.addWidget(self.button_toggle)
        self.button_toggle.setIcon(self.icon_close)

    def on_enter_event(self, event):
        self.button_toggle.setStyleSheet(f"border: 1px solid {ThemeConfig.Color.primary};")
    def on_leave_event(self, event):
        self.button_toggle.setStyleSheet("")