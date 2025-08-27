import shutil, random, string
from pathlib import Path

DEFAULT_PATH = 'public'

def random_name() -> str:
    folder_path = Path(DEFAULT_PATH)
    count = sum(1 for _ in folder_path.iterdir())
    random_letter = random.choice(string.ascii_lowercase)
    return f'{count}{random_letter}'

class FolderManager:
    def __init__(self, folder_name: str):
        self.folder_name = folder_name.strip() if folder_name else random_name()
        self.folder = Path(DEFAULT_PATH, self.folder_name)
        self.folder.mkdir(parents=True, exist_ok=True)

    def add_file(self, file_path: str, move: bool = False):
        src = Path(file_path)
        dest = self.folder / src.name

        if src.is_file():
            if dest.exists():
                print(f'[~] File already exists: {dest.name}, skipping.')
                return
            if move:
                shutil.move(src, dest)
            else:
                shutil.copy2(src, dest)
            print(f'[+] {src.name} -> {dest.name}')
        else:
            print(f'[!] File not found: {file_path}')


    def add_files(self, file_paths: list[str], move: bool = False):
        for path in file_paths:
            self.add_file(path, move)

    def list_files(self) -> list[str]:
        return [f.name for f in self.folder.iterdir() if f.is_file()]
    
    def delete_folder(self) -> bool:
        if self.folder.exists():
            shutil.rmtree(self.folder)
            print(f'[x] Folder deleted: {self.folder}')
            return True
        else:
            print(f'[!] Folder not found: {self.folder}')
            return False