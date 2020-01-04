for item in 'Python':
    print(item)

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 10):
    print(item)

for item in range(5, 10, 2):
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
