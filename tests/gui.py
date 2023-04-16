import sys
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets


class App(QtWidgets.QApplication):
    def __init__(self):
        # initialize QApplication
        super(App, self).__init__(sys.argv)
        # create main window
        self._window = Window()
        # setup the ui
        self.setup_ui()

    def setup_ui(self):
        # load and set stylesheet
        pass
        
    def exit(self): 
        # exit the application
        self.exec()

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        # initialize QMainWindow
        super(Window, self).__init__()        
        # setup the ui
        self.setup_ui()
                

    def setup_ui(self):
        # window title
        self.setWindowTitle(f'Test 123')        
        # window size                
        self.setMinimumSize(420, 450)        
        self.setMaximumSize(420, 450)         
        # show the window
        self.show()

if __name__ == "__main__":
    app = App()
    app.exit()
