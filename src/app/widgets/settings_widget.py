import sys, os, json, shutil, time, asyncio, random, pathlib
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy, QTabWidget,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel


class SettingsWidget(QWidget):
    def __init__(self):
        super().__init__()

        # layout = QGridLayout(self)

        # label = QLabel('Settings')

        # widget = QTabWidget()
        # widget.addTab(QLabel('setting_1'), 'setting_1')
        # widget.addTab(QLabel('setting_2'), 'setting_2')
        # widget.addTab(QLabel('setting_3'), 'setting_3')

        # layout.addWidget(label, 0, 0, 1, 1)
        # layout.addWidget(widget, 1, 0, 1, 1)