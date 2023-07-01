from PySide6 import QtWidgets

from config.theme import Style, ThemeColor


class HLine(QtWidgets.QFrame):
    def __init__(self, color=ThemeColor.gray, width=1):
        super().__init__(objectName='LineHorizontal')
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setStyleSheet(Style.line_horizontal(color, width))

class LabelHeading(QtWidgets.QLabel):
    def __init__(self, text=""):
        super().__init__(objectName='LabelHeading')
        self.setText(text)  
        self.setWordWrap(True)      

class LabelWidgetTitle(QtWidgets.QWidget):
    def __init__(self, title_text):
        super().__init__()
        self.title_label = QtWidgets.QLabel(title_text, objectName='LabelWidgetTitle')

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)        
        layout.addWidget(self.title_label)
        layout.addWidget(HLine(color=ThemeColor.secondary))
        