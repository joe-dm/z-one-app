from PySide6 import QtCore

from utils.log import Log


class ThreadSignals(QtCore.QObject):       
    finished = QtCore.Signal(object)
    waiting = QtCore.Signal(object)
    # used for console output
    log_info = QtCore.Signal(str, str)
    log_warning = QtCore.Signal(str, str)
    log_error = QtCore.Signal(str, str)
    log_critical = QtCore.Signal(str, str)    
    log_operation = QtCore.Signal(str, str)
    log_task = QtCore.Signal(str, str)
    log_debug = QtCore.Signal(str, str)
    log_debug_init = QtCore.Signal(object, bool)
    

class Thread(QtCore.QRunnable):
    def __init__(self):
        super().__init__()        
        self.thread_signals = ThreadSignals()
        self.thread_name = type(self).__name__  
        self.is_running = True         
                
        # connect finished/waiting signal
        self.thread_signals.finished.connect(ThreadManager.report_finished)
        self.thread_signals.waiting.connect(ThreadManager.report_waiting)
        # connect log thread
        self.thread_signals.log_info.connect(Log.info)
        self.thread_signals.log_warning.connect(Log.warning)
        self.thread_signals.log_error.connect(Log.error)
        self.thread_signals.log_critical.connect(Log.critical)
        self.thread_signals.log_operation.connect(Log.operation)
        self.thread_signals.log_task.connect(Log.task)
        self.thread_signals.log_debug.connect(Log.debug)    
        self.thread_signals.log_debug_init.connect(Log.debug_init)        

        # start the thread
        ThreadManager.start_thread(self)

    @QtCore.Slot()
    def run(self):      
        self.execute()
        self.thread_signals.finished.emit(self)     
    # overridden by child classes
    def execute(self): pass     
    def finish(self): 
        self.is_running = False


class ThreadManager(QtCore.QObject):
    thread_pool = QtCore.QThreadPool()
    active_threads = []

    def start_thread(thread):
        Log.debug(f"Starting thread: {thread.__class__.__name__}")
        ThreadManager.thread_pool.start(thread)
        ThreadManager.active_threads.append(thread)
        
    def report_finished(thread):
        Log.debug(f"Finished thread: {thread.__class__.__name__}")        
        ThreadManager.active_threads.remove(thread)
    
    def report_waiting(thread):
        Log.debug(f"Waiting for thread: {thread.__class__.__name__}")
    
    def clean_up():        
        if ThreadManager.active_threads:            
            Log.debug(f"Cleaning up {ThreadManager.thread_pool.activeThreadCount()} threads")
            for thread in ThreadManager.active_threads[:]:
                thread.finish()

