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

from app.db.repositories.tag_repo import TagRepo
from app.db import session

class QTagEditorWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.tag_repo = TagRepo(session)

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

        self.flow_widget = FlowScrollWidget()

        layout = QGridLayout(self)
        layout.addWidget(label,         0, 0, 1, 1)
        layout.addWidget(self.lineEdit, 0, 1, 1, 1)
        layout.addWidget(button,        0, 2, 1, 1)
        layout.addWidget(self.flow_widget,   1, 0, 1, 3)

        self.fetch_tags()

    def form_tag_approve(self):
        tag_name = self.lineEdit.text()
        self.add_tag(tag_name)
        self.fetch_tags()

    def fetch_tags(self):
        self.flow_widget.clear()
        [self.add_tag(tag.name) for tag in self.tag_repo.get_all_tags()]

    def add_tag(self, tag_name:str):
        tag = self.tag_repo.create_or_update_tag(str(tag_name).strip())
        tag_template = TagTemplate(tag.name)
        tag_template.deleted.connect(self.rem_tag)
        self.flow_widget.addWidget(tag_template)
        self.lineEdit.clear()

    def rem_tag(self, tag_name:str):
        print(tag_name)
        self.tag_repo.delete_tag_by_name(tag_name)