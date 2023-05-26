from PySide6 import QtCore

from utils.log import Logger


class ThreadManager:    
    thread_pool = QtCore.QThreadPool() 
    active_threads = []

    @staticmethod
    def start_thread(thread):        
        Logger.send(f"Starting thread {thread}")
        ThreadManager.active_threads.append(thread)
        ThreadManager.thread_pool.start(thread)
    
    @staticmethod
    def report_finished(thread):        
        Logger.send(f"Finished thread {thread}")
        ThreadManager.active_threads.remove(thread)
    
    @staticmethod
    def report_waiting(thread):
        Logger.send(f"Waiting for thread {thread}")

    @staticmethod
    def clean_up():
        if ThreadManager.active_threads:            
            Logger.send(f"Cleaning up {ThreadManager.thread_pool.activeThreadCount()} threads")
            for thread in ThreadManager.active_threads[:]:
                thread.finish()     