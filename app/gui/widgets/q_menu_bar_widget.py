from PyQt6.QtWidgets import QMenuBar, QWizard, QWizardPage, QVBoxLayout, QLabel

from app.gui.widgets.q_central_widget import QCentralWidget

from app.modules.q_file_menu import QFileMenu
from app.modules.q_edit_menu import QEditMenu
from app.modules.q_view_menu import QViewMenu
from app.modules.q_help_menu import QHelpMenu

class QMenuBarWidget(QMenuBar):
    def __init__(self, parent=None, tab_widget:QCentralWidget=None):
        super().__init__(parent)
        
        self.addMenu(QFileMenu(self, tab_widget))
        self.addMenu(QEditMenu(self, tab_widget))
        self.addMenu(QViewMenu(self, tab_widget))
        self.addMenu(QHelpMenu(self, tab_widget))

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

        

        
