from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtCore import Qt, pyqtSignal

from app.db.models import FolderModel

class ItemTemplate(QWidget):
    clicked = pyqtSignal()
    def __init__(self, folder_model:FolderModel):
        super().__init__()

        self.id = folder_model.id
        self.title = folder_model.name
        self.tags = folder_model.tags
        self.files = folder_model.files
        self.created_at = folder_model.created_at
        self.updated_at = folder_model.updated_at

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
            print('[~] ->', f'{self.id} {self.title} {self.tags} {self.files} {self.created_at} {self.updated_at}')
        super().mousePressEvent(event)