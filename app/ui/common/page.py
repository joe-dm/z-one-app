from PySide6 import QtWidgets

from config.theme import ThemeColor
from ui.common.element import HLine
from utils.log import Log


class Page(QtWidgets.QScrollArea):
    def __init__(self, title):
        super().__init__(objectName='Page')  
        self.title = title

        # main widgets
        self.label_title = QtWidgets.QLabel(self.title, objectName='PageTitleLabel')   
        self.separator = HLine(color=ThemeColor.primary)        
        
        # container properties
        self.page_container = QtWidgets.QWidget() 
        self.page_container.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
               
        # setup layout
        self.page_layout = QtWidgets.QVBoxLayout(self.page_container)              
        self.page_layout.addWidget(self.label_title) 
        self.page_layout.addWidget(self.separator)         
        
        # page properties       
        self.setWidget(self.page_container)    
        self.setWidgetResizable(True)  

        Log.debug_init(self)     

    def insert_widget(self, widget):
        #self.page_layout.addSpacing(10)
        #self.page_layout.insertSpacerItem
        self.page_layout.addWidget(widget)
    
    def remove_widget(self, widget):
        self.page_layout.removeWidget(widget)
        widget.setParent(None)