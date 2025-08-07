from PyQt6.QtWidgets import QWidget, QSizePolicy,QSizePolicy, QGridLayout, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap, QMouseEvent
from PyQt6.QtCore import Qt, pyqtSignal

# from app.utils.str_util import filter_images
# from app.utils.fs_util import get_file_paths_in_folder
from app.gui.templates.item_template import ItemTemplate

class ColumnsItemTemplate(ItemTemplate):
    def __init__(self, data):
        super().__init__(data)

        # file_paths = get_file_paths_in_folder(self.title, self.files)
        # self.pic_path = filter_images(file_paths)
        # self.pixmap = QPixmap(self.pic_path)
        self.pixmap = QPixmap('app/resources/pic.png')
        
        layout = QGridLayout(self)

        self.pic_label = QLabel()

        labels = {}

        labels['id'] = QLabel()
        labels['title'] = QLabel()
        labels['tags'] = QLabel()
        labels['files'] = QLabel()
        labels['created_at'] = QLabel()
        labels['updated_at'] = QLabel()

        labels['id'].setText(f'ID: {str(self.id)}')
        labels['title'].setText(f'TITLE: {self.title}')
        labels['tags'].setText(f'TAGS: {',\n'.join(self.tags['names'])}')
        labels['files'].setText(f'FILES: {', '.join(self.files)}')
        labels['created_at'].setText(f'CREATED_AT: {self.created_at}')
        labels['updated_at'].setText(f'UPDATED_AT: {self.updated_at}')

        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)
        container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        for _, item in labels.items():
            container_layout.addWidget(item)
        
        layout.addWidget(self.pic_label, 0, 0)
        layout.addWidget(container_widget, 0, 1)

    def resize_image(self, height: int = 100):
        width = (self.pixmap.width() * height) // self.pixmap.height()
        scaled_pixmap = self.pixmap.scaled(
            width,
            height,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.pic_label.setPixmap(scaled_pixmap)
        # self.title_label.setText(elide_text(self.title, scaled_pixmap.width(), self.title_label.font()))