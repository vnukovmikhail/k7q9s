from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import ForeignKey, Table, Column

class BaseModel(DeclarativeBase):
    ...

folder_tags = Table(
    "folder_tags",
    BaseModel.metadata,
    Column("folder_id", ForeignKey("folders.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)

folder_files = Table(
    "folder_files",
    BaseModel.metadata,
    Column("folder_id", ForeignKey("folders.id"), primary_key=True),
    Column("file_id", ForeignKey("files.id"), primary_key=True),
)

from app.db.models.tag_model import TagModel
from app.db.models.folder_model import FolderModel
from app.db.models.file_model import FileModel

__all__ = [
    TagModel,
    FolderModel,
    FileModel,
]