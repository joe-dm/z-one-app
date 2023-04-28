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
    def hardware():
        return [
            ('Processor', 'Intel Core i7'),
            ('Memory', '16 GB'),
            ('Storage', '1 TB SSD'),
            ('Graphics', 'NVIDIA GeForce RTX 3080'),
            ('Display', '27 inch 4K monitor'),
            ('Motherboard', 'ASUS Prime H310M-E R2.0')]
        
    
    def operating_system():
        return [
            ('OS Name', 'Windows 10'),
            ('OS Architecture', '64-bit'),
            ('User Name', 'John Doe'),
            ('Install Date', '04/15/2023'),
            ('OS Version', '10.0.19042'),
            ('OS Release', '21H1'),
            ('Build Number', '19042.1234'),
            ('Product ID', 'XXXXX-XXXXX-XXXXX-XXXXX-XXXXX')]