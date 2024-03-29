from PySide6 import QtWidgets, QtGui

from config.theme import ThemeColor
from utils.log import Log, LogFlag, LogHandler


class Console(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit = QtWidgets.QTextEdit(objectName='Console')
        self.vertical_scrollbar = self.text_edit.verticalScrollBar()
        
        self.previous_scroll_value = self.vertical_scrollbar.value() 
        self.auto_scroll = True

        self.init_ui()
        
        LogHandler.set_gui_console(self)

    def init_ui(self):
        # setup layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.text_edit)      

        # connect scroll event
        self.vertical_scrollbar.valueChanged.connect(self.scrollbar_value_changed)         

        # text edit properties
        self.text_edit.setReadOnly(True)
        self.text_edit.setWordWrapMode(QtGui.QTextOption.NoWrap) 

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
        
        self.scroll_to_bottom()
    
    def scroll_to_bottom(self):
        if self.auto_scroll:
            self.text_edit.ensureCursorVisible()
            self.vertical_scrollbar.setValue(self.vertical_scrollbar.maximum())                 
            
    def scrollbar_value_changed(self, value):
        if value < self.previous_scroll_value:
            self.auto_scroll = False
        elif value >= self.vertical_scrollbar.maximum() - 50:
            self.auto_scroll = True
            self.previous_scroll_value = self.vertical_scrollbar.maximum()
        self.previous_scroll_value = value   

    def get_color(self, flag):
        color = ThemeColor.white_2

        if flag == LogFlag.operation:
            color = ThemeColor.secondary   
        elif flag == LogFlag.info:
            color = ThemeColor.white
        elif flag == LogFlag.warning:
            color = ThemeColor.yellow
        elif flag == LogFlag.error or flag == LogFlag.critical:
            color = ThemeColor.red
        elif flag == LogFlag.debug:
            color = ThemeColor.gray
        elif flag == LogFlag.no_flag:
            color = ThemeColor.primary
        return color 

