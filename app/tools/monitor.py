import subprocess
import time

class MonitorNetwork:
    
    @staticmethod
    def ping(address='8.8.8.8'):
        while True:
            result = subprocess.run(["ping", "-c", "1", address], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Ping to {address} successful")
            else:
                print(f"Ping to {address} failed")
            time.sleep(1)