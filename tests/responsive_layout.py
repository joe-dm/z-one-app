from PySide6 import QtCore, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Responsive Layout Example")
        self.resize(600, 400)

        # Create the main widget and its layout
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout(self.main_widget)
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.setCentralWidget(self.main_widget)

        # Create the widgets
        self.widgets = []
        for i in range(6):
            widget = QtWidgets.QLabel(f"Widget {i+1}")
            widget.setStyleSheet("background-color: lightblue; font-size: 20px; padding: 20px;")
            self.widgets.append(widget)

        # Add the widgets to the layout
        self.add_widgets()

    def add_widgets(self):
        # Clear the layout
        for i in reversed(range(self.main_layout.count())):
            item = self.main_layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            self.main_layout.removeItem(item)

        # Calculate the number of columns based on window width
        window_width = self.width()
        if window_width >= 600:
            num_columns = 3
        elif window_width >= 400:
            num_columns = 2
        else:
            num_columns = 1

        # Add the widgets to the layout
        for i, widget in enumerate(self.widgets):
            row = i // num_columns
            column = i % num_columns
            self.main_layout.addWidget(widget, row, column)

    def resizeEvent(self, event):
        # Update the layout when the window is resized
        self.add_widgets()
        super().resizeEvent(event)


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
