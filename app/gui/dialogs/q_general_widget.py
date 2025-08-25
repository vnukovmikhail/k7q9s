from PyQt6.QtWidgets import QWidget, QSizePolicy, QSlider, QSpinBox, QGridLayout, QLabel, QComboBox, QLineEdit, QPushButton, QHBoxLayout, QStyle
from PyQt6.QtCore import Qt, QTimer
import sys, os, json, shutil, time, asyncio, random, pathlib
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy, QTabWidget,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem, QTableView,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

class QGeneralWidget(QWidget):
    def __init__(self, widget_name:str):
        super().__init__()

        self.settings = QSettings('config.ini', QSettings.Format.IniFormat)

        title_label = QLabel(widget_name)
        title_label.setFont(QFont('monospace', 13, 700))

        folder_path_label = QLabel('Folder path:')

        self.folder_path_line_edit = QLineEdit()
        self.folder_path_line_edit.setReadOnly(True)

        select_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView)

        choose_folder_button = QPushButton()
        choose_folder_button.setIcon(select_icon)
        choose_folder_button.setFixedSize(24, 16)
        choose_folder_button.setFlat(True)
        choose_folder_button.clicked.connect(self.select_folder)

        h_layout = QHBoxLayout()
        h_layout.addWidget(folder_path_label)
        h_layout.addWidget(self.folder_path_line_edit)
        h_layout.addWidget(choose_folder_button)

        layout = QVBoxLayout(self)
        layout.addWidget(title_label)
        layout.addLayout(h_layout)
        layout.addStretch()

        self.update_ui()

    def update_ui(self):
        folder_path = self.settings.value('User/Folder', pathlib.Path(__file__).resolve().parent)
        self.folder_path_line_edit.setText(folder_path)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose folder')
        if folder_path:
            self.settings.setValue('User/Folder', str(folder_path))
            self.update_ui()