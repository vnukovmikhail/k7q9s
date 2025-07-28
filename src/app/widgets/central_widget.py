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

        labels['title'] = QLabel('"Not my first application"')
        labels['title'].setFont(QFont('monospace', 11))
        labels['author'] = QLabel('Author: Mihail')
        labels['version'] = QLabel('Version: v1.0.0')

        for _, item in labels.items():
            item.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            layout1.addWidget(item)