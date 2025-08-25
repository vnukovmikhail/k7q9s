from PyQt6.QtWidgets import QDialog

class ImportDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle('Import')
        self.setMinimumSize(356, 256)