from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon, QFont

from src.app.widgets.menu_widget import MenuWidget
from src.app.widgets.central_widget import CentralWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Not my first application')
        self.setWindowIcon(QIcon('src/resources/pic.png'))
        self.setFont(QFont('monospace'))
        self.setMinimumSize(300, 500)

        self.setMenuWidget(MenuWidget(self))
        
        self.setCentralWidget(CentralWidget(self))