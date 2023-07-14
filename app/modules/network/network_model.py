import psutil
import socket
import subprocess
import speedtest

from PySide6 import QtCore

from utils.thread import Thread


class NetworkModelSignals(QtCore.QObject):
    updated_interfaces = QtCore.Signal(list)
    updated_internet_available = QtCore.Signal(bool)
    updated_speed_download = QtCore.Signal(object)
    updated_speed_upload = QtCore.Signal(object)
    updated_ip_isp = QtCore.Signal()    
    updated_latency = QtCore.Signal(float)
    updated_quality = QtCore.Signal(str)
    updated_bytes_sent = QtCore.Signal(float)
    updated_bytes_received = QtCore.Signal(float)

class NetworkModel:
    def __init__(self):
        self.signals = NetworkModelSignals()

        self._internet_available = None
        self._ip_address = None
        self._isp = None
        self._latency = None
        self._quality = None

        self._bytes_sent = None
        self._bytes_received = None

        self._speed_download = None
        self._speed_upload = None

        self._interfaces = []

        self._net_io_monitor = NetIOMonitor(self)
        self._net_monitor = NetMonitor(self)
        self._net_ping_monitor = NetPingMonitor(self)        
        self._net_slow_monitor = NetSpeedMonitor(self)

    def get_bytes_sent(self):
        return self._bytes_sent
    def get_bytes_received(self):
        return self._bytes_received
    def get_interfaces(self):
        return self._interfaces
    def get_internet_available(self):
        return self._internet_available
    def get_speed_download(self):
        return self._speed_download
    def get_speed_upload(self):
        return self._speed_upload
    def get_ip_address(self):
        return self._ip_address
    def get_isp(self):
        return self._isp
    def get_latency(self):
        return self._latency
    def get_quality(self):
        return self._quality

    def update_bytes_sent(self, sent):
        if not sent == self._bytes_sent:
            self._bytes_sent = sent
            self.signals.updated_bytes_sent.emit(self.get_bytes_sent())
    def update_bytes_received(self, received):
        if not received == self._bytes_received:
            self._bytes_received = received
            self.signals.updated_bytes_received.emit(self.get_bytes_received())            
    def update_ip_address(self, ip):
        if not ip == self._ip_address:
            self._ip_address = ip
            self.signals.updated_ip_isp.emit()    
    def update_isp(self, isp):
        if not isp == self._isp:
            self._isp = isp
            self.signals.updated_ip_isp.emit()
    def update_interfaces(self, interfaces):  
        if not interfaces == self._interfaces:                          
            self._interfaces = interfaces        
            self.signals.updated_interfaces.emit(self.get_interfaces())
    def update_internet_available(self, internet_available):          
        self._internet_available = internet_available
        self.signals.updated_internet_available.emit(self.get_internet_available())
    def update_speed_download(self, speed):
        if not speed == self._speed_download:
            self._speed_download = speed
            self.signals.updated_speed_download.emit(self.get_speed_download())
    def update_speed_upload(self, speed): 
        if not speed == self._speed_upload:      
            self._speed_upload = speed
            self.signals.updated_speed_upload.emit(self.get_speed_upload())
    def update_latency(self, latency):
        if not latency == self._latency:
            self._latency = latency
            self.signals.updated_latency.emit(self.get_latency())
    def update_quality(self, quality):        
        if not quality == self._quality:
            self._quality = quality
            self.signals.updated_quality.emit(self.get_quality())
    

class NetMonitor(Thread):
    def __init__(self, model: NetworkModel):
        super().__init__()
        self.model = model        
    
    def execute(self):
        self.thread_signals.log_task.emit('Started monitoring network', None)        
        self.check_interfaces()          

        while self.is_running:               
            self.check_interfaces()

            try:
                self.speedtest_obj = speedtest.Speedtest(secure=True)  
                self.check_latency()
            except:
                self.model.update_latency(None)
                self.model.update_quality(None)
            QtCore.QThread.msleep(100)       

    def check_latency(self):        
        if self.model.get_internet_available():
            self.speedtest_obj.get_best_server()
            
            latency = self.speedtest_obj.results.ping
            self.model.update_latency(latency)

            if latency < 50: 
                quality = '✦✦✦✦'
            elif latency < 100: 
                quality = '✦✦✦✧'
            elif latency < 200: 
                quality = '✦✦✧✧'
            else: 
                quality = '✦✧✧✧'            
            self.model.update_quality(quality)  
        else:
            self.model.update_latency(None)
            self.model.update_quality(None)
                
    
    def check_interfaces(self):
        psutil_obj = psutil.net_if_addrs()
        interfaces = []

        for interface, addresses in psutil_obj.items():
            info_dict = {
                "interface": interface, "addresses": [], 
                "mac_address": None, "mtu": None, "flags": [],
                "ipv6_addresses": []}
            
            # get the addresses
            for address in addresses:
                if address.family == socket.AF_INET:
                    info_dict["addresses"].append((address.address, address.netmask))
                elif address.family == psutil.AF_LINK:
                    info_dict["mac_address"] = address.address
                elif address.family == socket.AF_INET6:
                    clean_ipv6 = address.address.split("%")[0]
                    clean_ipv6_netmask_cidr = "/" + str(address.netmask.count("f") * 4)
                    info_dict["ipv6_addresses"].append((clean_ipv6, clean_ipv6_netmask_cidr))
            # get mtu and flags
            interface_stats = psutil.net_if_stats().get(interface)
            if interface_stats:
                info_dict["mtu"] = interface_stats.mtu
                info_dict["flags"] = interface_stats.flags
            
            if info_dict["addresses"] or info_dict["mac_address"] or info_dict["ipv6_addresses"]:
                interfaces.append(info_dict)        
        
        self.model.update_interfaces(interfaces)

class NetIOMonitor(Thread):
    def __init__(self, model: NetworkModel):
        super().__init__()
        self.model = model
        self.last_bytes_sent = 0
        self.last_bytes_received = 0
        self.interval = 1000
    
    def execute(self):
        while self.is_running:
            if self.model.get_internet_available():
                net_io = psutil.net_io_counters()
                # get sent/received
                sent = net_io.bytes_sent
                received = net_io.bytes_recv
                # calculate the difference
                sent_difference = sent - self.last_bytes_sent
                received_difference = received - self.last_bytes_received
                # calculate speed in Mbps per second                
                self.model.update_bytes_sent(((sent_difference * 8) / (1000 * self.interval)))                
                self.model.update_bytes_received(((received_difference * 8) / (1000 * self.interval)))                
                # set last bytes for next iteration
                self.last_bytes_sent = sent
                self.last_bytes_received = received
            else:
                self.model.update_bytes_sent(None)
                self.model.update_bytes_received(None)

            QtCore.QThread.msleep(self.interval) 
    

class NetPingMonitor(Thread):
    def __init__(self, model: NetworkModel):
        super().__init__()
        self.model = model

    def execute(self, address='8.8.8.8'):
        self.thread_signals.log_task.emit('Started monitoring internet availability', None)
        
        while self.is_running:    
            result = subprocess.run(["ping", "-c", "1", address], capture_output=True, text=True)
            if result.returncode == 0:
                self.model.update_internet_available(True)                
            else:
                self.model.update_internet_available(False) 
            QtCore.QThread.msleep(100)


class NetSpeedMonitor(Thread):
    def __init__(self, model: NetworkModel):
        super().__init__()
        self.model = model

    def execute(self):
        self.thread_signals.log_task.emit('Started monitoring internet speeds', None)
        
        while self.is_running:
            try:
                self.speedtest_obj = speedtest.Speedtest(secure=True)
                self.speedtest_obj.get_best_server()
                self.check_ip()
                self.check_isp()                
                self.check_speeds()                
            except:
                self.model.update_ip_address(None)
                self.model.update_isp(None)
                self.model.update_speed_download(None) 
                self.model.update_speed_upload(None)
    
    def check_ip(self):
        try:
            ip_address = self.speedtest_obj.get_config()['client']['ip']            
            self.model.update_ip_address(ip_address) 
        except:
            self.model.update_ip_address(None)            
            
    
    def check_isp(self):     
        try:   
            isp = self.speedtest_obj.get_config()['client']['isp']          
            self.model.update_isp(isp)         
        except:
            self.model.update_isp(None)
        

    def check_speeds(self):
        try:
            # get download speed
            down_speed = self.speedtest_obj.download() / 10**6                
            self.model.update_speed_download(down_speed) 
            # get upload speed
            up_speed = self.speedtest_obj.upload() / 10**6
            self.model.update_speed_upload(up_speed)  
        except:                
            self.model.update_speed_download(None) 
            self.model.update_speed_upload(None) 
    
    
    
    