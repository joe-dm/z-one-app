import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets

from resources.config import ThemeConfig
from util.logger import Logger

class Console(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()          
        
        self.text_edit = QtWidgets.QTextEdit()

        self.setup_ui()
        Logger.set_gui_console(self)

    def setup_ui(self):       
        # setup layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.text_edit)

        # set font
        font = QtGui.QFont(ThemeConfig.font_console_name(), ThemeConfig.font_console_size())
        self.text_edit.setFont(font)
        # Disable text wrapping
        self.text_edit.setWordWrapMode(QtGui.QTextOption.NoWrap)
        # set background color
        self.text_edit.setStyleSheet(f"background-color: {ThemeConfig.color_black_dark()}; border: none;")
        # disable editing
        self.text_edit.setReadOnly(True)


    def append(self, message):
        self.text_edit.append(message)
        self.text_edit.ensureCursorVisible()
        
        scroll_bar = self.text_edit.horizontalScrollBar()
        scroll_bar.setSliderPosition(scroll_bar.minimum())