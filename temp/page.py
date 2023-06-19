from PySide6 import QtWidgets, QtCore

from gui.widgets.cpu import CPUMonitor
from utils.theme import ThemeStylesheet
from utils.log import Log

class PageStack(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()       

        self.stacked_layout = QtWidgets.QStackedLayout(self)
        self.page_dashboard = PageDashboard()
        self.page_cpu = PageCPU()
        self.page_gpu = PageGPU()
        self.page_memory = PageMemory()
        self.page_disk = PageDisk()
        self.page_network = PageNetwork()
        self.page_apps = PageApps()
        self.page_settings = PageSettings()
        self.page_logs = PageLogs()
        
        self.setup_ui()        
    
    def setup_ui(self):
        self.stacked_layout.addWidget(self.page_dashboard)
        self.stacked_layout.addWidget(self.page_cpu)
        self.stacked_layout.addWidget(self.page_gpu)
        self.stacked_layout.addWidget(self.page_memory)
        self.stacked_layout.addWidget(self.page_disk)
        self.stacked_layout.addWidget(self.page_network)
        self.stacked_layout.addWidget(self.page_apps)
        self.stacked_layout.addWidget(self.page_settings)
        self.stacked_layout.addWidget(self.page_logs)
        self.setStyleSheet(ThemeStylesheet.page)

        Log.debug_init(self)
    
    def switch_page(self, page):
        Log.debug(f"Switching to page '{page.title}'")
        self.stacked_layout.setCurrentWidget(page)
        

class Page(QtWidgets.QScrollArea):
    def __init__(self, title):
        super().__init__()
        
        self.title = title
        self.label_title = QtWidgets.QLabel(self.title)   
        self.separator = QtWidgets.QFrame()

        self.page_container = QtWidgets.QWidget()
        self.page_layout = QtWidgets.QGridLayout()  
        self.current_row = 0
        self.current_col = 0
        self.max_cols = 3    
        
        # scroll area properties
        self.setWidget(self.page_container)    
        self.setWidgetResizable(True)    
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        # title properties
        self.label_title.setStyleSheet(ThemeStylesheet.page_title)

        # separator properties
        self.separator.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator.setFrameShadow(QtWidgets.QFrame.Sunken)    
        self.separator.setStyleSheet(ThemeStylesheet.line_horizontal_1)

        # set the container layout
        self.page_container.setLayout(self.page_layout)

        # add common widgets to layout
        self.insert_widget(self.label_title, 3) 
        self.insert_widget(self.separator, 3)     
        
        # push items to the top
        self.page_container.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)

        Log.debug_init(self)
    
    def insert_widget(self, widget, col_span=1):
        # Calculate the current column
        current_col = self.current_col % self.max_cols

        # Calculate the widget's column span
        if current_col + col_span > self.max_cols:
            col_span = self.max_cols - current_col

        # Insert the widget at the current row and column
        self.page_layout.addWidget(widget, self.current_row, current_col, 1, col_span)

        # Update the current row and column
        self.current_col += col_span
        if current_col + col_span == self.max_cols:
            self.current_row += 1

        # Set the maximum width of the widget
        widget.setMaximumWidth(self.width())

        # Update the current row and column
        self.current_col += col_span
        if current_col + col_span == self.max_cols:
            self.current_row += 1
            
    def resizeEvent(self, event):
        super().resizeEvent(event)

        # Update the maximum width of the child widgets when the scroll area is resized
        for i in range(self.page_layout.count()):
            item = self.page_layout.itemAt(i)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.setMaximumWidth(self.width())

class PageDashboard(Page):
    def __init__(self):
        super().__init__('Dashboard')        
        self.description = QtWidgets.QLabel(f'This is the Dashboard page!')
        self.setup_ui()

    def setup_ui(self):
        self.te = QtWidgets.QTextEdit()
        self.te2 = QtWidgets.QTextEdit()
        self.te3 = QtWidgets.QTextEdit()
        self.te.setStyleSheet(f"border: 1px solid #ffffff;")
        self.te2.setStyleSheet(f"border: 1px solid #ffffff;")
        self.te3.setStyleSheet(f"border: 1px solid #ffffff;")
        self.insert_widget(self.te, 1)
        self.insert_widget(self.te2, 1)
        self.insert_widget(self.te3, 1)


class PageCPU(Page):
    def __init__(self):
        super().__init__('CPU')        
        self.description = QtWidgets.QLabel('This is the Processor page!')
        self.setup_ui()

    def setup_ui(self):
        self.cpu_monitor = CPUMonitor()
        self.insert_widget(self.cpu_monitor, 3)          
        #self.chart = Chart()
        #self.insert_widget(self.chart, 3)          
        
                
        #self.page_layout.addStretch()


class PageGPU(Page):
    def __init__(self):
        super().__init__('GPU')        
        self.description = QtWidgets.QLabel('This is the GPU page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()


class PageMemory(Page):
    def __init__(self):
        super().__init__('Memory')        
        self.description = QtWidgets.QLabel('This is the Memory page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()


class PageDisk(Page):
    def __init__(self):
        super().__init__('Disk')        
        self.description = QtWidgets.QLabel('This is the Disk page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()


class PageNetwork(Page):
    def __init__(self):
        super().__init__('Network')        
        self.description = QtWidgets.QLabel('This is the Network page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()


class PageApps(Page):
    def __init__(self):
        super().__init__('Apps')        
        self.description = QtWidgets.QLabel('This is the Apps page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()


class PageSettings(Page):
    def __init__(self):
        super().__init__('Settings')        
        self.description = QtWidgets.QLabel('This is the Settings page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()


class PageLogs(Page):
    def __init__(self):
        super().__init__('Logs')        
        self.description = QtWidgets.QLabel('This is the Logs page!')
        self.setup_ui()

    def setup_ui(self):
        self.page_layout.addWidget(self.description)
        #self.page_layout.addStretch()

        