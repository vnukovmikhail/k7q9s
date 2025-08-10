from PyQt6.QtWidgets import QWidget, QSizePolicy, QSlider, QSpinBox, QGridLayout, QLabel, QComboBox, QLineEdit, QPushButton, QHBoxLayout, QStyle
from PyQt6.QtCore import Qt, QTimer

from app.gui.widgets.flow_scroll_widget import FlowScrollWidget
from app.gui.templates.multi_combobox_template import MultiComboBox
from app.repositories.folder_repository import fetchall_folders, VALID_ORDER_FIELDS
from app.repositories.tag_repository import fetchall_tags

# Types of templates
from app.gui.templates.flow_item_template import FlowItemTemplate
from app.gui.templates.columns_item_template import ColumnsItemTemplate

class FolderViewerWidget(QWidget):
    def __init__(self):
        super().__init__()

        MIN_VALUE = 0
        MAX_VALUE = 1000
        DEFAULT_VALUE = 150
        self.PAGE = 1
        self.PAGE_SIZE = 50
        self.TOTAL_PAGES = None

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
        self.order_by_comboBox.addItems(VALID_ORDER_FIELDS)
        self.order_by_comboBox.currentIndexChanged.connect(self.fetch_folders)

        self.desc_comboBox = QComboBox()
        self.desc_comboBox.addItem('desc', True)
        self.desc_comboBox.addItem('asc', False)
        self.desc_comboBox.currentIndexChanged.connect(self.fetch_folders)

        self.search_field = QComboBox()
        self.search_field.addItems(VALID_ORDER_FIELDS)
        self.search_field.currentIndexChanged.connect(self.fetch_folders)

        self.search_value = QLineEdit()
        self.search_value.textChanged.connect(self.fetch_folders)

        self.tags_combobox = MultiComboBox()
        self.tags_combobox.currentTextChanged.connect(self.reset_page)
        self.tags_combobox.currentTextChanged.connect(self.fetch_folders)

        prev_button = QPushButton()
        prev_button.setFixedSize(24, 24)
        prev_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowLeft))
        prev_button.clicked.connect(lambda:self.change_page(-1))
        self.page_label = QLabel(str(self.PAGE))
        next_button = QPushButton()
        next_button.setFixedSize(24, 24)
        next_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowRight))
        next_button.clicked.connect(lambda:self.change_page(+1))

        layout = QGridLayout(self)
        layout.addWidget(self.search_field,      0, 1)
        layout.addWidget(self.search_value,      0, 2)
        layout.addWidget(self.order_by_comboBox, 0, 3)
        layout.addWidget(self.desc_comboBox,     0, 4)
        layout.addWidget(self.tags_combobox,     0, 5, 1, 2)

        layout.addWidget(self.flow_widget,       1, 0, 1, 7)

        pagination_layout = QHBoxLayout()
        pagination_layout.addWidget(prev_button)
        pagination_layout.addWidget(self.page_label)
        pagination_layout.addWidget(next_button)
        pagination_layout.addStretch()

        layout.addLayout(pagination_layout,      2, 0, 1, 3)
        layout.addWidget(size_label,             2, 4, 1, 1)
        layout.addWidget(self.size_slider,       2, 5, 1, 1)
        layout.addWidget(size_spinBox,           2, 6, 1, 1)



    def showEvent(self, event):
        super().showEvent(event)
        # self.fetch_folders()
        # self.fetch_tags()

    def reset_page(self):
        self.PAGE = 1
        self.page_label.setText(str(self.PAGE))
        # self.fetch_folders()

    def change_page(self, x:int):
        new_page = self.PAGE + x
        if 1 <= new_page <= self.TOTAL_PAGES:
            self.PAGE = new_page
            self.page_label.setText(str(self.PAGE))
            self.fetch_folders()
        
    def fetch_folders(self):
        return
        order_by: str = self.order_by_comboBox.currentText()
        desc: bool = self.desc_comboBox.currentData()
        search_field: str = self.search_field.currentText()
        search_value: str = self.search_value.text()
        tag_ids: list[int] = self.tags_combobox.value()

        self.flow_widget.clear()
        self.item_templates.clear()

        result = fetchall_folders(order_by, desc, search_field, search_value, tag_ids, self.PAGE, self.PAGE_SIZE)
        self.TOTAL_PAGES = result['result']['total_pages']
        print(result['result'])

        for folder in result['folders']:
            item_template = FlowItemTemplate(folder)
            self.item_templates.append(item_template)
            self.flow_widget.addWidget(item_template)

        self.img_size_change()

    def fetch_tags(self):
        self.tags_combobox.clear()
        [self.tags_combobox.addItem(tag['name'], tag['id']) for tag in fetchall_tags()]

    def img_size_change(self):
        for item_template in self.item_templates:
            item_template.resize_image(self.size_slider.value())