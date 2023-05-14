import PySide6.QtWidgets as QtWidgets

class Sidebar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()          
        self.setup_ui()

    def setup_ui(self):
        # set properties
        self.setFixedWidth(150)

        # create buttons
        self.button_dashboard = QtWidgets.QPushButton('Dashboard')
        self.button_cpu = QtWidgets.QPushButton('CPU')

        # create layout and add widgets
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.button_dashboard)
        layout.addWidget(self.button_cpu)
        layout.addStretch()