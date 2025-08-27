from app.db.models import BaseModel
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer

from app.db.models import folder_files

class FileModel(BaseModel):
    __tablename__ = 'files'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    folders = relationship(
        "FolderModel",
        secondary=folder_files,
        back_populates='files',
        cascade='all, delete'
    )