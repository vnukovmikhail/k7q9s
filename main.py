import sys, os, json, shutil, time, asyncio, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QFileDialog, QMessageBox,
                             QVBoxLayout, QHBoxLayout, QGridLayout,
                             QLabel, QLineEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt, QSize

""""""

PUBLIC_DIR = 'public'

if not os.path.exists(PUBLIC_DIR):
    os.mkdir(PUBLIC_DIR)
print(f'Folder: {PUBLIC_DIR} was successfully initialized')

PUBLIC_DIR_PATH = os.path.abspath(PUBLIC_DIR)
print(f'Folder was created on path: {PUBLIC_DIR_PATH}')

HOME_DIR_PATH = os.path.expanduser('~')

""""""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Not my first application')
        self.setWindowIcon(QIcon('pic.png'))
        self.setGeometry(0, 0, 300, 125)
        self.setFont(QFont('monospace'))

        """ label = QLineEdit(self)
        input = QLineEdit(self)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(input)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container) """

        """ input1 = QLineEdit(self)
        input2 = QLineEdit(self)
        input3 = QLineEdit(self)

        layout = QHBoxLayout()
        layout.addWidget(input1)
        layout.addWidget(input2)
        layout.addWidget(input3)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container) """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = MainWindow()
    root.show()
    sys.exit(app.exec())



        # self.initLowerUI()
        # self.initUpperUI()

        # self.entry = QLineEdit(self)
        # self.file_dialog = []
        # self.initUI()

    # def initUpperUI(self):
    #     container = QWidget()
    #     layout = QVBoxLayout()

    #     # layout.addStretch()
    #     button3 = QPushButton('Create collection')
    #     # button3.clicked.connect(self.createCollection)
    #     button3.clicked.connect(lambda:print('btn3'))
    #     layout.addWidget(button3)

    #     container.setLayout(layout)
    #     self.setMenuWidget(container)

    # def initLowerUI(self):
    #     container = QWidget()
    #     layout = QVBoxLayout()

    #     layout.addStretch() # stick to lower
    #     button2 = QPushButton('Create collection')
    #     # button2.clicked.connect(self.createCollection)
    #     button2.clicked.connect(lambda:print('btn2'))
    #     layout.addWidget(button2)

    #     container.setLayout(layout)
    #     self.setCentralWidget(container)

    # def initUI(self):
    #     pic_label = QLabel(self)
    #     pic_label.setGeometry(0, 0, 50, 50)
    #     pic_label.setScaledContents(True)
    #     pixmap = QPixmap('pic.png')
    #     pic_label.setPixmap(pixmap)

    #     label = QLabel('title:', self)
    #     label.move(55, 0)

    #     self.entry.setGeometry(105, 5, 100, 20)

    #     button = QPushButton('Select files', self)
    #     button.setGeometry(105, 0, 150, 20)
    #     button.move(55, 30)
    #     button.clicked.connect(self.chooseFiles)

    # def chooseFiles(self):
    #     self.file_dialog, _ = QFileDialog.getOpenFileNames(self, 'Choose files', HOME_DIR_PATH, 'png')

    # def createCollection(self):
    #     title = self.entry.text()
    #     files = self.file_dialog
    #     print(title, files)

    #     if not title:
    #         print('No title')
    #         return
        
    #     try:
    #         os.mkdir(f'{PUBLIC_DIR_PATH}/{title}')
    #         path = os.path.abspath(f'{PUBLIC_DIR_PATH}/{title}')

    #         for file in files:
    #             shutil.move(file, path)
    #     except Exception as e:
    #         print(e)
    #         return



