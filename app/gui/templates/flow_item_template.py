from PyQt6.QtWidgets import QSizePolicy,QSizePolicy, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from app.utils.str_util import elide_text, full_paths, image_filter
from app.gui.templates.item_template import ItemTemplate

class FlowItemTemplate(ItemTemplate):
    def __init__(self, data):
        super().__init__(data)
        file_paths = full_paths(self.title, self.files)
        filtered_paths = image_filter(file_paths)
        self.pic_paths = filtered_paths[0] if filtered_paths else 'app/resources/pic.png'
        
        self.pixmap = QPixmap(self.pic_paths)

        # self.pixmap = QPixmap('app/resources/pic.png')
        
        self.pic_label = QLabel()

        self.title_label = QLabel()
        self.title_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.pic_label)
        layout.addWidget(self.title_label)

        self.resize_image()

    def resize_image(self, height: int = 150):
        width = (self.pixmap.width() * height) // self.pixmap.height()
        scaled_pixmap = self.pixmap.scaled(
            width,
            height,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.pic_label.setPixmap(scaled_pixmap)
        self.title_label.setText(elide_text(self.title, scaled_pixmap.width(), self.title_label.font()))