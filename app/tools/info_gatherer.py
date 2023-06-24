import platform
import psutil
import cpuinfo
import inspect

from utils.log import Log, LogFile
from utils.helpers import Convert

class InfoGatherer:        
    
    def gather_all():
        cls_list = [OSInfo, PythonInfo, CPUInfo]
        for cls in cls_list:
            cls.gather_static_values()    

    def get_list(cls, format_output=True):
        method_names = [
            method_name
            for method_name, _ in cls.__dict__.items()
            if callable(getattr(cls, method_name)) and method_name.startswith("get_")
        ]

        result = []
        for method_name in method_names:
            getter_method = getattr(cls, method_name)
            try:
                value = getter_method(format_output)
            except TypeError:
                value = getter_method()

            attribute_name = method_name[4:].replace("_", " ").title()
            result.append((attribute_name, value))

        return result


class CPUInfo:
    name = None    
    architecture = None    

    cores_physical = None
    cores_logical = None

    frequency_min = None
    frequency_max = None

    l1_data_cache_size = None
    l1_instruction_cache_size = None
    l2_cache_size = None
    l2_cache_line_size = None
    l2_cache_associativity = None
    l3_cache_size = None

    def gather_static_values():   
        Log.task("Gathering CPU information")     
        cpuinfo_obj = cpuinfo.get_cpu_info()
        cpuinfo.get_cpu_info_json()

        CPUInfo.name = cpuinfo_obj["brand_raw"]        

        CPUInfo.architecture = cpuinfo_obj["bits"]        

        CPUInfo.cores_physical = psutil.cpu_count(logical=False)
        CPUInfo.cores_logical = psutil.cpu_count(logical=True)

        CPUInfo.frequency_min = psutil.cpu_freq()[1]
        CPUInfo.frequency_max = psutil.cpu_freq()[2]  

        CPUInfo.l1_data_cache_size = cpuinfo_obj["l1_data_cache_size"]
        CPUInfo.l1_instruction_cache_size = cpuinfo_obj["l1_instruction_cache_size"]
        CPUInfo.l2_cache_size = cpuinfo_obj["l2_cache_size"]
        CPUInfo.l2_cache_line_size = cpuinfo_obj["l2_cache_line_size"]
        CPUInfo.l2_cache_associativity = cpuinfo_obj["l2_cache_associativity"]
        CPUInfo.l3_cache_size = cpuinfo_obj["l3_cache_size"]

        Log.debug_static(CPUInfo, LogFile.system_info, show_timestamp=False)
   
   # static values getters    
    def get_name():          
        return CPUInfo.name
    
    def get_architecture(format_output=False):  
        architecture = CPUInfo.architecture
        if format_output:
            architecture = f"{architecture}-Bit"
        return architecture   
    
    def get_cores_physical():
        return CPUInfo.cores_physical 
    def get_cores_logical():
        return CPUInfo.cores_logical
    
    def get_frequency_min(format_output=False):
        frequency = CPUInfo.frequency_min
        if format_output:
            frequency = Convert.megahertz_to_gigahertz(frequency)
        return frequency
    def get_frequency_max(format_output=False):
        frequency = CPUInfo.frequency_max
        if format_output:
            frequency = Convert.megahertz_to_gigahertz(frequency)
        return frequency
    
    def get_l1_data_cache_size(format_output=False):
        cache_size = CPUInfo.l1_data_cache_size
        if format_output:
            cache_size = Convert.convert_bytes_to_unit(cache_size)
        return cache_size
    def get_l1_instruction_cache_size(format_output=False):
        cache_size = CPUInfo.l1_instruction_cache_size
        if format_output:
            cache_size = Convert.convert_bytes_to_unit(cache_size)
        return cache_size
    def get_l2_cache_size(format_output=False):
        cache_size = CPUInfo.l2_cache_size
        if format_output:
            cache_size = Convert.convert_bytes_to_unit(cache_size)
        return cache_size
    def get_l2_cache_line_size(format_output=False):
        cache_size = CPUInfo.l2_cache_line_size
        if format_output:
            cache_size = Convert.convert_bytes_to_unit(cache_size)
        return cache_size
    def get_l2_cache_associativity(format_output=False):
        return CPUInfo.l2_cache_associativity
    def get_l3_cache_size(format_output=False):
        cache_size = CPUInfo.l3_cache_size * CPUInfo.cores_logical
        if format_output:
            cache_size = Convert.convert_bytes_to_unit(cache_size)
        return cache_size

    # changing values getters
    def check_current_usage(format_output=False):
        usage = psutil.cpu_percent()
        if format_output:
            usage = f'{usage}%' 
        return usage
    def check_current_frequency(format_output=False):
        frequency = psutil.cpu_freq()[0]     
        if format_output:
            frequency = f'{Convert.megahertz_to_gigahertz(frequency)} GHz'
        return frequency
    

class OSInfo:
    type = None
    description = None

    release = None
    version = None
    
    host_name = None
    user_name = None

    boot_time = None

    def gather_static_values():   
        Log.task("Gathering OS information")             
        
        OSInfo.type = platform.system()
        OSInfo.description = platform.platform()

        OSInfo.release = platform.release()
        OSInfo.version = platform.version() 

        OSInfo.host_name = platform.node()
        OSInfo.user_name = psutil.users()[0][0]

        OSInfo.boot_time = psutil.boot_time()

        Log.debug_static(OSInfo, LogFile.system_info, show_timestamp=False)   

    # static values getters        
    def get_type():
        return OSInfo.type 
    def get_description():
        return OSInfo.description
    def get_release():
        return OSInfo.release
    def get_version():
        return OSInfo.version    
    def get_host_name():
        return OSInfo.host_name
    def get_user_name():
        return OSInfo.user_name    
    def get_boot_time(format_output=False):
        boot_time = OSInfo.boot_time
        if format_output:
            boot_time = Convert.timestamp_to_date(boot_time)
        return boot_time
    

class PythonInfo:
    version = None
    implementation = None
    compiler = None
    build = None

    def gather_static_values():
        Log.task(f"Gathering Python information")

        PythonInfo.version = platform.python_version()
        PythonInfo.implementation = platform.python_implementation()
        PythonInfo.compiler = platform.python_compiler()        
        PythonInfo.build = platform.python_build()        

        Log.debug_static(PythonInfo, LogFile.system_info, show_timestamp=False)

