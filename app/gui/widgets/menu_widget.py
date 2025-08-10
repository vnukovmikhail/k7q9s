from PyQt6.QtWidgets import QWidget, QTabWidget, QToolBox, QMenuBar, QMenu, QDialog, QWizard, QWizardPage, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QAction

from app.gui.widgets.folder_viewer_widget import FolderViewerWidget
from app.gui.widgets.folder_creator_widget import FolderCreatorWidget
from app.gui.widgets.tag_editor_widget import TagEditorWidget
from app.tests.test_widget import TestWidget
from app.tests.test2_widget import Test2Widget
from app.tests.test3_widget import Test3Widget
from app.tests.test4_widget import Test4Widget
from app.tests.test5_widget import PaginationWidget

class MenuWidget(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # menu0 = QMenu('menu', self)
        # menu0.addAction('hello1')
        # menu0.addAction('hello2')
        # menu0.addSeparator()
        # menu0.addAction('hello3')

        menu1 = QMenu('more', self)

        settings_action = QAction('settings', self)
        settings_action.triggered.connect(self.open_settings)
        menu1.addAction(settings_action)

        menu0 = QMenu('file', self)
        menu0.addAction(QAction('open', self))
        menu0.addAction(QAction('save', self))
        menu0.addSection('Additionally')
        menu0.addAction(QAction('export', self))
        menu0.addAction(QAction('import', self))

        self.addMenu(menu0)
        self.addMenu(menu1)

    def open_settings(self):
        # dialog = QDialog(self)
        # dialog.exec()

        page1 = QWizardPage()
        page1.setTitle("Шаг 1: Приветствие")
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Добро пожаловать в мастер установки!"))
        page1.setLayout(layout1)

        # Второй шаг
        page2 = QWizardPage()
        page2.setTitle("Шаг 2: Завершение")
        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Установка завершена."))
        page2.setLayout(layout2)

        # Сам мастер
        wizard = QWizard(self)
        wizard.setWindowTitle("Мастер установки")
        wizard.addPage(page1)
        wizard.addPage(page2)
        
        wizard.show()

        

        
