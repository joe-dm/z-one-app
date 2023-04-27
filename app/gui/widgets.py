import PySide6.QtWidgets as QtWidgets

class ButtonSidebar(QtWidgets.QPushButton):
    def __init__(self, text):
        super().__init__()  
        self.text = text
        self.setup_ui()

    def setup_ui(self):
        self.setText(self.text)


class HLineSeparator(QtWidgets.QFrame):
    def __init__(self, visible=True):
        super().__init__()  
        self.visible = visible
        self.setup_ui()

    def setup_ui(self):
        if self.visible == False: 
            self.setFixedHeight(0)        

        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)               

        self.setEnabled(False)