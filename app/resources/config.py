import os

class AppConfig:    
    name = 'z-one'
    version = '1.0.2304'
    dev_info = 'github.com/joe-dm'
    description = f'{name} {version} ({dev_info})'
    debug = True


class PathConfig:
    log_file = 'z-one.log'
    log_folder = 'logs'  

    stylesheet = './app/resources/style_dark.qss'
    images = './app/resources/img/'


class ThemeConfig:
    console_flags = {
        'info':    '[i]: ',
        'error':   '[E]: ',
        'warning': '[!]: ',
        'trying':  '[~]: ',
        'debug':   '[#]: ',
        'default': '[ ]: ',
        'child':   '     ',
        'none':    ''} 

    class Color:
        primary =   '#2596be'
        secondary = '#ff8400'

        black =     '#1d2022'
        black_dark ='#191919'

        grey_light ='#cccccc' 

    class Icon:
        logo =      f"{PathConfig.images}logo.png"
        default =   f"{PathConfig.images}ico_default.png"
        dashboard = f"{PathConfig.images}ico_dashboard.png"
        cpu =       f"{PathConfig.images}ico_cpu.png"
        gpu =       f"{PathConfig.images}ico_gpu.png"
        ram =       f"{PathConfig.images}ico_ram.png"
        disk =      f"{PathConfig.images}ico_disk.png"
        network =   f"{PathConfig.images}ico_network.png"
        apps =      f"{PathConfig.images}ico_apps.png"
        settings =  f"{PathConfig.images}ico_settings.png"
        logs =      f"{PathConfig.images}ico_logs.png"    

    class Font:
        monospace = 'Courier New'
        
        size_title = 15
        size_logo  = 12
        size_small = 9     