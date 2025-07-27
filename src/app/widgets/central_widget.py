import sys, os, json, shutil, time, asyncio, random, pathlib
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel

from src.app.widgets.custom_widget import CustomWidget
from src.app.widgets.init_widget import InitWidget
from src.app.widgets.another_widget import AnotherWidget

class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout1 = QVBoxLayout(self)
        layout1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        labels = {}

        labels['title'] = QLabel('"Not my first application"')
        labels['title'].setFont(QFont('monospace', 11))
        labels['version'] = QLabel('version: v1.0.0')

        for _, item in labels.items():
            item.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            layout1.addWidget(item)