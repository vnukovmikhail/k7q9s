import sys, os, json, shutil, time, asyncio, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem, QScrollArea,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer

from src.app.templates.item_template import GridItemWidget

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        data = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11"]
        columns = 3
        
        layout = QGridLayout(self)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        grid = QGridLayout(content_widget)

        for index, text in enumerate(data):
            row = index // columns
            col = index % columns

            label = GridItemWidget(text, text)
            grid.addWidget(label, row, col)


        """ pixmap = QPixmap('src/resources/pic.png')
        for i in range(9):
            for j in range(4):
                widget = GridItemWidget('pics', 'bububu')
                grid.addWidget(widget, i, j)
                label = QLabel()
                label.setFixedSize(70, 70)
                label.setScaledContents(True)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setPixmap(pixmap)
                grid.addWidget(label, i, j) """

        scroll_area.setWidget(content_widget)
        layout.addWidget(scroll_area, 0, 0, 1, 5)




""" class CustomWidget(QWidget):
    def __init__(self, rows=25, columns=4):
        super().__init__()

        self.layout = QGridLayout(self)

        x_label = QLabel('rows:')
        y_label = QLabel('columns:')
        x_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        y_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        x = QSpinBox()
        y = QSpinBox()
        x.setValue(rows)
        y.setValue(columns)
        x.valueChanged.connect(lambda:print('changed'))
        y.valueChanged.connect(lambda:print('changed'))
        self.layout.addWidget(x_label,     1, 3, 1, 1)
        self.layout.addWidget(x,           1, 4, 1, 1)
        self.layout.addWidget(y_label,     2, 3, 1, 1)
        self.layout.addWidget(y,           2, 4, 1, 1)

    def resizeEvent(self, event):
        item_size = 100

        new_size: QSize = event.size()
        print(f"New window: {new_size.width()} x {new_size.height()}")
        super().resizeEvent(event)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        grid = QGridLayout(content_widget)

        columns = new_size.width() // round(item_size * 1.15) 

        pixmap = QPixmap('src/resources/pic.png')
        for i in range(5):
            for j in range(columns):
                label = QLabel()
                label.setFixedSize(item_size, item_size)
                label.setScaledContents(True)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setPixmap(pixmap)
                grid.addWidget(label, i, j)

        scroll_area.setWidget(content_widget)
        self.layout.addWidget(scroll_area, 0, 0, 1, 5) """