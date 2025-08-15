from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction

from app.gui.widgets.q_central_widget import QCentralWidget

class QEditMenu(QMenu):
    def __init__(self, parent=None, tab_widget: QCentralWidget = None):
        super().__init__('Edit', parent)

        self.addSeparator()

        preferences_action = QAction('Preferences', self)
        self.addAction(preferences_action)

