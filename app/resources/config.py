import os

class AppConfig:    
    name = 'z-one'
    version = '1.0.2305'
    dev_info = 'github.com/joe-dm'
    description = f'{name} {version} ({dev_info})'
    debug = False

class PathConfig:
    stylesheet = os.path.join('app', 'resources', 'breeze_style', 'style.qss')    
    icons_directory = os.path.join('app', 'resources', 'images', 'icons')
    icon_dashboard = os.path.join(icons_directory, 'dashboard.svg')
    icon_processor = os.path.join(icons_directory, 'cpu.svg')
    icon_gpu = os.path.join(icons_directory, 'gpu.svg')
    icon_memory = os.path.join(icons_directory, 'ram.svg')
    icon_disk = os.path.join(icons_directory, 'hdd.svg')
    icon_network = os.path.join(icons_directory, 'network.svg')
    icon_apps = os.path.join(icons_directory, 'box.svg')
    icon_settings = os.path.join(icons_directory, 'cogwheel.svg')
    icon_logs = os.path.join(icons_directory, 'file.svg')