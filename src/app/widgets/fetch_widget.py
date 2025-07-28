import sys, os, json, shutil, time, asyncio, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem, QScrollArea,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer

from src.app.templates.item_template import ItemTemplate
from src.utils.fs_util import fetch_collections
from src.utils.str_util import filter_images
from src.app.layouts.flow_layout import FlowLayout

class FetchWidget(QWidget):
    def __init__(self):
        super().__init__()
        # self.setStyleSheet('border: 2px solid red;')

        collections = fetch_collections()

        layout = QGridLayout(self)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        flow_layout = FlowLayout(content_widget)
        flow_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        for collection in collections:
            item_template = ItemTemplate(collection)
            flow_layout.addWidget(item_template)

        scroll_area.setWidget(content_widget)
        layout.addWidget(scroll_area, 0, 0, 1, 7)

        size_slider = QSlider()
        size_slider.setOrientation(Qt.Orientation.Horizontal)
        size_slider.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        size_slider.setValue(50)

        size_label = QLabel('Image size:')
        size_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        size_spinBox = QSpinBox()
        size_spinBox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        size_spinBox.setMaximum(100)

        layout.addWidget(size_label,   1, 4, 1, 1)
        layout.addWidget(size_slider,  1, 5, 1, 1)
        layout.addWidget(size_spinBox, 1, 6, 1, 1)