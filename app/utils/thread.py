from PySide6 import QtCore

from utils.log import Log
from utils.sound import SoundAlert

class ThreadSignals(QtCore.QObject):       
    finished = QtCore.Signal(object)
    waiting = QtCore.Signal(object)
    # used for console output
    log_info = QtCore.Signal(str, str)
    log_warning = QtCore.Signal(str, str)
    log_error = QtCore.Signal(str, str)
    log_critical = QtCore.Signal(str, str)
    log_task = QtCore.Signal(str, str)
    log_debug = QtCore.Signal(str, str)
    log_debug_init = QtCore.Signal(object, bool)
    # sound alert
    play_alert = QtCore.Signal(str)

class Thread(QtCore.QRunnable):
    def __init__(self):
        super().__init__()        
        self.signals = ThreadSignals()
        self.thread_name = type(self).__name__  
        self.is_running = True      
                
        # connect finished/waiting signal
        self.signals.finished.connect(ThreadManager.report_finished)
        self.signals.waiting.connect(ThreadManager.report_waiting)
        # connect log signals
        self.signals.log_info.connect(Log.info)
        self.signals.log_warning.connect(Log.warning)
        self.signals.log_error.connect(Log.error)
        self.signals.log_critical.connect(Log.critical)
        self.signals.log_task.connect(Log.task)
        self.signals.log_debug.connect(Log.debug)    
        self.signals.log_debug_init.connect(Log.debug_init)    
        # connect alert signal
        self.signals.play_alert.connect(SoundAlert.play)

        # start the thread
        ThreadManager.start_thread(self)

    @QtCore.Slot()
    def run(self):      
        self.execute()
        self.signals.finished.emit(self)    
    
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

