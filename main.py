import sys
from PyQt6.QtWidgets import QApplication
from src.app.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = MainWindow()
    root.show()
    sys.exit(app.exec())