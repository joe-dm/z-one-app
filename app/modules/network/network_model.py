from PySide6 import QtCore

class NetworkModelSignals(QtCore.QObject):
    pass

class NetworkModel:
    def __init__(self):
        self.signals = NetworkModelSignals()

        self.internet_available = None
        self.bytes_sent = None
        self.bytes_received = None
        self.speed_download = None
        self.speed_upload = None