from pathlib import Path

from PyQt6.QtGui import QFontMetrics
from PyQt6.QtCore import Qt

from app.db.models import FileModel

from app.utils.fs_util import DEFAULT_PATH

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.svg'}

def elide_text(text, width, font):
    metrics = QFontMetrics(font)
    return metrics.elidedText(text, Qt.TextElideMode.ElideRight, width)

def full_paths(folder_name: str, files: list[dict[str]]) -> list[str]:
    return [
        str(Path(DEFAULT_PATH, folder_name, file.name).resolve())
        for file in files
    ]

def image_filter(file_paths: list[str]):
    return [
        str(file_path) for file_path in map(Path, file_paths)
        if file_path.suffix.lower() in IMAGE_EXTENSIONS
    ]