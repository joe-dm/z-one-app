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
        'info':     '[i]: ',
        'error':    '[E]: ERROR! ',
        'warning':  '[!]: WARNING! ',
        'operation':'[~]: ',
        'debug':    '[#]: ',
        'default':  '[ ]: ',
        'none':     ''} 

    class Color:
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
        arrow_left =f"{PathConfig.images}ico_arrow_left.png"    
        arrow_right=f"{PathConfig.images}ico_arrow_right.png"   

    class Font:
        monospace = 'Courier New'
        
        size_title = 15
        size_logo  = 12
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

    