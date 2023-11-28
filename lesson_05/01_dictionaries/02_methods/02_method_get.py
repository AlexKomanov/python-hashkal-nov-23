my_car = {
    "brand": "Tesla",
    "year": 2023,
    "color": "Black",
}

print(my_car["brand"])
print(my_car.get("brand"))

key_to_find = "year_of_production"
print(my_car.get(f"{key_to_find}"))
print(my_car.get("manufacturer", f"A key '{key_to_find}' was not found"))
