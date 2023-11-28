my_class = {
    "alex": 90,
    "ido": 95,
    "roei": 100,
    "alma": 105,
    "shoshana": 89,
}

print(my_class)
print(my_class.items())
print(type(my_class.items()))
print(list(my_class.items()))
print(type(list((my_class.items()))))

print(my_class.items().__sizeof__())
print(list(my_class.items()).__sizeof__())
