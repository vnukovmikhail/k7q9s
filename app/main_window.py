from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6.QtGui import QIcon, QFont

from app.gui.widgets.q_central_widget import QCentralWidget
from app.gui.widgets.q_menu_bar_widget import QMenuBarWidget
from app.utils.res_util import resource_path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Not my first application')
        self.setWindowIcon(QIcon(resource_path('app/resources/pic.png'))) 
        self.setMinimumSize(800, 600)

        tabs = QCentralWidget()
        
        self.setMenuBar(QMenuBarWidget(self, tabs))
        self.setCentralWidget(tabs)
        # self.setMenuWidget()
        
        status = self.statusBar()
        status.showMessage('program has been started!', 3000)
        online_label = QLabel('Not my first application v0.1.9 by k7osx')
        status.addPermanentWidget(online_label)