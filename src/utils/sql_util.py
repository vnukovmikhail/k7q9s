import sqlite3, json, os, inspect

from src.utils.fs_util import BASE_DIR

DB_FILE = 'test.db'
DB_PATH = os.path.join(BASE_DIR, DB_FILE)
VALID_COLUMNS = ['id', 'name', 'created_at', 'updated_at']

class Sql:
    def __init__(self, db_path=DB_PATH):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.init_db()
        # self.get_folders_by_tag_ids_prioritized([7])

    def __exit__(self):
        print(inspect.currentframe().f_code.co_name)
        self.close()

    def close(self):
        self.conn.close()

    def init_db(self) -> bool:
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS folders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    files TEXT,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS tags (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS folder_tags (
                    folder_id INTEGER,
                    tag_id INTEGER,
                    FOREIGN KEY(folder_id) REFERENCES folders(id) ON DELETE CASCADE,
                    FOREIGN KEY(tag_id) REFERENCES tags(id) ON DELETE CASCADE,
                    PRIMARY KEY (folder_id, tag_id)
                )
            """)
            self.conn.commit()
            # print(inspect.currentframe().f_code.co_name)
            return True
        except sqlite3.Error as error:
            print(error)
            return False

    def add_folder_to_db(
        self,
        folder_name: str,
        tag_ids: list[str],
        file_list: list[str],
    ) -> bool:
        try:
            files_json = json.dumps(file_list, ensure_ascii=False)

            self.cursor.execute("INSERT INTO folders (name, files) VALUES (?, ?)", (folder_name, files_json))
            folder_id = self.cursor.lastrowid

            for tag_id in tag_ids:
                self.cursor.execute("INSERT INTO folder_tags (folder_id, tag_id) VALUES (?, ?)", (folder_id, tag_id))

            self.conn.commit()
            print(f'{inspect.currentframe().f_code.co_name}:', f"folder '{folder_name}' was created with tag ids: {tag_ids}")
            return True
        except sqlite3.Error as error:
            print(error)
            return False
        
    def add_tag_to_db(self, tag_name:str) -> dict[int, str]:
        try:
            self.cursor.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (tag_name,))
            self.cursor.execute("SELECT id FROM tags WHERE name = ?", (tag_name,))
            tag_id = self.cursor.fetchone()[0]

            self.conn.commit()
            print(f'{inspect.currentframe().f_code.co_name}:', f"tag '{tag_name}' was created with id: {tag_id}")
            return {'id': tag_id, 'name': tag_name}
        except sqlite3.Error as error:
            print(error)
            return {}
        
    def remove_tag_from_db(self, tag_id: int) -> bool:
        try:
            self.cursor.execute("DELETE FROM folder_tags WHERE tag_id = ?", (tag_id,))
            self.cursor.execute("DELETE FROM tags WHERE id = ?", (tag_id,))

            self.conn.commit()
            print(f'{inspect.currentframe().f_code.co_name}:', f"tag with id'{tag_id}' was removed")
            return True
        except sqlite3.Error as error:
            print(error)
            return False

    def fetch_tags_from_db(self):
        try:
            self.cursor.execute("SELECT id, name FROM tags ORDER BY id")
            tags = self.cursor.fetchall()

            result = [{'id': tag_id, 'name': tag_name} for tag_id, tag_name in tags]

            print(f'{inspect.currentframe().f_code.co_name}:', result)
            return result
        except sqlite3.Error as error:
            print(error)
            return []

    def fetch_folders_from_db(
        self,
        order_by: str = 'created_at',
        desc: bool = False,
        search_field: str = None,
        search_value: str = None,
        tag_ids: list[int] = None,
    ) -> list[dict]:
        try:
            if tag_ids:
                return self._get_folders_with_tags(
                    tag_ids = tag_ids,
                )
            else:
                return self._get_folders_without_tags(
                    order_by = order_by,
                    desc = desc,
                    search_field = search_field,
                    search_value = search_value,
                )
        except sqlite3.Error as error:
            print(error)
            return []
        
    def _get_folders_with_tags(
            self,
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
            self.cursor.execute(full_match_query, tag_ids + [len(tag_ids)])
            full_matches = self.cursor.fetchall()
            
            self.cursor.execute(partial_match_query, tag_ids)
            all_matches = self.cursor.fetchall()
            
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

            print(f'{inspect.currentframe().f_code.co_name}:', result)
            return result
        except sqlite3.Error as error:
            print(error)
            return []

    def _get_folders_without_tags(
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
            self.cursor.execute(query, params)
            rows = self.cursor.fetchall()

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

            return result
        except sqlite3.Error as error:
            print(error)
        return []

    def print_all(self):
        self.cursor.execute("""
            SELECT folders.name, folders.files, GROUP_CONCAT(tags.name, ', ')
            FROM folders
            LEFT JOIN folder_tags ON folders.id = folder_tags.folder_id
            LEFT JOIN tags ON tags.id = folder_tags.tag_id
            GROUP BY folders.id
        """)
    
        for row in self.cursor.fetchall():
            name, files, tags = row
            print(f'📁 {name} - files: {files} - tags: {tags}')

    def delete_folder_by_id(self, folder_id: int) -> bool:
        try:
            self.cursor.execute("DELETE FROM folders WHERE id = ?", (folder_id,))
            self.conn.commit()
            print(f'[DELETED FOLDER id={folder_id}]')
            return True
        except sqlite3.Error as error:
            print(f'[DELETE ERROR] {error}')
            return False