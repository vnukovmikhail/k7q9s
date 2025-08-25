from pathlib import Path
from PyQt6.QtWidgets import QDialog, QFileDialog, QLabel, QPushButton, QHBoxLayout, QLineEdit, QListWidget, QStackedWidget, QSizePolicy
from PyQt6.QtCore import QSettings, Qt

from app.gui.dialogs.q_general_widget import QGeneralWidget

class PreferencesDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle('Preferences')
        self.setMinimumSize(556, 256)

        all_items = {
            'General': QGeneralWidget,
        }

        list = QListWidget()
        list.setMaximumWidth(100)
        stack = QStackedWidget()

        for i, (key, value) in enumerate(all_items.items()):
            list.insertItem(i, key)
            stack.addWidget(value(key))
            # print(i, key, value)

        list.currentRowChanged.connect(stack.setCurrentIndex)

        layout = QHBoxLayout(self)
        layout.addWidget(list)
        layout.addWidget(stack)