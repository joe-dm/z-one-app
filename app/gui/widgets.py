import PySide6.QtWidgets as QtWidgets
import PySide6.QtGui as QtGui

class ButtonSidebar(QtWidgets.QPushButton):
    def __init__(self, text):
        super().__init__()  
        self.text = text
        self.setup_ui()

    def setup_ui(self):
        self.setText(self.text)


class PageTitle(QtWidgets.QLabel):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.setup_ui()

    def setup_ui(self):
        self.setText(self.text)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.setFont(font)
        self.setStyleSheet('color: #cccccc;')


class SeparatorHLine(QtWidgets.QFrame):
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

class Table(QtWidgets.QTableWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setup_ui()

    def setup_ui(self):
        # set table size
        self.setRowCount(5)
        self.setColumnCount(2)
        
        # disable headers
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)

        # populate table
        for row, (label, value) in enumerate(self.data):
            self.setItem(row, 0, QtWidgets.QTableWidgetItem(label))
            self.setItem(row, 1, QtWidgets.QTableWidgetItem(value))

        # resize first column to fit contents
        self.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # stretch second column to fill remaining space
        self.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # disable editing
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)