import sqlite3, json
from app.utils.sql_util import DatabaseConnection, VALID_COLUMNS
from app.utils.logger_util import get_logger

logger = get_logger(__name__)

class FolderRepository:
    def __init__(self, db_connection: DatabaseConnection = None):
        self.db = db_connection if db_connection else DatabaseConnection()

    def create(self,
        folder_name: str,
        tag_ids: list[str],
        file_list: list[str],
    ) -> bool:
        try:
            with self.db.get_cursor() as cursor:
                files_json = json.dumps(file_list, ensure_ascii=False)

                cursor.execute("INSERT INTO folders (name, files) VALUES (?, ?)", (folder_name, files_json))

                folder_id = self.cursor.lastrowid

                for tag_id in tag_ids:
                    cursor.execute("INSERT INTO folder_tags (folder_id, tag_id) VALUES (?, ?)", (folder_id, tag_id))

                logger.debug(f"📂 folder '{folder_name}' was created with tag ids: {tag_ids}")
                return True
        except sqlite3.Error as e:
            logger.error(e)
            return False
        
    def fetchall(self,
        order_by: str = 'created_at',
        desc: bool = False,
        search_field: str = None,
        search_value: str = None,
        tag_ids: list[int] = None,
    ) -> list[dict]:
        try:
            if tag_ids:
                return self._get_by_tags(
                    tag_ids = tag_ids,
                )
            else:
                return self._get_by_args(
                    order_by = order_by,
                    desc = desc,
                    search_field = search_field,
                    search_value = search_value,
                )
        except sqlite3.Error as e:
            logger.error(e)
            return []
        
    def _get_by_tags(self,
        tag_ids: list[int],
    ) -> list[dict]:
        placeholders = ','.join('?' for _ in tag_ids)
        
        full_match_query = f"""
            SELECT f.id, f.name, f.files, f.created_at, f.updated_at,
                GROUP_CONCAT(t.name, ', ') as tag_names,
                GROUP_CONCAT(t.id, ', ') as tag_ids
            FROM folders f
            JOIN folder_tags ft ON f.id = ft.folder_id
            JOIN tags t ON t.id = ft.tag_id
            WHERE ft.tag_id IN ({placeholders})
            GROUP BY f.id
            HAVING COUNT(DISTINCT ft.tag_id) = ?
        """
        
        partial_match_query = f"""
            SELECT DISTINCT f.id, f.name, f.files, f.created_at, f.updated_at,
                GROUP_CONCAT(t.name, ', ') as tag_names,
                GROUP_CONCAT(t.id, ', ') as tag_ids
            FROM folders f
            JOIN folder_tags ft ON f.id = ft.folder_id
            JOIN tags t ON t.id = ft.tag_id
            WHERE t.id IN ({placeholders})
            GROUP BY f.id
        """
        
        try:
            with self.db.get_cursor() as cursor:
                cursor.execute(full_match_query, tag_ids + [len(tag_ids)])
                full_matches = cursor.fetchall()
                
                cursor.execute(partial_match_query, tag_ids)
                all_matches = cursor.fetchall()
                
                full_match_ids = {row[0] for row in full_matches}
                partial_matches = [row for row in all_matches if row[0] not in full_match_ids]
            
                combined_results = full_matches + partial_matches
                
                result = []
                for row in combined_results:
                    folder = {
                        'id': row[0],
                        'name': row[1],
                        'files': json.loads(row[2]) if row[2] else [],
                        'created_at': row[3],
                        'updated_at': row[4],
                        'tags': {
                            'names': row[5].split(', ') if row[5] else [],
                            'ids': list(map(int, row[6].split(', '))) if row[6] else []
                        },
                        'match_type': 'full' if row in full_matches else 'partial'
                    }
                    result.append(folder)

                logger.debug(f'fetched by tags: {result}')
                return result
        except sqlite3.Error as e:
            logger.error(e)
            return []

    def _get_by_args(
        self,
        order_by: str = 'created_at',
        desc: bool = False,
        search_field: str = None,
        search_value: str = None,
    ) -> list[dict]:
        order_by = order_by if order_by in VALID_COLUMNS else 'created_at'
        direction = 'DESC' if desc else 'ASC'

        query = """
            SELECT 
                f.id, f.name, f.files, f.created_at, f.updated_at,
                GROUP_CONCAT(DISTINCT t.name) as tag_names,
                GROUP_CONCAT(DISTINCT t.id) as tag_ids
            FROM folders f
            LEFT JOIN folder_tags ft ON f.id = ft.folder_id
            LEFT JOIN tags t ON t.id = ft.tag_id
        """
        
        params = []

        if search_field in VALID_COLUMNS and search_value:
            if search_field == 'id' and search_value.isdigit():
                query += f" WHERE f.{search_field} = ?"
                params.append(int(search_value))
            else:
                query += f" WHERE f.{search_field} LIKE ?"
                params.append(f"%{search_value}%")

        query += f" GROUP BY f.id, f.name, f.files, f.created_at, f.updated_at ORDER BY f.{order_by} {direction}"

        try:
            with self.db.get_cursor() as cursor:
                cursor.execute(query, params)
                rows = cursor.fetchall()

                result = []
                for row in rows:
                    folder = {
                        'id': row[0],
                        'name': row[1],
                        'files': json.loads(row[2]) if row[2] else [],
                        'created_at': row[3],
                        'updated_at': row[4],
                        'tags': {
                            'names': row[5].split(',') if row[5] else [],
                            'ids': list(map(int, row[6].split(','))) if row[6] else []
                        },
                        'match_type': 'none'
                    }
                    result.append(folder)

                logger.debug(f'fetched by args: {result}')
                return result
        except sqlite3.Error as error:
            print(error)
            return []
