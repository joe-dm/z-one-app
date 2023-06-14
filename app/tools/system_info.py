import platform
import psutil

from PySide6 import QtCore

from utils.log import Log 
from utils.thread import Thread

class InfoGatherer(Thread):
    def __init__(self):
        super().__init__()
        self.signals.log_task.emit(f"Gathering system information", None)

    def execute(self):       

        self.os = OperatingSystem()
        self.signals.log_debug_init.emit(self.os, True)

        self.cpu = Processor()
        self.signals.log_debug_init.emit(self.cpu, True)
        
        self.python = Python()
        self.signals.log_debug_init.emit(self.python, True)
        
        

    def finish(self):
        self.signals.waiting.emit(self)


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


class Processor:
    def __init__(self):
        #Log.task(f"Gathering CPU info")

        self.architecture = platform.processor()
        self.cores = psutil.cpu_count(logical=False)
        self.threads = psutil.cpu_count(logical=True)        
        self.frequency_min = psutil.cpu_freq()[1]
        self.frequency_max = psutil.cpu_freq()[2]

        #Log.debug_init(self, show_attributes=True)


class Python:
    def __init__(self):
        #Log.task(f"Gathering Python info")

        self.version = platform.python_version()
        self.implementation = platform.python_implementation()
        self.compiler = platform.python_compiler()        
        self.build = platform.python_build()        

        #Log.debug_init(self, show_attributes=True)

