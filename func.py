def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome abroad')


print("Start")
greet_user("John", "Smith")
greet_user("Mary", "Smith")
print("Finish")

print("Start")
greet_user(last_name="John", first_name="Smith")
print("Finish")


# ------------------------------------------------
def square(number):
    return number * number


print(square(3))
