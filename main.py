import sys, os, json
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QLabel, QLineEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Not my first application')
        self.setWindowIcon(QIcon('pic.png'))
        self.setGeometry(0, 0, 300, 75)

        self.initUI()

    def initUI(self):
        self.counter = 0
        self.label = QLabel(f'Text: {self.counter}', self)
        self.label.move(10, 0)
        button = QPushButton('Push me!', self)
        button.setGeometry(0, 0, 70, 20)
        button.move(60, 5)
        button.clicked.connect(self.incCounter)

    def incCounter(self):
        self.counter += 1
        self.label.setText(f'Text: {self.counter}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = MainWindow()
    root.show()
    sys.exit(app.exec())





""" import sys, os, json
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QLineEdit,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QFileDialog)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first GUI')
        self.setGeometry(0, 0, 300, 350)
        self.setWindowIcon(QIcon('pic.png'))
        self.setFont(QFont('monospace', 11))


        self.button = QPushButton('Browse files', self)

        self.initUI()

    def initUI(self):
        self.button.clicked.connect(self.browse_files)
        self.button.setGeometry(0, 0, 300, 30)

    def browse_files(self):
        file_dialog = QFileDialog.getOpenFileNames(self, 'Open file')
        print(file_dialog[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 """
""" import sys, os, json
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QLineEdit,
                             QCheckBox, QRadioButton, QButtonGroup, QPushButton,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QFileDialog)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first GUI')
        self.setGeometry(0, 0, 300, 350)
        self.setWindowIcon(QIcon('pic.png'))
        self.setFont(QFont('monospace', 11))

        self.file_dialog = QFileDialog(self)

        self.initUI()

    def initUI(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 """
""" class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first GUI')
        self.setGeometry(0, 0, 300, 350)
        self.setWindowIcon(QIcon('pic.png'))
        self.setFont(QFont('monospace', 11))

        self.line_edit = QLineEdit(self)
        self.button = QPushButton('submit', self)

        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(5, 5, 150, 25)
        self.line_edit.setPlaceholderText('Enter your name')
        self.button.setGeometry(160, 5, 75, 25)

        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f'Hello, {text}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) """

""" 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first GUI')
        self.setGeometry(0, 0, 300, 350)
        self.setWindowIcon(QIcon('pic.png'))

        self.radio1 = QRadioButton('kiki', self)
        self.radio2 = QRadioButton('rita', self)
        self.radio3 = QRadioButton('jack', self)
        self.radio4 = QRadioButton('male', self)
        self.radio5 = QRadioButton('female', self)

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(5, 5, 300, 20)
        self.radio2.setGeometry(5, 25, 300, 20)
        self.radio3.setGeometry(5, 45, 300, 20)
        self.setStyleSheet('QRadioButton{'
                           'font-family: monospace;'
                           '}')
        self.radio4.setGeometry(85, 5, 300, 20)
        self.radio5.setGeometry(85, 25, 300, 20)

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f'{radio_button.text()} is selected')
        else:
            print(f'{radio_button.text()} is unselected')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
"""

""" class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first GUI')
        self.setGeometry(0, 0, 300, 350)
        self.setWindowIcon(QIcon('pic.png'))

        self.checkbox = QCheckBox('will you be mine?', self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(5, 0, self.width(), 30)
        self.checkbox.setFont(QFont('monospace', 11))
        self.checkbox.setStyleSheet('font-weight: bold;')
        self.checkbox.setChecked(True)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print('you are mine', state)
        else:
            print('why not?', state)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) """

""" class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first GUI')
        self.setGeometry(0, 0, 300, 350)
        self.setWindowIcon(QIcon('pic.png'))

        label = QLabel('Hello', self)
        label.setFont(QFont('monospace', 11))
        label.setStyleSheet('color: #F0F0F0;' 'font-weight: bold;' 'text-decoration: underline;' 'background-color: #1B1116;')

        label.setGeometry(0, 0, 300, 30)
        # label.setAlignment(Qt.AlignTop)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)


        pic_label = QLabel(self)
        pic_label.setGeometry(0, 0, 150, 150)

        pixmap = QPixmap('pic.png')
        pic_label.setPixmap(pixmap)
        pic_label.setScaledContents(True)

        pic_label.setGeometry((self.width() - pic_label.width()) // 2,
                              (self.height() - pic_label.height()) // 6,
                              pic_label.width(),
                              pic_label.height())
        # pic_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) 

        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel('#1', self)
        label2 = QLabel('#2', self)
        label3 = QLabel('#3', self)
        label4 = QLabel('#4', self)
        label5 = QLabel('#5', self)

        label1.setStyleSheet('background-color: red;')
        label2.setStyleSheet('background-color: yello;')
        label3.setStyleSheet('background-color: pink;')
        label4.setStyleSheet('background-color: brown;')
        label5.setStyleSheet('background-color: blue;')

        vbox = QGridLayout()
        vbox.addWidget(label1, 0, 0)
        vbox.addWidget(label2, 0, 1)
        vbox.addWidget(label3, 0, 2)
        vbox.addWidget(label4, 1, 0)
        vbox.addWidget(label5, 1, 1)

        central_widget.setLayout(vbox)

        self.button = QPushButton('Click me!', self)
        self.button.setGeometry(0, 0, 150, 75)
        self.button.setGeometry((self.width() - self.button.width()) // 2, 15, 150, 35)
        self.button.setStyleSheet('font-size: 15px;' 'font-family: monospace;' 'font-weight: bold;')
        # button.setFont(QFont('monospace', 30))
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print('button clicked')
        self.button.setText('Clicked')
        self.button.setDisabled(True)
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() """