from flask import Flask, request
from datetime import datetime
from wakeonlan import send_magic_packet

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/wake-up')
def wake_up():
    print('hello')
    mac = request.args.get('mac')
    send_magic_packet(mac)
    print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'), mac)
    return mac


if __name__ == '__main__':
    app.run(debug=True, port=5050)
