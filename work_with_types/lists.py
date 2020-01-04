import utils

numbers = [3, 6, 2, 8, 4, 10]
max = utils.find_max(numbers)
print(f"Max value: {max}")

# --------------------------------------
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[0])
print(names[-1])
print(names[2:])
print(names[2:4])
print(names[:])

names[0] = 'Jon'
print(names)

# --------------------------------------
numbers = [5, 2, 1, 5, 7, 4]

numbers.append(13)
print(numbers)

numbers.insert(0, 10)
print(numbers)

numbers.remove(10)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(2))
print(50 in numbers)
print(5 in numbers)
print(numbers.count(5))

print(f'Origin list: {numbers}')
numbers.sort()
print(f'Sorted list: {numbers}')
numbers.reverse()
print(f'Reversed list: {numbers}')

numbers2 = numbers
numbers2.remove(5)
print(numbers)

numbers3 = numbers.copy()
numbers3.remove(5)
print(numbers)

numbers.clear()
print(numbers)
