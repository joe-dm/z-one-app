from PySide6 import QtCore, QtWidgets, QtGui

from resources.config import AppConfig, PathConfig
from resources.theme import ThemeSize, ThemeStylesheet

class Sidebar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # expanded/collapsed status
        self.is_expanded = True
        # header
        self.header = SidebarHeader()
        # buttons
        self.button_dashboard = SidebarButton('Dashboard', PathConfig.icon_dashboard, PathConfig.icon_dashboard_active)
        self.button_processor = SidebarButton('Processor', PathConfig.icon_processor, PathConfig.icon_processor_active)
        self.button_gpu = SidebarButton('GPU', PathConfig.icon_gpu, PathConfig.icon_gpu_active)
        self.button_memory = SidebarButton('Memory', PathConfig.icon_memory, PathConfig.icon_memory_active)
        self.button_disk = SidebarButton('Disk', PathConfig.icon_disk, PathConfig.icon_disk_active)
        self.button_network = SidebarButton('Network', PathConfig.icon_network, PathConfig.icon_network_active)
        self.button_apps = SidebarButton('Apps', PathConfig.icon_apps, PathConfig.icon_apps_active)
        self.button_settings = SidebarButton('Settings', PathConfig.icon_settings, PathConfig.icon_settings_active)
        self.button_logs = SidebarButton('Logs', PathConfig.icon_logs, PathConfig.icon_logs_active)
        # list of all buttons
        self.sidebar_buttons = [
            self.button_dashboard, self.button_processor,
            self.button_gpu, self.button_memory,
            self.button_disk, self.button_network,
            self.button_apps, self.button_settings,
            self.button_logs]

        self.setup_ui()

    def setup_ui(self):
        # sidebar properties
        self.setMaximumWidth(130)

        # setup layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(ThemeSize.widget_spacing)
        layout.addSpacing(5)
        layout.addWidget(self.header)
        layout.addSpacing(5)
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
        
        # set dashboard as active page
        self.set_active_button(self.button_dashboard)
        
    
    def set_active_button(self, button):        
        for btn in self.sidebar_buttons:
            if btn is button:
                btn.set_active()
            else:
                btn.set_inactive()

    def toggle(self):
        if self.is_expanded:            
            # hide text buttons
            for button in self.sidebar_buttons:
                button.button_text.setVisible(False)  
            # shrink header          
            self.header.shrink()
            self.is_expanded = False
        else:
            # show text buttons
            for button in self.sidebar_buttons:
                button.button_text.setVisible(True) 
            # expand header          
            self.header.expand()
            self.is_expanded = True


class SidebarButton(QtWidgets.QWidget):
    def __init__(self, text, icon, icon_active):
        super().__init__()        
        self.icon = icon
        self.icon_active = icon_active
        self.text = text       
        self.is_active = False

        self.button_icon = QtWidgets.QPushButton()
        self.button_text = QtWidgets.QPushButton()        

        self.setup_ui()


    def setup_ui(self):
        # icon button properties        
        self.button_icon.setIcon(QtGui.QIcon(self.icon))
        self.button_icon.setIconSize(QtCore.QSize(ThemeSize.sidebar_icon, ThemeSize.sidebar_icon))
        self.button_icon.setFixedWidth(ThemeSize.sidebar_button)
        self.button_icon.setFixedHeight(ThemeSize.sidebar_button)   
        self.button_icon.setCursor(QtCore.Qt.PointingHandCursor)
        self.button_icon.setStyleSheet(f'text-align: center;') 

        # button text properties
        self.button_text.setText(self.text)
        self.button_text.setFixedHeight(ThemeSize.sidebar_button)
        self.button_text.setCursor(QtCore.Qt.PointingHandCursor)

        # setup layout
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(ThemeSize.widget_spacing)
        layout.addWidget(self.button_icon)
        layout.addWidget(self.button_text)
        layout.setSpacing(0)

        # set style
        self.setStyleSheet(ThemeStylesheet.sidebar_button)

        # setup enter/leave events
        self.button_icon.enterEvent = self.on_enter_event
        self.button_icon.leaveEvent = self.on_leave_event
        self.button_text.enterEvent = self.on_enter_event
        self.button_text.leaveEvent = self.on_leave_event
    
    def set_active(self):
        self.setStyleSheet(ThemeStylesheet.sidebar_button_active)
        self.button_icon.setIcon(QtGui.QIcon(self.icon_active))
        self.is_active = True    
    def set_inactive(self):
        self.setStyleSheet(ThemeStylesheet.sidebar_button)
        self.button_icon.setIcon(QtGui.QIcon(self.icon))
        self.is_active = False

    def on_enter_event(self, event):
        if not self.is_active:            
            self.setStyleSheet(ThemeStylesheet.sidebar_button_hover)
    def on_leave_event(self, event):
        if not self.is_active:
            self.setStyleSheet(ThemeStylesheet.sidebar_button)

class SidebarHeader(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.logo_image = QtWidgets.QLabel()
        self.logo_text = QtWidgets.QLabel(AppConfig.name)
        self.button_toggle = QtWidgets.QPushButton('‹')
        self.spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.header_layout = QtWidgets.QHBoxLayout(self)

        self.setup_ui()
    
    def setup_ui(self):
        # header properties
        self.setMinimumHeight(ThemeSize.sidebar_button)        

        # setup logo image
        logo_pixmap = QtGui.QPixmap(PathConfig.logo)
        size = ThemeSize.sidebar_button - 2
        logo_pixmap = logo_pixmap.scaled(size, size, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.logo_image.setPixmap(logo_pixmap)     

        # setup logo text
        self.logo_text.setStyleSheet(ThemeStylesheet.sidebar_header_text)
        
        # setup toggle buttons
        self.button_toggle.setStyleSheet(ThemeStylesheet.sidebar_header_button)
        self.button_toggle.setFixedWidth(20)           

        # setup layout
        self.header_layout.setAlignment(QtCore.Qt.AlignLeft)
        self.header_layout.setContentsMargins(0,0,0,0)
        self.header_layout.addWidget(self.logo_image)
        self.header_layout.addWidget(self.logo_text)
        self.header_layout.addSpacerItem(self.spacer)
        self.header_layout.addWidget(self.button_toggle)

        # setup enter/leave events
        self.button_toggle.enterEvent = self.on_enter_event
        self.button_toggle.leaveEvent = self.on_leave_event
    
    def shrink(self):
        self.header_layout.removeWidget(self.logo_image)
        self.logo_image.setVisible(False)
        self.header_layout.removeWidget(self.logo_text)
        self.logo_text.setVisible(False)
        self.header_layout.removeItem(self.spacer)
        self.button_toggle.setFixedWidth(ThemeSize.sidebar_button)
    
    def expand(self):
        self.header_layout.removeWidget(self.button_toggle)

        self.header_layout.insertWidget(0, self.logo_image)
        self.logo_image.setVisible(True)
        self.header_layout.insertWidget(1, self.logo_text)
        self.logo_text.setVisible(True)
        self.header_layout.addItem(self.spacer)
        self.header_layout.addWidget(self.button_toggle)
        self.button_toggle.setFixedWidth(20)

    def on_enter_event(self, event):        
        self.button_toggle.setStyleSheet(ThemeStylesheet.sidebar_header_button_hover)
    def on_leave_event(self, event):
        self.button_toggle.setStyleSheet(ThemeStylesheet.sidebar_header_button)