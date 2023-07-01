import cpuinfo
import psutil

from PySide6 import QtCore

from utils.thread import Thread

class CPUModelSignals(QtCore.QObject):
    updated_usage = QtCore.Signal(int)

class CPUModel:
    def __init__(self):
        self.signals = CPUModelSignals()
        cpuinfo_dict = cpuinfo.get_cpu_info()

        self.name = cpuinfo_dict['brand_raw']
        self.architecture = cpuinfo_dict['bits']
        self.usage = psutil.cpu_percent()
        
        self.cores_physical = psutil.cpu_count(logical=False)
        self.cores_logical = psutil.cpu_count(logical=True)

        self.frequency_current = psutil.cpu_freq()[0]
        self.frequency_min = psutil.cpu_freq()[1]
        self.frequency_max = psutil.cpu_freq()[2]

        self.l1_data_cache_size = cpuinfo_dict['l1_data_cache_size']
        self.l1_instruction_cache_size = cpuinfo_dict['l1_instruction_cache_size']
        self.l2_cache_size = cpuinfo_dict['l2_cache_size']
        self.l2_cache_line_size = cpuinfo_dict['l2_cache_line_size']
        self.l2_cache_associativity = cpuinfo_dict['l2_cache_associativity']
        self.l3_cache_size = cpuinfo_dict['l3_cache_size']

        self._monitor = CPUMonitor(self)

    def get_usage(self):
        return self.usage

    def update_usage(self, usage):
        self.usage = usage
        self.signals.updated_usage.emit(self.get_usage())
    
    def update_frequency(self, frequency):
        self.frequency_current = frequency        


class CPUMonitor(Thread):
    def __init__(self, model: CPUModel):
        super().__init__()
        self.model = model
        self.thread_signals.log_task.emit('Monitoring CPU', None)        
        

    def execute(self):
        while self.is_running:
            self.model.update_usage(psutil.cpu_percent()) # i want to update this every 100ms
            self.model.update_frequency(psutil.cpu_freq()[0]) # i want to update this every 1000ms
            QtCore.QThread.msleep(100)