import cpuinfo
import psutil

from PySide6 import QtCore

from config.config import PathConfig

from models.software_model import SoftwareModel

from utils.convert import Convert
from utils.decorators import singleton
from utils.file import JSON
from utils.log import Log
from utils.thread import Thread
from utils.session import Session


class CPUModelSignals(QtCore.QObject):
    updated_usage = QtCore.Signal(int)
    updated_frequency = QtCore.Signal(float)


@singleton
class CPUModel:
    def __init__(self):
        Log.task('Gathering CPU info')

        self.signals = CPUModelSignals()
        cpuinfo_dict = cpuinfo.get_cpu_info()

        # gathered from platform-specific code with admin privileges
        self._id = None
        self._manufacturer = None
        self._socket = None
        self._voltage = None
        self._signature = None

        self._name = cpuinfo_dict['brand_raw']
        self._architecture = cpuinfo_dict['bits']        
        self._usage = psutil.cpu_percent()
        
        self._cores_physical = psutil.cpu_count(logical=False)
        self._cores_logical = psutil.cpu_count(logical=True)

        self._frequency_current = psutil.cpu_freq()[0]
        self._frequency_min = psutil.cpu_freq()[1]
        self._frequency_max = psutil.cpu_freq()[2]

        self._l1_data_cache_size = cpuinfo_dict['l1_data_cache_size']
        self._l1_instruction_cache_size = cpuinfo_dict['l1_instruction_cache_size']
        self._l2_cache_size = cpuinfo_dict['l2_cache_size']
        self._l2_cache_line_size = cpuinfo_dict['l2_cache_line_size']
        self._l2_cache_associativity = cpuinfo_dict['l2_cache_associativity']
        self._l3_cache_size = cpuinfo_dict['l3_cache_size']             

        self._monitor = CPUMonitor(self)   
        self._gather_info_from_os()

    def _gather_info_from_os(self):
        # from dmi
        if Session.os_type == 'Linux' and Session.is_admin:
            # get cpu info from json file
            dmi_cpu_info = JSON.find_dmi_entries("Processor Information")
            dmi_cpu_info = dmi_cpu_info[0]
            # set values
            self._socket = dmi_cpu_info['Socket Designation']            
            self._frequency_max = float(dmi_cpu_info['Max Speed'].replace(' MHz', ''))
            self._manufacturer = dmi_cpu_info['Manufacturer']
            self._voltage = dmi_cpu_info['Voltage']
            self._id = dmi_cpu_info['ID']
            self._signature = dmi_cpu_info['Signature']


    # main info getters
    def get_name(self): 
        return self._name
    def get_id(self):
        return self._id
    def get_architecture(self): 
        return self._architecture
    def get_socket(self):
        return self._socket
    def get_signature(self):
        return self._signature
    def get_manufacturer(self):
        return self._manufacturer
    def get_voltage(self):
        return self._voltage
    def get_usage(self): 
        return self._usage
    # cores getters
    def get_cores_physical(self): 
        return self._cores_physical
    def get_cores_logical(self): 
        return self._cores_logical        
    # frequency getters
    def get_frequency_current(self): 
        return Convert.mhz_to_ghz(self._frequency_current)
    def get_frequency_min(self): 
        return Convert.mhz_to_ghz(self._frequency_min)
    def get_frequency_max(self): 
        return Convert.mhz_to_ghz(self._frequency_max)
    # l1 cache getters
    def get_l1_total_size(self): 
        return self._l1_data_cache_size + self._l1_instruction_cache_size 
    def get_l1_data_cache_size(self): 
        return self._l1_data_cache_size
    def get_l1_instruction_cache_size(self): 
        return self._l1_instruction_cache_size        
    # l2 cache getters
    def get_l2_total_size(self): 
        return self._l2_cache_size + self._l2_cache_line_size
    def get_l2_cache_size(self): 
        return self._l2_cache_size
    def get_l2_cache_line_size(self): 
        return self._l2_cache_line_size
    def get_l2_cache_associativity(self): 
        return self._l2_cache_associativity
    # l3 cache getters
    def get_l3_cache_size(self): 
        return self._l3_cache_size * self._cores_logical
    
    # updaters
    def update_usage(self):        
        self._usage = psutil.cpu_percent() 
        self.signals.updated_usage.emit(self.get_usage())    
    def update_frequency(self):
        self._frequency_current = psutil.cpu_freq()[0]  
        self.signals.updated_frequency.emit(self.get_frequency_current())    
        

class CPUMonitor(Thread):
    def __init__(self, model: CPUModel):
        super().__init__()
        self.model = model               

    def execute(self):   
        self.thread_signals.log_operation.emit('Started monitoring CPU usage', None)      
        while self.is_running:            
            self.model.update_usage()
            self.model.update_frequency()            
            QtCore.QThread.msleep(100)