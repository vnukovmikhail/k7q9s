import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QSlider, QLabel, QFileDialog, QGridLayout, QSizePolicy, QToolBox, QTabBar, QTreeView
)
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import Qt, QUrl, QTime
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QDir

from PyQt6.QtWidgets import QWidget, QTabWidget, QToolBox, QMenuBar, QMenu, QDialog, QWizard, QWizardPage, QVBoxLayout, QLabel
class Test4Widget(QWidget):
    def __init__(self):
        super().__init__()

        """ self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())  # "/" на Linux/macOS, "C:\" на Windows

        # Дерево
        self.tree = QTreeView(self)
        self.tree.setModel(self.model)

        # Отображать только из домашней папки
        self.tree.setRootIndex(self.model.index(QDir.homePath()))

        # Настройки столбцов
        self.tree.setColumnWidth(0, 250) """



        # toolbox = QToolBox(self)

        # # Первая вкладка
        # page1 = QWidget()
        # page1_layout = QVBoxLayout()
        # page1_layout.addWidget(QLabel("Содержимое вкладки 1"))
        # page1.setLayout(page1_layout)

        # # Вторая вкладка
        # page2 = QWidget()
        # page2_layout = QVBoxLayout()
        # page2_layout.addWidget(QLabel("Содержимое вкладки 2"))
        # page2.setLayout(page2_layout)

        # # Добавляем вкладки
        # toolbox.addItem(page1, "Общие настройки")
        # toolbox.addItem(page2, "Дополнительно")

        """ # self.setWindowTitle("Видеоплеер с управлением")
        # self.resize(900, 600)

        # Виджет видео
        self.video_widget = QVideoWidget()
        # self.video_widget.setMinimumHeight(360)

        # Плеер и аудио
        self.audio_output = QAudioOutput()
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)
        self.player.setVideoOutput(self.video_widget)

        # Кнопки управления
        self.play_btn = QPushButton("▶ Play")
        self.pause_btn = QPushButton("⏸ Pause")
        self.stop_btn = QPushButton("⏹ Stop")
        self.open_btn = QPushButton("📁 Открыть видео")

        self.play_btn.clicked.connect(self.player.play)
        self.pause_btn.clicked.connect(self.player.pause)
        self.stop_btn.clicked.connect(self.player.stop)
        self.open_btn.clicked.connect(self.open_file)

        # Слайдер для перемотки
        self.position_slider = QSlider(Qt.Orientation.Horizontal)
        self.position_slider.setRange(0, 0)
        self.position_slider.sliderMoved.connect(self.set_position)

        # Метки времени
        self.label_current_time = QLabel("00:00")
        self.label_current_time.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.label_total_time = QLabel("00:00")
        self.label_total_time.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # Layout управления
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.play_btn)
        control_layout.addWidget(self.pause_btn)
        control_layout.addWidget(self.stop_btn)
        control_layout.addWidget(self.open_btn)
        control_layout.addStretch()

        # Layout времени и слайдера
        time_layout = QHBoxLayout()
        time_layout.addWidget(self.label_current_time)
        time_layout.addWidget(self.position_slider)
        time_layout.addWidget(self.label_total_time)

        # Основной layout
        main_layout = QGridLayout(self)
        main_layout.addWidget(self.video_widget, 0, 0)
        main_layout.addLayout(time_layout, 1, 0)
        main_layout.addLayout(control_layout, 2, 0)
        

        # widget = QWidget()
        # widget.setLayout(main_layout)
        # self.setCentralWidget(widget)

        # Обновления позиции
        self.player.positionChanged.connect(self.update_position)
        self.player.durationChanged.connect(self.update_duration) """

    """ def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Выбрать видео", "", "Видео (*.mp4 *.avi *.mov *.mkv)")
        if file_name:
            self.player.setSource(QUrl.fromLocalFile(file_name))
            # self.player.play()

    def update_position(self, position):
        self.position_slider.setValue(position)
        self.label_current_time.setText(self.format_time(position))

    def update_duration(self, duration):
        self.position_slider.setRange(0, duration)
        self.label_total_time.setText(self.format_time(duration))

    def set_position(self, position):
        self.player.setPosition(position)

    def format_time(self, ms):
        time = QTime(0, 0, 0)
        time = time.addMSecs(ms)
        return time.toString("mm:ss") """


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = VideoPlayer()
#     window.show()
#     sys.exit(app.exec())
