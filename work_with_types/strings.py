first = "John"
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)
print(len(first))
print(message.upper())
print(message.lower())
print(message.title())
print(message.find(last))
print(message.replace(first, last))
print(first in message)