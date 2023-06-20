import os

class LogFlag:
    default  = '•| '
    info     = 'i| '
    
    warning  = '!| '
    error    = '×| '
    critical = '✖| '

    task     = '»| '    

    debug    = '#| '  
    none     = ''   

class LogFile:
    default = os.path.join('logs', 'z-one.log')
    network = os.path.join('logs', 'network.log')
        
    log_directory = os.path.join('logs')
    def check_dir():
        if not os.path.exists(LogFile.log_directory): 
            os.makedirs(LogFile.log_directory) 

class Log:
    def write(message, flag=LogFlag.default, file=LogFile.default):
        print(f"{flag}{message}")
        

