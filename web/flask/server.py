import time
from datetime import datetime

from flask import Flask, request, jsonify

app = Flask(__name__)
messages = [
    {'username': 'Jack', 'text': 'Hello', 'time': time.time()},
    {'username': 'Mary', 'text': 'Hi, Jack', 'time': time.time()}
]
users = {
    # 'user': 'password'
    'Jack': 'black',
    'Mary': '1324'
}


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/status')
def status():
    return {
        'status': True,
        'time': datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        'messages_count': len(messages),
        'user_count': len(users)
    }


@app.route('/history')
def history():
    """
    request: after
    response: [{'username': 'str', 'text': 'str', 'time': float}, ...]
    """
    after = float(request.args['after'])
    # filtered_messages = []
    # for message in messages:
    #     if after < message['time']:
    #         filtered_messages.append(message)

    filtered_messages = [msg for msg in messages if after < msg['time']]

    return {'messages': filtered_messages}


@app.route('/send', methods=['POST'])
def send():
    """
    request: {'username': 'str', 'password': 'str', 'text': 'str'}
    response: {'ok': true}
    """
    data = request.json
    username = data['username']
    password = data['password']
    text = data['text']

    if username in users:
        real_password = users[username]
        if real_password != password:
            print('Wrong psw')
            return jsonify({'ok': False})
    else:
        print('New user')
        users[username] = password

    new_message = {'username': username, 'text': text, 'time': time.time()}
    messages.append(new_message)
    print('ok')
    return jsonify({'ok': True})


if __name__ == '__main__':
    app.run(debug=False)
