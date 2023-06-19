import psutil

from PySide6 import QtCharts, QtCore, QtGui, QtWidgets
from utils.theme import ThemeColor

class CPUChart(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(150)                
        
        self.setContentsMargins(0,0,0,0)
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # create the chart view         
        self.chart_view = QtCharts.QChartView()
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chart_view.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.chart_view)
        
        

        # Create the chart 
        self.my_chart = QtCharts.QChart() 
        self.my_chart.setMargins(QtCore.QMargins(0, 0, 0, 0))  
        self.my_chart.layout().setContentsMargins(0,0,0,0)      
        self.my_chart.setBackgroundRoundness(0)

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
        opacity = 200
        color.setAlpha(opacity)
        area_brush = QtGui.QBrush(color)
        self.area_series_effect.setBrush(area_brush)
        self.area_series_effect.setPen(QtGui.QPen(QtCore.Qt.NoPen)) 

        # Add the series to the chart
        self.my_chart.addSeries(self.area_series_effect)

        # Set the X-axis and Y-axis ranges
        self.x_axis = QtCharts.QValueAxis()
        self.x_axis.setRange(0, 60)
        self.x_axis.setTickCount(9)
        self.x_axis.setLabelsVisible(False)
        self.x_axis.setLineVisible(False)
        self.x_axis.setGridLineVisible(True)
        self.x_axis.setGridLineColor(QtGui.QColor(ThemeColor.gray)) 

        self.y_axis = QtCharts.QValueAxis()
        self.y_axis.setRange(0, 100)
        self.y_axis.setLabelsVisible(False)
        self.y_axis.setLineVisible(False)
        self.y_axis.setGridLineVisible(True)
        self.y_axis.setGridLineColor(QtGui.QColor(ThemeColor.gray))  

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
        self.chart_view.setChart(self.my_chart)        

        # Create a timer to update the graph every 100 milliseconds
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(100)  # 100 milliseconds

        # Initialize the time counter
        self.time_counter = 0    
    

    def update_graph(self):
        # Get the current CPU usage
        cpu_percent = psutil.cpu_percent()

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = CPUChart()
    window.show()
    sys.exit(app.exec())