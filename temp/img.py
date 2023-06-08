from PySide6 import QtWidgets, QtGui, QtCore, QtSvg
import os
class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Create a QLabel widget to display the SVG image
        self.image_label = QtWidgets.QLabel()

        # Load the SVG image using QSvgRenderer
        path = os.path.join('app', 'resources', 'images', 'logo-text.svg')
        svg_renderer = QtSvg.QSvgRenderer(path)

        # Create a QPixmap to render the SVG onto
        size = QtCore.QSize(200, 200)  # Set the desired size of the image
        pixmap = QtGui.QPixmap(size)
        pixmap.fill(QtGui.QColor(QtCore.Qt.transparent))  # Set transparent background

        # Render the SVG onto the QPixmap
        painter = QtGui.QPainter(pixmap)
        svg_renderer.render(painter)
        painter.end()

        # Set the pixmap on the QLabel
        self.image_label.setPixmap(pixmap)

        # Set the layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.image_label)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
