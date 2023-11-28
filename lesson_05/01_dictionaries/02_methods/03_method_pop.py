my_car = {
    "brand": "Tesla",
    "year": 2023,
    "color": "Black",
}

print(my_car)
print(my_car.pop("brand"))
print(my_car)

key_to_find = "year_of_production"
# print(my_car.pop(f"{key_to_find}"))

print(my_car.pop("manufacturer", f"A key '{key_to_find}' was not found"))
