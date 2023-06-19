from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QScrollArea

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Scroll Area Example")
window.resize(400, 300)

# Create a scroll area widget
scroll_area = QScrollArea()
scroll_area.setWidgetResizable(True)  # Allows the widget inside the scroll area to resize
scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Disables horizontal scrolling

# Create a widget to contain the scrollable content
scroll_content = QWidget()
scroll_area.setWidget(scroll_content)

# Create a layout for the scrollable content
scroll_layout = QVBoxLayout(scroll_content)
scroll_layout.setAlignment(Qt.AlignTop)

# Add some content to the scrollable area
for i in range(20):
    label = QLabel(f"Label.................................................................... {i}")
    scroll_layout.addWidget(label)

# Set the scroll area as the central widget of the main window
window.setCentralWidget(scroll_area)

window.show()
app.exec()
