from PySide6 import QtWidgets

from gui.common.elements import LabelWidgetTitle


class Table(QtWidgets.QWidget):
    def __init__(self, data, title=None):
        super().__init__()   
        
        # create table and set num of rows and cols
        self.table = QtWidgets.QTableWidget(objectName='Table')
        num_rows = len(data)
        num_cols = max(len(row) for row in data)
        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols)        

        # disable headers
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)

        # populate table with data        
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value)) 
                self.table.setItem(row, col, item)     
        
        # resize first column to fit contents
        self.table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # stretch last column to fill remaining space
        self.table.horizontalHeader().setStretchLastSection(True)
        # adjust table height
        table_height = sum([self.table.rowHeight(row) for row in range(num_rows)])        
        self.table.setFixedHeight(table_height)         
        # disable editing
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # disable cell selection        
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)        
        # enable alternating colors
        self.table.setAlternatingRowColors(True)
               
        # setup layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        # add title 
        if title:
            title_label = LabelWidgetTitle(title)
            layout.addWidget(title_label)            
        layout.addWidget(self.table)          