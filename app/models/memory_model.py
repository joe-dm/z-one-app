import psutil

from PySide6 import QtCore

from utils.decorators import singleton
from utils.thread import Thread
from utils.log import Log
from utils.session import Session
from utils.file import JSON

class MemoryModelSignals(QtCore.QObject):
    updated_ram_usage = QtCore.Signal(float)


@singleton
class MemoryModel:
    def __init__(self):
        Log.task('Gathering memory info')

        self.signals = MemoryModelSignals()

        # gathered from platform-specific code with admin privileges
        self._ram_devices = None        

        self._ram_total = psutil.virtual_memory().total
        self._ram_usage = psutil.virtual_memory().percent        

        self._monitor = MemoryMonitor(self)
        self._gather_info_from_os()

    def _gather_info_from_os(self):
        # from dmi
        if Session.os_type == 'Linux' and Session.is_admin:
            self._ram_devices = []
            dmi_ram_info = JSON.find_dmi_entries('Memory Device')
            
            for device in dmi_ram_info:                
                self._ram_devices.append(device)


    def get_ram_usage(self):
        return self._ram_usage
    def get_ram_total(self):
        return self._ram_total
    def get_ram_devices(self):
        return self._ram_devices
    def get_ram_type(self):
        if self._ram_devices:
            for device in self._ram_devices:
                return device['Type']
        else: return self._ram_devices
    
    def update_usage(self):
        self._ram_usage = psutil.virtual_memory().percent        
        self.signals.updated_ram_usage.emit(self.get_ram_usage())


class MemoryMonitor(Thread):
    def __init__(self, model: MemoryModel):
        super().__init__()
        self.model = model 
    
    def execute(self):
        self.thread_signals.log_operation.emit('Started monitoring memory usage', None)      
        while self.is_running:            
            self.model.update_usage()                       
            QtCore.QThread.msleep(100)