from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QStandardItem, QStandardItemModel, QMouseEvent
from PyQt6.QtCore import Qt, QEvent

class MultiComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.setModel(QStandardItemModel(self))
        self.model().dataChanged.connect(self.updateLineEdit)
        self.lineEdit().installEventFilter(self)

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
            self.addItem(text, data)

    def addItem(self, text, userData=None):
        item = QStandardItem()
        item.setText(text)

        if userData is not None:
            item.setData(userData)

        item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
        item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole) 

        self.model().appendRow(item)

        self.setCurrentIndex(-1)

    def value(self):
        ids = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.CheckState.Checked:
                user_data = self.model().item(i).data()
                if user_data is not None:
                    ids.append(user_data)
        return ids

    def eventFilter(self, obj, event):
        if obj == self.lineEdit() and event.type() == QEvent.Type.MouseButtonPress: 
            self.showPopup()
            return True
        return super().eventFilter(obj, event)

    def clear(self):
        self.model().clear()
        self.lineEdit().clear()

    