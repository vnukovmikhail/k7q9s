from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class AnotherWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        labels = {}

        labels['Hello world'] = QLabel()
        labels['Hello world'].setText('Hello World')
        labels['who are you?'] = QLabel()
        labels['who are you?'].setText('who are you?')
        labels['404'] = QLabel()
        labels['404'].setText('error: 404')
        labels['error'] = QLabel()
        labels['error'].setText('out of use')

        for _, item in labels.items():
            item.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            layout.addWidget(item)