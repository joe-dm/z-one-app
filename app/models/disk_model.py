import subprocess
import shlex

from utils.decorators import singleton
from utils.log import Log
from utils.session import Session


@singleton
class DiskModel:
    def __init__(self):
        Log.task('Gathering disk info')

        self._disk_devices = []
        self._gather_info_from_os() 
        

    def _gather_info_from_os(self):
        if Session.os_type == 'Linux':
            Log.debug('Gathering disk info from lsblk')
            # run lsblk command and capture output
            cmd = "lsblk -P --output NAME,PARTTYPENAME,ZONED,STATE,PATH,FSTYPE,SIZE,FSUSED,MOUNTPOINT,MODEL,SERIAL,TRAN,TYPE,ROTA,RO,PARTTYPENAME"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

            # check if command ran successfully
            if result.returncode != 0:
                Log.error(f"Error gathering disk info from lsblk (Code {result.returncode})")
                return None
        
            try:
                output_lines = result.stdout.strip()                
                all_disks_info = self._parse_lsblk_output(output_lines)                
                self._disk_devices = all_disks_info
            except Exception as e:
                Log.error(f'Error parsing disk info from lsblk output ({e})')
    
    def _parse_lsblk_output(self, output):
        Log.debug('Parsing disk info from lsblk output')

        lines = output.strip().split('\n')
        all_disks_info = {}
        current_disk = None

        for line in lines:
            disk_info = {}
            fields = shlex.split(line)

            for field in fields:
                key, value = field.split('=')
                disk_info[key] = value.strip('"')
            
            if disk_info:
                if disk_info.get('TYPE') == 'disk':
                    # save current disk and reset partitions list
                    current_disk = disk_info
                    current_disk['PARTITIONS'] = []
                    all_disks_info[current_disk['NAME']] = current_disk
                elif disk_info.get('TYPE') == 'part':
                    # append partition info to current disk
                    if current_disk is not None:
                        current_disk['PARTITIONS'].append(disk_info)
        
        return all_disks_info.values()

    def get_disk_devices(self):
        return self._disk_devices