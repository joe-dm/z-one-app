import json
import subprocess
import os
import sys

from config.config import PathConfig
from utils.log import Log
from utils.session import Session


class File:    
    def run_admin_script(file_name):
        # Get the directory of the current script (where Session is defined)
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Assuming get_dmi_info.py is in the "utils" directory within the script's directory
        privileged_script = os.path.join(script_dir, 'admin_scripts', file_name)

        Log.task(f'Running script "{file_name}" as admin')

        if os.name == 'posix':
            sudo_command = ['pkexec', sys.executable, privileged_script]
        else:
            raise NotImplementedError("Running with elevated privileges on Windows is more complex.")

        try:
            completed_process = subprocess.run(
                sudo_command, check=True, 
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            Session.is_admin = True
        except subprocess.CalledProcessError as e:
            Log.error(f"Failed to run {file_name} as admin (Code {e.returncode})")
            Log.warning(f"Some features will be unavailable due to lack of elevation")
            Session.is_admin = False


class JSON:
    dmi_file = os.path.join(PathConfig.admin_scripts_output_directory, 'dmi_info.json')

    def find_dmi_entries(dmi_name):        
        json_file_path = JSON.dmi_file
        Log.debug(f"Looking for '{dmi_name}' in dmi info file")

        with open(json_file_path, "r") as json_file:
            dmi_data = json.load(json_file)

        matching_entries = []

        for entry_list in dmi_data:
            for entry_dict in entry_list:
                if entry_dict["DMIName"] == dmi_name:
                    matching_entries.append(entry_dict)

        return matching_entries
