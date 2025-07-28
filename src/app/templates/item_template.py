import sys, os, json, shutil, time, asyncio, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy, QGraphicsView, QGraphicsScene,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem, QScrollArea,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QMouseEvent
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, pyqtSignal
from typing import Optional, List, Dict

from src.utils.str_util import filter_images

class ItemTemplate(QWidget):
    clicked = pyqtSignal()
    def __init__(self, data):
        super().__init__()

        self.data = data

        title = self.data['meta']['title']
        pic_path = filter_images(self.data['files'])
        
        layout = QVBoxLayout(self)

        pic_label = QLabel()
        pixmap = QPixmap(pic_path)
        pic_label.setPixmap(pixmap)

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        layout.addWidget(pic_label)
        layout.addWidget(title_label)

        # self.resize_image()

        # self.labels = {}

        # self.labels['picture'] = QLabel('ff')
        # self.labels['picture'].setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.pixmap = QPixmap(pic_path)

        # width = 500
        # height = (self.pixmap.height() * width) // self.pixmap.width()
        # scaled_pixmap = self.pixmap.scaled(
        #     width,
        #     height,
        #     Qt.AspectRatioMode.KeepAspectRatio,
        #     Qt.TransformationMode.SmoothTransformation
        # )

        # self.labels['picture'].setPixmap(scaled_pixmap)

        # self.labels['title'] = QLabel(title)
        # self.labels['title'].setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.labels['title'].setMaximumWidth(100)

        # for _, item in self.labels.items():
        #     layout.addWidget(item) 

        # self.resize_image()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
            print(self.data)
        super().mousePressEvent(event)


    # def resizeEvent(self, event):
    #     print(1)
    #     # self.resize_image()
    #     super().resizeEvent(event)

    def resize_image(self):
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.width() - self.labels['picture'].width(),
                self.height() - self.labels['picture'].height(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.labels['picture'].setPixmap(scaled_pixmap)

    """ def __init__(self, data):
        super().__init__()

        self.data = data

        self.setWindowTitle("Масштабируемое изображение (QGraphicsView)")
        self.layout = QVBoxLayout()
        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.layout.addWidget(self.view)
        self.setLayout(self.layout)

        # Загружаем изображение
        self.pixmap = QPixmap(filter_images(self.data['files']))
        if not self.pixmap.isNull():
            self.scene.addPixmap(self.pixmap)
            self.view.fitInView(self.scene.itemsBoundingRect(), Qt.AspectRatioMode.KeepAspectRatio)

    def resizeEvent(self, event):
        if not self.pixmap.isNull():
            self.view.fitInView(self.scene.itemsBoundingRect(), Qt.AspectRatioMode.KeepAspectRatio)
        super().resizeEvent(event) """