from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction

from app.gui.widgets.q_central_widget import QCentralWidget
from app.gui.dialogs.preferences_dialog import PreferencesDialog

class QEditMenu(QMenu):
    def __init__(self, parent=None, tab_widget:QCentralWidget = None):
        super().__init__('Edit', parent)

        self.addSeparator()

        preferences_action = QAction('Preferences', self)
        preferences_action.triggered.connect(self.open_preferences_settings)
        self.addAction(preferences_action)

    def open_preferences_settings(self):
        preferences_dialog = PreferencesDialog(self)
        preferences_dialog.exec()