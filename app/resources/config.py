import os

class AppConfig:
    debug = True

    class Info:
        name = 'z-one'
        version = '1.0.2305'
        dev_info = 'github.com/joe-dm'
        description = f'{name} {version} ({dev_info})'

    class Path:
        log_folder = os.path.join('logs')
        log_app = os.path.join(log_folder, 'z-one.log')    
        
        stylesheet = os.path.join('app', 'resources', 'style_dark.qss')
        images = os.path.join('app', 'resources', 'images')   



class ThemeConfig:
    class Color:
        # main colors
        primary =       '#ff8400'
        secondary =     '#7dd2ff'   
        secondary_dark ='#3daee9'  
        # traffic light
        green =         '#79ffb1'
        yellow =        '#fffd8a'
        red =           '#ff7d6c'
        # grayscale
        white =         '#ffffff'
        gray_light =    '#cccccc'
        gray_dark =     '#757575'
        black =         '#1d2022'
        black_dark =    '#191919'

        
    class Icon:
        _base_path = AppConfig.Path.images
    
        logo        = os.path.join(_base_path, 'logo.png')
        #icons
        default     = os.path.join(_base_path, 'ico_default.png')
        dashboard   = os.path.join(_base_path, 'ico_dashboard.png')
        cpu         = os.path.join(_base_path, 'ico_cpu.png')
        gpu         = os.path.join(_base_path, 'ico_gpu.png')
        ram         = os.path.join(_base_path, 'ico_ram.png')
        disk        = os.path.join(_base_path, 'ico_disk.png')
        network     = os.path.join(_base_path, 'ico_network.png')
        apps        = os.path.join(_base_path, 'ico_apps.png')
        settings    = os.path.join(_base_path, 'ico_settings.png')
        logs        = os.path.join(_base_path, 'ico_logs.png')
        arrow_left  = os.path.join(_base_path, 'ico_arrow_left.png')
        arrow_right = os.path.join(_base_path, 'ico_arrow_right.png')

    class Font:
        family_monospace = 'Courier New'
        
        size_large = 15
        size_medium= 12
        size_small = 10


class SampleData: 
    cpu_info = [
        ('CPU Model', 'Intel Core i7-8700K'),
        ('CPU Cores', '6'),
        ('CPU Threads', '12'),
        ('CPU Frequency', '3.7 GHz'),
        ('CPU Usage', '25%'),
        ('CPU Temperature', '65°C')]

    gpu_info = [
        ('GPU Model', 'NVIDIA GeForce RTX 2080 Ti'),
        ('GPU Memory', '11 GB'),
        ('GPU Clock', '1350 MHz'),
        ('GPU Temperature', '70°C'),
        ('GPU Usage', '75%')]

    disk_info = [
        ('Drive C:', 'SSD', '250 GB', '120 GB', '130 GB'),
        ('Drive D:', 'HDD', '2 TB', '500 GB', '1.5 TB'),
        ('Drive E:', 'SSD', '500 GB', '400 GB', '100 GB')]

    os_info = [
        ('OS Name', 'Windows 10'),
        ('OS Architecture', '64-bit'),
        ('User Name', 'John Doe'),
        ('Install Date', '04/15/2023'),
        ('OS Version', '10.0.19042'),
        ('OS Release', '21H1'),
        ('Build Number', '19042.1234'),
        ('Product ID', 'XXXXX-XXXXX-XXXXX-XXXXX-XXXXX')]

    