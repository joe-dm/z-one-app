import subprocess
import time

from PySide6 import QtCore

class NetMon(QtCore.QRunnable):
    def __init__(self, *args, **kwargs):
        super(NetMon, self).__init__()
        self.args = args
        self.kwargs = kwargs

    @QtCore.Slot()
    def run(self, address='8.8.8.8'):
        while True:
            result = subprocess.run(["ping", "-c", "1", address], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Ping to {address} successful")
            else:
                print(f"Ping to {address} failed")
            time.sleep(1)

