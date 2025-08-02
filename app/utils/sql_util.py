import sqlite3, os
from contextlib import contextmanager

from app.utils.fs_util import BASE_DIR

DB_FILE = 'test.db'
DB_PATH = os.path.join(BASE_DIR, DB_FILE)
VALID_COLUMNS = ['id', 'name', 'created_at', 'updated_at']

class DatabaseConnection:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self.conn = None
        
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn.cursor()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.conn.close()
            
    @contextmanager
    def get_cursor(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()