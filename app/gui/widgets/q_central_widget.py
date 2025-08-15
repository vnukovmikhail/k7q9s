from PyQt6.QtWidgets import QTabWidget
from app.gui.widgets.q_home_widget import QHomeWidget

class QCentralWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTabsClosable(True)
        
        self.create_tab(QHomeWidget(), 'Home')

        self.tabCloseRequested.connect(self.close_tab)

    def create_tab(self, widget, name):
        self.addTab(widget, name)
        self.setCurrentIndex(self.count() - 1)
        # print(self.count())

    def close_tab(self, index):
        self.removeTab(index)