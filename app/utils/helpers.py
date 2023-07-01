from datetime import datetime

from PySide6 import QtCore, QtMultimedia


class SoundAlert:
    sound_obj = QtCore.QObject()   

    def play(path_to_wav):
        sound_effect = QtMultimedia.QSoundEffect(SoundAlert.sound_obj)
        sound_effect.setSource(QtCore.QUrl.fromLocalFile(path_to_wav))
        sound_effect.setVolume(1.0)        
        sound_effect.play() 

class Convert:
    def timestamp_to_date(timestamp, format="%Y-%m-%d %H:%M"):
        date = datetime.fromtimestamp(timestamp)
        date = date.strftime(format)
        return date
    
    def mhz_to_ghz(mhz):
        ghz = mhz / 1000
        ghz = round(ghz, 1)
        return ghz

    def bytes_to_unit(bytes_value):
        units = ['B', 'KB', 'MB', 'GB', 'TB']
        unit_index = 0
        while bytes_value >= 1024 and unit_index < len(units) - 1:
            bytes_value /= 1024
            unit_index += 1
        return f"{int(bytes_value)} {units[unit_index]}"

    


        



