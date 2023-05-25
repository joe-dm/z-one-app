import sys
from PySide6 import QtWidgets

class QApp(QtWidgets.QApplication):
    def __init__(self):
        super().__init__()

        self.main_window = MainWindow()

        self._setup_ui()

    def _setup_ui(self):
        pass

    def quit(self):
        sys.exit(self.exec())
        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        self.show()


