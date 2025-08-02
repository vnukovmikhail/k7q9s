import os, shutil
from app.utils.logger_util import get_logger

logger = get_logger(__name__)

BASE_DIR = 'public'

def get_file_paths_in_folder(
    folder_name: str,
    file_names: list[str],
    base_dir: str = BASE_DIR,
) -> list[str]:
    return [os.path.join(base_dir, folder_name, file_name)  for file_name in file_names]

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

            logger.info('added', dest_path, file_name)
        return True
    except Exception as e:
        logger.error(e)
        return False

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
    
    logger.info(f'load: {folder_path}, {file_paths}')
    return file_paths