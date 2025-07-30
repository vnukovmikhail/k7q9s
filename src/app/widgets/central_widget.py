import sys, os, json, shutil, time, asyncio, random, pathlib
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy, QTabWidget, QWidgetAction,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel

from src.app.widgets.fetch_widget import FetchWidget
from src.app.widgets.create_widget import InitWidget
from src.app.widgets.config_widget import ConfigWidget
from src.app.widgets.settings_widget import SettingsWidget

class CentralWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.addTab(FetchWidget(), 'tab_1')
        self.addTab(InitWidget(), 'tab_2')
        self.addTab(ConfigWidget(), 'tab_3')
        self.addTab(SettingsWidget(), 'tab_4')

        actions = [
            QAction('action_1', self),
            QAction('action_2', self),
            QAction('action_3', self)
        ]
        for action in actions:
            action.triggered.connect(lambda _, text=action.text(): print(text))
        self.addActions(actions)

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)