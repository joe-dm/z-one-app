from PySide6 import QtCore, QtWidgets, QtGui

from config.config import PathConfig
from config.theme import Style
from utils.log import Log

class Sidebar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # expanded/collapsed status
        self.is_expanded = True
        # header
        self.header = SidebarHeader()
        # buttons
        self.button_dashboard = SidebarButton('Dashboard', PathConfig.icon_dashboard, PathConfig.icon_dashboard_active)
        self.button_cpu = SidebarButton('CPU', PathConfig.icon_processor, PathConfig.icon_processor_active)
        self.button_gpu = SidebarButton('GPU', PathConfig.icon_gpu, PathConfig.icon_gpu_active)
        self.button_memory = SidebarButton('Memory', PathConfig.icon_memory, PathConfig.icon_memory_active)
        self.button_disk = SidebarButton('Disk', PathConfig.icon_disk, PathConfig.icon_disk_active)
        self.button_network = SidebarButton('Network', PathConfig.icon_network, PathConfig.icon_network_active)
        self.button_apps = SidebarButton('Apps', PathConfig.icon_apps, PathConfig.icon_apps_active)
        self.button_settings = SidebarButton('Settings', PathConfig.icon_settings, PathConfig.icon_settings_active)
        self.button_logs = SidebarButton('Logs', PathConfig.icon_logs, PathConfig.icon_logs_active)
        # list of all buttons
        self.sidebar_buttons = [
            self.button_dashboard, self.button_cpu,
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
        layout.setSpacing(3)
        layout.addSpacing(5)
        layout.addWidget(self.header)
        layout.addSpacing(10)
        layout.addWidget(self.button_dashboard)
        layout.addWidget(self.button_cpu)
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

        Log.debug_init(self)
        
    
    def set_active_button(self, button):        
        for btn in self.sidebar_buttons:
            if btn is button:
                btn.set_active()
            else:
                btn.set_inactive()

    def toggle(self):
        if self.is_expanded:     
            Log.debug(f"Collapsing sidebar")   
            # hide text buttons
            for button in self.sidebar_buttons:
                button.button_text.setVisible(False)                
            # shrink header          
            self.header.shrink()
            self.is_expanded = False
        else:
            Log.debug(f"Expanding sidebar")   
            # show text buttons
            for button in self.sidebar_buttons:
                button.button_text.setVisible(True)             
            # expand header          
            self.header.expand()
            self.is_expanded = True


class SidebarButton(QtWidgets.QWidget):
    ICON_SIZE = 20
    BUTTON_SIZE = 32

    def __init__(self, text, icon, icon_active):
        super().__init__(objectName='SidebarButton')        
        self.icon = icon
        self.icon_active = icon_active
        self.text = text       
        self.is_active = False

        self.button_icon = QtWidgets.QPushButton(objectName='SidebarButton')
        self.button_text = QtWidgets.QPushButton(objectName='SidebarButton')        

        self.setup_ui()


    def setup_ui(self):
        # icon button properties                
        self.button_icon.setIcon(QtGui.QIcon(self.icon))
        self.button_icon.setIconSize(QtCore.QSize(SidebarButton.ICON_SIZE, SidebarButton.ICON_SIZE))
        self.button_icon.setFixedWidth(SidebarButton.BUTTON_SIZE)
        self.button_icon.setFixedHeight(SidebarButton.BUTTON_SIZE)   
        self.button_icon.setCursor(QtCore.Qt.PointingHandCursor)        
        self.button_icon.setStyleSheet(f'text-align: center;') 

        # button text properties        
        self.button_text.setText(self.text)
        self.button_text.setFixedHeight(SidebarButton.BUTTON_SIZE)
        self.button_text.setCursor(QtCore.Qt.PointingHandCursor)

        # setup layout
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.addWidget(self.button_icon)
        layout.addWidget(self.button_text)       

        # setup enter/leave events
        self.button_icon.enterEvent = self.on_enter_event
        self.button_icon.leaveEvent = self.on_leave_event
        self.button_text.enterEvent = self.on_enter_event
        self.button_text.leaveEvent = self.on_leave_event

        #self.setStyleSheet(Style.sidebar_button())
        Log.debug_init(self, obj_name=self.text)
    
    def set_active(self):        
        self.setStyleSheet(Style.sidebar_button(active=True))   
        self.button_icon.setIcon(QtGui.QIcon(self.icon_active))
        self.is_active = True    
    def set_inactive(self):
        self.setStyleSheet(Style.sidebar_button())      
        self.button_icon.setIcon(QtGui.QIcon(self.icon))
        self.is_active = False

    def on_enter_event(self, event):
        if not self.is_active: 
            self.setStyleSheet(Style.sidebar_button(hover=True))     
    def on_leave_event(self, event):
        if not self.is_active:
            self.setStyleSheet(Style.sidebar_button())

class SidebarHeader(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.logo_image = QtWidgets.QLabel()
        self.logo_text = QtWidgets.QLabel()
        self.button_toggle = QtWidgets.QPushButton('‹', objectName='SidebarToggleButton')
        self.spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.header_layout = QtWidgets.QHBoxLayout(self)

        self.setup_ui()
    
    def setup_ui(self):
        # header properties
        self.setMinimumHeight(SidebarButton.BUTTON_SIZE)        

        # setup logo image
        logo_pixmap = QtGui.QPixmap(PathConfig.logo)
        logo_size = SidebarButton.BUTTON_SIZE - 2
        logo_pixmap = logo_pixmap.scaled(logo_size, logo_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.logo_image.setPixmap(logo_pixmap)     

        # setup logo text image
        logo_text_pixmap = QtGui.QPixmap(PathConfig.logo_text)
        logo_text_size = SidebarButton.BUTTON_SIZE + 45
        logo_text_pixmap = logo_text_pixmap.scaled(logo_text_size, logo_text_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.logo_text.setPixmap(logo_text_pixmap)    
        
        # setup toggle buttons
        self.button_toggle.setFixedWidth(20)           

        # setup layout
        self.header_layout.setAlignment(QtCore.Qt.AlignLeft)
        self.header_layout.setContentsMargins(0,0,0,0)
        self.header_layout.setSpacing(0)
        self.header_layout.addWidget(self.logo_image)
        self.header_layout.addWidget(self.logo_text)
        self.header_layout.addSpacerItem(self.spacer)
        self.header_layout.addWidget(self.button_toggle)
        
        Log.debug_init(self)
    
    def shrink(self):
        self.button_toggle.setText('›')
        self.header_layout.removeWidget(self.logo_image)
        self.logo_image.setVisible(False)
        self.header_layout.removeWidget(self.logo_text)
        self.logo_text.setVisible(False)
        self.header_layout.removeItem(self.spacer)
        self.button_toggle.setFixedWidth(SidebarButton.BUTTON_SIZE)
    
    def expand(self):
        self.header_layout.removeWidget(self.button_toggle)

        self.button_toggle.setText('‹')
        self.header_layout.insertWidget(0, self.logo_image)
        self.logo_image.setVisible(True)
        self.header_layout.insertWidget(1, self.logo_text)
        self.logo_text.setVisible(True)
        self.header_layout.addItem(self.spacer)
        self.header_layout.addWidget(self.button_toggle)
        self.button_toggle.setFixedWidth(20)