from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout

from pyqt_transparent_frame_widget.transparentFrame import TransparentFrame


class TransparentFrameWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initUi()

    def __initUi(self):
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        lay = QGridLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)
        self.__frame = TransparentFrame(self)

    def addWidget(self, widget):
        self.layout().addWidget(widget)
        self.__frame.raise_()
