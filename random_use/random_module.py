import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)

ages = [random.randint(0, 100) for _ in range(20)]
print(ages)

squares = [x ** 2 for x in range(10)]
print(squares)
