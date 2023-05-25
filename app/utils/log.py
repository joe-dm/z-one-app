from PySide6 import QtCore


class LogWriter(QtCore.QRunnable):
    def __init__(self):
        super().__init__()
    

    @QtCore.Slot()
    def run(self):
        pass

class Logger:

    @staticmethod
    def send(message):
        pass