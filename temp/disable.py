from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([])

window = QMainWindow()
button = QPushButton("Click me", window)

# Disable the button without graying out the interface
button.setDisabled(True)

window.show()
app.exec()