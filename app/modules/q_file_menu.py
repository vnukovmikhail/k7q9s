from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction

from app.gui.widgets.q_central_widget import QCentralWidget

from app.gui.dialogs.export_dialog import ExportDialog
from app.gui.dialogs.import_dialog import ImportDialog

class QFileMenu(QMenu):
    def __init__(self, parent=None, tab_widget:QCentralWidget = None):
        super().__init__('File', parent)

        self.addSeparator()

        export_action = QAction('Export', self)
        export_action.triggered.connect(self.open_export_dialog)
        self.addAction(export_action)

        import_action = QAction('Import', self)
        import_action.triggered.connect(self.open_import_dialog)
        self.addAction(import_action)

    def open_export_dialog(self):
        dialog = ExportDialog(self)
        if dialog.exec():
            print("Экспорт выполнен ✅")
        else:
            print("Экспорт отменён ❌")

    def open_import_dialog(self):
        dialog = ImportDialog(self)
        if dialog.exec():
            print("Импорт выполнен ✅")
        else:
            print("Импорт отменён ❌")