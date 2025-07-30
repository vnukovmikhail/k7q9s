from PyQt6.QtGui import QFontMetrics
from PyQt6.QtCore import Qt
from typing import Optional, List, Dict, Union
import os, inspect
from datetime import datetime


def log(text):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'[{now}] {text}\n'

def validate_data(data):
    print(inspect.currentframe().f_code.co_name, data)
    is_valid = False
    error_msg = []

    for field, value in data.items():
        if not value:
            error_msg.append(f'❌ Not defined "{field}"')

    if not error_msg:
        is_valid = True
    else:
        error_msg = 'Details:\n' + '\n'.join(error_msg)
    
    return is_valid, error_msg
    
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

def elide_text(text, width, font):
    metrics = QFontMetrics(font)
    return metrics.elidedText(text, Qt.TextElideMode.ElideRight, width)

def to_dict(*args:str):
    frame = inspect.currentframe().f_back
    names = {id(v): k for k, v in frame.f_locals.items()}

    return {names.get(id(v), f"var_{i}"): v for i, v in enumerate(args)}