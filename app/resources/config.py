class AppConfig():
    def name(): return 'z-one'
    def version(): return '1.0.2304'
    def dev_info(): return 'github.com/joe-dm'
    def description(): return f'{AppConfig.name()} v{AppConfig.version()} ({AppConfig.dev_info()})'
    def debug(): return True


class PathConfig():
    def log_file():   return 'z-one.log'
    def log_folder(): return 'logs'    
    def stylesheet(): return './app/resources/style_dark.qss'
    def images(): return      './app/resources/img/'

class ThemeConfig():    
    console_flags = {
        'info':    '[i]: ',
        'error':   '[E]: ',
        'warning': '[!]: ',
        'trying':  '[~]: ',
        'debug':   '[#]: ',
        'default': '[ ]: ',
        'child':   '     ',
        'none':    ''} 

    # colors
    def color_primary(): return     '#2596be'
    def color_black(): return       '#1d2022'
    def color_black_dark(): return  '#191919'
    def color_grey_light(): return  '#cccccc'    
    
    # logo 
    def logo(): return f"{PathConfig.images()}logo.png"
    # icons
    def icon_default(): return f"{PathConfig.images()}ico_default.png"    

    # fonts
    def font_console_name(): return  'Courier New'
    def font_console_size(): return  10    
    def font_title_size(): return    15

    