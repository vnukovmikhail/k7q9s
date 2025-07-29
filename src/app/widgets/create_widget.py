import sys, os, json, shutil, time, asyncio, random, pathlib
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel

from src.utils.str_util import validate_data, text_to_arr
from src.utils.fs_util import create_collection
from src.utils.config_util import config

class MultiComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().installEventFilter(self)
        self.model().dataChanged.connect(self.updateLineEdit)

    def updateLineEdit(self):
        text_container = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.CheckState.Checked:
                text_container.append(self.model().item(i).text())
        text_string = ', '.join(text_container)
        self.lineEdit().setText(text_string)    

    def addItems(self, items, itemList = None):
        for id, text in enumerate(items):
            try:
                data = itemList[id]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)

    def addItem(self, text, userData = None):
        item = QStandardItem()
        item.setText(text)

        if not userData is None:
            item.setData(userData)

        item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
        item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole) 

        self.model().appendRow(item)

class InitWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.data = {
            'title': None,
            'tags': None,
            'files': None,
        }

        layout = QGridLayout(self)

        labels = {}
        self.lineEdits = {}
        buttons = {}

        labels['Title'] = QLabel('Title')
        labels['Title'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.lineEdits['Title'] = QLineEdit()

        labels['Tags'] = QLabel('Tags:')
        self.combo = MultiComboBox()
        self.combo.addItems(config().get('tags') or [])
        self.combo.lineEdit().setText('')

        buttons['Select'] = QPushButton('Select file(s)')
        buttons['Select'].clicked.connect(self.select_files)

        buttons['Init'] = QPushButton('Init Collection')
        buttons['Init'].clicked.connect(self.approve_creation)
        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)

        layout.addWidget(labels['Title'],         0, 0, 1, 1)
        layout.addWidget(self.lineEdits['Title'], 0, 1, 1, 2)

        layout.addWidget(labels['Tags'],          1, 0, 1, 1)
        layout.addWidget(self.combo,              1, 1, 1, 2)

        layout.addWidget(buttons['Select'],       2, 0, 1, 3)

        layout.addWidget(buttons['Init'],         3, 0, 1, 3)
        layout.addWidget(self.textEdit,           4, 0, 1, 3)

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            parent = self,
            caption = 'Select file(s)',
            directory = os.path.expanduser('~'),
        )
        self.data['files'] = files

    def approve_creation(self):
        self.data['title'] = self.lineEdits['Title'].text()
        self.data['tags'] = text_to_arr(self.combo.lineEdit().text(), ', ')

        print(self.data)

        title = 'Error'
        message = 'Validation error:'
        details = validate_data(self.data)
        
        if details[1]:
            info = create_collection(self.data['title'], self.data['tags'], self.data['files'])
            self.textEdit.setText(self.textEdit.toPlainText() + f'✅ Created on path: {info['folder_path']}\n')
        else:
            self.show_error_dialog(title, message, details[0])

    def show_error_dialog(self, title, message, details):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Critical)

        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setDetailedText(details)

        msg.setStandardButtons(QMessageBox.StandardButton.Cancel)
        msg.exec()
        