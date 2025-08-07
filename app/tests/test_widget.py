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

from app.utils.sql_util import SQLITE_PATH

class TestWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.create_connection()

        folder_tags_model = QSqlTableModel()
        folder_tags_model.setTable('folder_tags')
        folder_tags_model.select()
        self.view0 = QTableView()
        self.view0.setModel(folder_tags_model)

        tags_model = QSqlTableModel()
        tags_model.setTable('tags')
        tags_model.select()
        self.view1 = QTableView()
        self.view1.setModel(tags_model)

        folders_model = QSqlTableModel()
        folders_model.setTable('folders')
        folders_model.select()
        self.view2 = QTableView()
        self.view2.setModel(folders_model)

        folder_files_model = QSqlTableModel()
        folder_files_model.setTable('folder_files')
        folder_files_model.select()
        self.view3 = QTableView()
        self.view3.setModel(folder_files_model)

        layout = QGridLayout(self)
        layout.addWidget(self.view0, 0, 0)
        layout.addWidget(self.view3, 0, 1)
        layout.addWidget(self.view1, 0, 2)
        layout.addWidget(self.view2, 1, 0, 1, 3)
        

    def create_connection(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(SQLITE_PATH)
        if not db.open():
            print('fd')
            return False
        return True

    def showEvent(self, event):
        super().showEvent(event)
        self.view0.model().select()
        self.view1.model().select()
        self.view2.model().select()