from PySide6 import QtWidgets, QtCore


class ThemeStylesheet:
    # dialog styles    
    dialog = (
        '''
        EmbeddedDialog {
            background-color: transparent;
        }
        QWidget#DialogContainer {
            border: 2px solid gray;
        }
        '''
    )
    dialog_heading = (
        'font-weight: bold;'
        'font-size: 18px;'
        'color: white;'
        'border: 1px solid #fff;'
    )


class EmbeddedDialog(QtWidgets.QWidget):
    def __init__(self, parent_widget):
        super().__init__(parent_widget)
        self.parent_widget = parent_widget

        self.full_layout = QtWidgets.QVBoxLayout(self)
        self.container = QtWidgets.QWidget(objectName='DialogContainer')
        self.container_layout = QtWidgets.QVBoxLayout(self.container)

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setStyleSheet(ThemeStylesheet.dialog)

        self.full_layout.addWidget(self.container, alignment=QtCore.Qt.AlignCenter)

    def showEvent(self, event):
        self.setGeometry(self.parent().rect())


class ExitDialog(EmbeddedDialog):
    def __init__(self, parent_widget):
        super().__init__(parent_widget)

        self.heading = QtWidgets.QLabel('Exiting')
        self.message = QtWidgets.QLabel('Cleaning up and exiting...\nPlease wait.')
        self.progress_bar = QtWidgets.QProgressBar()

        self.setup_ui()

    def setup_ui(self):
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setStyleSheet(ThemeStylesheet.dialog_heading)

        self.message.setAlignment(QtCore.Qt.AlignCenter)

        self.progress_bar.setRange(0, 0)
        self.progress_bar.setStyleSheet('border: 1px solid #fff;')
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)

        
        self.container_layout.addWidget(self.heading)
        self.container_layout.addWidget(self.message)
        self.container_layout.addWidget(self.progress_bar)        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QMainWindow()
    window.setWindowTitle("Progress Bar Dialog Test")
    window.resize(400, 300)

    exit_dialog = ExitDialog(window)
    exit_dialog.show()

    window.show()
    sys.exit(app.exec())
