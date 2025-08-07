from datetime import datetime
from pathlib import Path
from app.utils.sql_util import SQLiteDatabase
from app.utils.fs_util import FolderManager, random_name

def folders_count():
    with SQLiteDatabase() as db:
        try:
            db.execute("SELECT COUNT(*) as count FROM folders")
            result = db.fetchone()
            return result['count']
        except:
            return 0

def fetchall_folders(
    order_by: str = 'created_at',
    desc: bool = False,
    search_field: str = None,
    search_value: str = None,
    tag_ids: list[str] = None,
    page: int = 1,
    page_size: int = 10
) -> list[dict[str]]:
    offset = (page - 1) * page_size
    
    with SQLiteDatabase() as db:
        try:
            # db.execute("SELECT * FROM folders")
            # print('[!] Folders', [dict(row) for row in db.fetchall()])
            # db.execute("SELECT * FROM files")
            # print('[!] Files', [dict(row) for row in db.fetchall()])
            # db.execute("SELECT * FROM folder_files")
            # print('[!] Folder->Files', [dict(row) for row in db.fetchall()])

            db.execute("SELECT * FROM folders")
            # db.execute("""SELECT * FROM folders
            # ORDER BY created_at DESC   ORDER BY ? ?
            # LIMIT ? OFFSET ?""", (page_size, offset))
            folders = [dict(row) for row in db.fetchall()]
            
            result = []
            for folder in folders:
                folder_id = folder['id']

                db.execute("SELECT * FROM folders WHERE id = ?", (folder_id,))
                folder = db.fetchone()
                
                db.execute('''
                    SELECT f.id, f.name 
                    FROM files f
                    JOIN folder_files ff ON f.id = ff.file_id
                    WHERE ff.folder_id = ?
                ''', (folder_id,))
                files = [{'id': row[0], 'name': row[1]} for row in db.fetchall()]

                tags = []
                try:
                    db.execute('''
                        SELECT t.id, t.name 
                        FROM tags t
                        JOIN folder_tags ft ON t.id = ft.tag_id
                        WHERE ft.folder_id = ?
                    ''', (folder_id,))
                    tags = [{'id': row[0], 'name': row[1]} for row in db.fetchall()]
                except:
                    pass
            
                result.append({**folder, 'files': files, 'tags': tags}) 

            return result
        except:
            return []
        
        

class FolderRepository:
    def __init__(self, folder_name:str):
        self.folder_name = folder_name.strip() if folder_name else random_name()
        self.folder_id = None
        self.fs = FolderManager(self.folder_name)

        self._ensure_schema()
        self._ensure_folder_in_db()

    def _ensure_schema(self):
        with SQLiteDatabase() as db:
            db.execute("""
                CREATE TABLE IF NOT EXISTS folders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """)
            db.execute("""
                CREATE TABLE IF NOT EXISTS files (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                )
            """)
            db.execute("""CREATE TABLE IF NOT EXISTS folder_files (
                folder_id INTEGER NOT NULL,
                file_id INTEGER NOT NULL,
                PRIMARY KEY (folder_id, file_id),
                FOREIGN KEY (folder_id) REFERENCES folders(id) ON DELETE CASCADE,
                FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
            )""")

    def _ensure_folder_in_db(self):
        with SQLiteDatabase() as db:
            db.execute("SELECT id FROM folders WHERE name = ?", (self.folder_name,))
            result = db.fetchone()

            if result:
                self.folder_id = result['id']
            else:
                db.execute(
                    "INSERT OR IGNORE INTO folders (name) VALUES (?)",
                    (self.folder_name,)
                )
                self.folder_id = db.lastrowid()

    def add_file(self, file_path: str, move: bool = False):
        src = Path(file_path)
        with SQLiteDatabase() as db:
            db.execute("INSERT OR IGNORE INTO files (name) VALUES (?)", (src.name,))

            db.execute("SELECT id FROM files WHERE name = ?", (src.name,))
            file_row = db.fetchone()
            if not file_row:
                print(f'[!] Failed to fetch file_id for {src.name}')
                return
            file_id = file_row["id"] 

            db.execute("""
                INSERT OR IGNORE INTO folder_files (folder_id, file_id) VALUES (?, ?)
            """, (self.folder_id, file_id))
        self.fs.add_file(file_path, move)

    def add_files(self, file_paths: list[str], move: bool = False):
        for path in file_paths:
            self.add_file(path, move)

    def add_tag(self, tag_id:int):
        with SQLiteDatabase() as db:
            db.execute("""
                INSERT OR IGNORE INTO folder_tags (folder_id, tag_id) VALUES (?, ?)
            """, (self.folder_id, tag_id))

    def add_tags(self, tag_ids: list[int]):
        for tag_id in tag_ids:
            self.add_tag(tag_id)

    def delete(self):
        with SQLiteDatabase() as db:
            db.execute("PRAGMA foreign_keys = ON")
            db.execute("DELETE FROM folders WHERE id = ?", (self.folder_id,))
            # db.execute("DELETE FROM folder_files WHERE folder_id = ?", (self.folder_id,))
            db.execute("DELETE FROM files WHERE id NOT IN (SELECT file_id FROM folder_files)")

        if self.fs.delete_folder():
            print(f"[x] Folder '{self.folder_name}' deleted from disk and database.")
        else:
            print(f"[!] Folder '{self.folder_name}' not found on disk.")

    def get(self):
        with SQLiteDatabase() as db:
            db.execute("SELECT * FROM folders WHERE id = ?", (self.folder_id,))
            folder = db.fetchone()
            
            db.execute('''
                SELECT f.id, f.name 
                FROM files f
                JOIN folder_files ff ON f.id = ff.file_id
                WHERE ff.folder_id = ?
            ''', (self.folder_id,))
            
            files = [{'id': row[0], 'name': row[1]} for row in db.fetchall()]

            db.execute('''
                SELECT t.id, t.name 
                FROM tags t
                JOIN folder_tags ft ON t.id = ft.tag_id
                WHERE ft.folder_id = ?
            ''', (self.folder_id,))
            tags = [{'id': row[0], 'name': row[1]} for row in db.fetchall()]
        
            return {**folder, 'files': files, 'tags': tags}