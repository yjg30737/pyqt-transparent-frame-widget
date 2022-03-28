from PyQt5.QtCore import Qt
from pyqt_frameless_window import FramelessWindow


class TransparentFrame(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('frame')
        self.setMouseTracking(True)
        self.installEventFilter(self)

        parent.setObjectName('parent')
        parent.setMouseTracking(True)
        parent.installEventFilter(self)
        self.setParent(parent)

        self.__initBasicUi()

    def __initBasicUi(self):
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setPressToMove(True)

        self.setMinimumSize(self.window().sizeHint().width(), self.window().sizeHint().height())
        self.parent().setMinimumSize(self.minimumSize())

    def eventFilter(self, obj, e):
        if obj.objectName() == 'parent':
            if e.type() == 14:
                self.resize(e.size())
        return super().eventFilter(obj, e)
