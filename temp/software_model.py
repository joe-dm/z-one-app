import platform
import distro
import psutil
import subprocess

from utils.log import Log

class SoftwareModel:
    def __init__(self):
        self.operating_system = OSModel()  
        self.apps_model = AppsModel(self.operating_system)
    
    def get_installed_apps(self):
        return self.apps_model.app_list    
        

class OSModel:
    def __init__(self):
        self.type = platform.system()
        self.name = ''
        self.version = platform.version()        
        self.release = platform.release()
        self.family = ''
        self.codename = ''
    
        if self.type == 'Linux':
            self.name = distro.name()
            self.version = distro.version()
            self.family = f'{distro.like().capitalize()}'
            self.codename = distro.codename()            
        
        self.hostname = platform.node()
        self.boot_time = psutil.boot_time()
            
        Log.debug_init(self, True)
    
    def get_type(self): 
        return self.type
    def get_name(self): 
        return self.name
    def get_version(self): 
        return self.version
    def get_release(self): 
        return self.release
    def get_family(self): 
        return self.family
    def get_codename(self): 
        return self.codename
    def get_hostname(self): 
        return self.hostname
    def get_boot_time(self): 
        return self.boot_time

class AppsModel:
    def __init__(self, os: OSModel):        
        self.os = os
        self.app_list = self.gather_apps()

    def gather_apps(self):        
        apps = []

        if self.os.type == 'Linux' and self.os.family == 'Debian':
            try:
                # retrieve snap store package apps
                cmd = "snap list 2>/dev/null"
                output = subprocess.check_output(cmd, shell=True)
                snap_apps = [line.split()[0] for line in output.decode().splitlines()[1:]]
                apps.append(('Snap Apps', snap_apps))
            except: pass

            try:
                # retrieve flatpak package apps
                cmd = "flatpak list --app --columns=application 2>/dev/null"
                output = subprocess.check_output(cmd, shell=True)
                flatpak_apps = output.decode().splitlines()
                apps.append(('Flatpak Apps', flatpak_apps))
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

                apps.append(('Debian Apps (Non-System)', debian_non_system_apps))                
                apps.append(('Python', python_apps))
                apps.append(('System', system_apps))
            except: pass

        return apps
    