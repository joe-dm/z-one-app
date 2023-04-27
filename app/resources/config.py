class AppConfig():        
    def name(): return 'z-one'
    def version(): return '1.0.2304'
    def dev_info(): return 'github.com/joe-dm'
    def description(): 
        return f'{AppConfig.name()} v{AppConfig.version()} ({AppConfig.dev_info()})'
    def debug(): return True

class ThemeConfig():
    def path_to_stylesheet(): return './app/resources/style_dark.qss'   

class TestData():
    def system_info():
        return [
            ('Processor', f'Intel Core i5'),
            ('Memory', f'8 GB'),
            ('Storage', f'500 GB'),
            ('Graphics', f'NVIDIA GeForce'),
            ('Operating System', f'Windows 10')] 