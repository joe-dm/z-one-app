from PySide6 import QtWidgets, QtCore
from ui.common.element import LabelWidgetTitle

class TableForm(QtWidgets.QWidget):
    def __init__(self, title):
        super().__init__()

        self.widget_layout = QtWidgets.QGridLayout(self)        
        self.widget_layout.setContentsMargins(0,0,0,0)
        self.widget_layout.setSpacing(3)

        title_label = LabelWidgetTitle(title)
        self.widget_layout.addWidget(title_label, 0, 0, 1, 2)        
    
    def set_data(self, data):
        for row, item in enumerate(data):
            description, value = item
            label = QtWidgets.QLabel(description, objectName='FancyTableLabel')
            label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

            text_edit = QtWidgets.QTextEdit(str(value), objectName='FancyTableTextEdit')
            text_edit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
            text_edit.setFixedHeight(30)
            text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            text_edit.setReadOnly(True) 

            self.widget_layout.addWidget(label, row + 1, 0)
            self.widget_layout.addWidget(text_edit, row + 1, 1)