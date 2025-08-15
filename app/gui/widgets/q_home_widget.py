from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class QHomeWidget(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel('Home page:')
        label1 = QLabel('Title: Not my first application')
        label2 = QLabel('Version: v0.1.9')
        label3 = QLabel('Author: k7osx')

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addStretch()

        