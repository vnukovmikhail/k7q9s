from PyQt6.QtWidgets import QWidget, QTabWidget

from app.gui.widgets.folder_viewer_widget import FolderViewerWidget
from app.gui.widgets.folder_creator_widget import FolderCreatorWidget
from app.gui.widgets.tag_editor_widget import TagEditorWidget
from app.tests.test_widget import TestWidget

class CentralWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.addTab(FolderViewerWidget(), 'tab_1')
        self.addTab(FolderCreatorWidget(), 'tab_2')
        self.addTab(TagEditorWidget(), 'tab_3')
        self.addTab(TestWidget(), 'tab_4')
        # self.addTab(MyWidget(), 'tab_5')