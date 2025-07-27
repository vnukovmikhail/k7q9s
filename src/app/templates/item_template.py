import sys, os, json, shutil, time, asyncio, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem, QScrollArea,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QMouseEvent
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, pyqtSignal

class GridItemWidget(QWidget):
    clicked = pyqtSignal()
    def __init__(self, pic, title):
        super().__init__()

        """"""
        self.setStyleSheet('border: 2px solid red;')
        """"""

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        labels = {}

        pixmap = QPixmap('src/resources/pic.png')

        labels['picture'] = QLabel('ff')
        labels['picture'].setAlignment(Qt.AlignmentFlag.AlignCenter)
        labels['picture'].setFixedSize(70, 70)
        labels['picture'].setScaledContents(True)
        labels['picture'].setPixmap(pixmap)

        labels['title'] = QLabel(title)
        labels['title'].setAlignment(Qt.AlignmentFlag.AlignCenter)

        for _, item in labels.items():
            layout.addWidget(item) 

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
            print(1)
        super().mousePressEvent(event)
