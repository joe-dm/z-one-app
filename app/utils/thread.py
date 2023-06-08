from PySide6 import QtCore
from utils.log import Log

class ThreadSignals(QtCore.QObject):       
    finished = QtCore.Signal(object)  
    # used for console output
    log_info = QtCore.Signal(str)
    log_warning = QtCore.Signal(str)
    log_error = QtCore.Signal(str)
    log_critical = QtCore.Signal(str)
    log_task = QtCore.Signal(str)
    log_debug = QtCore.Signal(str)

class Thread(QtCore.QRunnable):
    def __init__(self):
        super().__init__()        
        self.signals = ThreadSignals()
        self.thread_name = type(self).__name__        
                
        # connect finished signal
        self.signals.finished.connect(ThreadManager.report_finished)
        # connect log signals
        self.signals.log_info.connect(Log.info)
        self.signals.log_warning.connect(Log.warning)
        self.signals.log_error.connect(Log.error)
        self.signals.log_critical.connect(Log.critical)
        self.signals.log_task.connect(Log.task)
        self.signals.log_debug.connect(Log.debug)        

        # start the thread
        ThreadManager.start_thread(self)

    @QtCore.Slot()
    def run(self):      
        self.execute()
        self.signals.finished.emit(self)
        
    def execute(self): pass # overridden by child classes

class ThreadManager:
    thread_pool = QtCore.QThreadPool()
    active_threads = []
        
    def start_thread(thread):
        Log.task(f"Starting {thread.__class__.__name__}")
        ThreadManager.thread_pool.start(thread)
        ThreadManager.active_threads.append(thread)
        
    def report_finished(thread):
        Log.info(f"Finished {thread.__class__.__name__}")        
        ThreadManager.active_threads.remove(thread)
    