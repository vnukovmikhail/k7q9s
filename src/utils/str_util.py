from typing import Optional, List, Dict, Union
import os

def validate_data(data):
    details = []
    for field, value in data.items():
        if not value:
            details.append(f'Not defined "{field}"')
    
    if details:
        return 'Details:\n ❌ ' + '\n ❌ '.join(details), False
    else:
        return '', True
    
def text_to_arr(text: str, sep: str):
    arr = []
    if text:
        arr = text.split(sep)
    return arr

def filter_images(file_paths: List[str]) -> Union[List[str], str]:
    IMAGE_EXTENSIONS = {
        '.jpg', '.jpeg', '.png', '.gif',
        '.bmp', '.webp', '.tiff', '.svg'
    }

    DEFAULT_IMAGE_PATH = 'src/resources/pic.png'
    
    filtered = [
        path for path in file_paths
        if (os.path.isfile(path) and os.path.splitext(path)[1].lower() in IMAGE_EXTENSIONS)
    ]
    
    return filtered[0] if filtered else DEFAULT_IMAGE_PATH