import requests

print('Enter username: ')
username = input()
print('Enter password: ')
password = input()

while True:
    print('Enter message: ')
    text = input()

    url = 'http://127.0.0.1:5000/send'
    msg = {'username': username, 'password': password, 'text': text}

    response = requests.post(url=url, json=msg)
    print(response.status_code)
    # if not response.json()['ok']:
    #     print('Access denied')
    #     break
