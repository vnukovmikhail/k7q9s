import sys, os, json, shutil, time, asyncio, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)

        labels = {}
        lineEdits = {}

        labels['Username'] = QLabel('Username')
        labels['Password'] = QLabel('Password')
        labels['Username'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['Password'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        lineEdits['Username'] = QLineEdit()
        lineEdits['Password'] = QLineEdit()
        lineEdits['Password'].setEchoMode(QLineEdit.EchoMode.Password)
        button = QPushButton('Log In')
        textEdit = QTextEdit()

        layout.addWidget(labels['Username'],    0, 0, 1, 1)
        layout.addWidget(lineEdits['Username'], 0, 1, 1, 3)

        layout.addWidget(labels['Password'],    1, 0, 1, 1)
        layout.addWidget(lineEdits['Password'], 1, 1, 1, 3)

        layout.addWidget(button,                2, 0, 1, 4)
        layout.addWidget(textEdit,              3, 0, 1, 4)
