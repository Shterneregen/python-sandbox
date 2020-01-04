customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer)
print(customer["name"])
print(customer.get("name"))
print(customer["age"])
print(customer["is_verified"])

# print(customer["birthdate"]) # KeyError
print(customer.get("birthdate"))  # None
print(customer.get("birthdate", "Jan 1 1980"))

customer["name"] = "Jack Smith"
print(customer)

customer["birthdate"] = "Jan 1 1980"
print(customer)
print(customer["birthdate"])

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
