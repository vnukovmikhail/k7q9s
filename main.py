import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
from app.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont(QFont('monospace', 10))
    root = MainWindow()
    root.show()
    sys.exit(app.exec())