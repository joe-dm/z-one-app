from PySide6 import QtWidgets, QtCore
from utils.theme import ThemeStylesheet
from utils.log import Log

class EmbeddedDialog(QtWidgets.QWidget):
    def __init__(self, parent_widget):
        super().__init__(parent_widget)       

        self.parent_widget = parent_widget        
        
        self.full_layout = QtWidgets.QVBoxLayout(self)
        self.container = QtWidgets.QWidget(objectName='DialogContainer')        
        self.container_layout = QtWidgets.QVBoxLayout(self.container)
        
        # widget options        
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)                     
        self.setStyleSheet(ThemeStylesheet.dialog)        

        # container layout
        self.container_layout.setContentsMargins(10,10,10,10)
        self.container_layout.setSpacing(20)

        # add container to full layout
        self.full_layout.addWidget(self.container, alignment=QtCore.Qt.AlignCenter)     

        Log.debug_init(self)   
        

    def showEvent(self, event):
        self.setGeometry(self.parent().rect())    

    
class ExitDialog(EmbeddedDialog):
    def __init__(self, parent_widget):
        super().__init__(parent_widget)

        self.heading = QtWidgets.QLabel('Exiting')
        self.message = QtWidgets.QLabel('Cleaning up threads and exiting\nPlease wait.')
        self.progress_bar = QtWidgets.QProgressBar()

        self.setup_ui()

    def setup_ui(self):
        # heading
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setStyleSheet(ThemeStylesheet.dialog_heading)

        # message
        self.message.setAlignment(QtCore.Qt.AlignCenter)

        # progress bar
        self.progress_bar.setRange(0, 0)              
        self.progress_bar.setStyleSheet(ThemeStylesheet.progress_bar)         

        # add widgets to dialog        
        self.container_layout.addWidget(self.heading)
        self.container_layout.addWidget(self.message)
        self.container_layout.addWidget(self.progress_bar)
        