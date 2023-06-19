from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea

app = QApplication([])

widget = QWidget()
layout = QVBoxLayout(widget)

scroll_area = QScrollArea()
scroll_widget = QWidget()

scroll_layout = QVBoxLayout(scroll_widget)

label = QLabel("This is a long text that might overflow outside the label's parent widget.")
label.setWordWrap(False)
label.setAlignment(Qt.AlignTop)  # or Qt.AlignLeft

scroll_layout.addWidget(label)
scroll_widget.setLayout(scroll_layout)
scroll_area.setWidget(scroll_widget)

layout.addWidget(scroll_area)
widget.show()

app.exec()
