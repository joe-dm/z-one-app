from PySide6 import QtWidgets

from config.theme import ThemeStylesheet

class HLine(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setStyleSheet(ThemeStylesheet.line_horizontal_1)

class Heading(QtWidgets.QLabel):
    def __init__(self, text=""):
        super().__init__()
        self.setText(text)     
        self.setStyleSheet(ThemeStylesheet.label_heading)