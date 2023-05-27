from PySide6 import QtGui, QtWidgets

from resources.config import AppConfig, ThemeConfig
from utils.log import Log

class Console(QtWidgets.QWidget):
    last_used_color = None

    def __init__(self):
        super().__init__()          
        
        self.text_edit = QtWidgets.QTextEdit()
        self.text_color = ThemeConfig.Color.white

        self.setup_ui()
        Log.set_gui_console(self)

    def setup_ui(self):       
        # setup layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.text_edit)

        # set font
        font = QtGui.QFont(ThemeConfig.Font.family_monospace, ThemeConfig.Font.size_small)
        self.text_edit.setFont(font)
        # disable text wrapping
        self.text_edit.setWordWrapMode(QtGui.QTextOption.NoWrap)
        # set colors
        self.text_edit.setStyleSheet(
            f"background-color: {ThemeConfig.Color.black_dark}; border: none;")
        # disable editing
        self.text_edit.setReadOnly(True)

        Log.debug_init(self)

    def append(self,message, flag):
        # create full message
        full_message = f"{flag}{message}".replace(" ", "&nbsp;")

        # get cursor position
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)

        # insert message and new line
        cursor.insertHtml(f"<span>{full_message}</span>")
        cursor.insertText("\n")

        # scroll to the bottom
        self.text_edit.ensureCursorVisible()
        # scroll left
        scroll_bar = self.text_edit.horizontalScrollBar()
        scroll_bar.setSliderPosition(scroll_bar.minimum())