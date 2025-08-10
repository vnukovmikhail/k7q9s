import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QLabel
)
from PyQt6.QtCore import Qt, pyqtSignal

class PaginationWidget(QWidget):
    page_changed = pyqtSignal(int)
    def __init__(self, total_pages=10, visible_count=3):
        super().__init__()
        self.total_pages = total_pages
        self.visible_count = visible_count
        self.current_page = 1

        self.pagination_layout = QHBoxLayout(self)

    
    def set(self, total_pages):
        self.total_pages = total_pages
        self.update_pagination()

    def update_pagination(self):
        while self.pagination_layout.count():
            item = self.pagination_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        start = max(1, self.current_page - self.visible_count // 2)
        end = start + self.visible_count - 1

        if end > self.total_pages:
            end = self.total_pages
            start = max(1, end - self.visible_count + 1)

        self.pagination_layout.addStretch()

        if start > 1:
            btn_prev_dots = QPushButton("...")
            btn_prev_dots.setStyleSheet('padding: 0px 5px;')
            btn_prev_dots.setEnabled(False)
            self.pagination_layout.addWidget(btn_prev_dots)

        for i in range(start, end + 1):
            btn = QPushButton(str(i))
            btn.setStyleSheet('padding: 0px 5px;')
            btn.setCheckable(True)
            btn.setChecked(i == self.current_page)
            btn.clicked.connect(lambda checked, x=i: self.set_page(x))
            self.pagination_layout.addWidget(btn)

        if end < self.total_pages:
            btn_next_dots = QPushButton("...")
            btn_next_dots.setStyleSheet('padding: 0px 5px;')
            btn_next_dots.setEnabled(False)
            self.pagination_layout.addWidget(btn_next_dots)

        self.pagination_layout.addStretch()

    def set_page(self, page, emit: bool = True):
        if self.current_page == page:
            return
        
        self.current_page = page
        self.update_pagination()

        if emit:
            self.page_changed.emit(page)
