import sys, os
from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PySide6.QtSvg import QSvgRenderer

if __name__ == '__main__':
    app = QApplication(sys.argv)

    path = os.path.join('app', 'resources', 'images', 'logo-text.svg')

    scene = QGraphicsScene()
    view = QGraphicsView(scene)

    renderer = QSvgRenderer(path)
    item = scene.addPixmap(renderer.render())

    view.show()
    sys.exit(app.exec())

