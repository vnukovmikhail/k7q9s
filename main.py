import sys
from PyQt6.QtWidgets import QApplication
from app.main_window import MainWindow

from app.repositories.folder_repository import fetchall_folders, FolderRepository
from app.repositories.tag_repository import fetchall_tags, TagRepository

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = MainWindow()
    root.show()
    sys.exit(app.exec())