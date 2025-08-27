from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db.models.file_model import FileModel

class FileRepo:
    def __init__(self, session: Session):
        self._session = session

    def get_file_by_name(self, file_name:str) -> FileModel | None:
        statement = select(FileModel).where(FileModel.name == file_name)
        return self._session.scalar(statement)

    def create_or_update_file(self, file_name:str) -> FileModel:
        file = self.get_file_by_name(file_name)

        if not file:
            file = FileModel(name=file_name)
            self._session.add(file)

        self._session.commit()
        self._session.refresh(file)
        return file

    def get_all_files(self) -> list[FileModel]:
        return self._session.query(FileModel).all()
    
    def delete_file_by_name(self, file_name: str) -> bool:
        file = self.get_file_by_name(file_name)
        if not file:
            return False

        self._session.delete(file)
        self._session.commit()
        return True
