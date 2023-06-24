from PySide6 import QtCharts, QtCore, QtGui, QtWidgets
import PySide6.QtGui

from config.theme import ThemeColor
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
        
        
class Chart(QtWidgets.QWidget):
    def __init__(self, get_value_func, y_axis_max=None, title=None, unit='%'):
        super().__init__() 
        # value to be updated/tracked
        self.get_value_func = get_value_func
        
        self.y_axis_max = y_axis_max
        self.unit = unit

        # determine if the y axis has a fixed max value
        self.has_fixed_y_axis = None
        if self.y_axis_max: 
            self.has_fixed_y_axis = True            
        else: 
            self.has_fixed_y_axis = False
            self.y_axis_max = 0
        
        # chart title and max labels
        #self.title_label = QtWidgets.QLabel(objectName='GraphTitle')
        #self.max_label = QtWidgets.QLabel(f"{y_axis_max} {unit}", objectName='GraphMax')

        # widget properties
        self.setMaximumHeight(119)        

        # x axis
        self.x_axis = QtCharts.QValueAxis()        
        self.x_axis.setRange(0, 60)
        self.x_axis.setTickCount(9)
        self.x_axis.setLabelsVisible(False)
        self.x_axis.setLineVisible(False)
        self.x_axis.setGridLineVisible(True)
        self.x_axis.setGridLineColor(QtGui.QColor(ThemeColor.gray_2)) 
        # y axis
        self.y_axis = QtCharts.QValueAxis()
        if self.has_fixed_y_axis:
            self.y_axis.setRange(0, y_axis_max)          
        self.y_axis.setTickCount(5)    
        self.y_axis.setLabelsVisible(False)
        self.y_axis.setLineVisible(False)
        self.y_axis.setGridLineVisible(True)
        self.y_axis.setGridLineColor(QtGui.QColor(ThemeColor.gray_2))

        # bottom line series
        self.line_series_bottom = QtCharts.QLineSeries()
        self.line_series_bottom.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        # top line series
        self.line_series_top = QtCharts.QLineSeries()
        self.line_series_top.setPen(QtGui.QPen(QtCore.Qt.NoPen)) 
        # area series effect
        self.area_series_effect = QtCharts.QAreaSeries(self.line_series_bottom, self.line_series_top)        
        area_series_color = QtGui.QColor(ThemeColor.white_2)                
        area_series_color.setAlpha(100)
        area_brush = QtGui.QBrush(area_series_color)
        self.area_series_effect.setBrush(area_brush)
        area_pen = QtGui.QPen(QtGui.QColor(ThemeColor.secondary))
        area_pen.setWidth(1)
        self.area_series_effect.setPen(area_pen)         

        # chart 
        self.my_chart = QtCharts.QChart() 
        self.my_chart.setMargins(QtCore.QMargins(0, 0, 0, 0))  
        self.my_chart.layout().setContentsMargins(0,0,0,0)      
        self.my_chart.setBackgroundRoundness(0)
        self.my_chart.addSeries(self.area_series_effect)
        self.my_chart.addAxis(self.x_axis, QtCore.Qt.AlignBottom)
        self.my_chart.addAxis(self.y_axis, QtCore.Qt.AlignRight)
        self.my_chart.setBackgroundBrush(QtCore.Qt.transparent)
        self.my_chart.legend().hide()

        # attach axis
        self.area_series_effect.attachAxis(self.x_axis)
        self.area_series_effect.attachAxis(self.y_axis)        

        # setup chart view
        self.chart_view = QtCharts.QChartView()
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chart_view.setChart(self.my_chart)  

        
        # setup layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0) 
        if title: 
            self.title_label = LabelWidgetTitle(title)            
            layout.addWidget(self.title_label)
            #if self.y_axis_max:
            #    layout.addWidget(self.max_label)
            layout.addWidget(self.chart_view) 
        else:
            layout.addWidget(self.chart_view) 

        # usage graph timer
        self.graph_timer = QtCore.QTimer()
        self.graph_timer.timeout.connect(self.update_graph)
        self.graph_timer.start(100)  
        self.time_counter = 0 

        self.data_point_counter = 0
    
    def update_graph(self): 
        value = self.get_value_func()        

        if value:
            # add the value to the graph
            self.line_series_bottom.append(QtCore.QPointF(self.time_counter / 10, 0))
            self.line_series_top.append(QtCore.QPointF(self.time_counter / 10, value))
            self.time_counter += 1

            # remove the oldest data point if the x-axis range exceeds 60 seconds
            if self.time_counter > 600:
                self.line_series_bottom.remove(0)
                self.line_series_top.remove(0)

            # Update the chart's x-axis range to keep only the last 60 seconds in view
            self.x_axis.setRange((self.time_counter - 600) / 10, self.time_counter / 10)

            # Update the y-axis range based on the maximum value encountered
            if (not self.has_fixed_y_axis) and (value > self.y_axis_max):
                self.y_axis_max = value
                self.y_axis.setRange(0, self.y_axis_max)

            # Redraw the chart
            self.repaint()