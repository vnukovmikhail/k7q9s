from app.models import BaseModel
from sqlalchemy.orm import mapped_column, Mapped

class TagModel(BaseModel):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]