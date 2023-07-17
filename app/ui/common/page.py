from PySide6 import QtWidgets, QtGui, QtCore

from config.theme import ThemeColor
from ui.common.element import HLine
from config.config import PathConfig


class Page(QtWidgets.QScrollArea):
    def __init__(self, title):
        super().__init__(objectName='Page')  
        self.title = title
        self.missing_info = False 

        # main widgets
        self.label_title = QtWidgets.QLabel(self.title, objectName='PageTitleLabel')   
        self.separator = HLine(color=ThemeColor.primary)  
        self.warning_missing_info = PageWarningMissingInfo()   

        # remove missing info banner   
        self.warning_missing_info.setVisible(False)
        
        # container properties
        self.page_container = QtWidgets.QWidget() 
        self.page_container.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
               
        # setup layout
        self.page_layout = QtWidgets.QVBoxLayout(self.page_container)              
        self.page_layout.addWidget(self.label_title) 
        self.page_layout.addWidget(self.separator)    
        self.page_layout.addWidget(self.warning_missing_info)     
        
        # page properties       
        self.setWidget(self.page_container)    
        self.setWidgetResizable(True) 
    
    def check_missing_info(self):       
        self.warning_missing_info.setVisible(self.missing_info)        

    def insert_widget(self, widget):
        self.page_layout.addWidget(widget)
    
    def remove_widget(self, widget):
        self.page_layout.removeWidget(widget)
        widget.setParent(None)


class PageWarningMissingInfo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)

        icon = QtWidgets.QLabel()
        icon.setPixmap(QtGui.QPixmap(PathConfig.icon_warning).scaled(15, 15, 
            QtCore.Qt.KeepAspectRatio, 
            QtCore.Qt.SmoothTransformation))
        icon.setMaximumWidth(20)        

        text = QtWidgets.QLabel(
            'Some features on this page are unavailable! ' 
            'Run as admin to see more content.',
            objectName='WarningText')
        text.setWordWrap(True)
        
        layout.addWidget(icon)
        layout.addWidget(text)
        