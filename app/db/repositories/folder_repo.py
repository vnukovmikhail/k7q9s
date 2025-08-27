from math import ceil
from sqlalchemy import select, func, asc, desc
from sqlalchemy.orm import Session, joinedload
from app.db.models import TagModel, FolderModel, FileModel

class FolderRepo:
    def __init__(self, session: Session):
        self._session = session

    def get_folder_by_name(self, folder_name: str) -> FolderModel | None:
        statement = select(FolderModel).where(FolderModel.name == folder_name)
        return self._session.scalar(statement)

    def create_or_update_folder(self,
        folder_name: str,
        tag_names: list[str],
        file_names: list[str]
    )-> FolderModel:
        folder = self.get_folder_by_name(folder_name)

        if not folder:
            folder = FolderModel(name=folder_name)
            self._session.add(folder)

        if tag_names:
            tags = []
            for name in tag_names:
                tag = self._session.query(TagModel).filter_by(name=name).first()
                if not tag:
                    tag = TagModel(name=name)
                    self._session.add(tag)
                tags.append(tag)
            folder.tags = tags

        if file_names:
            files = []
            for name in file_names:
                file = self._session.query(FileModel).filter_by(name=name).first()
                if not file:
                    file = FileModel(name=name)
                    self._session.add(file)
                files.append(file)
            folder.files = files

        self._session.commit()
        self._session.refresh(folder)
        return folder

    def get_all_folders(self) -> list[FolderModel]:
        return self._session.query(FolderModel).all()
    
    def delete_folder_by_name(self, folder_name: str) -> bool:
        folder = self.get_folder_by_name(folder_name)
        if not folder:
            return False

        self._session.delete(folder)
        self._session.commit()
        return True
    
    def get_folders_with_pagination(
        self,
        page: int = 1,
        per_page: int = 10,
        sort_field: str = "id",
        sort_order_desc: bool = False,
        search_field: str | None = None,
        search_value: str | None = None,
        tags: list[str] | None = None
    ) -> dict:
        query = select(FolderModel).options(joinedload(FolderModel.tags))

        if search_field and search_value:
            field = getattr(FolderModel, search_field, None)
            if field is not None:
                query = query.where(field.ilike(f"%{search_value}%"))

        if tags:
            query = query.join(FolderModel.tags).where(TagModel.name.in_(tags)).distinct()

        sort_col = getattr(FolderModel, sort_field, None)
        if sort_col is not None:
            if sort_order_desc:
                query = query.order_by(desc(sort_col))
            else:
                query = query.order_by(asc(sort_col))

        all_folders = self._session.execute(query).unique().scalars().all()

        if tags:
            required_tags = set(tags)


            all_folders = [
                f for f in all_folders
                if len(required_tags & {t.name for t in f.tags}) > 0
            ]


            def rank(folder: FolderModel):
                folder_tags = {t.name for t in folder.tags}
                full_match = required_tags.issubset(folder_tags)
                partial_overlap = len(required_tags & folder_tags)
                return (1 if full_match else 0, partial_overlap)

            all_folders.sort(key=rank, reverse=True)

        total_count = len(all_folders)
        total_pages = ceil(total_count / per_page) if total_count else 1
        page = min(page, total_pages)
        start = (page - 1) * per_page
        end = start + per_page
        folders = all_folders[start:end]

        return {
            "items": folders,
            "page": page,
            "per_page": per_page,
            "total_pages": total_pages,
            "total_items": total_count,
        }