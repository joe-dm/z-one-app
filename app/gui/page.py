import PySide6.QtWidgets as QtWidgets



class PageDashboard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    
    def setup_ui(self):
        label_title = QtWidgets.QLabel('Dashboard')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label_title)
        
        self.setLayout(layout)

class PageSystemInfo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    
    def setup_ui(self):
        label_title = QtWidgets.QLabel('System Info')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label_title)
        
        self.setLayout(layout)
    




    
    
