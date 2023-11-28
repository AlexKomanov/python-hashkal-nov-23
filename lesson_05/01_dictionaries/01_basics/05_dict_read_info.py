my_car = {
    "brand": "Tesla",
    (56, 78): "Home",
    12: True,
    # ["White", "Black"]: "color_options",
    "cords": {
        "lat": 35.6,
        "long": 56.8
    }
}

print(my_car["brand"])
print(my_car["cords"])
print(my_car["cords"]["lat"])

print("manufacturer" in my_car)

if "cords" in my_car:
    print("cords" in my_car)

if "manufacturer" in my_car:
    print(my_car["manufacturer"])
else:
    print("A key 'manufacturer' was not found")

# print(my_car["manufacturer"])  # KeyError: 'manufacturer'
