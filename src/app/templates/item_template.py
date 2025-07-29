from PyQt6.QtWidgets import QWidget, QSizePolicy,QSizePolicy, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap, QMouseEvent
from PyQt6.QtCore import Qt, pyqtSignal

from src.utils.str_util import filter_images, elide_text

class ItemTemplate(QWidget):
    clicked = pyqtSignal()
    def __init__(self, data):
        super().__init__()
        self.title = data['meta']['title']
        self.tags = data['meta']['tags']
        self.created_at = data['meta']['created_at']
        self.folder_path = data['folder_path']
        self.pic_path = filter_images(data['files'])

        # print(data)
        
        layout = QVBoxLayout(self)

        self.pic_label = QLabel()
        self.pixmap = QPixmap(self.pic_path)

        self.title_label = QLabel()
        self.title_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        layout.addWidget(self.pic_label)
        layout.addWidget(self.title_label)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
            print('->', self.title)
        super().mousePressEvent(event)

    def resize_image2(self, height=500):
        width = (self.pixmap.width() * height) // self.pixmap.height()
        scaled_pixmap = self.pixmap.scaled(
            width,
            height,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.pic_label.setPixmap(scaled_pixmap)
        self.title_label.setText(elide_text(self.title, scaled_pixmap.width(), self.title_label.font()))