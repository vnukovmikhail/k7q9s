import sys, os, json, shutil, time, asyncio, random, pathlib
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel

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

        layout = QGridLayout(self)

        labels = {}
        lineEdits = {}
        buttons = {}

        labels['Title'] = QLabel('Title')
        labels['Title'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        lineEdits['Title'] = QLineEdit()

        labels['Tags'] = QLabel('Tags:')

        combo = MultiComboBox()
        combo.addItems(['element_1', 'element_2', 'element_3', 'element_4', 'element_5'])
        combo.lineEdit().setText('')

        buttons['Select'] = QPushButton('Select file(s)')
        buttons['Select'].clicked.connect(self.selectFiles)

        buttons['Init'] = QPushButton('Init Collection')
        textEdit = QTextEdit()

        layout.addWidget(labels['Title'],       0, 0, 1, 1)
        layout.addWidget(lineEdits['Title'],    0, 1, 1, 2)

        layout.addWidget(labels['Tags'],        1, 0, 1, 1)
        layout.addWidget(combo,                 1, 1, 1, 2)

        layout.addWidget(buttons['Select'],     2, 0, 1, 3)

        layout.addWidget(buttons['Init'],       3, 0, 1, 3)
        layout.addWidget(textEdit,              4, 0, 1, 3)

    def selectFiles(self):
        files, _ = QFileDialog.getOpenFileNames(
            parent = self,
            caption = 'Select file(s)',
            directory = os.path.expanduser('~'),
        )
        print(files)