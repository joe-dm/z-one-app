class AppConfig():
    def name(): return 'z-one'
    def version(): return '1.0.2304'
    def dev_info(): return 'github.com/joe-dm'
    def description(): 
        return f'{AppConfig.name()} v{AppConfig.version()} ({AppConfig.dev_info()})'
    def debug(): return True

class ConsoleConfig():
    flags = {
        'info':    '[i]: ',
        'error':   '[E]: ',
        'warning': '[!]: ',
        'trying':  '[~]: ',
        'debug':   '[#]: ',
        'default': '[ ]: ',
        'child':   '     ',
        'none':    ''} 

class PathConfig():
    icons = {
        'default':  './app/resources/img/ico_default.png',
        'settings': './app/resources/img/ico_settings.png',}

    def log_file():   return 'z-one.log'
    def log_folder(): return 'logs'
    
    def stylesheet(): 
        return './app/resources/style_dark.qss'

class ThemeConfig():    
    colors = {
        'black':        '#1d2022',
        'black-dark':   '#191919',
        'grey-light':   '#cccccc',
        'blue':         '#2596be',}  

    def get_color(name): return ThemeConfig.colors.get(name)
    def get_icon_path(name): return PathConfig.icons.get(name)

