from PyQt6.QtWidgets import QWidget, QSizePolicy, QSlider, QSpinBox, QGridLayout, QLabel, QComboBox, QLineEdit
from PyQt6.QtCore import Qt

from app.gui.widgets.flow_scroll_widget import FlowScrollWidget
from app.gui.templates.multi_combobox_template import MultiComboBox

# Types of templates
from app.gui.templates.flow_item_template import FlowItemTemplate
from app.gui.templates.columns_item_template import ColumnsItemTemplate

from app.repositories.folder_repository import FolderRepository
from app.repositories.tag_repository import TagRepository
from app.utils.sql_util import VALID_COLUMNS

class FolderViewerWidget(QWidget):
    def __init__(self):
        super().__init__()

        MIN_VALUE = 0
        MAX_VALUE = 1000
        DEFAULT_VALUE = 300
        
        layout = QGridLayout(self)

        self.flow_widget = FlowScrollWidget()

        self.item_templates = []

        self.size_slider = QSlider()
        self.size_slider.setOrientation(Qt.Orientation.Horizontal)
        self.size_slider.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.size_slider.setMinimum(MIN_VALUE)
        self.size_slider.setMaximum(MAX_VALUE)
        self.size_slider.setValue(DEFAULT_VALUE)

        size_label = QLabel('Image size:')
        size_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        size_spinBox = QSpinBox()
        size_spinBox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        size_spinBox.setMinimum(MIN_VALUE)
        size_spinBox.setMaximum(MAX_VALUE)
        size_spinBox.setValue(DEFAULT_VALUE)

        self.size_slider.valueChanged.connect(size_spinBox.setValue)
        size_spinBox.valueChanged.connect(self.size_slider.setValue)

        self.size_slider.valueChanged.connect(self.img_size_change)

        self.order_by_comboBox = QComboBox()
        self.order_by_comboBox.addItems(VALID_COLUMNS)
        self.order_by_comboBox.currentIndexChanged.connect(self.fetch_folders)

        self.desc_comboBox = QComboBox()
        self.desc_comboBox.addItem('desc', True)
        self.desc_comboBox.addItem('asc', False)
        self.desc_comboBox.currentIndexChanged.connect(self.fetch_folders)

        self.search_field = QComboBox()
        self.search_field.addItems(VALID_COLUMNS)
        self.search_field.currentIndexChanged.connect(self.fetch_folders)

        self.search_value = QLineEdit()
        self.search_value.textChanged.connect(self.fetch_folders)

        self.tags_combobox = MultiComboBox()
        self.tags_combobox.currentTextChanged.connect(self.fetch_folders)
        self.tags_combobox.lineEdit().setText('')

        layout.addWidget(self.search_field,      0, 0, 1, 1)
        layout.addWidget(self.search_value,      0, 1, 1, 1)
        layout.addWidget(self.order_by_comboBox, 0, 2, 1, 1)
        layout.addWidget(self.desc_comboBox,     0, 3, 1, 1)
        layout.addWidget(self.tags_combobox,     0, 4, 1, 3)

        layout.addWidget(self.flow_widget,       1, 0, 1, 7)
        
        layout.addWidget(size_label,             2, 4, 1, 1)
        layout.addWidget(self.size_slider,       2, 5, 1, 1)
        layout.addWidget(size_spinBox,           2, 6, 1, 1)

    def showEvent(self, event):
        super().showEvent(event)
        self.fetch_folders()
        self.fetch_tags()
        
    def fetch_folders(self):
        order_by: str = self.order_by_comboBox.currentText()
        desc: bool = self.desc_comboBox.currentData()
        search_field: str = self.search_field.currentText()
        search_value: str = self.search_value.text()
        tag_ids: list[int] = self.tags_combobox.value()

        self.flow_widget.clear()
        self.item_templates.clear()

        folder_repo = FolderRepository()

        folder_items = folder_repo.fetchall(order_by, desc, search_field, search_value, tag_ids)
        for folder_item in folder_items:
            item_template = FlowItemTemplate(folder_item)
            self.item_templates.append(item_template)
            self.flow_widget.addWidget(item_template)

        self.img_size_change()

    def fetch_tags(self):
        tag_repo = TagRepository()
        [self.tags_combobox.addItem(tag['name'], tag['id']) for tag in tag_repo.fetchall()]

    def img_size_change(self):
        for item_template in self.item_templates:
            item_template.resize_image(self.size_slider.value())