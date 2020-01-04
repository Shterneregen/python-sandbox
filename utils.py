def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


def find_uniques(numbers):
    uniques = []
    for number in numbers:
        if number not in uniques:
            uniques.append(number)
    return uniques
