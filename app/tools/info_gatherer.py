import platform
import psutil

from utils.log import Logger

class BasicInfo:
    def __init__(self):
        Logger.log('Gathering basic system info', 'operation')

        # from platform
        self.system = platform.system()
        self.node = platform.node()
        self.release = platform.release()
        self.version = platform.version()
        self.machine = platform.machine()
        self.processor = platform.processor()
        self.python_version = platform.python_version()
        self.python_compiler = platform.python_compiler()
        self.python_implementation = platform.python_implementation()
        self.python_build = platform.python_build()
        self.os_info = platform.platform()

        self.ln = '-----------------------------------------------------------------------'
        # from psutil
        self.boot_time = psutil.boot_time()
        self.cpu_count_logical = psutil.cpu_count(logical=True)
        self.cpu_count_physical = psutil.cpu_count(logical=False)
        self.cpu_percent = psutil.cpu_percent()
        self.cpu_freq = psutil.cpu_freq()
        self.virtual_memory = psutil.virtual_memory()
        self.swap_memory = psutil.swap_memory()
        self.disk_partitions = psutil.disk_partitions()
        self.disk_usage = {}
        for partition in self.disk_partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            self.disk_usage[partition.device] = {
                'total': usage.total,
                'used': usage.used,
                'free': usage.free,
                'percent': usage.percent
            }
        self.net_io_counters = psutil.net_io_counters()
        self.net_if_addrs = {}
        self.net_if_stats = {}
        for interface, addresses in psutil.net_if_addrs().items():
            self.net_if_addrs[interface] = []
            for address in addresses:
                addr = {
                    'family': address.family,
                    'address': address.address,
                    'netmask': address.netmask,
                    'broadcast': address.broadcast,
                    'ptp': address.ptp
                }
                self.net_if_addrs[interface].append(addr)
            self.net_if_stats[interface] = psutil.net_if_stats()[interface]
        self.users = psutil.users()

        Logger.log_init(self, True)