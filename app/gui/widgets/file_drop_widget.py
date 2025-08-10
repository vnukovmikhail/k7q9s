import sys, os, json, shutil, time, asyncio, random, pathlib, inspect
from datetime import datetime

from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit, QStyle)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel, QDropEvent, QDragEnterEvent
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel

from app.gui.widgets.flow_scroll_widget import FlowScrollWidget
from app.gui.templates.file_template import FileTemplate

class FileDropWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # icon_label = QLabel()
        # icon_pixmap = self.style().standardPixmap(QStyle.StandardPixmap.SP_FileDialogNewFolder)
        # icon_label.setPixmap(icon_pixmap)
        # icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.flow_scroll = FlowScrollWidget()

        self.setAcceptDrops(True)

        self.label = QLabel("Перетащи сюда файлы")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        add_pixmap = self.style().standardPixmap(QStyle.StandardPixmap.SP_FileDialogListView)

        # label = QLabel()
        # label.setPixmap(add_pixmap)
        # label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QGridLayout(self)
        layout.addWidget(self.flow_scroll, 0, 0)
        # layout.addWidget(icon_label, 0, 0)
        layout.setContentsMargins(0, 0, 0, 0)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            file_paths = []
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                file_paths.append(file_path)

            self.handle_files_dropped(file_paths)
            self.test(file_paths)
            event.acceptProposedAction()
        else:
            event.ignore()

    def handle_files_dropped(self, file_paths):
        self.label.setText("Файлы:\n" + "\n".join(file_paths))
        print("Файлы были перетащены:", file_paths)

    def test(self, file_paths: list[str]):
        self.flow_scroll.clear()
        for file_path in file_paths:
            item_template = FileTemplate(file_path)
            item_template.resize_image()
            self.flow_scroll.addWidget(item_template)
            

