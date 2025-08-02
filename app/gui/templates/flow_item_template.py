from PyQt6.QtWidgets import QSizePolicy,QSizePolicy, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from app.utils.str_util import filter_images, elide_text
from app.utils.fs_util import get_file_paths_in_folder
from app.gui.templates.item_template import ItemTemplate

class FlowItemTemplate(ItemTemplate):
    def __init__(self, data):
        super().__init__(data)
        
        file_paths = get_file_paths_in_folder(self.title, self.files)
        self.pic_path = filter_images(file_paths)
        self.pixmap = QPixmap(self.pic_path)
        
        layout = QVBoxLayout(self)

        self.pic_label = QLabel()

        self.title_label = QLabel()
        self.title_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        layout.addWidget(self.pic_label)
        layout.addWidget(self.title_label)

    def resize_image(self, height: int = 100):
        width = (self.pixmap.width() * height) // self.pixmap.height()
        scaled_pixmap = self.pixmap.scaled(
            width,
            height,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.pic_label.setPixmap(scaled_pixmap)
        self.title_label.setText(elide_text(self.title, scaled_pixmap.width(), self.title_label.font()))