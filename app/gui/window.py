from PySide6 import QtWidgets

class QApp(QtWidgets.QApplication):
    def __init__(self):
        super().__init__()
        self.main_window = MainWindow()

    def load_stylesheet(self):
        pass


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        self.show()


