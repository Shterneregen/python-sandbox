from datetime import datetime

import requests
from PyQt5 import QtWidgets, uic, QtCore


class MessengerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MessengerWindow, self).__init__()
        uic.loadUi('messenger.ui', self)
        self.pushButton.pressed.connect(self.send_message)
        self.last_message_time = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_updates)
        self.timer.start(1000)

    def send_message(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        text = self.textEdit.toPlainText()

        error = False
        if not username:
            error = True
            self.add_text('ERROR: username is empty!')
        if not password:
            error = True
            self.add_text('ERROR: password is empty!')
        if not text:
            error = True
            self.add_text('ERROR: text is empty!')

        if error:
            self.add_text('')
            return

        url = 'http://127.0.0.1:5000/send'
        msg = {'username': username, 'password': password, 'text': text}

        response = requests.post(url=url, json=msg)
        if not response.json()['ok']:
            self.add_text('Access denied')
            self.add_text('')
            return

        self.textEdit.clear()
        self.textEdit.repaint()

    def add_text(self, text):
        self.textBrowser.append(text)
        self.textBrowser.repaint()

    def get_updates(self):
        response = requests.get(
            'http://127.0.0.1:5000/history?',
            params={'after': self.last_message_time}
        )
        data = response.json()
        for message in data['messages']:
            # float -> datetime
            beauty_time = datetime.fromtimestamp(message['time'])
            beauty_time = beauty_time.strftime('%Y/%m/%d %H:%M:%S')
            self.add_text(beauty_time + ' ' + message['username'])
            self.add_text(message['text'])
            self.add_text('')
            self.last_message_time = message['time']


app = QtWidgets.QApplication([])
window = MessengerWindow()
window.show()
app.exec_()
