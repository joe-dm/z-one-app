import cpuinfo
import psutil

from PySide6 import QtCore

from utils.thread import Thread
from utils.log import Log
from tools.system_info import CPUInfo

class CPUGatherer:
    def __init__(self):        
        Log.task('Gathering CPU info')

        self.cpuinfo_dict = cpuinfo.get_cpu_info()

        CPUInfo.name = self.cpuinfo_dict["brand_raw"]   
        CPUInfo.architecture = self.cpuinfo_dict["bits"]
        # cores
        CPUInfo.cores_physical = psutil.cpu_count(logical=False)
        CPUInfo.cores_logical = psutil.cpu_count(logical=True)
        # frequency
        CPUInfo.frequency_min = psutil.cpu_freq()[1]
        CPUInfo.frequency_max = psutil.cpu_freq()[2]
        # cache
        CPUInfo.l1_data_cache_size = self.cpuinfo_dict["l1_data_cache_size"]
        CPUInfo.l1_instruction_cache_size = self.cpuinfo_dict["l1_instruction_cache_size"]
        CPUInfo.l2_cache_size = self.cpuinfo_dict["l2_cache_size"]
        CPUInfo.l2_cache_line_size = self.cpuinfo_dict["l2_cache_line_size"]
        CPUInfo.l2_cache_associativity = self.cpuinfo_dict["l2_cache_associativity"]
        CPUInfo.l3_cache_size = self.cpuinfo_dict["l3_cache_size"]


class CPUMonitor(Thread):
    def __init__(self):
        super().__init__()
        self.signals.log_task.emit('Monitoring CPU', None)
    
    def execute(self):
        while self.is_running:
            CPUInfo.current_usage = psutil.cpu_percent()
            CPUInfo.current_frequency = psutil.cpu_freq()[0]
            QtCore.QThread.msleep(100)