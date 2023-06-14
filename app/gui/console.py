from PySide6 import QtWidgets, QtGui

from utils.theme import ThemeStylesheet, ThemeColor
from utils.log import Log, LogFlag, LogHandler

class Console(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit = QtWidgets.QTextEdit()
        self.vertical_scrollbar = self.text_edit.verticalScrollBar()
        self.auto_scroll = True

        self.init_ui()
        
        LogHandler.set_gui_console(self)

    def init_ui(self):
        # setup layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.text_edit)
        
        # disable text wrapping
        self.text_edit.setWordWrapMode(QtGui.QTextOption.NoWrap)
        # set stylesheet
        self.text_edit.setStyleSheet(ThemeStylesheet.console)

        Log.debug_init(self)
        

    def append(self, message, flag):
        # get cursor position
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)

        # create message and append
        full_message = f"{flag}{message}".replace('\n', '<br>')
        full_message = full_message.replace(" ", "&nbsp;")
        cursor.insertHtml(f"<span style='color: {self.get_color(flag)};'>{full_message}</span>")
        cursor.insertText('\n')       

        # scroll to bottom if user hasn't scrolled up
        if self.vertical_scrollbar.value() >= self.vertical_scrollbar.maximum() - 50:
            if self.auto_scroll:
                self.scroll_to_bottom()
    
    def scroll_to_bottom(self):
        self.vertical_scrollbar.setValue(self.vertical_scrollbar.maximum())

    def get_color(self, flag):
        color = ThemeColor.white

        if flag == LogFlag.task:
            color = ThemeColor.secondary
        elif flag == LogFlag.warning:
            color = ThemeColor.yellow
        elif flag == LogFlag.error or flag == LogFlag.critical:
            color = ThemeColor.red
        elif flag == LogFlag.debug:
            color = ThemeColor.gray
        elif flag == LogFlag.no_flag:
            color = ThemeColor.primary
        return color 
