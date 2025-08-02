from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QStyle

from app.repositories.tag_repository import TagRepository

class TagTemplate(QWidget):
    def __init__(self, data):
        super().__init__()
        self.id = int(data['id'])
        name = data['name']

        layout = QHBoxLayout(self)

        label = QLabel(name)

        button = QPushButton()
        icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TrashIcon)
        button.setIcon(icon)
        button.setFlat(True)
        button.setFixedSize(16, 16)
        
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

                tag_repo = TagRepository()
                tag_repo.delete(self.id)

                self.deleteLater()