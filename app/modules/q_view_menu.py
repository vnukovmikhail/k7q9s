from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction

from app.gui.widgets.q_central_widget import QCentralWidget
from app.gui.widgets.q_preview_widget import QPreviewWidget
from app.gui.widgets.q_creator_widget import QCreatorWidget
from app.gui.widgets.q_tag_editor_widget import QTagEditorWidget
from app.gui.widgets.q_home_widget import QHomeWidget

class QViewMenu(QMenu):
    def __init__(self, parent=None, tab_widget:QCentralWidget=None):
        super().__init__('View', parent)

        preview_action = QAction('Preview', self)
        preview_action.triggered.connect(lambda:tab_widget.create_tab(QPreviewWidget(), 'Viewer'))
        self.addAction(preview_action)

        folder_creator_action = QAction('Folder creator', self)
        folder_creator_action.triggered.connect(lambda:tab_widget.create_tab(QCreatorWidget(), 'Folder creator'))
        self.addAction(folder_creator_action)

        tag_editor_action = QAction('Tag editor', self)
        tag_editor_action.triggered.connect(lambda:tab_widget.create_tab(QTagEditorWidget(), 'Tag editor'))
        self.addAction(tag_editor_action)

        self.addSeparator()

        home_action = QAction('Home', self)
        home_action.triggered.connect(lambda:tab_widget.create_tab(QHomeWidget(), 'Home'))
        self.addAction(home_action)

