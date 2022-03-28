# pyqt-transparent-frame-widget
PyQt widget(window) which has transparent frame(title bar), resizable, movable

## Requirements
* PyQt5 >= 5.15

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-transparent-frame-widget.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-frameless-window.git">pyqt-frameless-window</a>

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_fitting_graphics_view import FittingGraphicsView
from pyqt_transparent_frame_widget import TransparentFrameWidget


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    customTitlebarWindow = TransparentFrameWidget()
    view = FittingGraphicsView() # https://github.com/yjg30737/pyqt-fitting-graphics-view.git
    view.setFilename('cloud.jpg')
    customTitlebarWindow.addWidget(view)
    customTitlebarWindow.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/160344194-046be239-d30d-4e1b-8827-69c8b1962aad.png)

Expand horizontally by resize

![image](https://user-images.githubusercontent.com/55078043/160344253-d9e50834-0a82-4121-8c56-2324971fa14b.png)

