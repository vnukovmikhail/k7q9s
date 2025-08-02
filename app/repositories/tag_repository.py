import sqlite3
from app.utils.sql_util import DatabaseConnection
from app.utils.logger_util import get_logger

logger = get_logger(__name__)

class TagRepository:
    def __init__(self, db_connection: DatabaseConnection = None):
        self.db = db_connection if db_connection else DatabaseConnection()

    def create(self, tag_name:str) -> dict[int, str]:
        try:
            with self.db.get_cursor() as cursor:
                cursor.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (tag_name,))
                cursor.execute("SELECT id FROM tags WHERE name = ?", (tag_name,))
                tag_id = cursor.fetchone()[0]

                logger.debug(f"tag '{tag_name}' was created with id: {tag_id}")
                return {'id': tag_id, 'name': tag_name}
        except sqlite3.Error as e:
            logger.error(e)
            return {}
        
    def delete(self, tag_id:int) -> bool:
        try:
            with self.db.get_cursor() as cursor:
                cursor.execute("DELETE FROM folder_tags WHERE tag_id = ?", (tag_id,))
                cursor.execute("DELETE FROM tags WHERE id = ?", (tag_id,))
            
                logger.debug(f"tag with id'{tag_id}' was removed")
                return True
        except sqlite3.Error as e:
            logger.error(e)
            return False
        
    def fetchall(self) -> list[dict[int, str]]:
        try:
            with self.db.get_cursor() as cursor:
                cursor.execute("SELECT id, name FROM tags ORDER BY id")
                tags = cursor.fetchall()

                result = [{'id': tag_id, 'name': tag_name} for tag_id, tag_name in tags]

                logger.debug(f'fetched: {result}')
                return result
        except sqlite3.Error as e:
            logger.error(e)
            return []
    