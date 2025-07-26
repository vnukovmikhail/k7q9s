import sys, os, json, shutil, time, asyncio, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer

from src.app.widgets.custom_widget import CustomWidget
from src.app.widgets.init_widget import InitWidget
from src.app.widgets.another_widget import AnotherWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Not my first application')
        self.setWindowIcon(QIcon('src/resources/pic.png'))
        self.setFont(QFont('monospace'))
        self.setMinimumSize(300, 500)

        widget = QWidget()
        self.setMenuWidget(widget)
        layout = QHBoxLayout(widget)

        buttons = {}

        buttons['button_1'] = QPushButton('button_1')
        buttons['button_1'].clicked.connect(lambda:self.setCentralWidget(CustomWidget()))
        buttons['button_2'] = QPushButton('button_2')
        buttons['button_2'].clicked.connect(lambda:self.setCentralWidget(InitWidget()))
        buttons['button_3'] = QPushButton('button_3')
        buttons['button_3'].clicked.connect(lambda:self.setCentralWidget(AnotherWidget()))

        for _, item in buttons.items():
            layout.addWidget(item)

        widget1 = QWidget()
        self.setCentralWidget(widget1)
        layout1 = QVBoxLayout(widget1)

        # label = QLabel('Not my first application')
        # label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # layout1.addWidget(label)

        labels = {}

        labels['title'] = QLabel('Not my first application')
        labels['title'].setAlignment(Qt.AlignmentFlag.AlignCenter)
        labels['version'] = QLabel('version: v1.0.0')
        labels['version'].setAlignment(Qt.AlignmentFlag.AlignAbsolute | Qt.AlignmentFlag.AlignBottom)

        for _, item in labels.items():
            layout1.addWidget(item)