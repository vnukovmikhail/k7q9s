from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtCore import Qt, pyqtSignal

class ItemTemplate(QWidget):
    clicked = pyqtSignal()
    def __init__(self, data):
        super().__init__()

        self.id = data['id']
        self.title = data['name']
        self.tags = data['tags']
        self.files = data['files']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
            print('[~] ->', f'{self.id} {self.title} {self.tags} {self.files} {self.created_at} {self.updated_at}')
        super().mousePressEvent(event)