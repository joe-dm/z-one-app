from PySide6 import QtWidgets, QtCore
from ui.common.element import LabelWidgetTitle

class TableSingleColumn(QtWidgets.QWidget):
    def __init__(self, title):
        super().__init__()

        title_label = LabelWidgetTitle(title)
        
        self.widget_layout = QtWidgets.QVBoxLayout(self)
        self.widget_layout.setContentsMargins(0,0,0,0)
        self.widget_layout.setSpacing(3)
        self.widget_layout.addWidget(title_label)

    def set_data(self, data):
        for value in data:
            text_edit = QtWidgets.QTextEdit(objectName='FancyTableTextEdit')
            text_edit.setText(value)
            text_edit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
            text_edit.setFixedHeight(30)
            text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            text_edit.setReadOnly(True)
            self.widget_layout.addWidget(text_edit)
            

class TableForm(QtWidgets.QWidget):
    def __init__(self, title):
        super().__init__()        

        title_label = LabelWidgetTitle(title)
        self.text_edits = []

        self.widget_layout = QtWidgets.QGridLayout(self)        
        self.widget_layout.setContentsMargins(0,0,0,0)
        self.widget_layout.setSpacing(3)
        self.widget_layout.addWidget(title_label, 0, 0, 1, 2)        
    
    def set_data(self, data):
        for row, item in enumerate(data):
            description, value = item

            if value != None and value != '':
                label = QtWidgets.QLabel(description, objectName='FancyTableLabel')
                label.setMinimumWidth(100)
                label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                text_edit = QtWidgets.QTextEdit(objectName='FancyTableTextEdit')
                text_edit.setText(str(value))
                text_edit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
                text_edit.setFixedHeight(30)
                text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                text_edit.setReadOnly(True)             
                self.text_edits.append(text_edit)

                self.widget_layout.addWidget(label, row + 1, 0)
                self.widget_layout.addWidget(text_edit, row + 1, 1)
    
    def update_data(self, data):
        for row, item in enumerate(data):
            description, value = item
            if row < len(self.text_edits):
                text_edit = self.text_edits[row]
                text_edit.setText(str(value))

    def clear_data(self):
        for text_edit in reversed(self.text_edits):            
            text_edit.clear()
            text_edit.setText('n/a')