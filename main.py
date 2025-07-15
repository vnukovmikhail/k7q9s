import sys, os, json
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first GUI')
        self.setGeometry(0, 0, 300, 350)
        self.setWindowIcon(QIcon('pic.png'))

        """ label = QLabel('Hello', self)
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
        # pic_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) """

        self.initUI()
        
    def initUI(self):
        """ central_widget = QWidget()
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

        central_widget.setLayout(vbox) """

        button = QPushButton('Click me!', self)
        button.setGeometry(0, 0, 150, 75)
        button.setGeometry((self.width() - button.width()) // 2, 15, 150, 35)
        button.setStyleSheet('font-size: 15px;' 'font-family: monospace;' 'font-weight: bold;')
        # button.setFont(QFont('monospace', 30))
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()