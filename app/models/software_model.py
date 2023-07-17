import platform
import distro
import psutil
import subprocess

from utils.decorators import singleton
from utils.log import Log
from utils.file import File, JSON
from utils.session import Session

@singleton
class SoftwareModel:   

    def __init__(self):
        Log.task('Gathering software info')

        self._os_type = platform.system()
        Session.os_type = self._os_type
        self._os_name = None
        self._os_family = None
        self._os_codename = None
        self._os_version = platform.version()
        self._os_release = platform.release()
        self._hostname = platform.node()
        self._boot_time = psutil.boot_time()        
        self._installed_apps = []

        self._gather_additional_info()
        self._gather_installed_apps()
                

    def _gather_additional_info(self):
        if self._os_type == 'Linux':            
            File.run_admin_script('get_dmi_info.py')

            self._os_name = distro.name()
            self._os_version = distro.version()
            self._os_family = f'{distro.like().capitalize()}'
            self._os_codename = distro.codename()            
            


    def _gather_installed_apps(self):
        if self._os_type == 'Linux' and self._os_family == 'Debian':
            try:
                # retrieve snap store package apps
                cmd = "snap list 2>/dev/null"
                output = subprocess.check_output(cmd, shell=True)
                snap_apps = [line.split()[0] for line in output.decode().splitlines()[1:]]
                self._installed_apps.append(('Snap Apps', snap_apps))
            except: pass

            try:
                # retrieve flatpak package apps
                cmd = "flatpak list --app --columns=application 2>/dev/null"
                output = subprocess.check_output(cmd, shell=True)
                flatpak_apps = output.decode().splitlines()
                self._installed_apps.append(('Flatpak Apps', flatpak_apps))
            except: pass

            try:
                # retrieve debian package manager apps
                cmd = "dpkg-query -W -f='${Package}\n'"
                output = subprocess.check_output(cmd, shell=True)
                debian_apps = output.decode().splitlines()
                
                # categorize apps as debian (non-system), system and python
                debian_non_system_apps = [app for app in debian_apps if not app.startswith('lib') and not app.startswith('python')]                
                python_apps = [app for app in debian_apps if app.startswith('python')]
                system_apps = [app for app in debian_apps if app.startswith('lib')]

                self._installed_apps.append(('Debian Apps (Non-System)', debian_non_system_apps))                
                self._installed_apps.append(('Python', python_apps))
                self._installed_apps.append(('System', system_apps))
            except: pass    

    def get_os_type(self): 
        return self._os_type
    def get_os_name(self):
        return self._os_name
    def get_os_family(self):
        return self._os_family
    def get_os_codename(self):
        return self._os_codename
    def get_os_version(self):
        return self._os_version
    def get_os_release(self):
        return self._os_release
    def get_hostname(self):
        return self._hostname
    def get_boot_time(self):
        return self._boot_time
    def get_installed_apps(self):
        return self._installed_apps