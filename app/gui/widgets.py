from PySide6 import QtGui, QtWidgets

from resources.config import ThemeConfig
from utils.log import Log

class TableWithTitle(QtWidgets.QWidget):
    def __init__(self, title, data):
        super().__init__()        
        # widgets
        self.table_title = QtWidgets.QLabel(title)        
        self.table = Table(data)
        self.setup_ui()

    def setup_ui(self):        
        # widget properties
        self.table_title.setStyleSheet("font-weight: bold;")           
  
        # Set size policy for the whole widget
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.setSizePolicy(size_policy)

        # create layout and add widgets
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.table_title)
        layout.addWidget(Separator(color=ThemeConfig.Color.primary))
        layout.addWidget(self.table)    
        self.setLayout(layout)

        Log.debug_init(self)
        

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

        # disable table headers
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)

        # populate table
        for row, row_data in enumerate(self.data):
            for col, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value)) 
                self.setItem(row, col, item)
        
        # resize first column to fit contents
        self.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # stretch last column to fill remaining space
        self.horizontalHeader().setStretchLastSection(True)
        # adjust table height
        table_height = sum([self.rowHeight(row) for row in range(num_rows)])
        self.setFixedHeight(table_height)

        # disable editing
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # disable cell selection        
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        # disable hover color effect
        self.setStyleSheet("QTableWidget::item{background-color: transparent; qproperty-alignment: 'AlignLeft|AlignVCenter';}")         


class PageTitle(QtWidgets.QLabel):
    def __init__(self, text):
        super().__init__()
        self.page_name = text
        self.setup_ui()

    def setup_ui(self):
        self.setText(self.page_name)
        #self.setStyleSheet(f"color: {ThemeConfig.Color.grey_light};")

        font = QtGui.QFont()
        font.setPointSize(ThemeConfig.Font.size_large)
        self.setFont(font)


class Separator(QtWidgets.QFrame):
    def __init__(self, color=None):
        super().__init__()   
        self.color = color     
        self.setup_ui()
    
    def setup_ui(self):
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setEnabled(False)     

        if self.color is not None:
            self.setStyleSheet(f"border-color: {self.color}")