from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox
import os, shutil

def pack(folder: str, archive_name: str, format_: str = "zip"):
    folder = os.path.abspath(folder)
    archive_file = shutil.make_archive(archive_name, format_, root_dir=folder)
    return archive_file

class ExportDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle('Export')
        self.setMinimumSize(356, 256)

        folder = QFileDialog.getExistingDirectory(self, 'Choose folder to archivate')
        if not folder:
            return

        save_path, _ = QFileDialog.getSaveFileName(
            self,
            'Save archive',
            'archive.zip',
            "Zip archive (*.zip);;Tar.gz archive (*.tar.gz)"
        )

        if not save_path:
            return

        if save_path.endswith(".tar.gz"):
            fmt = "gztar"
        elif save_path.endswith(".zip"):
            fmt = "zip"
        else:
            fmt = "zip"

        try:
            archive = pack(folder, os.path.splitext(save_path)[0], fmt)
            QMessageBox.information(self, 'Done', f'✅ Archive was created:\n{archive}')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'❌ Failed to pack: {e}')