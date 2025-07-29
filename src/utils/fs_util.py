import sys, os, json, shutil, time, asyncio, random, datetime
from typing import Optional, List, Dict

BASE_DIR = 'public'

def initialize_base_dir():
    if not os.path.isdir(BASE_DIR):
        os.mkdir(BASE_DIR)

def create_collection(
    title: str,
    tags: Optional[List[str]] = None,
    files: Optional[List[str]] = None,
) -> Dict[str, str]:
    tags = tags or []
    files = files or []

    folder_path = os.path.join(BASE_DIR, title)
    os.makedirs(folder_path, exist_ok=True)

    meta = {
        'title': title,
        'tags': tags,
        'created_at': datetime.datetime.now().isoformat()
    }

    meta_path = os.path.join(folder_path, 'meta.json')

    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(meta, f, indent=4, ensure_ascii=False)

    for index, file_path in enumerate(files):
        if os.path.isfile(file_path):
            filename = os.path.basename(file_path)
            new_filename = f"{index}_{filename}"
            dest_path = os.path.join(folder_path, new_filename)
            shutil.copy2(file_path, dest_path)

    return {
        'folder_path': os.path.abspath(folder_path)
    }

def read_collection(
    folder_name: str
) -> Dict[str, str]:
    folder_path = os.path.join(BASE_DIR, folder_name)

    if not os.path.isdir(folder_path):
        return None
    
    meta_path = os.path.join(folder_path, 'meta.json')
    meta = {}

    if os.path.isfile(meta_path):
        with open(meta_path, 'r', encoding='utf-8') as f:
            meta = json.load(f)

    files = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) and item != 'meta.json':
            files.append(item_path)

    return {
        'meta': meta,
        'files': files,
        'folder_path': folder_path
    }

def fetch_collections():
    initialize_base_dir()

    collections = []
    folder_names = os.listdir(BASE_DIR)

    for folder_name in folder_names:
        collections.append(read_collection(folder_name))

    return collections
    