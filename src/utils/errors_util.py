import sys, os, json, shutil, time, asyncio, random, pathlib
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy, QStyle, QToolTip,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel, QPoint

class Dialog:
    def error(parent, title, message, details):
        msg = QMessageBox(parent)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setDetailedText(details)
        msg.setStandardButtons(QMessageBox.StandardButton.Cancel)
        msg.exec()

    def warning(parent, title, message, details):
        msg = QMessageBox(parent)
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setDetailedText(details)
        msg.setStandardButtons(QMessageBox.StandardButton.Cancel)
        msg.exec()

    def info(parent, title, message, details):
        msg = QMessageBox(parent)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setDetailedText(details)
        msg.setStandardButtons(QMessageBox.StandardButton.Cancel)
        msg.exec()

def create_help_icon(self, tooltip_text: str) -> QLabel:
    help_label = QLabel()
    icon = self.style().standardPixmap(QStyle.StandardPixmap.SP_MessageBoxInformation)
    help_label.setPixmap(icon)

    help_label.setToolTip(tooltip_text)  
    help_label.setToolTipDuration(0)
    
    def show_tooltip(event):
        # QToolTip.showText(
        #     help_label.mapToGlobal(QPoint(0, help_label.height())),
        #     tooltip_text,
        #     help_label
        # )
        QToolTip.showText(
            help_label.mapToGlobal(QPoint(0, 0)),
            tooltip_text,
            help_label
        )
    
    def hide_tooltip(event):
        QToolTip.hideText()
    
    help_label.enterEvent = show_tooltip
    help_label.leaveEvent = hide_tooltip
    
    return help_label