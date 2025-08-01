import sys, os, json, shutil, time, asyncio, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy, QStyle,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem, QScrollArea,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer

from src.app.templates.tag_template import TagTemplate
from src.app.layouts.flow_layout import FlowLayout
from src.utils.sql_util import Sql

class ConfigWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)

        label = QLabel('Add tag:')

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('Write new tag')

        button = QPushButton()
        icon = self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogNewFolder)
        button.setIcon(icon)
        button.setFixedSize(16, 16)
        button.setFlat(True)

        self.lineEdit.returnPressed.connect(self.form_tag_approve)
        button.clicked.connect(self.form_tag_approve)

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

    def form_tag_approve(self):
        sql = Sql()
        tag = sql.add_tag_to_db(self.lineEdit.text())
        self.add_tag(tag)
        sql.close()

    def fetch_tags(self):
        sql = Sql()
        tags = sql.fetch_tags_from_db()
        self.flow_layout.clear()
        [self.add_tag(tag) for tag in tags]
        sql.close()

    def add_tag(self, tag):
        tag_template = TagTemplate(tag)
        self.flow_layout.addWidget(tag_template)
        self.lineEdit.clear()