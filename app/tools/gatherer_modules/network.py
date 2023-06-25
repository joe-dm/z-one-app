import subprocess
import psutil
import speedtest

from PySide6 import QtCore

from utils.thread import Thread
from utils.log import Log, LogFile
from tools.system_info import NetworkInfo

class NetworkMonitor:
    def __init__(self):
        Log.task('Monitoring network')
        internet_monitor = NetInternetMonitor()
        io_monitor = NetIOMonitor()
        down_speed_monitor = NetDownSpeedMonitor()
        up_speed_monitor = NetUpSpeedMonitor()


class NetDownSpeedMonitor(Thread):
    def __init__(self):
        super().__init__()
        
    def execute(self):
        while self.is_running:
            try:             
                self.speedtest_obj = speedtest.Speedtest()   
                self.speedtest_obj.get_best_server()                
                
                down_speed = self.speedtest_obj.download() / 10**6
                NetworkInfo.speed_download = down_speed
                
                self.signals.log_debug.emit(
                    f"Net download speed: {NetworkInfo.get_speed_download(include_unit=True)}",
                    LogFile.network)
            except:
                pass
            QtCore.QThread.msleep(100)

class NetUpSpeedMonitor(Thread):
    def __init__(self):
        super().__init__()
        
    def execute(self):
        while self.is_running:
            try:     
                self.speedtest_obj = speedtest.Speedtest()           
                self.speedtest_obj.get_best_server()

                up_speed = self.speedtest_obj.upload() / 10**6                 
                NetworkInfo.speed_upload = up_speed

                self.signals.log_debug.emit(
                    f"Net upload speed: {NetworkInfo.get_speed_upload(include_unit=True)}",
                    LogFile.network)
            except:
                pass
            QtCore.QThread.msleep(100) 


class NetIOMonitor(Thread):
    def __init__(self, interval=1000):
        super().__init__()                
        self.last_bytes_sent = 0
        self.last_bytes_received = 0
        self.interval = interval
        

    def execute(self):
        while self.is_running:
            if NetworkInfo.internet_available:
                net_io = psutil.net_io_counters()
                # get sent/received
                bytes_sent = net_io.bytes_sent
                bytes_received = net_io.bytes_recv
                # calculate the difference
                sent_difference = bytes_sent - self.last_bytes_sent
                received_difference = bytes_received - self.last_bytes_received
                # set values in system info class
                NetworkInfo.bytes_sent = (sent_difference * 8) / (1000 * self.interval)
                NetworkInfo.bytes_received = (received_difference * 8) / (1000 * self.interval)
                # set last bytes for next iteration
                self.last_bytes_sent = bytes_sent
                self.last_bytes_received = bytes_received
            else:
                NetworkInfo.bytes_sent = None
                NetworkInfo.bytes_received = None
                        
            QtCore.QThread.msleep(self.interval)    


class NetInternetMonitor(Thread):
    def __init__(self):
        super().__init__()             
    
    def execute(self, address='8.8.8.8'):
        while self.is_running:
            result = subprocess.run(["ping", "-c", "1", address], capture_output=True, text=True)
            if result.returncode == 0:
                NetworkInfo.internet_available = True
                self.signals.log_debug.emit(f"Ping to {address} successful", LogFile.network)
            else:
                NetworkInfo.internet_available = False
                NetworkInfo.speed_download = None
                NetworkInfo.speed_upload = None
                self.signals.log_debug.emit(f"Ping to {address} failed", LogFile.network)
            QtCore.QThread.msleep(1000)        

     
