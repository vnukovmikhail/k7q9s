import sys, os, json, shutil, time, asyncio, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy, QStyle,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem, QScrollArea,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer

from app.gui.templates.tag_template import TagTemplate
from app.gui.widgets.flow_scroll_widget import FlowScrollWidget
from app.repositories.tag_repository import TagRepository

class TagEditorWidget(QWidget):
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

        self.flow_widget = FlowScrollWidget()

        layout.addWidget(self.flow_widget,   1, 0, 1, 3)

        self.fetch_tags()

    def form_tag_approve(self):
        tag_repo = TagRepository()
        tag_name = self.lineEdit.text()

        tag = tag_repo.create(tag_name)

        self.add_tag(tag)

    def fetch_tags(self):
        tag_repo = TagRepository()
        tags = tag_repo.fetchall()

        self.flow_widget.clear()

        [self.add_tag(tag) for tag in tags]

    def add_tag(self, tag):
        tag_template = TagTemplate(tag)
        self.flow_widget.addWidget(tag_template)
        self.lineEdit.clear()