from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import QTimer
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resize Delay Example")
        self.resize(400, 300)

        self.label = QLabel("Resize the window", self)
        self.setCentralWidget(self.label)

        self.resize_timer = QTimer(self)
        self.resize_timer.setInterval(300)  # 300 мс после последнего resize
        self.resize_timer.setSingleShot(True)
        self.resize_timer.timeout.connect(self.on_resize_done)

    def resizeEvent(self, event):
        # Сбрасываем и перезапускаем таймер
        self.resize_timer.start()
        return super().resizeEvent(event)

    def on_resize_done(self):
        size = self.size()
        print(f"Resize finished: {size.width()} x {size.height()}")
        self.label.setText(f"Window: {size.width()} x {size.height()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


""" class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Not my first application')
        self.setWindowIcon(QIcon('pic.png'))
        self.setFont(QFont('monospace'))

        widget1 = QWidget()
        self.setCentralWidget(widget1)
        layout1 = QVBoxLayout(widget1)

        slider = QSlider(Qt.Orientation.Horizontal)
        layout1.addWidget(slider)

        push = QPushButton('push me!')
        layout1.addWidget(push)
        push.clicked.connect(self.new_screen)

    def new_screen(self):
        widget2 = QWidget()
        self.setCentralWidget(widget2)
        layout = QVBoxLayout(widget2)

        label = QLabel('lol')
        layout.addWidget(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = MainWindow()
    root.show()
    sys.exit(app.exec()) """

""" widget = QWidget()
    self.setCentralWidget(widget)
    layout = QGridLayout(widget)

    pixmap = QPixmap('pic.png')
    for x in range(5):
        for y in range(4):
            label = QLabel()
            label.setPixmap(pixmap)
            label.setFixedSize(50, 50)
            label.setScaledContents(True)
            layout.addWidget(label, y, x, 1, 1) """


""" class ProgressBar(QProgressBar):
        def __init__(self):
            super().__init__()
            self.setMaximum(100)
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_value)
            self.step = 0
        
        def updateBar(self, i):
            self.step = i
            self.timer.start(50) 
        
        def update_value(self):
            value = self.value() + self.step
            self.setValue(value)
            if value >= self.maximum():
                self.timer.stop()
                self.setValue(self.maximum())

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('Not my first application')
            self.setWindowIcon(QIcon('pic.png'))
            self.setFont(QFont('monospace'))  

            widget = QWidget()
            self.setCentralWidget(widget)
            layout = QVBoxLayout(widget)

            self.progressBar = ProgressBar()
            layout.addWidget(self.progressBar)

            button = QPushButton('Update Progress Bar')
            button.clicked.connect(self.updateProgressBar)
            layout.addWidget(button)

        def updateProgressBar(self):
            self.progressBar.updateBar(1)
            
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        root = MainWindow()
        root.show()
        sys.exit(app.exec())
    """

""" widget = QWidget()
        self.setCentralWidget(widget)
        layout = QGridLayout(widget)

        labels = {}
        lineEdits = {}
        labels['Username'] = QLabel('Username')
        labels['Password'] = QLabel('Password')
        labels['Username'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['Password'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        lineEdits['Username'] = QLineEdit()
        lineEdits['Password'] = QLineEdit()
        lineEdits['Password'].setEchoMode(QLineEdit.EchoMode.Password)
        button = QPushButton('Log In')
        textEdit = QTextEdit()

        layout.addWidget(labels['Username'],    0, 0, 1, 1)
        layout.addWidget(lineEdits['Username'], 0, 1, 1, 3)

        layout.addWidget(labels['Password'],    1, 0, 1, 1)
        layout.addWidget(lineEdits['Password'], 1, 1, 1, 3)

        layout.addWidget(button,                2, 0, 1, 4)
        layout.addWidget(textEdit,              3, 0, 1, 4) """

""" widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)

        lineEdits = {}
        lineEdits['NoEcho'] = QLineEdit()
        lineEdits['NoEcho'].setPlaceholderText('No Text')
        lineEdits['NoEcho'].setEchoMode(QLineEdit.EchoMode.NoEcho)
        lineEdits['NoEcho'].textChanged.connect(self.printValue)

        lineEdits['Normal'] = QLineEdit()
        lineEdits['Normal'].setPlaceholderText('No Text')
        lineEdits['Normal'].setEchoMode(QLineEdit.EchoMode.Normal)
        lineEdits['Normal'].textChanged.connect(self.printValue)

        lineEdits['Password'] = QLineEdit()
        lineEdits['Password'].setPlaceholderText('No Text')
        lineEdits['Password'].setEchoMode(QLineEdit.EchoMode.Password)
        lineEdits['Password'].textChanged.connect(self.printValue)

        lineEdits['PasswordEchoOnEdit'] = QLineEdit()
        lineEdits['PasswordEchoOnEdit'].setPlaceholderText('No Text')
        lineEdits['PasswordEchoOnEdit'].setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        lineEdits['PasswordEchoOnEdit'].textChanged.connect(self.printValue)

        for _, item in lineEdits.items():
            layout.addWidget(item) 
            
    def printValue(self, v):
        print(v) """

""" layout = QVBoxLayout()
        self.input = QLineEdit()
        button = QPushButton('Who are you?')
        self.output = QTextEdit()
        layout.addWidget(self.input)
        layout.addWidget(button)
        layout.addWidget(self.output)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        button.clicked.connect(self.press_button)

    def press_button(self):
        text = self.input.text()
        self.output.setText('You are {0}.'.format(text)) """

"""
QListWidget(self).addItems(['one', 'two', 'three'])
QComboBox(self).addItems(['one', 'two', 'three'])
QFontComboBox(self)
QLCDNumber(self)
QTimeEdit(self)
QSpinBox(self)
QSlider(self)
QProgressBar(self).setValue(59)
"""

""" def contextMenuEvent(self, e):
context = QMenu(self)
context.addAction(QAction("test 1", self))
context.addAction(QAction("test 2", self))
context.addAction(QAction("test 3", self))
context.exec(e.globalPos()) """

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

"""

PUBLIC_DIR = 'public'

if not os.path.exists(PUBLIC_DIR):
    os.mkdir(PUBLIC_DIR)
print(f'Folder: {PUBLIC_DIR} was successfully initialized')

PUBLIC_DIR_PATH = os.path.abspath(PUBLIC_DIR)
print(f'Folder was created on path: {PUBLIC_DIR_PATH}')

HOME_DIR_PATH = os.path.expanduser('~')

"""