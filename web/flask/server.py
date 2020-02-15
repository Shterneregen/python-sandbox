import time
from datetime import datetime

from flask import Flask, request

app = Flask(__name__)
messages = [
    {'username': 'Jack', 'text': 'Hello', 'time': time.time()},
    {'username': 'Mary', 'text': 'Hi, Jack', 'time': time.time()}
]


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    return {
        'status': True,
        'time': datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }


@app.route("/history")
def history():
    """
    request: after
    response: [{"username": "str", "text": "str", "time": float}, ...]
    """
    after = float(request.args['after'])
    # filtered_messages = []
    # for message in messages:
    #     if after < message['time']:
    #         filtered_messages.append(message)

    filtered_messages = [msg for msg in messages if after < msg['time']]

    return {'messages': filtered_messages}


@app.route("/send", methods=['POST'])
def send():
    """
    request: {"username": "str", "text": "str"}
    response: {"ok": true}
    """
    data = request.json
    username = data['username']
    text = data['text']
    new_message = {'username': username, 'text': text, 'time': time.time()}
    messages.append(new_message)
    return {"ok", True}


app.run()
