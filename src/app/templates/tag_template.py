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

class TagTemplate(QWidget):
    deleted = pyqtSignal(str)

    def __init__(self, data):
        super().__init__()
        self.tag = data

        layout = QHBoxLayout(self)

        label = QLabel(self.tag)

        button = QPushButton()
        button.setIcon(QIcon.fromTheme('edit-delete'))
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
                self.deleted.emit(self.tag)
                self.deleteLater()