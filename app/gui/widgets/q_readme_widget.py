import markdown
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit

class QReadmeWidget(QWidget):
    def __init__(self):
        super().__init__()

        text_edit = QTextEdit()
        text_edit.setReadOnly(True)

        try:
            with open('README.md', 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            content = 'README file not found.'

        text_edit.setHtml(markdown.markdown(content))

        layout = QVBoxLayout(self)
        layout.addWidget(text_edit)
