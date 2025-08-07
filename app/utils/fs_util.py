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
        self.folder = Path(DEFAULT_PATH, folder_name)
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


    def add_files(self, file_paths: list[str]):
        for path in file_paths:
            self.add_file(path)

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



# fm = FolderManager('tiktak')
# fm.add_files(['/home/k7osx/Downloads/Telegram/rainy-day-lewdfroggo_1080p.mp4', '/home/k7osx/Downloads/Telegram/enjoyed-the-best-life-of-a-dog-60fps-jackerman_1080p.mp4'])
# print(fm.list_files())
# fm.delete_folder()

# def add_files_to_folder_on_disk(
#     folder_path: str,
#     file_paths: list[str],
#     move: bool = False,
# ) -> bool:
#     try:
#         os.makedirs(folder_path, exist_ok=True)

#         for file_path in file_paths:
#             file_name = os.path.basename(file_path)
#             dest_path = os.path.join(folder_path, file_name)
            
#             if move:
#                 shutil.move(file_path, dest_path)
#             else:
#                 shutil.copy2(file_path, dest_path)
#     except Exception as e:
#         print(e)

# def create_folder_on_disk(
#     folder_name: str,
#     file_paths: list[str],
#     move: bool = False,
# ) -> str:
#     try:
#         folder_path = os.path.join(DEFAULT_PATH, folder_name)
#         os.makedirs(folder_path, exist_ok=True)

#         add_files_to_folder_on_disk(folder_path, file_paths, move)

#         return os.path.abspath(folder_path)
#     except Exception as e:
#         print(e)

# def remove_folder_from_disk(
#     folder_name: str,
# ) -> bool:
#     folder_path = os.path.join(DEFAULT_PATH, folder_name)
#     try:
#         if os.path.exists(folder_path):
#             shutil.rmtree(folder_path)
#     except Exception as e:
#         print(e)

# def read_folder_on_disk(
#     folder_name: str
# ) -> list[str]:
#     try:
#         folder_path = os.path.join(DEFAULT_PATH, folder_name)
#         if not os.path.isdir(folder_path):
#             return []

#         file_paths: list[str] = []
#         for file_name in os.listdir(folder_path):
#             file_path = os.path.join(folder_path, file_name)
#             if os.path.isfile(file_path):
#                 file_paths.append(file_path)
        
#         return file_paths
#     except Exception as e:
#         print(e)

# create_folder_on_disk('bibi2', ['README.md', 'requirements.txt'], False)
# read_folder_on_disk('bibi2')
# remove_folder_from_disk('bibi2')