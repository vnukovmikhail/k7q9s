from pathlib import Path
# import cv2

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QMouseEvent, QPixmap, QMovie
from PyQt6.QtCore import Qt, pyqtSignal

from app.utils.str_util import elide_text

class FileTemplate(QWidget):
    clicked = pyqtSignal()
    def __init__(self, file_path: str):
        super().__init__()

        # self.pixmap = QPixmap(file_path)
        self.pic_label = QLabel()

        layout = QVBoxLayout(self)
        layout.addWidget(self.pic_label)

        ext = Path(file_path).suffix.lower()

        if ext in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']:
            self.pixmap = QPixmap(str(file_path))
        elif ext in ['.mp4', '.avi', '.mov', '.mkv', '.webm']:
            self.pixmap = QPixmap('app/resources/pic.png')
        else:
            self.pixmap = QPixmap('app/resources/pic.png') 

    def resize_image(self, height: int = 70):
        width = (self.pixmap.width() * height) // self.pixmap.height()
        scaled_pixmap = self.pixmap.scaled(
            width,
            height,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.pic_label.setPixmap(scaled_pixmap)

    # def mousePressEvent(self, event: QMouseEvent):
    #     if event.button() == Qt.MouseButton.LeftButton:
    #         self.clicked.emit()
    #         print('[~] ->', f'{self.id} {self.title} {self.tags} {self.files} {self.created_at} {self.updated_at}')
    #     super().mousePressEvent(event)