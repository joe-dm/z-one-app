import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets

from resources.config import ThemeConfig

class ButtonWithIcon(QtWidgets.QWidget):
    def __init__(self, text, icon_path):
        super().__init__()

        self.text = text
        self.icon_path = icon_path

        self.button_icon = QtWidgets.QPushButton()
        self.button_text = QtWidgets.QPushButton()

        self.setup_ui()

    def setup_ui(self):
        # button icon properties
        self.button_icon.setIcon(QtGui.QIcon(self.icon_path))
        self.button_icon.setFixedWidth(30)

        # button text properties
        self.button_text.setText(self.text)
        self.button_text.setStyleSheet("text-align: left;")

        # setup layout and add widgets to it
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(1)
        layout.addWidget(self.button_icon)
        layout.addWidget(self.button_text)

        # setup enter/leave events
        self.button_icon.enterEvent = self.on_enter_event
        self.button_icon.leaveEvent = self.on_leave_event
        self.button_text.enterEvent = self.on_enter_event
        self.button_text.leaveEvent = self.on_leave_event
        
    
    def on_enter_event(self, event):
        self.setStyleSheet(f"border: 1px solid {ThemeConfig.color_primary()};")
    def on_leave_event(self, event):
        self.setStyleSheet("")



class LabelTitle(QtWidgets.QLabel):
    def __init__(self, text):
        super().__init__()
        self.page_name = text
        self.setup_ui()

    def setup_ui(self):
        self.setText(self.page_name)
        self.setStyleSheet(f"color: {ThemeConfig.color_grey_light()};")

        font = QtGui.QFont()
        font.setPointSize(ThemeConfig.font_title_size())
        self.setFont(font)


class SeparatorHLine(QtWidgets.QFrame):
    def __init__(self, color=None, visible=True):
        super().__init__()
        self.color = color
        self.visible = visible
        self.init_ui()

    def init_ui(self):
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setEnabled(False)

        if self.visible == False:
            self.setFixedHeight(0)
        
        if self.color is not None:
            self.setStyleSheet(f"border-color: {self.color};")


