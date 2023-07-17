from PySide6 import QtWidgets, QtCore

from utils.log import Log


class OverlayDialog(QtWidgets.QWidget):
    def __init__(self, heading, message, parent_widget, loading_bar=True):
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
        # add heading and message to layout
        self.container_layout.addWidget(self.heading)
        self.container_layout.addSpacing(5)
        self.container_layout.addWidget(self.message)
        # add loading bar (if applicable)
        if loading_bar:
            self.loading_bar = QtWidgets.QProgressBar(objectName='DialogProgressBar')
            self.loading_bar.setRange(0, 0)
            self.container_layout.addSpacing(5)
            self.container_layout.addWidget(self.loading_bar)

        Log.debug_init(self)   
        

    def showEvent(self, event):
        self.setGeometry(self.parent().rect())    


