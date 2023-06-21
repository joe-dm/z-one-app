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
        self.setWordWrap(True)      

class WidgetTitle(QtWidgets.QWidget):
    def __init__(self, title_text):
        super().__init__()
        self.title_label = QtWidgets.QLabel(title_text)
        self.title_label.setStyleSheet(ThemeStylesheet.label_widget_title)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)        
        layout.addWidget(self.title_label)
        layout.addWidget(HLine())
        