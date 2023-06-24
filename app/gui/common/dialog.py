from PySide6 import QtWidgets, QtCore

from gui.common.elements import HLine
from utils.log import Log

class EmbeddedDialog(QtWidgets.QWidget):
    def __init__(self, parent_widget, heading, message):
        super().__init__(parent_widget, objectName='DialogOverlay')       

        self.parent_widget = parent_widget        
        
        # widget options        
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)        

        # add container to full layout
        self.container = QtWidgets.QWidget(objectName='DialogContainer')
        self.full_layout = QtWidgets.QVBoxLayout(self)   
        self.full_layout.addWidget(self.container, alignment=QtCore.Qt.AlignCenter)     

        # main widgets
        self.heading = QtWidgets.QLabel(heading, objectName='DialogHeadingLabel')
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.message = QtWidgets.QLabel(message)
        self.message.setAlignment(QtCore.Qt.AlignCenter)

        # container layout
        self.container_layout = QtWidgets.QVBoxLayout(self.container)
        self.container_layout.setContentsMargins(10,10,10,10)
        self.container_layout.setSpacing(20)
        self.container_layout.addWidget(self.heading)
        self.container_layout.addSpacing(5)
        self.container_layout.addWidget(self.message)

        Log.debug_init(self)   
        

    def showEvent(self, event):
        self.setGeometry(self.parent().rect())    

    
class ExitDialog(EmbeddedDialog):
    def __init__(self, parent_widget):
        super().__init__(parent_widget, 'Exiting', 'Cleaning up and exiting\nPlease wait.')

        # progress bar
        self.progress_bar = QtWidgets.QProgressBar(objectName='DialogProgressBar')
        self.progress_bar.setRange(0, 0)              
        
        # add widgets to dialog                
        self.container_layout.addWidget(self.progress_bar)
        