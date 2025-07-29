import sys, os, json, shutil, time, asyncio, random, pathlib
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel

class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout1 = QVBoxLayout(self)
        layout1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        labels = {}

        labels['title'] = QLabel('title: Not my first application')
        labels['description'] = QLabel('description: Organizer for files')
        labels['author'] = QLabel('author: Mihail Vnukov')
        labels['version'] = QLabel('version: x.x.xx-dev')

        for _, item in labels.items():
            item.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            layout1.addWidget(item)