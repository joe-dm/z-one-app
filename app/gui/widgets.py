import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets


class ButtonSidebar(QtWidgets.QPushButton):
    def __init__(self, text):
        super().__init__()  
        self.text = text
        self.setup_ui()

    def setup_ui(self):
        self.setText(self.text)


class PageTitle(QtWidgets.QLabel):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.setup_ui()

    def setup_ui(self):
        self.setText(self.text)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.setFont(font)
        self.setStyleSheet('color: #cccccc;')


class SeparatorHLine(QtWidgets.QFrame):
    def __init__(self, visible=True, color=None):
        super().__init__()  
        self.visible = visible
        self.color = color
        self.setup_ui()

    def setup_ui(self):
        if self.visible == False: 
            self.setFixedHeight(0)        

        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)               

        if self.color is not None:
            self.setStyleSheet(f"border-color: {self.color};")

        self.setEnabled(False)


class TableWithTitle(QtWidgets.QWidget):
    def __init__(self, title, data):
        super().__init__()
        self.title = title
        self.data = data
        self.setup_ui()

    def setup_ui(self):
        # Create a QLabel widget for the title
        title_label = QtWidgets.QLabel(self.title)        
        title_label.setStyleSheet("font-weight: bold;")

        # Create a Table widget for the data
        table = Table(self.data)

        # Create a QVBoxLayout and add the title, separator, and table widgets
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(SeparatorHLine(color='#2596be'))
        layout.addWidget(table)

        self.setLayout(layout)



class Table(QtWidgets.QTableWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setup_ui()

    def setup_ui(self):
        # determine number of rows and columns
        num_rows = len(self.data)
        num_cols = max(len(row) for row in self.data)
        
        # set table size
        self.setRowCount(num_rows)
        self.setColumnCount(num_cols)

        # disable headers
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)

        # populate table
        for row, row_data in enumerate(self.data):
            for col, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))               
                self.setItem(row, col, item)
                

        # resize first column to fit contents
        self.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # stretch second column to fill remaining space
        self.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        # set size policy to expanding
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(size_policy)

        # disable cell selection
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        # disable hover color effect
        self.setStyleSheet("QTableWidget::item{background-color: transparent; qproperty-alignment: 'AlignLeft|AlignVCenter';}")
        # disable editing
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)       
        # disable vertical scrolling
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)        
        # adjust table height
        table_height = sum([self.rowHeight(row) for row in range(num_rows)])
        self.setFixedHeight(table_height)