def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


def find_uniques(numbers):
    uniques = []
    for number in numbers:
        if number not in uniques:
            uniques.append(number)
    return uniques
