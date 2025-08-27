from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QPushButton
)
from PyQt6.QtCore import Qt, pyqtSignal
import sys

class MultiListWidget(QWidget):
    clicked = pyqtSignal()
    def __init__(self, hide: bool = False):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText('search_tag...')
        self.search_box.textChanged.connect(self.filter_tags)
        layout.addWidget(self.search_box)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        if not hide:
            self.button = QPushButton('Find')
            self.button.clicked.connect(self.print_selected_tags)
            layout.addWidget(self.button)

    def addItem(self, name: str, id: int):
        item = QListWidgetItem(name)
        item.setData(Qt.ItemDataRole.UserRole, id)
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        item.setCheckState(Qt.CheckState.Unchecked)
        self.list_widget.addItem(item)

    def filter_tags(self, text: str):
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            item.setHidden(text.lower() not in item.text().lower())

    def value(self):
        selected = []
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                selected.append(item.text())
        return selected
    
    def clear(self):
        self.list_widget.clear()

    def print_selected_tags(self):
        selected = []
        selected_ids = []
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                selected.append(item.text())
                selected_ids.append(item.data(Qt.ItemDataRole.UserRole))
        print('Selected Tags:', selected)
        print('IDs:', selected_ids)
        self.clicked.emit()