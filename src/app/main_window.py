from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon, QFont

from src.app.widgets.central_widget import CentralWidget
from src.utils.config_util import resource_path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Not my first application')
        self.setWindowIcon(QIcon(resource_path('src/resources/pic.png'))) 
        self.setFont(QFont('monospace'))
        self.setMinimumSize(300, 500)

        # self.setMenuWidget(MenuWidget(self))
        
        self.setCentralWidget(CentralWidget(self))