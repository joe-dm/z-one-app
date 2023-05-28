from PySide6 import QtWidgets, QtCore

class Popup(QtWidgets.QDialog):
    def __init__(self, parent, message, title=''):
        super().__init__() 


class PopupExit(QtWidgets.QDialog):
    def __init__(self, parent, message, title=''):
        super().__init__(parent)
        self.message = message
        self.title = title        
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(self.title)
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel(self.message)
        layout.addWidget(label)
        self.setLayout(layout)
        self.setModal(True)       
        self.show()

    def closeEvent(self, event):
        event.ignore()
