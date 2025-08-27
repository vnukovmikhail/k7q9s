from PyQt6.QtWidgets import QWidget, QLabel, QScrollArea, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QAction, QStandardItem, QStandardItemModel, QDropEvent, QDragEnterEvent
from PyQt6.QtCore import Qt

from app.gui.layouts.flow_layout import FlowLayout
from app.gui.templates.file_template import FileTemplate

class FlowContainerWidget(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAcceptDrops(True)

        self.container = QWidget()
        self.layout = FlowLayout(self.container)
        self.container.setLayout(self.layout)

        self.placeholder = QLabel("Drag file[s] here", self.container)
        self.placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setWidgetResizable(True)
        self.setWidget(self.container)

        self.update_placeholder()

        self._files : list[str] = []

    def addItem(self, item):
        self.layout.addWidget(item)
        self.update_placeholder()

    def clear(self):
        self.layout.clear()
        self.update_placeholder()

    def update_placeholder(self):
        if self.layout.count() == 0:
            self.placeholder.show()
        else:
            self.placeholder.hide()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.placeholder:
            self.placeholder.setGeometry(self.viewport().rect())

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            file_paths = []
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                file_paths.append(file_path)
            
            self._files = file_paths
            self.test(file_paths)
            event.acceptProposedAction()
        else:
            event.ignore()

    def test(self, file_paths: list[str]):
        self.clear()
        for file_path in file_paths:
            item_template = FileTemplate(file_path)
            item_template.resize_image()
            self.addItem(item_template)

    def files(self):
        return self._files
