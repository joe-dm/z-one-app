import platform
import psutil
import cpuinfo

from utils.log import Log 

class InfoGatherer:
    def gather_all():
        Log.task("Gathering all system information")
        CPUInfo.gather_static_values()

class CPUInfo:
    NAME = None
    ARCHITECTURE = None
    CORES = None
    THREADS = None
    FREQUENCY_MIN = None
    FREQUENCY_MAX = None

    def gather_static_values():   
        Log.task("Gathering CPU information")     
        cpuinfo_obj = cpuinfo.get_cpu_info()

        CPUInfo.NAME = cpuinfo_obj["brand_raw"]
        CPUInfo.ARCHITECTURE = platform.processor()
        CPUInfo.CORES = psutil.cpu_count(logical=False)
        CPUInfo.THREADS = psutil.cpu_count(logical=True)
        CPUInfo.FREQUENCY_MIN = psutil.cpu_freq()[1]
        CPUInfo.FREQUENCY_MAX = psutil.cpu_freq()[2]  

        Log.debug_init(CPUInfo, True, obj_name='CPUInfo')
   
   # static values getters
    def get_name():          
        return CPUInfo.NAME    
    def get_architecture():  
        return CPUInfo.ARCHITECTURE    
    def get_cores():
        return CPUInfo.CORES    
    def get_threads():
        return CPUInfo.THREADS
    def get_frequency_min():
        return CPUInfo.FREQUENCY_MIN
    def get_frequency_max():
        return CPUInfo.FREQUENCY_MAX     

    # changing values getters
    def get_current_usage():
        return psutil.cpu_percent()
    def get_current_frequency():
        return psutil.cpu_freq()[0] 







class OperatingSystem:
    def __init__(self):                
        #Log.task(f"Gathering OS info")

        self.type = platform.system()
        self.release = platform.release()
        self.version = platform.version()
        self.description = platform.platform()
        self.host_name = platform.node()
        self.boot_time = psutil.boot_time()

        #Log.debug_init(self, show_attributes=True)




class Python:
    def __init__(self):
        #Log.task(f"Gathering Python info")

        self.version = platform.python_version()
        self.implementation = platform.python_implementation()
        self.compiler = platform.python_compiler()        
        self.build = platform.python_build()        

        #Log.debug_init(self, show_attributes=True)

