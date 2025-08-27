from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db.models.tag_model import TagModel

class TagRepo:
    def __init__(self, session: Session):
        self._session = session

    def get_tag_by_name(self, tag_name:str) -> TagModel | None:
        statement = select(TagModel).where(TagModel.name == tag_name)
        return self._session.scalar(statement)

    def create_or_update_tag(self, tag_name:str) -> TagModel:
        tag = self.get_tag_by_name(tag_name)

        if not tag:
            tag = TagModel(name=tag_name)
            self._session.add(tag)

        self._session.commit()
        self._session.refresh(tag)
        return tag

    def get_all_tags(self) -> list[TagModel]:
        return self._session.query(TagModel).all()
    
    def delete_tag_by_name(self, tag_name: str) -> bool:
        tag = self.get_tag_by_name(tag_name)
        if not tag:
            return False

        self._session.delete(tag)
        self._session.commit()
        return True
