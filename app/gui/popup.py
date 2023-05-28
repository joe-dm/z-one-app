from PySide6 import QtWidgets, QtCore


class PopupExit(QtWidgets.QDialog):
    def __init__(self, parent_widget):
        super().__init__(parent_widget)
        self.parent_widget = parent_widget
        self.message = 'Exiting...'
        self.detail = 'Cleaning up and exiting.\nPlease wait.'             
        self.setup_ui()

    def setup_ui(self):       

        progress_bar = QtWidgets.QProgressBar()
        progress_bar.setRange(0, 0)
        
        label_message = QtWidgets.QLabel()
        label_message.setAlignment(QtCore.Qt.AlignCenter)
        label_message.setText(f'<b>{self.message}</b>')

        label_detail = QtWidgets.QLabel(self.detail)
        label_detail.setAlignment(QtCore.Qt.AlignCenter)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label_message)    
        layout.addWidget(label_detail)   
        layout.addWidget(progress_bar)    
        self.setLayout(layout)

        self.setModal(True)   
        self.setFixedSize(self.sizeHint())                
        self.show()        

    def closeEvent(self, event):
        event.ignore()
