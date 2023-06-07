from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
import sys

class ShadowWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("shadowWidget")
        self.setStyleSheet(
            "#shadowWidget {"
            "   background-color: gray;"
            "   border-radius: 5px;"
            "   border: 5px solid rgba(0, 0, 0, 0.5);"
            "}"
        )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a custom QWidget subclass for the shadow effect
        shadow_widget = ShadowWidget()

        # Create a QLabel
        label = QLabel("Hello, World!", shadow_widget)

        # Create a layout and add the QLabel to it
        layout = QVBoxLayout()
        layout.addWidget(label)

        # Set the layout on the shadow widget
        shadow_widget.setLayout(layout)

        # Set the shadow widget as the central widget of the main window
        self.setCentralWidget(shadow_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
