from app.utils.sql_util import SQLiteDatabase

def fetchall_tags() -> list[dict[str]]:
    with SQLiteDatabase() as db:
        try: 
            # db.execute("SELECT * FROM tags")
            # print('[!] Tags', [dict(row) for row in db.fetchall()])
            # db.execute("SELECT * FROM folder_tags")
            # print('[!] Folders->Tags', [dict(row) for row in db.fetchall()])
            
            db.execute("SELECT * FROM tags")
            return [dict(row) for row in db.fetchall()]
        except:
            return []

class TagRepository:
    def __init__(self, tag_name:str):
        self.tag_name = tag_name.strip()
        self.tag_id = None

        self._ensure_schema()
        self._ensure_tag_in_db()

    def _ensure_schema(self):
        with SQLiteDatabase() as db:
            db.execute("""CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )""")
            db.execute("""CREATE TABLE IF NOT EXISTS folder_tags (
                folder_id TEXT NOT NULL,
                tag_id INTEGER NOT NULL,
                PRIMARY KEY (folder_id, tag_id),
                FOREIGN KEY (folder_id) REFERENCES folders(id) ON DELETE CASCADE,
                FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE 
            )""")

    def _ensure_tag_in_db(self):
        with SQLiteDatabase() as db:
            db.execute("SELECT id FROM tags WHERE name = ?", (self.tag_name,))
            result = db.fetchone()

            if result:
                self.tag_id = result['id']
            else:
                db.execute("INSERT INTO tags (name) VALUES (?)", (self.tag_name,))
                self.tag_id = db.lastrowid

    def delete(self):
        with SQLiteDatabase() as db:
            db.execute("PRAGMA foreign_keys = ON")
            db.execute("DELETE FROM tags WHERE id = ?", (self.tag_id,))
            # db.execute("DELETE FROM folder_files WHERE folder_id = ?", (self.folder_id,))
            # db.execute("DELETE FROM tags WHERE id NOT IN (SELECT tag_id FROM folder_tags)")
    