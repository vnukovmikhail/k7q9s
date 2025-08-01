import sys, os, json, shutil, time, asyncio, random, pathlib, inspect
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel

from src.app.templates.custom_combobox_template import MultiComboBox
from src.utils.errors_util import Dialog, create_help_icon
from src.utils.str_util import validate_data, text_to_arr, to_dict
# from src.utils.fs_util import create_collection
from src.utils.config_util import config
from datetime import datetime



from src.utils.fs_util import create_folder_on_disk
from src.utils.sql_util import Sql

RADIO_HELP_MESSAGE = '''"Copy files" - will copy all files and put them in your folder
"Move files" - will move files from original path, to created folder path'''

class InitWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.input_fields = {}
        self.form_labels = {}
        self.action_buttons = {}
        self.radio_buttons = {}
        self.tags_combobox = MultiComboBox()
        self.log_output = QTextEdit()

        self.file_paths = []

        layout = QGridLayout(self)

        self.form_labels['title'] = QLabel('Title:')
        self.input_fields['title'] = QLineEdit()

        self.form_labels['tags'] = QLabel('Tags:')

        self.action_buttons['select_files'] = QPushButton('Select file(s)')
        self.action_buttons['select_files'].clicked.connect(self.select_files)

        self.action_buttons['init'] = QPushButton('Init Collection')
        self.action_buttons['init'].clicked.connect(self.approve_creation)
        self.input_fields['title'].setPlaceholderText('NAME_OF_FOLDER')
        self.log_output.setReadOnly(True)

        layout.addWidget(self.form_labels['title'],           0, 0, 1, 1)
        layout.addWidget(self.input_fields['title'],          0, 1, 1, 1)

        layout.addWidget(self.form_labels['tags'],            1, 0, 1, 1)
        layout.addWidget(self.tags_combobox,                  1, 1, 1, 1)

        layout.addWidget(self.action_buttons['select_files'], 2, 0, 1, 2)

        self.form_labels['type'] = QLabel('Type:')
        self.radio_buttons['copy'] = QRadioButton('Copy files')
        self.radio_buttons['move'] = QRadioButton('Move files')

        self.radio_buttons['copy'].setChecked(True)
        self.radio_buttons['copy'].setToolTip('File(s) will be copied')
        self.radio_buttons['move'].setToolTip('File(s) will be moved')

        self.radio_group = QButtonGroup(self)
        self.radio_group.addButton(self.radio_buttons['copy'], 0)
        self.radio_group.addButton(self.radio_buttons['move'], 1)

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.radio_buttons['copy'])
        radio_layout.addWidget(self.radio_buttons['move'])
        radio_layout.addWidget(create_help_icon(self, RADIO_HELP_MESSAGE))
        radio_layout.addStretch() 

        layout.addWidget(self.form_labels['type'],            3, 0, 1, 1)
        layout.addLayout(radio_layout,                        3, 1, 1, 1)

        layout.addWidget(self.action_buttons['init'],         4, 0, 1, 2)
        layout.addWidget(self.log_output,                     5, 0, 1, 2)

    def select_files(self):
        self.file_paths, _ = QFileDialog.getOpenFileNames(
            parent = self,
            caption = 'Select file(s)',
            directory = os.path.expanduser('~'),
        )

    def approve_creation(self):
        # Get values from QLineEdit, QComboBox & QFileDialog
        title = self.input_fields['title'].text()
        tags = self.tags_combobox.value()
        file_paths = self.file_paths
        files = [os.path.basename(path) for path in file_paths]
        move = bool(self.radio_group.checkedId())

        # Validation
        data = to_dict(title, tags, files)
        is_valid, error_msg = validate_data(data)

        print(is_valid, error_msg)

        if is_valid:
            # Adding to db
            sql = Sql()
            sql.add_folder_to_db(title, tags, files)
            sql.close()

            # Adding to disk
            folder_path = create_folder_on_disk(title, file_paths, move)

            self.log_text_edit(f'✅ Created on path: {folder_path}')
        else:
            Dialog.error(self, 'Error', 'Validation error:', error_msg)

    def log_text_edit(self, text):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.log_output.setText(self.log_output.toPlainText() + f'[{now}] {text}\n')

    def fetch_tags(self):
        self.tags_combobox.clear()
        sql = Sql()
        [self.tags_combobox.addItem(tag['name'], tag['id']) for tag in sql.fetch_tags_from_db()]
        sql.close()
        self.tags_combobox.lineEdit().setText('')

    def showEvent(self, event):
        super().showEvent(event)
        self.fetch_tags()
        
        