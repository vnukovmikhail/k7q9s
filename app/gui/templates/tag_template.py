from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QStyle

from app.repositories.tag_repository import TagRepository

class TagTemplate(QWidget):
    def __init__(self, tag_name:str):
        super().__init__()
        self.t = TagRepository(tag_name)

        label = QLabel(self.t.tag_name)

        button = QPushButton()
        icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TrashIcon)
        button.setIcon(icon)
        button.setFlat(True)
        button.setFixedSize(16, 16)

        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(button)

        button.clicked.connect(self.delete_self)

    def delete_self(self):
        parent_widget = self.parentWidget()
        if parent_widget:
            flow_layout = parent_widget.layout()
            if flow_layout:
                flow_layout.removeWidget(self)
                self.setParent(None)

                self.t.delete()

                self.deleteLater()