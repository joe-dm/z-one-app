import PySide6.QtWidgets as QtWidgets
from resources.config import ThemeConfig

class Console(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()          

        # main widgets
        self.text_edit = QtWidgets.QTextEdit()

        self.setup_ui()

    def setup_ui(self):       
        # setup layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.text_edit)

        self.text_edit.setStyleSheet(f"background-color: {ThemeConfig.get_color('black-dark')};")