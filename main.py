import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
from app.main_window import MainWindow


from app.db.models import BaseModel
from app.db import session, engine

def init_db(engine):
    BaseModel.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db(engine)

    app = QApplication(sys.argv)
    app.setFont(QFont('monospace', 10))
    
    root = MainWindow(session)
    root.show()

    sys.exit(app.exec())