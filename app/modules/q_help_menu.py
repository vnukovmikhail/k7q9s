from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction

from app.gui.widgets.q_central_widget import QCentralWidget

class QHelpMenu(QMenu):
    def __init__(self, parent=None, tab_widget:QCentralWidget=None):
        super().__init__('Help', parent)
        self.readme_action = QAction('README', parent)
        self.addAction(self.readme_action)

        self.addSeparator()

        self.tab1_action = QAction('Tab 1', parent)
        self.addAction(self.tab1_action)

        self.tab2_action = QAction('Tab 2', parent)
        self.addAction(self.tab2_action)

