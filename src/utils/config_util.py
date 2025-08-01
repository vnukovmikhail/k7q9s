from PyQt6.QtCore import QSettings
import os, sys

CONFIG_FILE = 'config.ini'

class config:
    def __init__(self):
        super().__init__()
        self.settings = QSettings(CONFIG_FILE, QSettings.Format.IniFormat)

    def set(self, key, value):
        return self.settings.setValue(key, value)

    def get(self, value):
        return self.settings.value(value)
    
config()

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)