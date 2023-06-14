import platform
import psutil

from utils.log import Log 

class OperatingSystem:
    def __init__(self):        
        self.type = platform.system()
        self.release = platform.release()
        self.version = platform.version()
        self.description = platform.platform()
        self.host_name = platform.node()
        self.boot_time = psutil.boot_time()

        Log.debug_init(self, show_attributes=True)


class Processor:
    def __init__(self):
        self.architecture = platform.processor()
        self.cores = psutil.cpu_count(logical=True)
        self.threads = psutil.cpu_count(logical=False)
        self.max_frequency = psutil.cpu_freq()[2]

        Log.debug_init(self, show_attributes=True)


class Python:
    def __init__(self):
        self.version = platform.python_version()
        self.revision = platform.python_revision()
        self.implementation = platform.python_implementation()
        self.compiler = platform.python_compiler()        
        self.branch = platform.python_branch()
        self.build = platform.python_build()        

        Log.debug_init(self, show_attributes=True)

