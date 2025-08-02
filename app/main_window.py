from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon, QFont

from app.gui.widgets.central_widget import CentralWidget
from app.utils.resource_util import resource_path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Not my first application')
        self.setWindowIcon(QIcon(resource_path('app/resources/pic.png'))) 
        self.setFont(QFont('monospace'))
        self.setMinimumSize(300, 500)
        
        # self.setMenuBar()
        # self.setMenuWidget()
        self.setCentralWidget(CentralWidget())