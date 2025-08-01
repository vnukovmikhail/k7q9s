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

from src.utils.sql_util import DB_PATH, Sql

class SettingsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.create_connection()

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search by name...")

        check_button = QPushButton('Print all')
        check_button.clicked.connect(lambda:Sql().print_all())

        self.model = QSqlTableModel()
        self.model.setTable('folder_tags')
        self.model.select()
        self.view = QTableView()
        self.view.setModel(self.model)

        model1 = QSqlTableModel()
        model1.setTable('tags')
        model1.select()
        self.view1 = QTableView()
        self.view1.setModel(model1)

        model2 = QSqlTableModel()
        model2.setTable('folders')
        model2.select()
        self.view2 = QTableView()
        self.view2.setModel(model2)

        self.search_box.textChanged.connect(self.apply_filter)

        layout = QGridLayout(self)
        
        layout.addWidget(self.view, 0, 0, 1, 2)
        layout.addWidget(self.view1, 0, 2,)
        layout.addWidget(self.search_box, 1, 0, 1, 3)
        layout.addWidget(self.view2, 2, 0, 1, 3)
        layout.addWidget(check_button, 3, 0, 1, 3)

    def create_connection(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(DB_PATH)
        if not db.open():
            print('Failed to connect to the database.')
            return False
        return True

    def apply_filter(self, text):
        text = text.replace("'", "''")
        if text:
            self.model.setFilter(f"name LIKE '%{text}%'")
        else:
            self.model.setFilter("")

    def showEvent(self, event):
        super().showEvent(event)
        self.view.model().select()
        self.view1.model().select()
        self.view2.model().select()
        print('update tables')

    
