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

class Log:
    def write(message, flag=LogFlag.default, file=LogFile.default):
        print(message)
        

