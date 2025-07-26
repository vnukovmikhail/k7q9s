import sys, os, json, shutil, time, asyncio, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer

class AnotherWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        labels = {}

        labels['Hello world'] = QLabel()
        labels['Hello world'].setText('Hello World')
        labels['who are you?'] = QLabel()
        labels['who are you?'].setText('who are you?')
        labels['lets go'] = QLabel()
        labels['lets go'].setText('lets go')

        for _, item in labels.items():
            item.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            layout.addWidget(item)