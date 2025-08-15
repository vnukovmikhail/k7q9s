from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction

from app.gui.widgets.q_central_widget import QCentralWidget

class QFileMenu(QMenu):
    def __init__(self, parent=None, tab_widget: QCentralWidget = None):
        super().__init__('File', parent)

        self.addSeparator()

        export_action = QAction('Export', self)
        export_menu = QMenu(self)
        export_menu.addAction("As PDF")
        export_menu.addAction("As HTML")
        export_menu.addAction("As TXT")
        export_action.setMenu(export_menu)
        self.addAction(export_action)

        import_action = QAction('Import', self)
        import_menu = QMenu(self)
        import_menu.addAction("From PDF")
        import_menu.addAction("From HTML")
        import_menu.addAction("From TXT")
        import_action.setMenu(import_menu)
        self.addAction(import_action)

