import sys
import traceback
import inspect

from PySide6 import QtCore

from utils.log import Logger

class Thread:
    threadpool = QtCore.QThreadPool()

    @staticmethod
    def start(function, *args, **kwargs):
        worker = Worker(function, *args, **kwargs)
        Thread.threadpool.start(worker)
        Thread.log_thread(worker)
        worker.signals.finished.connect(lambda: Thread.log_thread(worker, False))

    @staticmethod
    def log_thread(worker, started=True):
        # Retrieve the necessary information about the thread        
        function_name = worker.function.__name__
        function_module = inspect.getmodule(worker.function).__name__

        # Determine the thread status
        status = "started" if started else "finished"

        # Create the log message
        log_message = f"Thread {status}: {function_name} ({function_module})"

        # Log the message using the Logger
        Logger.log(log_message, 'debug')    
    


class Worker(QtCore.QRunnable):
    def __init__(self, function, *args, **kwargs):
        super().__init__()

        # store constructor arguments (re-used for processing)
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.signals = Signals()

    @QtCore.Slot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.function(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

class Signals(QtCore.QObject):
    error = QtCore.Signal(tuple)
    result = QtCore.Signal(object)
    progress = QtCore.Signal(int)
    finished = QtCore.Signal()
