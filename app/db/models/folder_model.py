from app.db.models import BaseModel
from sqlalchemy import DateTime, func
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer

from app.db.models import folder_tags, folder_files

class FolderModel(BaseModel):
    __tablename__ = 'folders'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    tags = relationship(
        'TagModel',
        secondary=folder_tags,
        back_populates="folders",
        cascade='all, delete'
    )

    files = relationship(
        'FileModel',
        secondary=folder_files,
        back_populates="folders",
        cascade='all, delete'
    )