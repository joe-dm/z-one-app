from PySide6 import QtCore

from utils.log import Log


class ThreadManager:    
    thread_pool = QtCore.QThreadPool() 
    active_threads = []    

    @staticmethod
    def start_thread(thread):        
        Log.debug(f"Starting thread: {thread.__class__.__name__}")
        ThreadManager.active_threads.append(thread)
        ThreadManager.thread_pool.start(thread)
    
    @staticmethod
    def report_finished(thread):        
        Log.debug(f"Finished thread: {thread.__class__.__name__}")
        ThreadManager.active_threads.remove(thread)
    
    @staticmethod
    def report_waiting(thread):
        Log.debug(f"Waiting for thread: {thread.__class__.__name__}")

    @staticmethod
    def clean_up():
        if ThreadManager.active_threads:            
            Log.debug(f"Cleaning up {ThreadManager.thread_pool.activeThreadCount()} threads")
            for thread in ThreadManager.active_threads[:]:
                thread.finish()     