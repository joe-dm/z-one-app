from PySide6 import QtCore

class ThreadManager:    
    thread_pool = QtCore.QThreadPool() 
    active_threads = []

    @staticmethod
    def start_thread(thread):
        print(f"Starting thread {thread}")
        ThreadManager.active_threads.append(thread)
        ThreadManager.thread_pool.start(thread)
    
    @staticmethod
    def finish_thread(thread):
        print(f"Finished thread {thread}")
        ThreadManager.active_threads.remove(thread)    

    @staticmethod
    def clean_up():
        for thread in ThreadManager.active_threads:
            thread.finish()
        ThreadManager.active_threads.clear()

