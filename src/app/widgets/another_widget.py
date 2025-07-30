import sys, os, json, shutil, time, asyncio, random, pathlib
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy, QTabWidget,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel


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
        labels['404'] = QLabel()
        labels['404'].setText('error: 404')
        labels['error'] = QLabel()
        labels['error'].setText('out of use')

        labels['tab'] = QTabWidget()
        labels['tab'].addTab(QLabel('pp'), 'page_1')
        labels['tab'].addTab(QPushButton('push'), 'page_2')

        for _, item in labels.items():
            # item.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            layout.addWidget(item)