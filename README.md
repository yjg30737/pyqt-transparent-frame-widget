# pyqt-transparent-frame-widget
PyQt widget(window) which has transparent frame(title bar)

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
from pyqt_transparent_frame_widget import TransparentFrameWidget
from pyqt_viewer_widget import ViewerWidget


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    customTitlebarWindow = TransparentFrameWidget()
    customTitlebarWindow.addWidget(ViewerWidget())
    customTitlebarWindow.show()
    app.exec_()
```
