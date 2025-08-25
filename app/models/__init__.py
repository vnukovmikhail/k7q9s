from sqlalchemy.orm import DeclarativeBase
from app.models.tag_model import TagModel
from app.models.folder_model import FolderModel

class BaseModel(DeclarativeBase):
    ...

__all__ = [
    TagModel,
    FolderModel,
]