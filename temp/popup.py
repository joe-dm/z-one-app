from PySide6 import QtWidgets, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a button to show the popup
        self.button = QtWidgets.QPushButton("Show Popup")
        self.button.clicked.connect(self.show_popup)

        # Create a central widget and set the button as its layout
        central_widget = QtWidgets.QWidget()
        central_layout = QtWidgets.QVBoxLayout()
        central_layout.addWidget(self.button)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def show_popup(self):
        popup = PopupExit("Popup Title", "Popup Message")
        popup.exec()


class PopupExit(QtWidgets.QDialog):
    def __init__(self, title, message):
        super().__init__()

        # Set the dialog as modal and without a title bar
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(True)

        # Set the dialog title
        self.title = title

        # Create a label and a button
        self.label = QtWidgets.QLabel(message)
        self.button = QtWidgets.QPushButton("Close")
        self.button.clicked.connect(self.close)

        # Create a layout and add the label and button to it
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Set the layout for the dialog
        self.setLayout(layout)

    def showEvent(self, event):
        # Calculate the center position of the screen
        desktop = QtWidgets.QApplication.desktop()
        screen_rect = desktop.screenGeometry(desktop.primaryScreen())
        center_point = screen_rect.center()

        # Calculate the position of the dialog to center it on the screen
        dialog_rect = self.geometry()
        dialog_rect.moveCenter(center_point)

        # Move the dialog to the calculated position
        self.moveCenter(dialog_rect.topLeft())

        # Set the dialog title
        self.setWindowTitle(self.title)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    # Create and show the main window
    window = MainWindow()
    window.show()

    app.exec()
