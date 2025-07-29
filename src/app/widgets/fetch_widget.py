from PyQt6.QtWidgets import QWidget, QSizePolicy, QSlider, QSpinBox, QGridLayout, QScrollArea, QLabel
from PyQt6.QtCore import Qt

from src.app.templates.item_template import ItemTemplate
from src.app.layouts.flow_layout import FlowLayout
from src.utils.fs_util import fetch_collections

class FetchWidget(QWidget):
    def __init__(self):
        super().__init__()

        MIN_VALUE = 0
        MAX_VALUE = 1000
        DEFAULT_VALUE = 300

        collections = fetch_collections()

        layout = QGridLayout(self)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        flow_layout = FlowLayout(content_widget)
        flow_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.item_templates = []

        for collection in collections:
            item_template = ItemTemplate(collection)
            self.item_templates.append(item_template)
            flow_layout.addWidget(item_template)

        scroll_area.setWidget(content_widget)
        layout.addWidget(scroll_area, 0, 0, 1, 7)

        size_slider = QSlider()
        size_slider.setOrientation(Qt.Orientation.Horizontal)
        size_slider.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        size_slider.setMinimum(MIN_VALUE)
        size_slider.setMaximum(MAX_VALUE)
        size_slider.setValue(DEFAULT_VALUE)

        size_label = QLabel('Image size:')
        size_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        size_spinBox = QSpinBox()
        size_spinBox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        size_spinBox.setMinimum(MIN_VALUE)
        size_spinBox.setMaximum(MAX_VALUE)
        size_spinBox.setValue(DEFAULT_VALUE)

        size_slider.valueChanged.connect(size_spinBox.setValue)
        size_spinBox.valueChanged.connect(size_slider.setValue)

        size_slider.valueChanged.connect(lambda:self.img_size_change(size_slider.value()))

        layout.addWidget(size_label,   1, 4, 1, 1)
        layout.addWidget(size_slider,  1, 5, 1, 1)
        layout.addWidget(size_spinBox, 1, 6, 1, 1)

        self.img_size_change(DEFAULT_VALUE)

    def img_size_change(self, value):
        for item_template in self.item_templates:
            item_template.resize_image2(value)