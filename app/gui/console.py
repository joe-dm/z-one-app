from PySide6 import QtGui, QtWidgets

from resources.config import ThemeConfig
from utils.log import Log, Flag

class Console(QtWidgets.QWidget):    

    def __init__(self):
        super().__init__()          
        
        self.text_edit = QtWidgets.QTextEdit()
        self.vertical_scroll_bar = self.text_edit.verticalScrollBar()
        self.horizontal_scroll_bar = self.text_edit.horizontalScrollBar()        
        
        self.auto_scroll = True

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

        #self.vertical_scroll_bar.valueChanged.connect(self.on_sidebar_value_changed)

        Log.debug_init(self)


    def append(self, message, flag):
        # create full message       
        full_message = f"{flag}{message}".replace(" ", "&nbsp;")

        # get cursor position
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)        

        # insert message and new line
        cursor.insertHtml(f"<span style='color: {self.get_color(flag)};'>&nbsp;{full_message}</span>")
        cursor.insertText("\n")

        #if self.vertical_scroll_bar.value() >= self.vertical_scroll_bar.maximum() - 50:
        #if self.auto_scroll:
        #    self.scroll_to_bottom()
        

    #def scroll_to_bottom(self):
    #    self.vertical_scroll_bar.setValue(self.vertical_scroll_bar.maximum())

    #def on_sidebar_value_changed(self, value):
    #    # Check if the user has manually scrolled up
    #    if value >= self.vertical_scroll_bar.maximum() - 50:
    #        self.auto_scroll = False
        
    
    def get_color(self, flag):
        color = ThemeConfig.Color.white

        if flag == Flag.task:
            color = ThemeConfig.Color.secondary
        elif flag == Flag.warning:
            color = ThemeConfig.Color.yellow
        elif flag == Flag.error:
            color = ThemeConfig.Color.red
        elif flag == Flag.debug:
            color = ThemeConfig.Color.gray_dark
        elif flag == Flag.none:
            color = ThemeConfig.Color.primary
        
        return color
