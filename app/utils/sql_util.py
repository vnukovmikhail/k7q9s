import os, sqlite3, uuid

# from fs_util import DEFAULT_PATH
from app.utils.fs_util import DEFAULT_PATH

SQLITE_FILE = 'test.db'
SQLITE_PATH = os.path.join(DEFAULT_PATH, SQLITE_FILE)

class SQLiteDatabase:
    def __init__(self, db_path: str = SQLITE_PATH):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.conn.close()

    def execute(self, query: str, params: tuple = ()):
        self.cursor.execute(query, params)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()
    
    def lastrowid(self):
        return self.cursor.lastrowid



# c.execute("SELECT * FROM folders")
# folders = c.fetchall()
# for folder in folders:
#     id, name, created_at, updated_at = folder
#     print(f'📁 {id} {name} {updated_at}')

# c.execute("SELECT * FROM tags")
# tags = c.fetchall()
# for tag in tags:
#     id, name = tag
#     print(f'🔖 {id} {name}')