from utils.helpers import Convert


class NetworkInfo:
    internet_available = None
    bytes_sent = None
    bytes_received = None
    speed_download = None
    speed_upload = None

    def get_speed_download(format_output=True, include_unit=False):
        speed = NetworkInfo.speed_download
        if speed and NetworkInfo.internet_available:
            if format_output:
                speed = f"{speed:.2f}"
            if include_unit:
                speed = f"{speed} Mbps"
        else: speed = '-'
        return speed
    def get_speed_upload(format_output=True, include_unit=False):
        speed = NetworkInfo.speed_upload
        if speed and NetworkInfo.internet_available:
            if format_output:
                speed = f"{speed:.2f}"
            if include_unit:
                speed = f"{speed} Mbps"
        else: speed = '-'
        return speed

    def get_bytes_sent(format_output=True, include_unit=False):
        sent = NetworkInfo.bytes_sent
        if sent:
            if format_output:
                sent = f"{sent:.2f}"
            if include_unit:
                sent = f"{sent} Mbps"
        else: sent = '-'
        return sent
    def get_bytes_received(format_output=True, include_unit=False):
        received = NetworkInfo.bytes_received
        if received:
            if format_output:
                received = f"{received:.2f}"
            if include_unit:
                received = f"{received} Mbps"
        else: received = '-'
        return received

    def get_internet_available(format_output=True):
        availability = NetworkInfo.internet_available
        if format_output:
            if NetworkInfo.internet_available:
                availability = 'UP'
            else:
                availability = 'DOWN'
        return availability

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
            ("Architecture", CPUInfo.get_architecture(include_unit=True)),
            ("Physical Cores", CPUInfo.get_cores_physical()),
            ("Logical Cores", CPUInfo.get_cores_logical()),
            ("Base Clock", CPUInfo.get_frequency_max(include_unit=True)),
            ("L1 Cache", CPUInfo.get_l1_total_size(include_unit=True)),
            ("L2 Cache", CPUInfo.get_l2_total_size(include_unit=True)),
            ("L3 Cache", CPUInfo.get_l3_cache_size(include_unit=True))]
        return tuple_list        


    def get_name():
        return CPUInfo.name         
    def get_architecture(include_unit=False):
        architecture = CPUInfo.architecture
        if include_unit:
            architecture = f"{architecture}-Bit"
        return architecture
    # cores
    def get_cores_physical():
        return CPUInfo.cores_physical     
    def get_cores_logical():
        return CPUInfo.cores_logical
    # usage
    def get_usage_current(include_unit=False):
        usage = CPUInfo.current_usage
        if include_unit:
            usage = f"{usage}%"
        return usage  
    # frequency
    def get_frequency_min(format_output=True, include_unit=False):
        frequency = CPUInfo.frequency_min
        if format_output:
            frequency = Convert.mhz_to_ghz(frequency)
        if include_unit:
            frequency = f"{frequency} GHz"
        return frequency
    def get_frequency_max(format_output=True, include_unit=False):
        frequency = CPUInfo.frequency_max
        if format_output:
            frequency = Convert.mhz_to_ghz(frequency)
        if include_unit:
            frequency = f"{frequency} GHz"
        return frequency    
    def get_frequency_current(format_output=True, include_unit=False):        
        frequency = CPUInfo.current_frequency
        if format_output:            
            frequency = Convert.mhz_to_ghz(frequency)
        if include_unit:
            frequency = f"{frequency} GHz"
        return frequency
    # cache
    def get_l1_total_size(include_unit=False):
        cache_size = CPUInfo.get_l1_data_cache_size() + CPUInfo.get_l1_instruction_cache_size()
        if include_unit:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size
    def get_l1_data_cache_size(include_unit=False):
        cache_size = CPUInfo.l1_data_cache_size
        if include_unit:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size
    def get_l1_instruction_cache_size(include_unit=False):
        cache_size = CPUInfo.l1_instruction_cache_size
        if include_unit:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size
    def get_l2_total_size(include_unit=False):
        cache_size = CPUInfo.get_l2_cache_size() + CPUInfo.get_l2_cache_line_size()
        if include_unit:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size
    def get_l2_cache_size(include_unit=False):
        cache_size = CPUInfo.l2_cache_size
        if include_unit:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size
    def get_l2_cache_line_size(include_unit=False):
        cache_size = CPUInfo.l2_cache_line_size
        if include_unit:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size
    def get_l2_cache_associativity():
        return CPUInfo.l2_cache_associativity
    def get_l3_cache_size(include_unit=False):
        cache_size = CPUInfo.l3_cache_size * CPUInfo.cores_logical
        if include_unit:
            cache_size = Convert.bytes_to_unit(cache_size)
        return cache_size   