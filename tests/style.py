import sys
from PySide6 import QtWidgets, QtCore


class Card(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(75, 75)
        self.setStyleSheet('background-color: blue;')
        self.setAttribute(QtCore.Qt.WA_StyledBackground)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel('Hi'))
        layout.addWidget(QtWidgets.QPushButton('Click Me'))

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(300, 300)
        self.setStyleSheet('background-color: red;')

        card = Card()
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(card)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
