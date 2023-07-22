import subprocess
import os

from models.software_model import SoftwareModel
from utils.decorators import singleton
from utils.log import Log
from utils.session import Session

@singleton
class GPUModel:
    def __init__(self):      
        Log.task('Gathering GPU info')

        self._display_adapter_dict = {}
        
        self._gather_info_from_os()
    
    def _gather_info_from_os(self):
        if Session.os_type == 'Linux':
            Log.debug('Gathering GPU info from lshw')
            try:
                output = subprocess.check_output(
                    ['lshw', '-C', 'display'], stderr=subprocess.DEVNULL, universal_newlines=True)
                lines = output.split('\n')
                for line in lines:
                    line = line.strip()
                    if line.startswith("*-display"):
                        continue
                    if ':' in line:
                        key, value = line.split(':', 1)
                        self._display_adapter_dict[key.strip()] = value.strip()                
            except FileNotFoundError:
                Log.error("Could not retrieve GPU info, lshw utility not found")

    def get_display_adapter_dict(self):
        return self._display_adapter_dict
