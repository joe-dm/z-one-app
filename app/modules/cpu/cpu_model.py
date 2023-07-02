import cpuinfo
import psutil

from PySide6 import QtCore

from utils.thread import Thread
from utils.helpers.convert import Convert


class CPUModelSignals(QtCore.QObject):
    updated_usage = QtCore.Signal(int)
    updated_frequency = QtCore.Signal(float)

class CPUModel:
    def __init__(self):
        self.signals = CPUModelSignals()
        cpuinfo_dict = cpuinfo.get_cpu_info()

        self.name = cpuinfo_dict['brand_raw']
        self.architecture = cpuinfo_dict['bits']
        self.usage = psutil.cpu_percent()
        
        self.cores_physical = psutil.cpu_count(logical=False)
        self.cores_logical = psutil.cpu_count(logical=True)

        self.frequency_currents = psutil.cpu_freq()[0]
        self.frequency_min = psutil.cpu_freq()[1]
        self.frequency_max = psutil.cpu_freq()[2]

        self.l1_data_cache_size = cpuinfo_dict['l1_data_cache_size']
        self.l1_instruction_cache_size = cpuinfo_dict['l1_instruction_cache_size']
        self.l2_cache_size = cpuinfo_dict['l2_cache_size']
        self.l2_cache_line_size = cpuinfo_dict['l2_cache_line_size']
        self.l2_cache_associativity = cpuinfo_dict['l2_cache_associativity']
        self.l3_cache_size = cpuinfo_dict['l3_cache_size']             

        self._monitor = CPUMonitor(self)   


    # main info getters
    def get_name(self): return self.name
    def get_architecture(self): return self.architecture
    def get_usage(self): return self.usage
    # cores getters
    def get_cores_physical(self): return self.cores_physical
    def get_cores_logical(self): return self.cores_logical        
    # frequency getters
    def get_frequency_current(self): return Convert.mhz_to_ghz(self.frequency_current)
    def get_frequency_min(self): return Convert.mhz_to_ghz(self.frequency_min)
    def get_frequency_max(self): return Convert.mhz_to_ghz(self.frequency_max)
    # l1 cache getters
    def get_l1_total_size(self): return self.get_l1_data_cache_size() + self.get_l1_instruction_cache_size()
    def get_l1_data_cache_size(self): return self.l1_data_cache_size
    def get_l1_instruction_cache_size(self): return self.l1_instruction_cache_size        
    # l2 cache getters
    def get_l2_total_size(self): return self.get_l2_cache_size() + self.get_l2_cache_line_size()
    def get_l2_cache_size(self): return self.l2_cache_size
    def get_l2_cache_line_size(self): return self.l2_cache_line_size
    def get_l2_cache_associativity(self): return self.l2_cache_associativity
    # l3 cache getters
    def get_l3_cache_size(self): return self.l3_cache_size * self.cores_logical
    
    # updaters
    def update_usage(self):
        self.usage = psutil.cpu_percent()        
        self.signals.updated_usage.emit(self.get_usage())    
    def update_frequency(self):
        self.frequency_current = psutil.cpu_freq()[0]  
        self.signals.updated_frequency.emit(self.get_frequency_current())    
        


class CPUMonitor(Thread):
    def __init__(self, model: CPUModel):
        super().__init__()
        self.model = model               

    def execute(self):   
        self.thread_signals.log_task.emit('Monitoring CPU', None)      
        while self.is_running:            
            self.model.update_usage()
            self.model.update_frequency()            
            QtCore.QThread.msleep(100)