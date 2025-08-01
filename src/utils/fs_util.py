import os, shutil

BASE_DIR = 'public'

def get_file_paths_in_folder(
    folder_name: str,
    file_names: list[str],
    base_dir: str = BASE_DIR,
) -> list[str]:
    return [os.path.join(base_dir, folder_name, file_name)  for file_name in file_names]

# print(get_file_paths_in_folder('yuki', ['photo_78_2025-05-09_20-21-39.jpg', 'photo_83_2025-05-09_20-09-49.jpg', 'photo_92_2025-05-09_20-22-06.jpg']))

def create_folder_on_disk(
    name: str,
    file_paths: list[str],
    move: bool = False,
) -> tuple[str, bool]: 
    folder_path = os.path.join(BASE_DIR, name)
    os.makedirs(folder_path, exist_ok=True)

    add_files_to_folder_on_disk(folder_path, file_paths, move)

    return os.path.abspath(folder_path)

def add_files_to_folder_on_disk(
    folder_path: str,
    file_paths: list[str],
    move: bool = False,
) -> bool:
    try:
        os.makedirs(folder_path, exist_ok=True)

        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            dest_path = os.path.join(folder_path, file_name)

            if move:
                shutil.move(file_path, dest_path)
            else:
                shutil.copy2(file_path, dest_path)

            print(dest_path, file_name)
        return True
    except Exception as exception:
        print(f'Error adding files: {exception}')
        return False

# create_folder_on_disk('yay', ['README.md', 'src/resources/pic.png']) # Test function :str, :list[str], :bool

def read_folder_on_disk(
    name: str
) -> list[str]:
    folder_path = os.path.join(BASE_DIR, name)
    if not os.path.isdir(folder_path):
        return []

    file_paths: list[str] = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            file_paths.append(file_path)
    
    print('Load:', folder_path, file_paths)
    return file_paths

# read_folder_on_disk('yay')

# def read_collection(
#     folder_name: str
# ) -> Dict[str, str]:
#     folder_path = os.path.join(BASE_DIR, folder_name)

#     if not os.path.isdir(folder_path):
#         return None
    
#     meta_path = os.path.join(folder_path, 'meta.json')
#     meta = {}

#     if os.path.isfile(meta_path):
#         with open(meta_path, 'r', encoding='utf-8') as f:
#             meta = json.load(f)

#     files = []
#     for item in os.listdir(folder_path):
#         item_path = os.path.join(folder_path, item)
#         if os.path.isfile(item_path) and item != 'meta.json':
#             files.append(item_path)

#     return {
#         'meta': meta,
#         'files': files,
#         'folder_path': folder_path
#     }

# def fetch_collections():
#     initialize_base_dir()

#     collections = []
#     folder_names = os.listdir(BASE_DIR)

#     for folder_name in folder_names:
#         collections.append(read_collection(folder_name))

#     return collections
    

# def initialize_base_dir():
#     if not os.path.isdir(BASE_DIR):
#         os.mkdir(BASE_DIR)