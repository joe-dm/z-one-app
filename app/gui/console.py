import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets

from resources.config import AppConfig, ThemeConfig
from util.logger import Logger

class Console(QtWidgets.QWidget):
    last_used_color = None

    def __init__(self):
        super().__init__()          
        
        self.text_edit = QtWidgets.QTextEdit()
        self.text_color = ThemeConfig.Color.white

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

        Logger.log_init(self)

    def append(self, message, flag):
        if AppConfig.debug==False and (flag=='debug' or flag=='debug child'):
            pass
        else:
            full_message = f"{ThemeConfig.console_flags.get(flag.strip(), '')}{message}"
            # Replace spaces with non-breaking spaces
            full_message = full_message.replace(" ", "&nbsp;")
            
            # Set message color        
            if flag == 'operation':
                self.text_color = ThemeConfig.Color.secondary
            elif flag == 'debug' or flag == 'debug child':
                self.text_color = ThemeConfig.Color.gray_dark
            elif flag == 'warning':
                self.text_color = ThemeConfig.Color.yellow
            elif flag == 'error':
                self.text_color = ThemeConfig.Color.red
            elif flag == 'child':
                self.text_color == Console.last_used_color
            else:
                self.text_color = ThemeConfig.Color.white
            Console.last_used_color = self.text_color

            # Get current cursor position
            cursor = self.text_edit.textCursor()
            cursor.movePosition(QtGui.QTextCursor.End)

            # Insert the message with the desired color
            cursor.insertHtml(f"<span style='color: {self.text_color};'>{full_message}</span>")
            self.text_edit.setTextCursor(cursor)

            # Move to the next line
            cursor.insertText("\n")

            # Scroll to the bottom and ensure cursor visibility
            self.text_edit.ensureCursorVisible()

            scroll_bar = self.text_edit.horizontalScrollBar()
            scroll_bar.setSliderPosition(scroll_bar.minimum())    