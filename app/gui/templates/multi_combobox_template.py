from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QStandardItem
from PyQt6.QtCore import Qt

class MultiComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().installEventFilter(self)
        self.model().dataChanged.connect(self.updateLineEdit)
        self._existing_items = set()

    def updateLineEdit(self):
        text_container = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.CheckState.Checked:
                text_container.append(self.model().item(i).text())
        text_string = ', '.join(text_container)
        self.lineEdit().setText(text_string)    

    def addItems(self, items, itemList=None):
        for id, text in enumerate(items):
            try:
                data = itemList[id] if itemList else None
            except (TypeError, IndexError):
                data = None
            
            item_key = (text, data)
            if item_key not in self._existing_items:
                self.addItem(text, data)
                self._existing_items.add(item_key)

    def addItem(self, text, userData=None):
        item_key = (text, userData)
        if item_key in self._existing_items:
            return
            
        item = QStandardItem()
        item.setText(text)

        if userData is not None:
            item.setData(userData)

        item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
        item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole) 

        self.model().appendRow(item)
        self._existing_items.add(item_key)

    def value(self):
        ids = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.CheckState.Checked:
                user_data = self.model().item(i).data()
                if user_data is not None:
                    ids.append(user_data)
        return ids

    def clear(self):
        super().clear()
        self._existing_items.clear()