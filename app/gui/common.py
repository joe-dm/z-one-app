from PySide6 import QtCharts, QtCore, QtGui, QtWidgets
from utils.theme import ThemeColor, ThemeStylesheet
from tools.info_gatherer import CPUInfo

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
        self.title_label = QtWidgets.QLabel(objectName='GraphTitle')
        self.max_label = QtWidgets.QLabel(f"{y_axis_max} {unit}", objectName='GraphMax')

        # widget properties
        self.setMaximumHeight(119)                
        self.setStyleSheet(ThemeStylesheet.chart)

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
        area_series_color = QtGui.QColor(ThemeColor.secondary)                
        area_series_color.setAlpha(180)
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
        layout = QtWidgets.QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0) # label widgets
        if title: 
            self.title_label.setText(title)
            layout.addWidget(self.title_label, 0, 0)
            if self.y_axis_max:
                layout.addWidget(self.max_label, 0, 1)
            layout.addWidget(self.chart_view, 1, 0, 1, 2) 
        else:
            layout.addWidget(self.chart_view, 0, 0, 1, 2) 

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

class HLine(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setStyleSheet(ThemeStylesheet.line_horizontal_1)

class Heading(QtWidgets.QLabel):
    def __init__(self, text=""):
        super().__init__()
        self.setText(text)     
        self.setStyleSheet(ThemeStylesheet.label_heading)






class CPUMonitor(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setMaximumHeight(150)        
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)        

        # create the chart view         
        
        #self.chart_view.setContentsMargins(0, 0, 0, 0)
          
        
        #self.frequency_label = QtWidgets.QLabel()
        #self.frequency_label.setStyleSheet(ThemeStylesheet.widget_label_large)
        #layout.addWidget(self.frequency_label)

        

        # Create the line series for the bottom line
        self.line_series_bottom = QtCharts.QLineSeries()
        self.line_series_bottom.setPen(QtGui.QPen(QtCore.Qt.NoPen))

        # Create the line series for the top line
        self.line_series_top = QtCharts.QLineSeries()
        self.line_series_top.setPen(QtGui.QPen(QtCore.Qt.NoPen))  

        # Create the area series effect
        self.area_series_effect = QtCharts.QAreaSeries(self.line_series_bottom, self.line_series_top)
        
        # Set the brush color for the area series effect
        color = QtGui.QColor(ThemeColor.secondary)        
        opacity = 180
        color.setAlpha(opacity)
        area_brush = QtGui.QBrush(color)
        self.area_series_effect.setBrush(area_brush)
        self.area_series_effect.setPen(QtGui.QPen(QtCore.Qt.NoPen)) 

        # Add the series to the chart
        # Create the chart 
        self.my_chart = QtCharts.QChart() 
        self.my_chart.setMargins(QtCore.QMargins(0, 0, 0, 0))  
        self.my_chart.layout().setContentsMargins(0,0,0,0)      
        self.my_chart.setBackgroundRoundness(0)
        self.my_chart.addSeries(self.area_series_effect)

        # Set the X-axis and Y-axis ranges
        self.x_axis = QtCharts.QValueAxis()
        self.x_axis.setRange(0, 60)
        self.x_axis.setTickCount(9)
        self.x_axis.setLabelsVisible(False)
        self.x_axis.setLineVisible(False)
        self.x_axis.setGridLineVisible(True)
        self.x_axis.setGridLineColor(QtGui.QColor(ThemeColor.gray_2)) 

        self.y_axis = QtCharts.QValueAxis()
        self.y_axis.setRange(0, 100)    
        self.y_axis.setTickCount(5)    
        self.y_axis.setLabelsVisible(False)
        self.y_axis.setLineVisible(False)
        self.y_axis.setGridLineVisible(True)
        self.y_axis.setGridLineColor(QtGui.QColor(ThemeColor.gray_2))  

        # Set custom labels for the y-axis
        #self.y_axis.append("", 0)
        #self.y_axis.append("", 25)
        #self.y_axis.append("", 50)
        #self.y_axis.append("", 75)
        #self.y_axis.append("100%", 100)
        #self.y_axis.setLabelsPosition(QtCharts.QCategoryAxis.AxisLabelsPositionOnValue)

        self.my_chart.addAxis(self.x_axis, QtCore.Qt.AlignBottom)
        self.my_chart.addAxis(self.y_axis, QtCore.Qt.AlignRight)
        self.my_chart.setBackgroundBrush(QtCore.Qt.transparent)
        self.area_series_effect.attachAxis(self.x_axis)
        self.area_series_effect.attachAxis(self.y_axis)

        self.my_chart.legend().hide()
        

        # Set the chart view's chart
        self.chart_view = QtCharts.QChartView()
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chart_view.setChart(self.my_chart)  

        layout.addWidget(self.chart_view)       

        # usage graph timer
        self.graph_timer = QtCore.QTimer()
        self.graph_timer.timeout.connect(self.update_graph)
        self.graph_timer.start(100)  # 100 milliseconds

        # frequency timer
        self.frequency_timer = QtCore.QTimer()
        self.frequency_timer.timeout.connect(self.update_frequency)
        self.frequency_timer.start(1000)

        # Initialize the time counter
        self.time_counter = 0               

    def update_frequency(self):        
        frequency = CPUInfo.current_frequency

        if frequency:
            formatted_frequency = "{:.2f}".format(frequency / 1000)

            max_frequency = CPUInfo.frequency_max
            formatted_max_frequency = "{:.2f}".format(max_frequency / 1000)
            
            #self.frequency_label.setText(f"{formatted_frequency} / {formatted_max_frequency} GHz")

    def update_graph(self):
        # Get the current CPU usage        
        cpu_percent = CPUInfo.current_usage      

        if cpu_percent:
            # Add the CPU usage to the graph
            self.line_series_bottom.append(QtCore.QPointF(self.time_counter / 10, 0))
            self.line_series_top.append(QtCore.QPointF(self.time_counter / 10, cpu_percent))
            self.time_counter += 1

            # Remove the oldest data point if the x-axis range exceeds 60 seconds
            if self.time_counter > 600:
                self.line_series_bottom.remove(0)
                self.line_series_top.remove(0)

            # Update the chart's x-axis range to keep only the last 60 seconds in view
            self.x_axis.setRange((self.time_counter - 600) / 10, self.time_counter / 10)

            # Redraw the chart
            self.repaint()