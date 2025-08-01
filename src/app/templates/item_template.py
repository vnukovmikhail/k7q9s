from PyQt6.QtWidgets import QWidget, QSizePolicy,QSizePolicy, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap, QMouseEvent
from PyQt6.QtCore import Qt, pyqtSignal

from src.utils.str_util import filter_images, elide_text
from src.utils.fs_util import get_file_paths_in_folder

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

        file_paths = get_file_paths_in_folder(self.title, self.files)
        self.pic_path = filter_images(file_paths)
        
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
            print('->', f'{self.id} {self.title} {self.tags} {self.files} {self.created_at} {self.updated_at}')
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