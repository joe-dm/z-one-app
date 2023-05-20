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
        font = QtGui.QFont(ThemeConfig.Font.monospace, ThemeConfig.Font.size_small)
        self.text_edit.setFont(font)
        # Disable text wrapping
        self.text_edit.setWordWrapMode(QtGui.QTextOption.NoWrap)
        # set colors
        self.text_edit.setStyleSheet(
            f"background-color: {ThemeConfig.Color.black_dark}; border: none;")
        # disable editing
        self.text_edit.setReadOnly(True)

    def append(self, message, flag):
        full_message = f"{ThemeConfig.console_flags.get(flag, '')}{message}"

        # Set message color
        color = ThemeConfig.Color.white
        if flag == 'operation':
            color = ThemeConfig.Color.secondary
        elif flag == 'debug':
            color = ThemeConfig.Color.gray_dark
        elif flag == 'warning':
            color = ThemeConfig.Color.yellow
        elif flag == 'error':
            color = ThemeConfig.Color.red

        # Get current cursor position
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)

        # Insert the message with the desired color
        cursor.insertHtml(f"<span style='color: {color};'>{full_message}</span>")
        self.text_edit.setTextCursor(cursor)

        # Move to the next line
        cursor.insertText("\n")

        # Scroll to the bottom and ensure cursor visibility
        self.text_edit.ensureCursorVisible()

        scroll_bar = self.text_edit.horizontalScrollBar()
        scroll_bar.setSliderPosition(scroll_bar.minimum())


    def append_old(self, message, flag):
        full_message = f"{ThemeConfig.console_flags.get(flag, '')}{message}"

        # set message color
        color = ThemeConfig.Color.white
        if flag == 'debug':
            color = ThemeConfig.Color.green                    
        self.text_edit.setStyleSheet(f"color: {color};")

        self.text_edit.append(full_message)
        self.text_edit.ensureCursorVisible()
        
        scroll_bar = self.text_edit.horizontalScrollBar()
        scroll_bar.setSliderPosition(scroll_bar.minimum())