import os

class AppConfig:    
    name = 'z-one'
    version = '1.0.2306'
    dev_info = 'github.com/joe-dm'
    description = f'{name} {version} ({dev_info})'
    debug = True
        

class PathConfig:
    stylesheet = os.path.join('app', 'resources', 'breeze_style', 'style.qss')    
    logo = os.path.join('app', 'resources', 'images', 'logo.png')
    logo_text = os.path.join('app', 'resources', 'images', 'logo-text.png')

    # sounds
    sounds_directory = os.path.join('app', 'resources', 'sounds')

    sound_internet_down = os.path.join(sounds_directory, 'internet_down.wav')
    sound_internet_restored = os.path.join(sounds_directory, 'internet_restored.wav')

    # icons
    icons_directory = os.path.join('app', 'resources', 'images', 'icons')

    icon_dashboard = os.path.join(icons_directory, 'dashboard.svg')
    icon_dashboard_active = os.path.join(icons_directory, 'dashboard_dark.svg')

    icon_processor = os.path.join(icons_directory, 'cpu.svg')
    icon_processor_active = os.path.join(icons_directory, 'cpu_dark.svg')

    icon_gpu = os.path.join(icons_directory, 'gpu.svg')
    icon_gpu_active = os.path.join(icons_directory, 'gpu_dark.svg')

    icon_memory = os.path.join(icons_directory, 'ram.svg')
    icon_memory_active = os.path.join(icons_directory, 'ram_dark.svg')

    icon_disk = os.path.join(icons_directory, 'hdd.svg')
    icon_disk_active = os.path.join(icons_directory, 'hdd_dark.svg')

    icon_network = os.path.join(icons_directory, 'network.svg')
    icon_network_active = os.path.join(icons_directory, 'network_dark.svg')

    icon_apps = os.path.join(icons_directory, 'box.svg')
    icon_apps_active = os.path.join(icons_directory, 'box_dark.svg')

    icon_settings = os.path.join(icons_directory, 'cogwheel.svg')
    icon_settings_active = os.path.join(icons_directory, 'cogwheel_dark.svg')

    icon_logs = os.path.join(icons_directory, 'file.svg')
    icon_logs_active = os.path.join(icons_directory, 'file_dark.svg')