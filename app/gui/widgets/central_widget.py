from PyQt6.QtWidgets import QWidget, QTabWidget, QToolBox
from PyQt6.QtGui import QIcon

from app.gui.widgets.folder_viewer_widget import FolderViewerWidget
from app.gui.widgets.folder_creator_widget import FolderCreatorWidget
from app.gui.widgets.tag_editor_widget import TagEditorWidget
from app.tests.test_widget import TestWidget
from app.tests.test2_widget import Test2Widget
from app.tests.test3_widget import Test3Widget
from app.tests.test4_widget import Test4Widget
from app.tests.test5_widget import PaginationWidget

class CentralWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.addTab(FolderViewerWidget(), 'tab_1')
        self.addTab(FolderCreatorWidget(), 'tab_2')
        self.addTab(TagEditorWidget(), 'tab_3')
        self.addTab(TestWidget(), 'tab_4')
        self.addTab(Test2Widget(), 'tab_5')
        self.addTab(Test3Widget(), 'tab_6')
        self.addTab(Test4Widget(), 'tab_7')
        self.addTab(QWidget(), QIcon("app/resources/pic.png"), "С иконкой")
        # self.setCurrentWidget()
        self.setCurrentIndex(2)
        # self.addTab(PaginationWidget(), 'tab_8')
        # self.removeTab()

        # self.setTabsClosable(True)
        # self.tabCloseRequested.connect(self.close_tab)
        # self.setTabsClosable(True)
        # self.tabCloseRequested.connect(lambda index: self.removeTab(index))

    # def close_tab(self, index: int):
    #     self.tabs.removeTab(index)