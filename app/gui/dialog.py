from PySide6 import QtWidgets, QtCore
from resources.theme import ThemeStylesheet

class EmbeddedDialog(QtWidgets.QWidget):
    def __init__(self, parent_widget):
        super().__init__(parent_widget)       

        self.parent_widget = parent_widget
        self.loop = QtCore.QEventLoop(self)
        self.container = QtWidgets.QWidget()
        self.full_layout = QtWidgets.QVBoxLayout(self)
        self.container_layout = QtWidgets.QVBoxLayout(self.container)

        # widget options        
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setAutoFillBackground(True)        
        self.setStyleSheet(ThemeStylesheet.dialog_overlay)

        # add container to full layout
        self.full_layout.addWidget(self.container, alignment=QtCore.Qt.AlignCenter)
        self.full_layout.setAlignment(QtCore.Qt.AlignCenter)


        # container options
        self.container.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.container.setStyleSheet(ThemeStylesheet.dialog_container)

        # container layout options
        self.container_layout.setAlignment(QtCore.Qt.AlignCenter)        
        self.container_layout.setContentsMargins(20, 20, 20, 20)
        self.container_layout.setSpacing(10)

    def showEvent(self, event):
        self.setGeometry(self.parent().rect())
    
    def exec(self):
        self.show()
        self.raise_()
        res = self.loop.exec()
        #self.hide()
        return res

    
class ExitDialog(EmbeddedDialog):
    def __init__(self, parent_widget):
        super().__init__(parent_widget)

        self.heading = QtWidgets.QLabel('Exiting')
        self.message = QtWidgets.QLabel('Cleaning up and exiting.\nPlease wait.')
        self.progress_bar = QtWidgets.QProgressBar()

        self.setup_ui()

    def setup_ui(self):
        self.progress_bar.setRange(0, 0) 
        self.progress_bar.setStyleSheet('border: none;')

        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setAlignment(QtCore.Qt.AlignCenter)

        self.container_layout.addWidget(self.heading)
        self.container_layout.addWidget(self.message)
        self.container_layout.addWidget(self.progress_bar)