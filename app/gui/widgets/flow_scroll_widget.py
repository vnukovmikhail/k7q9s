from PyQt6.QtWidgets import QWidget, QScrollArea
from PyQt6.QtCore import Qt

from app.gui.layouts.flow_layout import FlowLayout

class FlowScrollWidget(QScrollArea):
    def __init__(self):
        super().__init__()

        content_widget = QWidget()

        self.flow_layout = FlowLayout(content_widget)
        self.flow_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.setWidgetResizable(True)
        self.setWidget(content_widget)

    def addWidget(self, widget):
        self.flow_layout.addWidget(widget)
        
    def clear(self):
        while self.flow_layout.count():
            item = self.flow_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        