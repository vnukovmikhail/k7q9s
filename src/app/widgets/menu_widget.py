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

class MenuWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)

        buttons = {}

        buttons['button_1'] = QPushButton('button_1')
        buttons['button_2'] = QPushButton('button_2')
        buttons['button_3'] = QPushButton('button_3')

        buttons['button_1'].clicked.connect(lambda:parent.setCentralWidget(CustomWidget()))
        buttons['button_2'].clicked.connect(lambda:parent.setCentralWidget(InitWidget()))
        buttons['button_3'].clicked.connect(lambda:parent.setCentralWidget(AnotherWidget()))

        for _, item in buttons.items():
            layout.addWidget(item)