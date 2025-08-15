import sys, os, json, shutil, time, asyncio, random, pathlib, inspect
from datetime import datetime

from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit, QStyle, QToolTip)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel, QMovie
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel, QPoint

from app.gui.templates.multi_combobox_template import MultiComboBox
from app.gui.widgets.file_drop_widget import FileDropWidget
from app.gui.widgets.multi_list_widget import MultiListWidget
from app.repositories.folder_repository import FolderRepository
from app.repositories.tag_repository import fetchall_tags

class QCreatorWidget(QWidget):
    def __init__(self):
        super().__init__()

        title_label = QLabel('Title:')
        title_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        title_input = QLineEdit()
        title_input.setPlaceholderText('name_of_folder')

        tags_label = QLabel('Tags:')
        tags_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

        self.tags_list_widget = MultiListWidget(True)
        # self.tags_list_widget.setFixedHeight(170)

        info_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView)

        radio_label = QLabel('Move:')
        radio_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        radio_copy = QRadioButton('copy file(s)')
        radio_move = QRadioButton('move file(s)')
        radio_copy.setChecked(True)

        radio_info = QPushButton()
        radio_info.setIcon(info_icon)
        radio_info.setFixedSize(16, 16)
        radio_info.setFlat(True)
        radio_tooltip = """<b>📄 Copy</b> - File(s) will be copied<br><b>✂️ Move</b> - File(s) will be moved<hr>to destination folder"""
        radio_info.clicked.connect(lambda:self.show_tooltip(radio_info, radio_tooltip))

        

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(radio_copy)
        radio_layout.addWidget(radio_move)
        radio_layout.addWidget(radio_info)
        radio_layout.addStretch()

        radio_group = QButtonGroup(self)
        radio_group.addButton(radio_copy, 0)
        radio_group.addButton(radio_move, 1)

        file_label = QLabel('File[s]:')
        file_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        file_drop = FileDropWidget()

        file_drop_button = QPushButton('📁 select file[s] manually')
        file_drop_button.clicked.connect(self.select_files)

        aprove_button = QPushButton('init collection')
        aprove_button.clicked.connect(self.approve_creation)

        layout = QGridLayout(self)
        layout.addWidget(title_label,           0, 0, 1, 1)
        layout.addWidget(title_input,           0, 1, 1, 1)

        layout.addWidget(tags_label,            1, 0, 1, 1)
        layout.addWidget(self.tags_list_widget, 1, 1, 1, 1)

        layout.addWidget(file_drop,             2, 1, 1, 1)
        layout.addWidget(file_label,            2, 0, 1, 1)

        layout.addWidget(file_drop_button,      3, 1, 1, 1)

        layout.addWidget(radio_label,           4, 0, 1, 1)
        layout.addLayout(radio_layout,          4, 1, 1, 1)

        layout.addWidget(aprove_button,         5, 1, 1, 1)

    def showEvent(self, event):
        super().showEvent(event)
        self.fetch_tags()

    def show_tooltip(self, widget:QWidget, text:str):
        position = widget.mapToGlobal(QPoint(0, int(widget.height() * 0.1)))
        # position = widget.mapToGlobal(QPoint(0, -widget.height()))
        QToolTip.showText(position, text, widget)

    def fetch_tags(self):
        self.tags_list_widget.clear()
        [self.tags_list_widget.addItem(tag['name'], tag['id']) for tag in fetchall_tags()]

    def select_files(self):
        self.file_paths, _ = QFileDialog.getOpenFileNames(
            parent = self,
            caption = 'Select_file(s)',
            directory = os.path.expanduser('~'),
        )

    def approve_creation(self):
        # title = self.input_fields['title'].text()
        # tags = self.tags_combobox.value()
        # file_paths = self.file_paths
        # files = [os.path.basename(path) for path in file_paths]
        # move = bool(self.radio_group.checkedId())

        # print(title, tags, file_paths, move)
        return
        fr = FolderRepository(title)
        fr.add_files(file_paths, move)
        fr.add_tags(tags)

    
        