from PySide6 import QtGui, QtWidgets

from resources.config import ThemeConfig
from utils.log import Log

class Console(QtWidgets.QWidget):    

    def __init__(self):
        super().__init__()          
        
        self.text_edit = QtWidgets.QTextEdit()
        self.vertical_scroll_bar = self.text_edit.verticalScrollBar()
        self.horizontal_scroll_bar = self.text_edit.horizontalScrollBar()        

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

    def append(self, message, flag):
        # create full message
        full_message = f"{flag}{message}".replace(" ", "&nbsp;")

        # get cursor position
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)        

        # insert message and new line
        cursor.insertHtml(f"<span>{full_message}</span>")
        cursor.insertText("\n")

        if self.vertical_scroll_bar.value() > self.vertical_scroll_bar.maximum() - 50:
            self.vertical_scroll_bar.setValue(self.vertical_scroll_bar.maximum())
