from utils.helpers import Convert

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
    current_usage = None
    current_frequency = None    

    
    def get_tuple_list():
        tuple_list = [
            ("Name", CPUInfo.get_name()),
            ("Architecture", CPUInfo.get_architecture(True)),
            ("Physical Cores", CPUInfo.get_cores_physical()),
            ("Logical Cores", CPUInfo.get_cores_logical()),
            ("Base Clock", CPUInfo.get_frequency_max(True)),
            ("L1 Cache", CPUInfo.get_l1_total_size(True)),
            ("L2 Cache", CPUInfo.get_l2_total_size(True)),
            ("L3 Cache", CPUInfo.get_l3_cache_size(True))]
        return tuple_list        


    def get_name():
        return CPUInfo.name         
    def get_architecture(format_output=False):
        architecture = CPUInfo.architecture
        if format_output:
            architecture = f"{architecture}-Bit"
        return architecture
    # cores
    def get_cores_physical():
        return CPUInfo.cores_physical     
    def get_cores_logical():
        return CPUInfo.cores_logical
    # frequency
    def get_frequency_min(format_output=False):
        frequency = CPUInfo.frequency_min
        if format_output:
            frequency = Convert.mhz_to_ghz(frequency)
        return frequency
    def get_frequency_max(format_output=False):
        frequency = CPUInfo.frequency_max
        if format_output:
            frequency = Convert.mhz_to_ghz(frequency)
        return frequency    
    def get_frequency_current(format_output=False):        
        frequency = CPUInfo.current_frequency
        if format_output:            
            frequency = Convert.mhz_to_ghz(frequency)
        return frequency
    # cache
    def get_l1_total_size(format_output=False):
        cache_size = CPUInfo.get_l1_data_cache_size() + CPUInfo.get_l1_instruction_cache_size()
        if format_output:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size
    def get_l1_data_cache_size(format_output=False):
        cache_size = CPUInfo.l1_data_cache_size
        if format_output:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size
    def get_l1_instruction_cache_size(format_output=False):
        cache_size = CPUInfo.l1_instruction_cache_size
        if format_output:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size
    def get_l2_total_size(format_output=False):
        cache_size = CPUInfo.get_l2_cache_size() + CPUInfo.get_l2_cache_line_size()
        if format_output:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size
    def get_l2_cache_size(format_output=False):
        cache_size = CPUInfo.l2_cache_size
        if format_output:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size
    def get_l2_cache_line_size(format_output=False):
        cache_size = CPUInfo.l2_cache_line_size
        if format_output:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size
    def get_l2_cache_associativity(format_output=False):
        return CPUInfo.l2_cache_associativity
    def get_l3_cache_size(format_output=False):
        cache_size = CPUInfo.l3_cache_size * CPUInfo.cores_logical
        if format_output:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size

    def get_usage_current(format_output=False):
        usage = CPUInfo.current_usage
        if format_output:
            usage = f"{usage}%"
        return usage    
    


    