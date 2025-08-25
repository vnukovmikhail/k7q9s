from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction

from app.gui.widgets.q_central_widget import QCentralWidget
from app.gui.widgets.q_readme_widget import QReadmeWidget

class QHelpMenu(QMenu):
    def __init__(self, parent=None, tab_widget:QCentralWidget=None):
        super().__init__('Help', parent)
        
        readme_action = QAction('README', parent)
        readme_action.triggered.connect(lambda:tab_widget.create_tab(QReadmeWidget(), 'Readme'))
        self.addAction(readme_action)

        self.addSeparator()

        self.tab1_action = QAction('Tab 1', parent)
        self.addAction(self.tab1_action)

        self.tab2_action = QAction('Tab 2', parent)
        self.addAction(self.tab2_action)

