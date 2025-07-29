import sys, os, json, shutil, time, asyncio, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem, QScrollArea,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer

from src.utils.config_util import config
from src.app.templates.tag_template import TagTemplate
from src.app.layouts.flow_layout import FlowLayout

class ConfigWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.tags = []

        layout = QGridLayout(self)

        label = QLabel('Add tag:')

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('Write new tag')

        button = QPushButton()
        button.setIcon(QIcon.fromTheme('list-add'))
        button.setFixedSize(16, 16)
        button.setFlat(True)

        self.lineEdit.returnPressed.connect(lambda:self.add_tag(self.lineEdit.text()))
        button.clicked.connect(lambda:self.add_tag(self.lineEdit.text()))

        layout.addWidget(label,         0, 0, 1, 1)
        layout.addWidget(self.lineEdit, 0, 1, 1, 1)
        layout.addWidget(button,        0, 2, 1, 1)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        self.flow_layout = FlowLayout(content_widget)
        self.flow_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        scroll_area.setWidget(content_widget)
        layout.addWidget(scroll_area,   1, 0, 1, 3)

        self.fetch_tags()

    def fetch_tags(self):
        self.tags = config().get('tags') or []
        self.flow_layout.clear()
        
        [self.add_tag(tag, False) for tag in self.tags]

    def add_tag(self, value: str, new: bool = True):
        value = value.strip()
        if not value:
            return 

        if new:
            normalized_value = value.lower()
            normalized_array = [tag.strip().lower() for tag in self.tags]
            if normalized_value in normalized_array:
                return 
            
            self.tags.append(value)
            config().set('tags', self.tags)

        tag_template = TagTemplate(value)
        tag_template.deleted.connect(self.remove_tag)
        self.flow_layout.addWidget(tag_template)

        self.lineEdit.clear()

    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)
            config().set('tags', self.tags)