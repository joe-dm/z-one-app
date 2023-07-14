from PySide6 import QtWidgets, QtCore

from ui.common.element import LabelWidgetTitle

class Card(QtWidgets.QFrame):
    def __init__(self, title, unit=''):
        super().__init__(objectName='StatCard')

        # setup labels
        self.label_title = QtWidgets.QLabel(title, objectName='StatCardTitleLabel')
        self.label_title.setAlignment(QtCore.Qt.AlignCenter) 
        self.label_stat = QtWidgets.QLabel('-', objectName='StatCardTextLabel')
        self.label_stat.setAlignment(QtCore.Qt.AlignCenter) 
        self.label_unit = QtWidgets.QLabel(unit, objectName='StatCardUnitLabel')        
        self.label_unit.setAlignment(QtCore.Qt.AlignCenter) 

        # setup layout
        layout = QtWidgets.QVBoxLayout(self)   
        layout.setContentsMargins(5, 1, 5, 1)   
        layout.setSpacing(1) 
        layout.setAlignment(QtCore.Qt.AlignCenter)        
        layout.addWidget(self.label_title)    
        layout.addSpacing(5)
        layout.addWidget(self.label_stat)
        layout.addWidget(self.label_unit)

        self.setMinimumWidth(80)

    def update_stat(self, value):
        self.label_stat.setText(f"{value}")


class CardGroup(QtWidgets.QWidget):
    def __init__(self, title='Live Stats'):
        super().__init__()

        self.title_label = LabelWidgetTitle(title)

        self.card_container = QtWidgets.QWidget()
        self.card_container_layout = QtWidgets.QHBoxLayout(self.card_container)
        self.card_container_layout.setContentsMargins(0,0,0,0)

        self.widget_layout = QtWidgets.QVBoxLayout(self)
        self.widget_layout.setContentsMargins(0,0,0,0)
        self.widget_layout.addWidget(self.title_label)
        
    
    def insert_cards(self, card_list):
        self.widget_layout.addWidget(self.card_container)
        for card in card_list:
            self.card_container_layout.addWidget(card)
            self.card_container_layout.addSpacing(10)
        self.card_container_layout.addStretch()





