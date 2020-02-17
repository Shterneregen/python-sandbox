
[Qt Designer Download](https://build-system.fman.io/qt-designer-download)  
[PyQt5 Download](https://www.riverbankcomputing.com/software/pyqt/download5)  

* With converting .ui to .py
```
pip install requests
pip install PyQt5
# To convert .ui to .py
pyuic5 -x messenger.ui -o clientui.py
```
```python
import clientui
from PyQt5 import QtWidgets

class MessengerWindow(QtWidgets.QMainWindow, clientui.Ui_Messenger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
```

* Without creating .py file for UI
```python
from PyQt5 import QtWidgets, uic


class MessengerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MessengerWindow, self).__init__()
        uic.loadUi('messenger.ui', self)
```