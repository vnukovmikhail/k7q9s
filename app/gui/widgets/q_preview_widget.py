from PyQt6.QtWidgets import QWidget, QSizePolicy, QSlider, QSpinBox, QGridLayout, QLabel, QComboBox, QLineEdit, QPushButton, QHBoxLayout, QStyle
from PyQt6.QtCore import Qt, QTimer
import sys, os, json, shutil, time, asyncio, random, pathlib
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy, QTabWidget,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton, QTableWidget,
                             QProgressBar, QSlider, QSpinBox, QTimeEdit, QDial, QFontComboBox, QLCDNumber,
                             QFileDialog, QMessageBox, QComboBox, QMenu, QListWidget, QDialog, QListView,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLayoutItem, QTableView,
                             QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QSize, QSettings, QTimer, QEvent, QStringListModel
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

from app.gui.widgets.flow_scroll_widget import FlowScrollWidget
from app.gui.templates.multi_combobox_template import MultiComboBox
from app.repositories.folder_repository import fetchall_folders, VALID_ORDER_FIELDS
from app.repositories.tag_repository import fetchall_tags

# Types of templates
from app.gui.templates.flow_item_template import FlowItemTemplate
from app.gui.templates.columns_item_template import ColumnsItemTemplate
from app.gui.widgets.multi_list_widget import MultiListWidget
from app.gui.widgets.pagination_widget import PaginationWidget

class QPreviewWidget(QWidget):
    def __init__(self):
        super().__init__()

        MIN_VALUE = 50
        MAX_VALUE = 1000
        DEFAULT_VALUE = 100

        self.item_templates = []

        """ PAGINATION LAYOUT """
        self.pagination_widget = PaginationWidget()

        """ SIZE EDITITNG LAYOUT """
        size_label = QLabel('Image_size:')
        size_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter)

        size_slider = QSlider()
        size_slider.setOrientation(Qt.Orientation.Horizontal)
        size_slider.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        size_slider.setMinimum(MIN_VALUE)
        size_slider.setMaximum(MAX_VALUE)
        size_slider.setValue(DEFAULT_VALUE)

        self.size_spinbox = QSpinBox()
        self.size_spinbox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.size_spinbox.setMinimum(MIN_VALUE)
        self.size_spinbox.setMaximum(MAX_VALUE)
        self.size_spinbox.setValue(DEFAULT_VALUE)

        edit_layout = QHBoxLayout()
        edit_layout.addWidget(size_label)
        edit_layout.addWidget(size_slider)
        edit_layout.addWidget(self.size_spinbox)
        edit_layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        size_slider.valueChanged.connect(self.size_spinbox.setValue)
        self.size_spinbox.valueChanged.connect(size_slider.setValue)
        self.size_spinbox.valueChanged.connect(self.img_size_change)

        """ SEARCH LAYOUT """
        self.list_widget = MultiListWidget()

        search_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('search_by_name...')
        # search_input.addAction(search_icon, QLineEdit.ActionPosition.TrailingPosition)

        search_button = QPushButton()
        search_button.setIcon(search_icon)
        search_button.setFixedSize(16, 16)
        search_button.setFlat(True)

        search_bar_layout = QHBoxLayout()
        search_bar_layout.addWidget(self.search_input)
        search_bar_layout.addWidget(search_button)

        self.order_by_combobox = QComboBox()
        self.order_by_combobox.addItems(VALID_ORDER_FIELDS)

        radio_desc = QRadioButton('desc')
        radio_asc = QRadioButton('asc')
        radio_desc.setChecked(True)

        self.radio_group = QButtonGroup(self)
        self.radio_group.addButton(radio_desc)
        self.radio_group.addButton(radio_asc)
        
        sort_layout = QHBoxLayout()
        sort_layout.addWidget(self.order_by_combobox)
        sort_layout.addWidget(radio_desc)
        sort_layout.addWidget(radio_asc)
        sort_layout.addStretch()

        search_layout = QVBoxLayout()
        search_layout.addLayout(search_bar_layout)
        search_layout.addLayout(sort_layout)
        search_layout.addWidget(self.list_widget)

        search_layout.addStretch()
        """"""
        
        self.flow_widget = FlowScrollWidget()

        layout = QGridLayout(self)
        layout.addWidget(self.flow_widget,       0, 0, 2, 1)
        layout.addLayout(search_layout,     0, 1, 1, 2)
        layout.addWidget(self.pagination_widget, 2, 0, 1, 1)
        layout.addLayout(edit_layout,       2, 1, 1, 2)

        self.list_widget.clicked.connect(self.fetch_folders)
        self.search_input.returnPressed.connect(self.fetch_folders)
        search_button.clicked.connect(lambda _:self.fetch_folders())
        self.radio_group.buttonClicked.connect(lambda _:self.fetch_folders())
        self.order_by_combobox.currentIndexChanged.connect(lambda _:self.fetch_folders())
        self.pagination_widget.page_changed.connect(self.fetch_folders)

        """"""
        

    def showEvent(self, event):
        super().showEvent(event)
        self.fetch_folders()
        self.fetch_tags() 

    def fetch_tags(self):
        self.list_widget.clear()
        [self.list_widget.addItem(tag['name'], tag['id']) for tag in fetchall_tags()]

    def fetch_folders(self, page: int = 1, page_size: int = 20):
        order_by = self.order_by_combobox.currentText()
        desc = True if self.radio_group.checkedButton().text() == 'desc' else False
        search_field = 'name'
        search_value = self.search_input.text()
        tag_ids = self.list_widget.value()

        print(f"{order_by}_{desc}_'{search_value}'_{tag_ids}")
        self.flow_widget.clear()
        self.item_templates.clear()

        result = fetchall_folders(order_by, desc, search_field, search_value, tag_ids, page, page_size)
        # print(result['folders'])

        self.pagination_widget.set(result['result']['total_pages'])
        self.pagination_widget.set_page(page, False)

        for folder in result['folders']:
            item_template = FlowItemTemplate(folder)
            self.item_templates.append(item_template)
            self.flow_widget.addWidget(item_template)

        self.img_size_change()

    def img_size_change(self):
        value = self.size_spinbox.value()
        for item_template in self.item_templates:
            item_template.resize_image(value)