import sys, os, json, shutil, time, asyncio, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy, QGraphicsView, QGraphicsScene, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem, QScrollArea,
                             QLabel, QLineEdit, QTextEdit, QStyle)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QMouseEvent, QFontMetrics
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, pyqtSignal
from typing import Optional, List, Dict

from src.utils.sql_util import Sql

class TagTemplate(QWidget):
    # deleted = pyqtSignal(str)

    def __init__(self, data):
        super().__init__()
        self.id = int(data['id'])
        name = data['name']

        layout = QHBoxLayout(self)

        label = QLabel(name)

        button = QPushButton()
        icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TrashIcon)
        button.setIcon(icon)
        button.setFlat(True)
        button.setFixedSize(16, 16)
        
        layout.addWidget(label)
        layout.addWidget(button)

        button.clicked.connect(self.delete_self)

    def delete_self(self):
        parent_widget = self.parentWidget()
        if parent_widget:
            flow_layout = parent_widget.layout()
            if flow_layout:
                flow_layout.removeWidget(self)
                self.setParent(None)
                # self.deleted.emit(self.tag)

                sql = Sql()
                sql.remove_tag_from_db(self.id)
                sql.close()

                self.deleteLater()