from PySide6 import QtCore, QtMultimedia

class SoundAlert:
    sound_obj = QtCore.QObject()   

    def play(path_to_wav):
        sound_effect = QtMultimedia.QSoundEffect(SoundAlert.sound_obj)
        sound_effect.setSource(QtCore.QUrl.fromLocalFile(path_to_wav))
        sound_effect.setVolume(1.0)        
        sound_effect.play() 